from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_active:Optional[bool]
    is_staff:Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff":False,
                "is_active": True,
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str = \
        "4e9aa79b2027fe0495692e1670f558e51dc322eabe754184deafd4e22eb5a482"

class LoginModel(BaseModel):
    username:str
    password:str

class OrderModel(BaseModel):
    id=Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"