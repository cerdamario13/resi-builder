from setuptools import setup, find_packages

setup(
    name="resi-builder",
    version="0.2.0",
    author="Mario Cerda",
    author_email="cerdamario13@gmail.com",
    description="Create a resume and cover letter automatically",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(include=["resi", "resi.*"]),
    python_requires=">=3.10",
    url='https://github.com/cerdamario13/resi-builder',
)
