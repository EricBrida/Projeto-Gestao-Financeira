from pydantic import BaseModel

class Transactions(BaseModel):
    transaction_id: int
    user_id: int
    type: bool 
    value: float
    category: str