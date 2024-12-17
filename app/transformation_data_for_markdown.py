from app.my_data import (
    cloud_services,
    programming_languages,
    frameworks,
    db,
    container,
    vcs, another_hard_skills, project_management_skills, bio, languages,
)


class MarkdownTransformer:
    """
    A class used to transform data into Markdown format.

    This class provides static methods to transform different types
    of data into Markdown format.
    """

    @staticmethod
    def bio_section() -> str:
        return "\n\n".join(bio)

    @staticmethod
    def programming_languages_section() -> str:
        return "".join(
            f"{language['badge']}\n" for language in programming_languages
        )

    @staticmethod
    def frameworks_section() -> str:
        return "".join(f"{framework['badge']}\n" for framework in frameworks)

    @staticmethod
    def data_bases_section() -> str:
        return "".join(f"{base['badge']}\n" for base in db)

    @staticmethod
    def container_section() -> str:
        return "\n".join(
            f"{container_item['badge']}" for container_item in container
        )

    @staticmethod
    def vcs_section() -> str:
        return "\n".join(f"{vcs_item['badge']}" for vcs_item in vcs)

    @staticmethod
    def cloud_services_section() -> str:
        cloud_services_list = []
        for cloud in cloud_services:
            cloud_logo = (
                f'<img src = "{cloud["logo_url"]}" alt="{cloud["name"]}" '
                f'width="50"> **{cloud["name"]}**\n'
            )
            for service in cloud["services"]:
                service_logo = (
                    f'<img src = "{service["logo_url"]}" '
                    f'alt="{service["name"]}" width ="30">'
                )
                cloud_logo += f"+ {service_logo} {service['name']}\n"
            cloud_services_list.append(cloud_logo)
            cloud_services_list.append("---")
            cloud_services_list.append("\n")

        return "\n".join(cloud_services_list)

    @staticmethod
    def another_hard_skills_section() -> str:
        return "\n".join(f"- {skill}" for skill in another_hard_skills)

    @staticmethod
    def project_management_skills_section() -> str:
        return "\n".join(f"- {skill}" for skill in project_management_skills)

    @staticmethod
    def soft_skills_section() -> str:
        return "\n".join(f"- {skill}" for skill in project_management_skills)

    @staticmethod
    def languages_section() -> str:
        return "".join(f"+ **{lang}**: {level}\n\n" for lang, level in languages.items())
