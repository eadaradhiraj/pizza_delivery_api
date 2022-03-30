from crypt import methods
from fastapi import FastAPI
from auth_routes import auth_router
from order_routes import order_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings
import inspect
import re
from fastapi.routing import APIRoute
from fastapi.openapi.utils import get_openapi

app = FastAPI()
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title = "Pizza Delivery API",
        version = "1.0",
        description="API for Pizza Delivery Service",
        routes=app.routes
    )
    openapi_schema["components"]["securitySchemes"] = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Enter **Bearer <token>"
        }
    }
    api_router = [r for r in app.routes if isinstance(r, APIRoute)]

    for r in api_router:
        path = getattr(r, "path")
        endpoint = getattr(r, "endpoint")
        methods = [m.lower() for m in getattr(r, "methods")]
        for m in methods:
            if (
                re.search("jwt_required", inspect.getsource(endpoint)) or
                re.search("fresh_jwt_requied", inspect.getsource(endpoint)) or
                re.search("jwt_optional", inspect.getsource(endpoint))
            ):
                openapi_schema["paths"][path][m]["security"] = [
                    {
                        "Bearer Auth": []
                    }
                ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth_router)
app.include_router(order_router)
