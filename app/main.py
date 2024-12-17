from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

from app.description_section import description
from app.my_data import bio, experience, programming_languages, frameworks

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
    "/programming-languages",
    tags=["Information"],
    summary="List of programming languages",
    description="Retrieve a list of programming languages I have experience "
                "working with.",
)
async def my_programming_languages():
    return [lang["name"] for lang in programming_languages]


@app.get(
    "/frameworks",
    tags=["Information"],
    summary="List of frameworks",
    description="Retrieve a list of frameworks I have experience "
                "working with.",
)
async def my_programming_languages():
    return [framework["name"] for framework in frameworks]


@app.get(
    "/experience",
    tags=["Information"],
    summary="My work experience",
    description="In this section, you will find my work experience.",
)
async def work_experience():
    return experience


@app.get("/contacts", tags=["Контакты"])
async def contacts():
    """Контактная информация."""
    return {
        "email": "your-email@example.com",
        "github": "https://github.com/your-profile",
        "linkedin": "https://linkedin.com/in/your-profile",
    }
