📌 README.md
# 🚀 Trade Order API (FastAPI + Docker + AWS + CI/CD)

A backend application for managing trade orders, built using **FastAPI**, **PostgreSQL**, and **Docker**, deployed on **AWS EC2**, with automated **CI/CD using GitHub Actions**. The programming language used is Python and for the database, PostgreSQL is used.
The application -
Accepts trade order details (e.g., symbol, price, quantity, order type) via POST /orders.
Returns the list of submitted orders via GET /orders.

---

## ⚡ Getting Started (Run Locally)

### 1. Clone Repository
git clone https://github.com/preethi-99/trade_order_details.git cd trade-app


### 2. Setup Environment
pip install -r requirements.txt


### 3. Run with Docker
docker-compose up --build


### 4. Test API
- **Swagger UI**: [`http://http://3.89.127.21:8000//docs`]
- **ReDoc UI**: [`http://http://3.89.127.21:8000//redoc`]

---

## ☁️ Deployment on AWS EC2

### 1. Transfer Files to EC2 Using SCP
To deploy the project on an AWS EC2 instance, transfer the application files using `scp`:
scp -i ~/Downloads/trade-app.pem -r ~/Downloads/trade-app ubuntu@3.89.127.21:/home/ubuntu/

### 2. SSH into EC2
ssh -i trade-app.pem ubuntu@3.89.127.21


### 3. Install Docker in EC2 instance
sudo apt update && sudo apt install docker.io docker-compose -y


### 4. Deploy API

**API is now live at:**  
[`http://http://3.89.127.21:8000/`]

---

## 🔄 CI/CD Pipeline (GitHub Actions)
- Runs tests on pull requests.
- Builds & pushes Docker image.
- SSHs into EC2 & deploys latest version.

📌 **Pipeline Config:** [`.github/workflows/deploy.yml`]

---

## 📬 API Endpoints
| Method | Endpoint   | Description          |
|--------|-----------|----------------------|
| `POST` | `/orders/` | Create a trade order |
| `GET`  | `/orders/` | Get all trade orders |

---

## 🛠 Tech Stack
- **Backend:** FastAPI, Pydantic,Python
- **Database:** PostgreSQL
- **DevOps:** Docker, AWS EC2, GitHub Actions
- **CI/CD:** Automated deployment

## ⚠️ Disclaimer
This project was created as part of a company recruitment assessment.  
All rights to this code remain with the author unless otherwise specified by the hiring company.

