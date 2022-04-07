"""
Runs tests and other routines.

Usage:
  1. Install "nox"
  2. Run "nox" or "nox -s test"
"""

import nox
from pathlib import Path


@nox.session
def test(session):
    """Run pytests"""
    session.install("-e", ".[testing]")
    session.run("pytest")


@nox.session
def build(session):
    """Build source and wheel distribution"""
    session.run("python", "setup.py", "sdist")
    session.run("python", "setup.py", "bdist_wheel")


@nox.session(python=False)
def release_patch(session):
    """Generate release patch"""
    Path("dist").mkdir(exist_ok=True)
    with open("./dist/updates.patch", "w") as out:
        session.run(
            "git", "format-patch", "--stdout", "origin/main",
            external=True,
            stdout=out
        )
