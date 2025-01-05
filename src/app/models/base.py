from pydantic import BaseModel


class BaseSchema(BaseModel):
    pass

class IDSchemaMixin(BaseModel):
    id: int

    class Config(BaseModel.Config):
        # allow database schematas mapping to ORM objects
        orm_mode = True