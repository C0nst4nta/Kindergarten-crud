from app.db.models.children import Child as ChildModel
from app.db.repositories.base import SQLAlchemyRepository
from app.models.domain.children import ChildCreate
from app.models.utility_schemas.children import ChildOptionalSchema


class ChildRepository(SQLAlchemyRepository):
    sqla_model = ChildModel

    create_schema = ChildCreate
    read_optional_schema = ChildOptionalSchema