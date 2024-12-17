from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

from app.description_section import description
from app.my_data import bio, experience, another_hard_skills, soft_skills, \
    my_skills, project_management_skills

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
    "/all-my-hard-skills",
    tags=["Information"],
    summary="Information about me",
    description="Retrieve all my hard skills at one place.",
)
async def all_my_hard_skills():
    return my_skills


@app.get(
    "/programming-languages",
    tags=["Information"],
    summary="List of programming languages",
    description="Retrieve a list of programming languages I have experience "
                "working with.",
)
async def my_programming_languages():
    return my_skills["Programming Languages"]


@app.get(
    "/frameworks",
    tags=["Information"],
    summary="List of frameworks",
    description="Retrieve a list of frameworks I have experience "
                "working with.",
)
async def my_frameworks():
    return my_skills["Frameworks"]


@app.get(
    "/database",
    tags=["Information"],
    summary="List of databases",
    description="Retrieve a list of databases I have experience "
                "working with.",
)
async def my_dbs():
    return my_skills["Databases"]


@app.get(
    "/cloud-services",
    tags=["Information"],
    summary="List of Clouds",
    description="Retrieve a list of cloud services I have experience "
                "working with.",
)
async def cloud_services_list():
    return my_skills["Cloud Services"]


@app.get(
    "/container",
    tags=["Information"],
    summary="List of container technology",
    description="Retrieve a list of container technology I have experience "
                "working with.",
)
async def containers():
    return my_skills["Containerization"]


@app.get(
    "/vcs",
    tags=["Information"],
    summary="Version control system",
    description="Retrieve a list of container technology I have experience "
                "working with.",
)
async def version_control():
    return my_skills["Version Control Systems"]


@app.get(
    "/another-my-hard-skills",
    tags=["Information"],
    summary="My another hard skills",
    description="Retrieve a list of my another hard skills.",
)
async def another_skills():
    return another_hard_skills


@app.get(
    "/project-management-skills",
    tags=["Information"],
    summary="My project management skills",
    description="Retrieve a list of my project management skills.",
)
async def project_management():
    return project_management_skills


@app.get(
    "/soft-skills",
    tags=["Information"],
    summary="My soft skills",
    description="Retrieve a list of my soft skills.",
)
async def another_skills():
    return soft_skills


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
    return {
        "email": "your-email@example.com",
        "github": "https://github.com/your-profile",
        "linkedin": "https://linkedin.com/in/your-profile",
    }
