from setuptools import setup, find_packages

setup(
    name="resi-builder",
    version="0.1.0",
    author="Mario Cerda",
    author_email="cerdamario13@gmail.com",
    description="Create a resume and cover letter automatically",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.10",
)
