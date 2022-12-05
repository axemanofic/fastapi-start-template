from string import Template

schemas_template = Template("""
from pydantic import BaseModel
""")

endpoints_template = Template("""
from fastapi.routing import APIRouter

router = APIRouter(prefix='/$app_name', tags=['$app_name'])
""")