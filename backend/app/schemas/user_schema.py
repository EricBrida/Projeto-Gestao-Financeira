from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    user_name: str
    password: str

class UserLogin(UserBase):
    password: str