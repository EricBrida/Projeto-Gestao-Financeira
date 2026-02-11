from sqlalchemy import Column, Integer, String, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class TransactionType(enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"

# Criação da Table de Transações Financeiras do Usuario
class Transactions(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, nullable=False)
    category = Column(String)
    type = Column(Enum(TransactionType), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="transactions")