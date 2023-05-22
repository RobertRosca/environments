from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()  # type: ignore

ROOT = Path(__file__).parent.parent

modules = list((ROOT / "modules").rglob("*"))
modules = [m for m in modules if m.is_file()]
modules = [m for m in modules if not (m.name.startswith(".") or "DEPRECATED" in str(m))]

MODULES_DICT = {}

PAGE_PREFIX = ""
if Path.cwd() != Path(__file__).parent.parent:
    PAGE_PREFIX = "euxfel-software-environments/"


for module in modules:
    name = module.relative_to(ROOT / "modules")
    page = module.relative_to(ROOT).with_suffix(".md")

    page_rel = page.relative_to("modules")
    nav[page_rel.with_suffix("").parts] = page_rel  # type: ignore

    if PAGE_PREFIX:
        page = PAGE_PREFIX + str(page)

    with mkdocs_gen_files.open(page, "w") as f:
        text = f"# `{name}`\n"
        text += f"```tcl\n{module.read_text()} \n```\n"
        f.write(text)

    mkdocs_gen_files.set_edit_path(page, "gen_modules.py")

with mkdocs_gen_files.open(f"{PAGE_PREFIX}modules/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
