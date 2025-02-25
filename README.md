📌 README.md
markdown

# 🚀 Trade Order API (FastAPI + Docker + AWS + CI/CD)

A backend service for managing trade orders, built using **FastAPI**, **PostgreSQL**, and **Docker**, deployed on **AWS EC2**, with automated **CI/CD using GitHub Actions**.

---

## 📌 Features
- ✅ **REST API**: Create and fetch trade orders (`POST /orders`, `GET /orders`)
- ✅ **Database**: Uses **PostgreSQL** for persistent storage
- ✅ **WebSockets**: (Bonus) Real-time order updates
- ✅ **Dockerized**: Runs in a container for portability
- ✅ **Deployed on AWS EC2**
- ✅ **CI/CD Pipeline**: Auto-deploys via **GitHub Actions**

---

## 📂 Project Structure
trade-app/ ├── .github/workflows/deploy.yml # CI/CD Pipeline ├── Dockerfile # Containerization ├── docker-compose.yml # Local multi-container setup ├── main.py # FastAPI entry point ├── models.py # Database models ├── schemas.py # Pydantic validation ├── database.py # Database connection ├── requirements.txt # Dependencies ├── README.md # Project documentation



## ⚡ Getting Started (Run Locally)

### 1️⃣ **Clone Repository**
```bash
git clone https://github.com/your-username/trade-app.git
cd trade-app
2️⃣ Setup Environment
```bash
pip install -r requirements.txt
3️⃣ Run with Docker
```bash
docker-compose up --build
4️⃣ Test API
```bash
Swagger UI: http://localhost:8000/docs
ReDoc UI: http://localhost:8000/redoc
☁️ Deployment on AWS EC2
1️⃣ SSH into EC2
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
2️⃣ Install Docker
```bash
sudo apt update && sudo apt install docker.io docker-compose -y
3️⃣ Deploy API
```bash
docker run -d -p 8000:8000 trade-api
API is now live at:
http://your-ec2-ip:8000

🔄 CI/CD Pipeline (GitHub Actions)
```bash
Runs tests on pull requests.
Builds & pushes Docker image.
SSHs into EC2 & deploys the latest version.
📌 Pipeline Config: .github/workflows/deploy.yml

📬 API Endpoints
Method	Endpoint	Description
POST	/orders/	Create a trade order
GET	/orders/	Get all trade orders
🛠 Tech Stack
Backend: FastAPI, Pydantic
Database: PostgreSQL
DevOps: Docker, AWS EC2, GitHub Actions
CI/CD: Automated deployment
📜 License
MIT License © 2025 Preethi Ranganathan

🚀 Developed with ❤️ for scalable cloud applications
