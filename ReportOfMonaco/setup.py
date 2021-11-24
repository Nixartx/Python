import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ReportOfMonaco",
    version="0.0.1",
    author="Artyom Litvinenko",
    author_email="nixart986@gmail.com",
    description="Show reports of Monaco from files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.foxminded.com.ua/foxstudent100631/foxpy",
    project_urls={
        "Bug Tracker": "https://git.foxminded.com.ua/foxstudent100631/foxpy",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)