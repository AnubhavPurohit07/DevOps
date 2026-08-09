# DevOps Internship — Task 1: Dockerized Web Application

A minimal Flask web app, containerized with Docker, built as part of a DevOps internship assignment.

## 📋 Overview

This app serves a simple page confirming it's running inside a Docker container (by displaying the container's hostname), plus a `/health` endpoint for basic health checking.

## 🛠️ Tech Stack

- Python 3.11
- Flask 3.0.3
- Docker

## 📁 Project Structure

```
DevOps_Internship/
├── app.py             # Flask application
├── Dockerfile         # Docker image definition
├── requirements.txt   # Python dependencies
├── .dockerignore       # Files excluded from the Docker build context
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Docker Desktop (or Docker Engine on Linux) installed and running

### Build the image

```bash
docker build -t devops-task1-app .
```

### Run the container

```bash
docker run -d -p 5000:5000 --name task1-container devops-task1-app
```

### Verify

Open **http://localhost:5000** in your browser — you should see a message confirming the app is running inside a container, along with the container's hostname.

Health check: **http://localhost:5000/health**

## 🐳 Docker Hub

This image is also published on Docker Hub:

```bash
docker pull <your-dockerhub-username>/devops-task1-app
```

*(Replace `<your-dockerhub-username>` with your actual Docker Hub username.)*

## 📌 Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Returns an HTML page showing the container hostname |
| `/health` | GET | Returns `{"status": "healthy"}` |

## 📝 About

Built as part of a structured DevOps internship covering:
1. Docker containerization
2. Git & GitHub workflows
3. Nginx web server deployment
4. CI/CD with GitHub Actions
5. Infrastructure as Code with Terraform
