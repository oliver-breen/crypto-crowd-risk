from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="crypto-crowd-risk",
    version="1.0.0",
    author="Oliver Breen",
    description="OWASP 2025 Cryptography Risk Assessment Tool for Cryptocurrency Markets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oliver-breen/crypto-crowd-risk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
    ],
    python_requires=">=3.8",
    install_requires=[
        "cryptography>=42.0.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0.1",
    ],
    entry_points={
        "console_scripts": [
            "crypto-risk=crypto_risk.cli:main",
        ],
    },
)
