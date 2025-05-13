# 🚀 FastAPI Backend Template

This project is a minimal, modular FastAPI application designed for demonstration and learning purposes. It includes multiple endpoints for serving static information, generating random numbers, and handling user input dynamically.

## 📦 Setup Instructions

### 🔧 Prerequisites

- Python 3.8+
- `pip` or any preferred Python environment manager

### ▶️ Installation

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/fastapi-backend-template.git
   cd fastapi-backend-template
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app locally

   ```bash
   uvicorn app:app --reload
   ```

The server will start at `http://127.0.0.1:8000`

---

## 🌐 API Endpoints

- `GET /api/info`  
  Returns static metadata about the project.

- `GET /api/random-number`  
  Returns a randomly generated number between 1 and 100.

- `GET /api/echo-input?message=hi`  
  Accepts a query parameter and echoes back the input.

---

## 🧪 Example Usage

Fetch static info:

```bash
curl http://127.0.0.1:8000/api/info
```

Fetch random number:

```bash
curl http://127.0.0.1:8000/api/random-number
```

Echo user input:

```bash
curl "http://127.0.0.1:8000/api/echo-input?message=hello"
```

---

## ✅ Tech Stack

- FastAPI
- Uvicorn
- Python 3.8+

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Anshu Singh**  
GitHub: [@anshupacific](https://github.com/anshupacific)
