from pydantic import BaseModel, EmailStr

class User(BaseModel):
    user_id: int
    user_name: str
    email: EmailStr
    password: str

class Transactions(BaseModel):
    transaction_id: int
    user_id: int
    type: bool 
    value: float
    category: str