from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.schemas.user_schema import UserCreate, UserLogin
from app.utils.security import hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    exisiting_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if exisiting_user:
        raise HTTPException(status_code=400, detail="Email já Cadastrado")
    
    new_user = models.User(
        user_name = user.user_name,
        email = user.email,
        password = hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Usuário criado com sucesso!!"}

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(
        models.User.email == data.email
    ).first()

    if not user:
        raise HTTPException(status_code=400, detail="Credenciais Inválidas")
    
    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=400, detail="Credenciais Inválidas")
    
    return {"message": "Login realizado com sucesso!!"}