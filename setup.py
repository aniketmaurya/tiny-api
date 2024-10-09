from setuptools import setup, find_packages

setup(
    name="tiny_api",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # List your project dependencies here, e.g., 'requests>=2.25.1'
    ],
    entry_points={
        "console_scripts": [
            # Define command-line scripts here, e.g., 'mycommand = tiny_api.module:function'
        ],
    },
    author="Aniket Maurya",
    author_email="theaniketmaurya@gmail.com",
    description="A brief description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aniketmaurya/tiny_api",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
