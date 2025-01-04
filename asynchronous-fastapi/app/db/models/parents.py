from sqlalchemy import Column, Date, Numeric, String
from sqlalchemy.orm import relationship

from app.db.models.base import Base, BaseDBModel
from app.db.models.metadata import metadata_family


class Parent(Base, BaseDBModel):
    __metadata__ = metadata_family

    name = Column(String)
    birthdate = Column(Date)
    height = Column(Numeric)

    children = relationship("Child", back_populates="parent")