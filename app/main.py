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
    summary="Retrieve detailed information about me",
    description="This endpoint provides detailed information about "
                "my name, profession, biography, and technical skills.",
)
async def me():
    return bio


@app.get(
    "/all-my-hard-skills",
    tags=["Information"],
    summary="Retrieve all hard skills",
    description="This endpoint provides a comprehensive list of all "
                "my hard skills, including technical and professional skills.",
)
async def all_my_hard_skills():
    return my_skills


@app.get(
    "/programming-languages",
    tags=["Information"],
    summary="List of programming languages",
    description="This endpoint returns a list of programming languages "
                "I have expertise in.",
)
async def my_programming_languages():
    return my_skills["Programming Languages"]


@app.get(
    "/frameworks",
    tags=["Information"],
    summary="List of frameworks",
    description="This endpoint provides a list of frameworks "
                "I have experience working with.",
)
async def my_frameworks():
    return my_skills["Frameworks"]


@app.get(
    "/database",
    tags=["Information"],
    summary="List of databases",
    description="This endpoint lists the databases I have worked with "
                "and have experience managing.",
)
async def my_dbs():
    return my_skills["Databases"]


@app.get(
    "/cloud-services",
    tags=["Information"],
    summary="List of cloud services",
    description="This endpoint provides a list of cloud platforms "
                "and services I have experience using.",
)
async def cloud_services_list():
    return my_skills["Cloud Services"]


@app.get(
    "/container",
    tags=["Information"],
    summary="List of container technologies",
    description="This endpoint provides a list of containerization "
                "technologies I have experience working with.",
)
async def containers():
    return my_skills["Containerization"]


@app.get(
    "/vcs",
    tags=["Information"],
    summary="List of version control systems",
    description="This endpoint provides a list of version control systems "
                "I have used in my projects.",
)
async def version_control():
    return my_skills["Version Control Systems"]


@app.get(
    "/another-my-hard-skills",
    tags=["Information"],
    summary="Additional hard skills",
    description="This endpoint provides a list of my additional hard "
                "skills beyond the main categories.",
)
async def another_skills():
    return another_hard_skills


@app.get(
    "/project-management-skills",
    tags=["Information"],
    summary="Project management skills",
    description="This endpoint provides a list of my project management "
                "skills, including methodologies and tools.",
)
async def project_management():
    return project_management_skills


@app.get(
    "/soft-skills",
    tags=["Information"],
    summary="Soft skills",
    description="This endpoint provides a list of my soft skills, "
                "focusing on interpersonal and communication abilities.",
)
async def soft_skills_endpoint():
    return soft_skills


@app.get(
    "/experience",
    tags=["Information"],
    summary="Work experience",
    description="This endpoint provides an overview of my professional "
                "work experience, including roles and achievements.",
)
async def work_experience():
    return experience


@app.get(
    "/contacts",
    tags=["Information"],
    summary="Contact information",
    description="This endpoint provides links and details to connect with me "
                "via email, GitHub, LinkedIn, Facebook, and Telegram.",
)
async def contacts():
    return {
        "email": "grytsai.alex@gmail.com",
        "github": "https://github.com/AlexGrytsai",
        "linkedin": "https://www.linkedin.com/in/alexgrytsai/",
        "facebook": "https://www.facebook.com/a.grytsai",
        "telegram": "https://t.me/grytsai",
    }
