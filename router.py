from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import *
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

@router.post("/create-user")
async def create_user(request:RequestUser, db:Session=Depends(get_db)):
    crud.create_user(db, user=request.parameter)
    return Response(code=200, status="User added", message="User was added successfully").dict(exclude_none=True)

@router.get("/")
async def get_all_users(db:Session=Depends(get_db)):
    _users = crud.get_users(db, 0, 100)
    return Response(code=200, status="Fetched", message="Users fetched successfully", result=_users).dict(exclude_none=True)

@router.get("/{id}")
async def get_by_id(id:int, db:Session=Depends(get_db)):
    _user = crud.get_user_by_id(db, id)
    return Response(code=200, status="User Fetched", message="User was fetched successfully", result=_user).dict(exclude_none=True)

@router.post("/update-user")
async def user_update(request:RequestUser, db:Session=Depends(get_db)):
    _user = crud.update_user(db, user_id=request.parameter.id, username=request.parameter.username)
    return Response(code=200, status="User updated", message="User has been updated successfully", result=_user).dict(exclude_none=True)

@router.delete("/delete-user/{id}")
async def user_delete(id:int, db:Session=Depends(get_db)):
    crud.remove_user(db, user_id=id)
    return Response(code=200, status="User deleted", message="User has been deleted successfully").dict(exclude_none=True)
    