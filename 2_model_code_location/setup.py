from setuptools import find_packages, setup

setup(
    name="2_model",
    packages=find_packages(exclude=["2_model_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pytest"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
    python_requires=">=3.10",
)
