from sqlalchemy.orm import Session
from model import User
from schemas import UserSchema

def get_users(db:Session, skip:int=0, limit:int=100):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db:Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db:Session, user: UserSchema):
    _user = User(gender=user.gender, username=user.username)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user

def remove_user(db:Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()

def update_user(db:Session, user_id:int, username:str):
    _user = get_user_by_id(db=db, user_id=user_id)
    _user.username = username
    db.commit()
    db.refresh(_user)
    return _user