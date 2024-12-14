from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

from app.description_section import description
from app.my_data import bio, experience

app = FastAPI(
    title="Oleksandr Grytsai",
    description=description,
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
)


@app.get("/", include_in_schema=False)
async def custom_docs():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title,
    )


@app.get("/redoc", include_in_schema=False)
async def redoc_docs():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - ReDoc",
    )


@app.get(
    "/about-me",
    tags=["Information"],
    summary="Information about me",
    description="This endpoint provides detailed information about "
    "my professional background, including my name, profession, "
    "technical skills, and biography.",
)
async def me():
    return bio


@app.get(
    "/experience",
    tags=["Information"],
    summary="My work experience with out details",
    description="In this section, you will find my work experience "
    "with out details.",
)
async def experience_short():
    short_details = [
        {k: v for k, v in exp.items() if k != "details"} for exp in experience
    ]
    return short_details


@app.get(
    "/experience-details",
    tags=["Information"],
    summary="My work experience with details",
    description="My work experience with details.",
)
async def experience_full():
    return experience


@app.get("/projects", tags=["Проекты"])
async def projects():
    """Список проектов."""
    return [
        {
            "name": "Проект 1",
            "description": "Описание проекта 1",
            "url": "https://example.com",
        },
        {
            "name": "Проект 2",
            "description": "Описание проекта 2",
            "url": "https://example.com",
        },
    ]


@app.get("/contacts", tags=["Контакты"])
async def contacts():
    """Контактная информация."""
    return {
        "email": "your-email@example.com",
        "github": "https://github.com/your-profile",
        "linkedin": "https://linkedin.com/in/your-profile",
    }
