from setuptools import setup, find_packages

setup(
    name="Housing Forecast",
    version="2.0",
    packages=find_packages(),
    install_requires=['pandas','scikit-learn'],
    description="Personal group work project for a personal project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sidharth S",
    author_email="sidharthsnair.8a@gmail.com",
    url="https://github.com/NINJAGAMING107/ai_project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
