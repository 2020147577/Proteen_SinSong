from setuptools import setup, find_packages

setup(
    name="pacman-game",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pacman = pacman.__main__:main",
        ],
    },
)

