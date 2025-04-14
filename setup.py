from setuptools import setup, find_packages

setup(
    name="my_tradesniff",  # Package name
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "ta",
        "discord-webhook"
    ],
    python_requires=">=3.7",
)
