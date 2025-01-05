from fastapi import APIRouter

from app.api.routes import children, parents, emails
from app.core.tags_metadata import parents_tag, children_tag


router = APIRouter()

router.include_router(children.router, prefix="/children", tags=[children_tag.name])
router.include_router(parents.router, prefix="/parents", tags=[parents_tag.name])
router.include_router(emails.router)
