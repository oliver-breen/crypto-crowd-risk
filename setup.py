from setuptools import setup, find_packages

setup(
    name="crypto-crowd-risk",
    version="1.0.0",
    description="Cryptocurrency crowd-sourced risk assessment application",
    author="Crypto Risk Analytics",
    packages=find_packages(),
    install_requires=[
        "flask>=2.3.2",
        "requests>=2.31.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "python-dotenv>=1.0.0",
        "sqlalchemy>=2.0.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
