import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='NetGsm',
    version="0.0.4",
    author="Yaşar Özyurt",
    author_email="blueromans@gmail.com",
    description='NetGsm Sms Client Python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/blueromans/netgsm.git',
    project_urls={
        "Bug Tracker": "https://github.com/blueromans/netgsm/issues",
    },
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['netgsm'],
    python_requires=">=3.6",
)
