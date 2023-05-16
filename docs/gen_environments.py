from pathlib import Path

import mkdocs_gen_files
import yaml

nav = mkdocs_gen_files.Nav()  # type: ignore

environments = (Path(__file__).parent.parent / "environments").glob("*")

ENVIRONMENTS_DICT = {}

FILES_SOURCE = ("0-desy-pinned.yml", "1-base.yml", "2-custom.yml")
FILES_GENERATED = ("environment.yml", "environment.lock.yml")
FILES = set(FILES_SOURCE) | set(FILES_GENERATED)


def generate_table(packages, lock_dict):
    text = "| Package | Version |\n" + "| --- | --- |\n"
    for package in packages:
        package = package.split("=")[0]
        version = lock_dict.get(package, package.split("=")[-1])
        text += f"| {package} | {version} |\n"

    text += "\n"
    return text


for environment in environments:
    name = environment.name
    files = {f: environment / f for f in FILES}
    files = {k: v for k, v in files.items() if v.exists()}

    page = f"environments/{name}.md"

    yamls = {k: yaml.safe_load(v.read_text()) for k, v in files.items()}

    lock_dict = {
        dep.split("=")[0]: "=".join(dep.split("=")[1:])
        for dep in yamls["environment.lock.yml"]["dependencies"]
    }

    page_rel = Path(page).relative_to("environments")
    nav[page_rel.with_suffix("").parts] = page_rel  # type: ignore

    with mkdocs_gen_files.open(page, "w") as f:
        text = f"# {name}\n"

        for category in FILES_SOURCE:
            if category in yamls:
                text += f"\n## {category}\n"
                text += generate_table(yamls[category]["dependencies"], lock_dict)

        text += "## environment.lock.yml\n"
        text += "| Package | Version |\n"
        text += "| --- | --- |\n"
        for package, version in lock_dict.items():
            text += f"| {package} | {version} |\n"

        f.write(text)

    mkdocs_gen_files.set_edit_path(page, "gen_pages.py")

    ENVIRONMENTS_DICT[name] = page

mkdocs_gen_files.set_edit_path("environments.md", "gen_pages.py")

index_file = Path(__file__).parent / "environments.md"
index = index_file.read_text()

with mkdocs_gen_files.open("environments.md", "w") as f:
    text = "".join(
        f"- [{name}]({filename})\n" for name, filename in ENVIRONMENTS_DICT.items()
    )
    f.write(index.replace("{{ ENVIRONMENT_LIST }}", text))

with mkdocs_gen_files.open("environments/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
