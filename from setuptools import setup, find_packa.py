from setuptools import setup, find_packages
import os

# Fix: Ensure the README.md file is closed after reading
with open('README.md') as f:
    long_description = f.read()

setup(
    name="penbot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "dnspython",
        "beautifulsoup4",
        "scapy",
    ],
    entry_points={
        'console_scripts': [
            'penbot=penbot:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple penetration testing tool",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/pentestool/penbot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# Automatically run penbot after installation
os.system('penbot')
