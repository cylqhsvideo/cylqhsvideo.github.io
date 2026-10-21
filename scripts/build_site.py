"""Package the repository's static files for GitHub Pages (Python 3)."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "_site"
EXCLUDED = {".git", ".github", ".gitignore", "README.md", "scripts", "_site"}


def build():
    index = ROOT / "index.html"
    if not index.is_file() or index.stat().st_size == 0:
        raise SystemExit("A non-empty index.html is required in the repository root.")

    # The only directory this script may remove is this repository's _site.
    if OUTPUT.is_symlink() or OUTPUT.resolve() != ROOT.resolve() / "_site":
        raise SystemExit("Refusing to replace an output path outside the repository.")
    if OUTPUT.exists():
        if not OUTPUT.is_dir():
            raise SystemExit("_site exists and is not a directory.")
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()

    for source in sorted(ROOT.iterdir()):
        if source.name in EXCLUDED:
            continue
        if source.is_symlink():
            raise SystemExit(f"Symbolic links are not supported: {source.name}")
        destination = OUTPUT / source.name
        if source.is_dir():
            shutil.copytree(source, destination)
        elif source.is_file():
            shutil.copy2(source, destination)

    (OUTPUT / ".nojekyll").touch()
    print(f"Static site ready: {OUTPUT}")


if __name__ == "__main__":
    build()
