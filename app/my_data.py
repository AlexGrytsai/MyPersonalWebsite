import json

programming_languages = [
    "Python",
]

frameworks = ["Django", "Django REST Framework", "FastAPI"]

db = [
    "PostgreSQL",
    "Redis",
    "Azure SQL",
    "SQLite",
]

clouds = {
    "AWS": [
        "EC2",
        "S3",
        "RDS",
        "Lambda",
        "DynamoDB",
    ],
    "Azure": [
        "Azure SQL",
        "Functions",
        "Container Apps",
        "Container Registry",
        "Key Vault",
        "Redis for Cache",
    ],
    "Google Cloud": [
        "Cloud Storage",
        "Cloud Run",
        "Secret Manager",
        "Logging",
        "Artifact Registry",
        "Cloud Tasks",
        "Compute Engine",
        "Cloud Build",
    ],
}

container = ["Docker", "Docker Compose"]

vcs = ["Git", "GitHub", "GitHub Actions", "CI/CD"]

another_hard_skills = [
    "OOP",
    "Algorithms and Data Structures",
    "REST API",
    "Unit Testing",
    "Asynchronous Python",
    "HTML",
    "CSS",
]

project_management_skills = [
    "Agile",
    "Scrum",
    "Kanban",
    "Leadership & Team management",
]

soft_skills = [
    "Effective Communication",
    "Teamwork",
    "Leadership",
    "Time Management",
    "Critical Thinking",
    "Problem Solving",
    "Adaptability",
    "Stress Management",
    "Planning Skills",
]

my_skills = {
    "Programming Languages": programming_languages,
    "Frameworks": frameworks,
    "Databases": db,
    "Cloud Services": clouds,
    "Containerization": container,
    "Version Control Systems": vcs,
    "Other Hard Skills": another_hard_skills,
    "Project Management Skills": project_management_skills,
}

bio = [
    "I am a Python developer specializing in Python, Django,"
    "the Django REST Framework (DRF), and Docker.",
    "I have expertise in PostgreSQL, Redis, and Azure SQL databases,"
    "as well as working with Azure, GCP and AWS cloud services. ",
    "Before transitioning to IT, I worked as an engineer "
    "designing engineering networks and as a project group leader, ",
    "where I developed strong organizational and communication skills.",
    "This experience honed my ability to solve complex problems, "
    "manage teamwork, and make independent decisions.",
]

info = {
    "name": "Oleksandr Grytsai",
    "profession": "Python Developer",
    "skills": my_skills,
    "bio": bio,
    "languages": {"English": "Intermediate", "Ukrainian": "Native"},
}

info_json = json.dumps(info, indent=4)
