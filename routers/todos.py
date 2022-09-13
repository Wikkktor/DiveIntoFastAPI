import sys
sys.path.append("..")

from fastapi import APIRouter, Depends, HTTPException
import models
from database import engine, get_db
from sqlalchemy.orm import Session
import schema
from .auth import get_current_user, get_user_exception

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"Description": "not found"}}
)

models.Base.metadata.create_all(bind=engine)


@router.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@router.get("/user")
async def read_all_by_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    return db.query(models.Todos).filter(models.Todos.owner_id == user.get('id')).all()


@router.get("/{todo_id}")
async def todo_single(todo_id: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    todo = db.query(models.Todos) \
        .filter(models.Todos.id == todo_id) \
        .filter(models.Todos.owner_id == user.get('id')) \
        .first()
    if todo is not None:
        return todo
    raise http_exception_not_found()


@router.post("/")
async def create_todo(todo: schema.CreateTodo, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    todo_model.owner_id = user.get("id")
    db.add(todo_model)
    db.commit()

    return successful_response(201)


@router.put("/{todo_id}")
async def update_todo(todo_id: int,
                      todo: schema.CreateTodo,
                      user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    todo_model = db.query(models.Todos) \
        .filter(models.Todos.id == todo_id) \
        .filter(models.Todos.owner_id == user.get("id")) \
        .first()

    if todo_model is None:
        raise http_exception_not_found()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()
    return successful_response(200)


@router.delete("/{todo_id}")
async def delete_id(todo_id: int,
                    user: dict = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    todo_model = db.query(models.Todos) \
        .filter(models.Todos.id == todo_id) \
        .filter(models.Todos.owner_id == user.get("id")) \
        .first()
    if todo_model is None:
        raise http_exception_not_found()
    db.delete(todo_model)
    db.commit()
    return successful_response(201)


def successful_response(status_code: int):
    return {
        "status": status_code,
        "transaction": "Successful"
    }


def http_exception_not_found():
    return HTTPException(status_code=404, detail="TODO not found")
