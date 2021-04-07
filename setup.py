import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cs-algorithms", # Replace with your own username
    version="0.0.9",
    author="Michael Groenewegen van der Weijden",
    author_email="",
    description="Sorting Algorithms & Data Structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michael-gvdw/cs-algorithms.git",
    project_urls={
        "GitHub": "https://github.com/michael-gvdw/cs-algorithms.git",
        "Linkedin": "https://www.linkedin.com/in/michael-groenewegen-van-der-weijden-4234b9206/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)