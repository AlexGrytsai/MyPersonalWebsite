# FastAPI Resume API

## Overview

This project is a personal backend API styled as an interactive resume or
portfolio site for a backend developer. Built with **FastAPI**, the API
organizes professional information into structured endpoints, making it easy to
showcase skills, experience, and contact information in a programmatic format.

The API is designed to provide detailed information about the developer's:

- Professional background

- Technical skills

- Work experience
    
- Educational courses

- Contact details

## Features

- **Structured API Endpoints**: Organized endpoints for accessing various
  sections like programming languages, frameworks, databases, etc.

- **Interactive Documentation**: Automatically generated API documentation
  using Swagger UI and ReDoc.

- **Markdown Support**: Styled descriptions and sections rendered as Markdown.

- **Expandable Design**: Easily extendable to include additional data or
  sections.

## Requirements

- Python 3.12+

- Poetry for dependency management

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/AlexGrytsai/MyPersonalWebsite.git
   cd MyPersonalWebsite
   ```

2. Install dependencies using Poetry:

   ```
   poetry install
   ```

3. Run the FastAPI server:

   ```
   poetry run uvicorn app.main:app --reload
   ```

4. Access the API documentation:

    - Swagger UI: http://127.0.0.1:8000

    - ReDoc: http://127.0.0.1:8000/redoc

## Endpoints Overview

The API includes endpoints to retrieve information about:

- About Me: Professional biography and background.

- Skills: Programming languages, frameworks, databases, and more.

- Work Experience: Details of past work roles and achievements.

- Contact Information: Links to social profiles and email.

## Purpose

This API serves as a portfolio for showcasing the developer's technical
expertise and professional journey.
It can be utilized as a backend for a frontend application or accessed directly
via API clients for programmatic exploration of the data.

## Author

- **Oleksandr Grytsai**

- [GitHub](https://github.com/AlexGrytsai)

- [LinkedIn](https://www.linkedin.com/in/alexgrytsai/)

- [Telegram](https://t.me/grytsai)