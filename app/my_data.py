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

courses = [
    {
        "name": "Endpoint Security",
        "platform": "Cisco Networking Academy",
        "url": "https://www.credly.com/badges/5f679577-9245-4d9f-94f2-3e109d7553b3"
    },
    {
        "name": "Networking Basics",
        "platform": "Cisco Networking Academy",
        "url": "https://www.credly.com/badges/633b006c-d312-44f3-a96b-b74dda19975b"
    },
    {
        "name": "Introduction to Cybersecurity",
        "platform": "Cisco Networking Academy",
        "url": "https://www.credly.com/badges/c74236b2-ff54-4ada-a403-a72c982b920e"
    },
    {
        "name": "AWS Fundamentals",
        "platform": "Coursera",
        "url": "https://coursera.org/share/defdf30529af4e9b7499863db1873ee7"
    }
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
    "my success as a developer. I am always seeking opportunities "
    "to grow and improve as a specialist, which helps "
    "me continue moving forward.",
]

experience = [
    {
        "role": "Python Developer",
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

info = {
    "Name": "Oleksandr Grytsai",
    "Profession": "Python Developer",
    "Bio": bio,
    "Skills": my_skills,
    "Courses": courses,
    "Experience": experience,
    "Languages": languages,
}

info_json = json.dumps(info, indent=4)
