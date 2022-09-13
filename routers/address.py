import sys
sys.path.append("..")

from typing import Optional
from fastapi import APIRouter, Depends
import models
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from schema import Address
from .auth import get_current_user, get_user_exception


router = APIRouter(
    prefix="/address",
    tags=['address'],
    responses={404: {"description": "Not Found"}}
)


@router.post("/")
async def create_address(address: Address, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    address_model = models.Address()
    address_model.address = address.address
    address_model.address2 = address.address2
    address_model.city = address.city
    address_model.post_code = address.post_code
    address_model.country = address.country
    address_model.apt_num = address.apt_num

    db.add(address_model)
    # Does not save but creates an instance with pk etc
    db.flush()

    user_model = db.query(models.Users).filter(models.Users.id == user.get("id")).first()
    user_model.address_id = address_model.id

    db.add(user_model)
    db.commit()

    return {"Success": 201}

