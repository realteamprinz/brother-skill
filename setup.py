from setuptools import setup, find_packages

setup(
    name="brother-skill",
    version="1.0.0",
    description="Distill your bros — online or offline",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="realteamprinz",
    author_email="",
    url="https://github.com/realteamprinz/brother-skill",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "requests>=2.31.0",
        "click>=8.1.0",
        "rich>=13.0.0",
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "distill-bro=distill:main",
        ],
    },
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
)
