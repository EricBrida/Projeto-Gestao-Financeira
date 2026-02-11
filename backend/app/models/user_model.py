from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

# Criação da Tabela User no Banco de dados
class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    transactions = relationship("Transactions", back_populates="users")