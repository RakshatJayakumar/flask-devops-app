# Flask DevOps App — CI/CD Pipeline

## Overview
A production-style CI/CD pipeline using GitHub Actions, Docker, AWS ECR,
and EC2. Every push to main automatically tests, builds, and deploys the app.

## Pipeline Flow
Push to main → Run Tests → Build Docker Image → Push to ECR → Deploy to EC2

## Tech Stack
- Python / Flask
- Docker
- GitHub Actions
- AWS ECR (container registry)
- AWS EC2 (deployment target)

## Project Structure
flask-devops-app/
├── app/
│   └── main.py          # Flask application
├── tests/
│   └── test_app.py      # Pytest unit tests
├── .github/
│   └── workflows/
│       └── deploy.yml   # CI/CD pipeline
├── Dockerfile
├── requirements.txt
└── README.md

## Running Locally
pip install -r requirements.txt
python app/main.py

## Running Tests
pytest tests/ -v

## Running with Docker
docker build -t flask-devops-app .
docker run -p 5000:5000 flask-devops-app