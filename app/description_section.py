from app.my_data import (
    experience,
    bio,
    programming_languages,
    frameworks,
    db,
    cloud_services,
    container,
    vcs,
    another_hard_skills,
    project_management_skills,
    soft_skills,
)

programming_languages_section = "".join(
    f"{language['badge']}\n" for language in programming_languages
)

frameworks_section = "".join(
    f"{framework['badge']}\n" for framework in frameworks
)

data_bases_section = "".join(f"{base['badge']}\n" for base in db)

cloud_services_section = "\n".join(
    f"{cloud['badge']}\n"
    + "\n".join(f"- {service}" for service in cloud["services"])
    + "\n"
    for cloud in cloud_services
)

container_section = "\n".join(
    f"{container_item['badge']}" for container_item in container
)

vcs_section = "\n".join(f"{vcs_item['badge']}" for vcs_item in vcs)

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

{"\n\n".join(bio)}

### Programming languages
{programming_languages_section}
---
---
### Main frameworks
{frameworks_section}
---
---
### Databases
{data_bases_section}
---
---
### Cloud services
| ![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white) | ![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white) | ![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white) |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| EC2<br>S3<br>RDS<br>Lambda<br>DynamoDB                                                                     | Azure SQL<br>Functions<br>Container<br>Apps<br>Container Registry<br>Key Vault<br>Redis for Cache                      | Cloud Storage<br>Cloud Run<br>Secret Manager<br>Logging<br>Artifact Registry<br>Cloud Tasks<br>Compute Engine<br>Cloud Build |
---
---

### Cloud services
<img src="https://storage.googleapis.com/my-website-bucket/logos/azure/microsoft-azure.svg" alt="Azure Logo" width="100">
| ![AWS Logo](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/aws.svg) | ![Azure Logo](https://cdn.svgporn.com/logos/microsoft-azure.svg) | ![Google Cloud Logo](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/google-cloud.svg) |
|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| ![EC2](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/aws-ec2.svg)<br>EC2 <br>![S3](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/aws-s3.svg)<br>S3 <br>![RDS](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/aws-rds.svg)<br>RDS <br>![Lambda](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/aws-lambda.svg)<br>Lambda <br>![DynamoDB](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/aws-dynamodb.svg)<br>DynamoDB | ![Azure SQL](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/microsoft-sql-server.svg)<br>Azure SQL <br>![Functions](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/azure-functions.svg)<br>Functions <br>![Container Apps](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/azure-container.svg)<br>Container Apps <br>![Key Vault](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/azure-key-vault.svg)<br>Key Vault | ![Cloud Storage](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/google-cloud-storage.svg)<br>Cloud Storage <br>![Cloud Run](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/google-cloud-run.svg)<br>Cloud Run <br>![Secret Manager](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/google-cloud-secret-manager.svg)<br>Secret Manager <br>![Logging](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/google-cloud-logging.svg)<br>Logging <br>![Cloud Build](https://raw.githubusercontent.com/gilbarbara/logos/master/logos/google-cloud-build.svg)<br>Cloud Build |



### Container
{container_section}
---
---
### Version control systems
{vcs_section}
---
---
### Other hard skills
{''.join(f'- {skill}\n' for skill in another_hard_skills)}
---
---
### Project management skills
{''.join(f'- {skill}\n' for skill in project_management_skills)}
---
---
### Soft skills
{''.join(f'- {skill}\n' for skill in soft_skills)}
---
---
### Experience
{''.join(f'- {exp["role"]}\n' for exp in experience)}
---
---
### Courses
![Endpoint Security](https://images.credly.com/size/340x340/images/0ca5f542-fb5e-4a22-9b7a-c1a1ce4c3db7/EndpointSecurity.png)
![Networking Basics](https://images.credly.com/size/340x340/images/5bdd6a39-3e03-4444-9510-ecff80c9ce79/image.png)
![Introduction to Cybersecurity](https://images.credly.com/size/340x340/images/af8c6b4e-fc31-47c4-8dcb-eb7a2065dc5b/I2CS__1_.png)

"""
