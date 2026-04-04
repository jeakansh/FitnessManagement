# 🏋️ ACEest Fitness & Gym – CI/CD Enabled Flask Application

## 📌 Overview

ACEest Fitness & Gym is a modular Flask-based web application designed to manage core fitness operations such as client profiles, workout programs, and service logic.
This project demonstrates a complete **DevOps lifecycle**, transitioning from local development to a fully automated CI/CD pipeline using Docker, Jenkins, and GitHub Actions.

The primary goal is to ensure:

* Code integrity through automated testing
* Environmental consistency via containerization
* Rapid and reliable delivery through CI/CD pipelines

---

# ⚙️ Tech Stack

* **Backend:** Flask (Python)
* **Testing:** Pytest
* **Containerization:** Docker
* **CI/CD Tools:**

  * Jenkins (Build & Quality Gate)
  * GitHub Actions (Automated CI Pipeline)
* **Version Control:** Git + GitHub

---

# 📁 Project Structure

```
FitnessManagement/
│
├── app.py
├── services.py
├── database.py
│
├── templates/
├── static/
│
├── tests/
│   ├── test_app.py
│   ├── test_services.py
│   ├── test_database.py
│
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── .github/workflows/main.yml
└── README.md
```

---

# 🚀 Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/jeakansh/FitnessManagement.git
cd FitnessManagement
```

---

## 2️⃣ Install Dependencies (Local Setup)

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run Flask Application

```bash
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

# 🐳 Docker Setup & Execution

## Build Docker Image

```bash
docker build -t aceest-fitness .
```

## Run Application (Optional)

```bash
docker run -p 5000:5000 aceest-fitness
```

---

# 🧪 Running Tests Manually

## Run Tests Locally

```bash
pytest
```

---

## Run Tests Using Docker (Recommended)

```bash
docker build -t aceest-fitness .
docker run --rm aceest-fitness pytest
```

---

# ⚙️ Jenkins Setup & Execution

## Jenkins Pipeline Overview

The Jenkins pipeline acts as a **BUILD & Quality Gate** by:

1. Pulling latest code from GitHub
2. Performing a clean Docker build
3. Running unit tests inside the container
4. Failing the build if any test fails

---

## Jenkinsfile Logic

```
pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-fitness .'
            }
        }

        stage('Run Tests in Container') {
            steps {
                sh 'docker run --rm aceest-fitness pytest'
            }
        }
    }
}
```

---

## Jenkins Workflow

```
GitHub Push →
    Jenkins Trigger →
        Clone Repository →
        Docker Build →
        Run Tests →
        SUCCESS / FAILURE (Quality Gate)
```

---

# 🔄 GitHub Actions CI/CD Pipeline

## Trigger Conditions

* On every **push**
* On every **pull request**

---

## Pipeline Stages

1. Checkout code
2. Build Docker image
3. Run tests inside container
4. Mark pipeline as success/failure

---

## Workflow File

Location:

```
.github/workflows/main.yml
```

---

## GitHub Actions Logic

```
Push / PR →
    GitHub Actions →
        Docker Build →
        Run Pytest →
        SUCCESS / FAILURE
```

---

# 🔗 Integration Logic (Jenkins + GitHub Actions)

This project uses a **dual CI validation strategy**:

### 🟢 GitHub Actions

* Immediate feedback on code changes
* Fast CI validation
* Ensures tests pass before merge

### 🔵 Jenkins

* Acts as a secondary validation layer
* Performs clean environment builds
* Ensures integration stability

---

## Combined Workflow

```
Developer →
    Git Push →
        ├── GitHub Actions (CI)
        │       → Build Docker
        │       → Run Tests
        │
        └── Jenkins (Quality Gate)
                → Clean Build
                → Run Tests
                → Final Validation
```

---

# 🎯 Key Features

* Modular Flask architecture
* Comprehensive unit testing using Pytest
* Docker-based environment consistency
* Automated CI/CD pipelines
* Dual validation system (GitHub Actions + Jenkins)


---

# 👨‍💻 Author

**Eakansh Jain**
Role Number: 2024tm93674

---
