from setuptools import find_packages, setup

setup(
    name="shared",
    packages=find_packages(),
    install_requires=[],  # shared_code_location has no install_requires, as it is only used as a local dependency.
    python_requires=">=3.10",
)
