#!/usr/bin/env python3
import sys
import subprocess
import os
from pathlib import Path
import argparse
import shutil

CODE_LOCATIONS = [
    "1_etl_code_location",
    "2_model_code_location",
    "3_evaluate_code_location",
    "4_deploy_code_location",
]


def setup():
    root_venv = Path(".venv")
    if not root_venv.exists():
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)

    subprocess.run([".venv/bin/pip", "install", "--upgrade",
                   "pip", "setuptools", "wheel"], check=True)
    subprocess.run([".venv/bin/pip", "install", "-r",
                   "requirements.txt"], check=True)

    for loc in CODE_LOCATIONS:
        venv_path = Path(loc) / ".venv"
        if not venv_path.exists():
            subprocess.run([sys.executable, "-m", "venv",
                           ".venv"], cwd=loc, check=True)

        subprocess.run([".venv/bin/pip", "install", "--upgrade",
                       "pip", "setuptools", "wheel"], cwd=loc, check=True)
        # Install shared_code_location in editable mode before the local package
        subprocess.run([".venv/bin/pip", "install", "-e",
                       "../shared_code_location"], cwd=loc, check=True)
        subprocess.run([".venv/bin/pip", "install", "-e", "."],
                       cwd=loc, check=True)
    print("Setup complete! Activate the root .venv before running Dagster commands.")

    sys.exit(0)


def clean():
    for loc in CODE_LOCATIONS + ["."]:
        venv_path = Path(loc) / ".venv"
        if venv_path.exists():
            shutil.rmtree(venv_path)
    for p in Path(".").rglob("__pycache__"):
        shutil.rmtree(p)
    print("Cleaned all .venv and __pycache__ directories.")
    sys.exit(0)


def test():
    for loc in CODE_LOCATIONS:
        venv_python = Path(loc) / ".venv/bin/python"
        if venv_python.exists():
            subprocess.run([str(venv_python), "-m", "pytest"], cwd=loc)

    print("Testing complete.")
    sys.exit(0)


def dev(location=None):
    # Persist Dagster instance data to example_persistent_home
    env = os.environ.copy()
    env["DAGSTER_HOME"] = str(Path("example_persistent_home").absolute())
    dagster_executable = Path(".venv/bin/dagster")
    if location:
        if location not in CODE_LOCATIONS:
            print(
                f"Error: unknown location '{location}'. Choose from {CODE_LOCATIONS}.", file=sys.stderr)
            sys.exit(1)
        loc_dir = location
        workspace_path = Path("../workspace.yaml")
        subprocess.run([str(dagster_executable), "dev", "-w",
                       str(workspace_path)], cwd=loc_dir, check=True, env=env)
    else:
        subprocess.run([str(dagster_executable), "dev",
                       "-w", "workspace.yaml"], check=True, env=env)
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description="Project orchestration commands.")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser(
        "setup", help="Set up all Python environments and install dependencies.")
    subparsers.add_parser(
        "clean", help="Remove all virtual environments and Python caches.")
    subparsers.add_parser("test", help="Run pytest in all code locations.")
    dev_parser = subparsers.add_parser(
        "dev", help="Start Dagster dev webserver for all or a single code location.")
    dev_parser.add_argument("location", nargs="?",
                            help="Code location to serve.")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)
    if args.command == "setup":
        setup()
    elif args.command == "clean":
        clean()
    elif args.command == "test":
        test()
    elif args.command == "dev":
        dev(args.location)


if __name__ == "__main__":
    main()
