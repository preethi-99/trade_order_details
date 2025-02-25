📌 README.md
# 🚀 Trade Order API (FastAPI + Docker + AWS + CI/CD)

A backend service for managing trade orders, built using **FastAPI**, **PostgreSQL**, and **Docker**, deployed on **AWS EC2**, with automated **CI/CD using GitHub Actions**.

---

## ⚡ Getting Started (Run Locally)

### 1. Clone Repository
git clone https://github.com/your-username/trade-app.git cd trade-app


### 2. Setup Environment
pip install -r requirements.txt


### 3. Run with Docker
docker-compose up --build


### 4. Test API
- **Swagger UI**: [`http://localhost:8000/docs`](http://localhost:8000/docs)
- **ReDoc UI**: [`http://localhost:8000/redoc`](http://localhost:8000/redoc)

---

## ☁️ Deployment on AWS EC2

### 1. SSH into EC2
ssh -i your-key.pem ubuntu@your-ec2-ip


### 2. Install Docker
sudo apt update && sudo apt install docker.io docker-compose -y


### 3. Deploy API

**API is now live at:**  
[`http://your-ec2-ip:8000`](http://your-ec2-ip:8000)

---

## 🔄 CI/CD Pipeline (GitHub Actions)
- Runs tests on pull requests.
- Builds & pushes Docker image.
- SSHs into EC2 & deploys latest version.

📌 **Pipeline Config:** [`.github/workflows/deploy.yml`](./.github/workflows/deploy.yml)

---

## 📬 API Endpoints
| Method | Endpoint   | Description          |
|--------|-----------|----------------------|
| `POST` | `/orders/` | Create a trade order |
| `GET`  | `/orders/` | Get all trade orders |

---

## 🛠 Tech Stack
- **Backend:** FastAPI, Pydantic
- **Database:** PostgreSQL
- **DevOps:** Docker, AWS EC2, GitHub Actions
- **CI/CD:** Automated deployment

## 📜 License
MIT License © 2025 **Preethi Ranganathan**

🚀 **Developed with ❤️ for scalable cloud applications**
