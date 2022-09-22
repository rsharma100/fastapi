from pydantic import BaseModel, SecretStr, EmailStr

class DataInfo(BaseModel):
    file_name: str
    coll_name: str
    # class Config():
    #     orm_mode = True

class UserInfo(BaseModel):
    name: str
    mail: EmailStr
    password: str
    
    # class Config():
    #     orm_mode = True
class Login(BaseModel):
    mail: EmailStr
    password: SecretStr
    class Config:
        json_encoders = {
            SecretStr: lambda v: v.get_secret_value() if v else None
         }