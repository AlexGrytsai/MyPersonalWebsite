import json

programming_languages = ["Python",]

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
        "Redis for Cache"
    ],
    "Google Cloud": [
        "Cloud Storage",
        "Cloud Run",
        "Secret Manager",
        "Logging",
        "Artifact Registry",
        "Cloud Tasks",
        "Compute Engine",
        "Cloud Build"
    ]
}

my_skills = [
    programming_languages,
    frameworks,
    "Docker",
    "Docker Compose",
    "Asynchronous Python",
    db,
    clouds,
    "GitHub Actions",
    "CI/CD"
]

bio = [
    "I am a Python developer specializing in Python, Django,"
    "the Django REST Framework (DRF), and Docker.",
    "I have expertise in PostgreSQL, Redis, and Azure SQL databases,"
    "as well as working with Azure, GCP and AWS cloud services. ",
    "Before transitioning to IT, I worked as an engineer "
    "designing engineering networks and as a project group leader, ",
    "where I developed strong organizational and communication skills.",
    "This experience honed my ability to solve complex problems, "
    "manage teamwork, and make independent decisions."
]

info = {
    "name": "Oleksandr Grytsai",
    "profession": "Python Developer",
    "skills": my_skills,
    "bio": bio,
    "languages": {
        "English": "Intermediate",
        "Ukrainian": "Native"
    }
}

info_json = json.dumps(info, indent=4)
