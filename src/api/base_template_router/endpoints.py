from fastapi.routing import APIRouter

template_router = APIRouter(prefix='/template', tags=['Template'])


@template_router.get('/')
def template():
    return {'response': 200}
