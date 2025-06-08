from setuptools import find_packages, setup

setup(
    name="4_deploy",
    packages=find_packages(exclude=["4_deploy_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pytest"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
    python_requires=">=3.10",
)
