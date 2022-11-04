from sqlalchemy import Column, Integer, String, VARCHAR
from config import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column("user_id",Integer, primary_key=True)
    gender = Column("gender", String)
    username = Column("username", String)

    