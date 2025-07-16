"""
Setup script for the superagentes project.
"""

from setuptools import setup, find_packages

setup(
    name="superagentes",
    version="1.0.0",
    description="Super Agents - AI agents development project",
    author="Andres Tobelem",
    packages=find_packages(),
    python_requires=">=3.13",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-cov>=6.0.0",
            "black>=25.0.0",
        ],
    },
)
