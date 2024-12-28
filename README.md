# PenBot

PenBot is a simple penetration testing tool that performs subdomain enumeration, vulnerability scanning, and generates reports.

## Features

- **Subdomain Enumeration**: Identifies subdomains associated with a given domain.
- **Vulnerability Scanning**: Scans for common vulnerabilities in web applications.
- **Report Generation**: Generates comprehensive reports of the findings.

## Installation

To install the package, run:

```sh
pip install .
```

## Usage

To run the tool and save results in a folder named PenBot, use the following command:

```sh
penbot -o PenBot
```

## Running Tests

To run the unit tests and save results in a folder named PenBot, use:

```sh
python -m unittest discover -s PenBot
```
