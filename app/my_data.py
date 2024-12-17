import json

programming_languages = [
    {
        "name": "Python",
        "badge": "![Python](https://img.shields.io/badge/Python-3776AB?"
                 "style=for-the-badge&logo=python&logoColor=white)",
    },
]

frameworks = [
    {
        "name": "Django",
        "badge": "![Django](https://img.shields.io/badge/Django-092E20?"
                 "style=for-the-badge&logo=django&logoColor=white)",
    },
    {
        "name": "Django REST Framework",
        "badge": "![Django REST Framework](https://img.shields.io/badge/"
                 "Django%20REST%20Framework-092E20?"
                 "style=for-the-badge&logo=django&logoColor=white)",
    },
    {
        "name": "FastAPI",
        "badge": "![FastAPI](https://img.shields.io/badge/"
                 "FastAPI-009688?"
                 "style=for-the-badge&logo=fastapi&logoColor=white)",
    },
]

db = [
    {
        "name": "PostgreSQL",
        "badge": "![PostgreSQL](https://img.shields.io/badge/"
                 "PostgreSQL-336791?"
                 "style=for-the-badge&logo=postgresql&logoColor=white)",
    },
    {
        "name": "Redis",
        "badge": "![Redis](https://img.shields.io/badge/"
                 "Redis-DC382D?"
                 "style=for-the-badge&logo=redis&logoColor=white)",
    },
    {
        "name": "Azure SQL",
        "badge": "![Azure SQL](https://img.shields.io/badge/"
                 "Azure%20SQL-0089FF?"
                 "style=for-the-badge&logo=azure-sql&logoColor=white)",
    },
    {
        "name": "SQLite",
        "badge": "![SQLite](https://img.shields.io/badge/"
                 "SQLite-003B57?"
                 "style=for-the-badge&logo=sqlite&logoColor=white)",
    },
]

cloud_services = [
    {
        "name": "Google Cloud",
        "logo_url": "https://storage.googleapis.com/my-website-bucket/logos/"
                    "gcp/google-cloud.svg",
        "services": [
            {
                "name": "Cloud Storage",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/gcp/google-cloud-storage.svg",
            },
            {
                "name": "Cloud Run",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/gcp/cloud_run.svg",
            },
            {
                "name": "Secret Manager",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/gcp/key_management_service.svg",
            },
            {
                "name": "Logging",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/gcp/google-cloud-logging.svg",
            },
            {
                "name": "Container Registry",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/gcp/container_registry.svg",
            },
            {
                "name": "Cloud Tasks",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/gcp/cloud_tasks.svg",
            },
            {
                "name": "Compute Engine",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/gcp/google-compute-engine.svg",
            },
            {
                "name": "Cloud Build",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/gcp/google-cloud-build.svg",
            }
        ],
    },
    {
        "name": "Azure",
        "logo_url": "https://storage.googleapis.com/my-website-bucket/logos/"
                    "azure/microsoft-azure.svg",
        "services": [
            {
                "name": "Azure SQL",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/azure/sql-database-generic.svg",
            },
            {
                "name": "Functions",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/azure/functions.svg",
            },
            {
                "name": "Container Apps",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/azure/Azure%20Container%20Apps.svg",
            },
            {
                "name": "Container Registry",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/azure/container-registry.svg",
            },
            {
                "name": "Key Vault",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/azure/key-vault.svg",
            },
            {
                "name": "Redis for Cache",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/azure/cache-redis-product-icon.svg",
            },
        ],
    },
    {
        "name": "AWS",
        "logo_url": "https://storage.googleapis.com/my-website-bucket/logos/"
                    "aws/Amazon_Web_Services_Logo.svg",
        "services": [
            {
                "name": "EC2",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/aws/ec2.svg",
            },
            {
                "name": "S3",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/aws/amazon-s3.svg",
            },
            {
                "name": "RDS",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/aws/amazon-rds.svg",
            },
            {
                "name": "DynamoDB",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/aws/amazon-dynamodb.svg",
            },
            {
                "name": "Lambda",
                "logo_url": "https://storage.googleapis.com/my-website-bucket/"
                            "logos/aws/lambda-function.svg",
            }
        ],
    },
]

container = [
    {
        "name": "Docker",
        "badge": "![Docker](https://img.shields.io/badge/"
                 "Docker-2496ED?"
                 "style=for-the-badge&logo=docker&logoColor=white)",
    },
    {
        "name": "Docker Compose",
        "badge": "![Docker Compose](https://img.shields.io/badge/"
                 "Docker%20Compose-2496ED?"
                 "style=for-the-badge&logo=docker&logoColor=white)",
    },
]

