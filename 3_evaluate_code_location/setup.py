from setuptools import find_packages, setup

setup(
    name="3_evaluate",
    packages=find_packages(exclude=["3_evaluate_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pytest"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
    python_requires=">=3.10",
)
