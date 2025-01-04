from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import declarative_base, declarative_mixin
from sqlalchemy.sql import func


Base = declarative_base()

@declarative_mixin
class BaseDBModel:
    # autoinc pk key
    id = Column(Integer, primary_key=True, autoincrement=True)
    updated_at = Column(DateTime, server_default=func.now())
    __name__: str

    # if not declared generate tablename automatically based on class name 
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    __mapper_args__ = {"eager_defaults": True}