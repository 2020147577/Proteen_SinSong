from setuptools import setup, find_packages

setup(
    name="pacman_game",
    version="0.1.0",
    packages=find_packages(),   # this will find your pacman/ package
    include_package_data=True,
    install_requires=[],        # list dependencies here, if any
    entry_points={
        'console_scripts': [
            'pacman = pacman.__main__:main',
        ],
    },
)

