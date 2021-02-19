from sqlalchemy import Column, Integer, String
from sql_app.database import Base


class UserInfo(Base):
    __tablename__ = "user_login"

    id = Column(Integer, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    

