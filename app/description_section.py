from app.transformation_data_for_markdown import MarkdownTransformer

my_data = MarkdownTransformer()

description = f"""
### Welcome to my professional site, which is styled like API documentation.

Explore details about my professional background, projects, 
and contact information, all presented through a structured API interface.

[![My GitHub](https://img.shields.io/badge/GitHub-12100E.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AlexGrytsai)
[![My LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alexgrytsai/)
[![My Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/a.grytsai)
[![My Telegram](https://img.shields.io/badge/Telegram-26A5E4.svg?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/grytsai)
[![My Email](https://img.shields.io/badge/Email-D14836.svg?style=for-the-badge&logo=gmail&logoColor=white)](mailto:a.grytsai1987@gmail.com)
---
---

{my_data.bio_section()}

[![My Resume](https://img.shields.io/badge/Resume-Download-blue)](https://storage.googleapis.com/my-website-bucket/Oleksandr-Grytsai-Python-Developer.pdf)

---
---
### Programming languages
{my_data.programming_languages_section()}
---
---
### Main frameworks
{my_data.frameworks_section()}
---
---
### Databases
{my_data.data_bases_section()}
---
---
### Cloud services
{my_data.cloud_services_section()}
### Container
{my_data.container_section()}
---
---
### Version control systems
{my_data.vcs_section()}
---
---
### Other hard skills
{my_data.another_hard_skills_section()}
---
---
### Project management skills
{my_data.project_management_skills_section()}
---
---
### Soft skills
{my_data.soft_skills_section()}
---
---
### Experience
{my_data.experience_section()}
---
---
### Courses
{my_data.courses_section()}
---
---
### Languages
{my_data.languages_section()}
"""
