from src.ai import AIEngine
from src.config import config_instance

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

settings = config_instance().application

app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    terms_of_service=settings.TERMS,
    contact={
        "name": settings.CONTACT_NAME,
        "url": settings.CONTACT_URL,
        "email": settings.CONTACT_EMAIL
    },
    license_info={
        "name": settings.LICENSE_NAME,
        "url": settings.LICENSE_URL,
    },
    docs_url=settings.DOCS_URL,
    openapi_url=settings.OPENAPI_URL,
    redoc_url=settings.REDOC_URL)

templates = Jinja2Templates(directory="src/templates")

ai_engine = AIEngine()


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home", "message": "Hello, World!"})
