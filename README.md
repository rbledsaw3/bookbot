# Dockerized BookBot

A containerized Python application that analyzes text files and generates statistical reports about their contents.

## Description

BookBot is a text analysis tool that reads books and generates reports including:
- Word count
- Character frequency
- Basic text statistics

## Prerequisites

- Docker
- Git (for cloning the repository)

## Getting Started

1. Clone the repository:
```bash
git clone [repository-url]
cd bookbot
```

2. Build the Docker image:
```bash
docker build -t bookbot .
```

3.  Run the container:
```bash
docker run bookbot
```

## Project Structure
```plaintext
bookbot/
├── Dockerfile
├── main.py
├── books/
│   └── frankenstein.txt
└── README.md
```

## Docker Details

The application runs in a Debian-based container with Python 3.10.8 built from source. The Dockerfile handles:

-   Installing build dependencies
-   Building Python from source code
-   Copying application code and data
-   Setting up the runtime environment

BookBot is my first [Boot.dev](https://www.boot.dev) project!
