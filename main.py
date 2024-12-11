from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

from app.my_data import info_json, info

description = f"""
### Welcome to my professional site, which is styled like API documentation.**

\n
Explore details about my professional background, projects, and contact information, all presented through a structured API interface.
\n
[![My GitHub](https://img.shields.io/badge/GitHub-12100E.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AlexGrytsai)
[![My LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alexgrytsai/)
[![My Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/a.grytsai)
[![My Telegram](https://img.shields.io/badge/Telegram-26A5E4.svg?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/grytsai)
[![My Email](https://img.shields.io/badge/Email-D14836.svg?style=for-the-badge&logo=gmail&logoColor=white)](mailto:a.grytsai1987@gmail.com)

### Information

```json
    {info_json}
```
"""
app = FastAPI(
    title="Oleksandr Grytsai",
    description=description,
    version="1.0.0",
    docs_url=None,
    redoc_url=None
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
    "/me",
    tags=["Information"],
    summary="Information about me",
    description="This endpoint provides detailed information about "
                "my professional background, including my name, profession, "
                "technical skills, and biography.",
)
async def me():
    return info


@app.get(
    "/experience",
    tags=["Information"],
    summary="My work experience",
    description="In this section, you will find details about my work experience, ",
)
async def about():
    return {
        "experience": [
            {
                "role": "Python Developer",
                "location": "Kyiv, Ukraine",
                "duration": "07/2023 – present",
                "details": [
                    "Developed a commercial project for parsing tenders on Prozorro (prozorro.gov.ua).",
                    "Solved technical challenges including API limitations and caching with Redis Cloud.",
                    "Automated deployment to Azure Container Apps via GitHub Actions.",
                ],
            },
            {
                "role": "Design Engineer (Private Entrepreneur)",
                "location": "Kyiv, Ukraine",
                "duration": "2018 – 2023",
                "details": [
                    "Implemented over 50 projects that were built.",
                    "Introduced SCRUM into project development processes.",
                    "Developed a solution to automate design processes up to 90%."
                ],
            },
            {
                "role": "Design Engineer (LLC 'RBK Spetsmontazhbud')",
                "location": "Kyiv, Ukraine",
                "duration": "02/2013 – 12/2017",
                "details": [
                    "Implemented over 30 successful construction projects.",
                    "Partially automated the design process to improve efficiency."
                ],
            }
        ]
    }


@app.get("/projects", tags=["Проекты"])
async def projects():
    """Список проектов."""
    return [
        {"name": "Проект 1", "description": "Описание проекта 1",
         "url": "https://example.com"},
        {"name": "Проект 2", "description": "Описание проекта 2",
         "url": "https://example.com"},
    ]


@app.get("/contacts", tags=["Контакты"])
async def contacts():
    """Контактная информация."""
    return {
        "email": "your-email@example.com",
        "github": "https://github.com/your-profile",
        "linkedin": "https://linkedin.com/in/your-profile",
    }
