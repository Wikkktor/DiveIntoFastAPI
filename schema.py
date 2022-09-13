from typing import Optional
from pydantic import BaseModel, Field


class CreateTodo(BaseModel):
    title: str = Field(min_length=1)
    description: Optional[str]
    priority: int = Field(gt=0, lt=6)
    complete: bool


class User(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str


class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str
    phone_number: str


class Address(BaseModel):
    address: str
    address2: str
    city: str
    post_code: str
    country: str
    apt_num: Optional[int]
