from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, Token
from app.database import SessionLocal
from app.models.user import User
from app.utils.security import verify_password, create_access_token, get_password_hash

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(SessionLocal)):
    hashed = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    return {"msg": "User created"}

@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(SessionLocal)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
