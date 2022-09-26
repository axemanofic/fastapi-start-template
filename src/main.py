from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from .config.settings import settings

from .api.base_template_router.endpoints import template_router


app = FastAPI(
    title=settings.app.title,
    description=settings.app.description,
    version=settings.app.version,
    debug=settings.secrets.DEBUG,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.secrets.CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.secrets.ALLOWED_HOSTS
)

app.include_router(template_router)
