import sys
sys.path.append("..")

import schema
from fastapi import APIRouter, Depends, HTTPException
import models
from database import engine, get_db
from sqlalchemy.orm import Session
from .auth import get_current_user, get_user_exception, verify_password, get_password_hash

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"Description": "not found"}}
)

models.Base.metadata.create_all(bind=engine)


@router.get("/")
async def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.Users).all()


@router.get("/{user_id}")
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/search")
async def find_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/")
async def modify_user(
        user_model: schema.User,
        db: Session = Depends(get_db),
        user: dict = Depends(get_current_user)
):
    if user is None:
        raise get_user_exception()
    user_modify = models.Users
    user_modify.email = user_model.email
    user_modify.username = user_model.username
    user_modify.first_name = user_model.first_name
    user_modify.last_name = user_model.last_name
    user_modify.hashed_password = get_password_hash(user_model.password)

    db.add(user_modify)
    db.commit()
    return {"status": 201}


@router.delete("/")
async def delete_user(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    if user is None:
        raise get_user_exception()
    user_model = db.query(models.Users).filter(models.Users.id == user.get("id")).first()
    if user_model is None:
        return "Invalid user"
    db.query(models.Users).filter(models.Users.id == user.get("id")).delete()
    db.commit()
    return {"status": 200}