vcs = [
    {
        "name": "Git",
        "badge": "![Git](https://img.shields.io/badge/"
                 "Git-F05032?style=for-the-badge&logo=git&logoColor=white)",
    },
    {
        "name": "GitHub",
        "badge": "![GitHub](https://img.shields.io/badge/"
                 "GitHub-181717?"
                 "style=for-the-badge&logo=github&logoColor=white)",
    },
    {
        "name": "GitHub Actions",
        "badge": "![GitHub Actions](https://img.shields.io/badge/"
                 "GitHub%20Actions-2088FF?"
                 "style=for-the-badge&logo=github-actions&logoColor=white)",
    },
    {
        "name": "CI/CD",
        "badge": "![CI/CD](https://img.shields.io/badge/"
                 "CI%2FCD-FF4F00?"
                 "style=for-the-badge&logo=github-actions&logoColor=white)",
    },
]

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
    "Cloud Services": cloud_services,
    "Containerization": container,
    "Version Control Systems": vcs,
    "Other Hard Skills": another_hard_skills,
    "Project Management Skills": project_management_skills,
}

courses = [
    {
        "name": "AWS Fundamentals",
        "platform": "Coursera",
        "url": "https://coursera.org/share/defdf30529af4e9b7499863db1873ee7",
        "badge_url": "",
    },
    {
        "name": "Endpoint Security",
        "platform": "Cisco Networking Academy",
        "url":
            "https://www.credly.com/badges/"
            "5f679577-9245-4d9f-94f2-3e109d7553b3",
        "badge_url": "https://images.credly.com/size/340x340/images/"
                     "0ca5f542-fb5e-4a22-9b7a-c1a1ce4c3db7/"
                     "EndpointSecurity.png",
    },
    {
        "name": "Networking Basics",
        "platform": "Cisco Networking Academy",
        "url":
            "https://www.credly.com/badges/"
            "633b006c-d312-44f3-a96b-b74dda19975b",
        "badge_url": "https://images.credly.com/size/340x340/images/"
                     "5bdd6a39-3e03-4444-9510-ecff80c9ce79/image.png",
    },
    {
        "name": "Introduction to Cybersecurity",
        "platform": "Cisco Networking Academy",
        "url":
            "https://www.credly.com/badges/"
            "c74236b2-ff54-4ada-a403-a72c982b920e",
        "badge_url": "https://images.credly.com/size/340x340/images/"
                     "af8c6b4e-fc31-47c4-8dcb-eb7a2065dc5b/I2CS__1_.png",
    },
]

languages = {
    "English": "Intermediate",
    "Ukrainian": "Native",
}

bio = [
    "I am a backend developer with over 1 year of experience specializing "
    "in Python, Django, the Django REST Framework (DRF), and Docker.",
    "I have experience with PostgreSQL, Redis, and Azure SQL databases, "
    "as well as working with Azure and AWS cloud services.",
    "Before transitioning to IT, I worked as an engineer designing "
    "engineering networks and as a project group leader.",
    "These roles helped me develop strong organizational "
    "and communication skills, as I had to manage teamwork, coordinate "
    "with multiple teams, and make independent decisions. "
    "This experience also honed my ability to solve complex, "
    "non-trivial problems. I am confident that my previous experience, "
    "combined with my technical skills, will contribute to "
    "my success as a developer.",
    "I am always seeking opportunities "
    "to grow and improve as a specialist, which helps "
    "me continue moving forward.",
]

experience = [
    {
        "role": "Python Developer (Private Entrepreneur)",
        "location": "Kyiv, Ukraine",
        "duration": "07/2023 – present",
        "details": [
            "Developed a commercial project for parsing tenders on "
            "Prozorro (prozorro.gov.ua).",
            "Solved technical challenges including API limitations "
            "and caching with Redis Cloud.",
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
            "Developed a solution to automate design processes up to 90%.",
        ],
    },
    {
        "role": "Design Engineer (LLC 'RBK Spetsmontazhbud')",
        "location": "Kyiv, Ukraine",
        "duration": "02/2015 – 12/2017",
        "details": [
            "Implemented over 30 successful construction projects.",
            "Partially automated the design process to improve efficiency.",
        ],
    },
    {
        "role": "External Engineering Networks Engineer ("
                "LLC 'Construction Company Intergal-Bud')",
        "location": "Kyiv, Ukraine",
        "duration": "08/2013 – 01/2015",
        "details": [
            "Built the process of development, control and construction "
            "of engineering networks of water supply and sewage on the part "
            "of the customer company and the investor.",
        ],
    },
]
