# Weather API 🌤️

A lightweight REST API built with **Python and FastAPI**. This project demonstrates the development of backend APIs, endpoint creation, health monitoring, and interactive API documentation.

##  Technologies Used

- **Python 3.14** – Backend programming language
- **FastAPI** – Web API framework
- **Uvicorn** – ASGI server
- **Swagger UI** – Interactive API documentation

##  Project Structure

```text
Weather-API/
│
├── main.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .venv/
├── src/
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Weather-API
```

### 3. Create a virtual environment (if one doesn't exist)

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install fastapi "uvicorn[standard]"
```

### 6. Run the application

```bash
python -m uvicorn main:app --reload --port 8080
```

The API will be available at:

```text
http://127.0.0.1:8080
```

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API homepage (if configured) |
| GET | `/Health_check` | Checks API health |
| GET | `/docs` | Interactive Swagger documentation |
| GET | `/redoc` | ReDoc API documentation |

### Health Check

**Request:**

```http
GET /Health_check
```

**Response:**

```json
{
    "message": "Healthyyy!!"
}
```

##  API Documentation

FastAPI automatically generates interactive API documentation.

- Swagger UI: `http://127.0.0.1:8080/docs`
- ReDoc: `http://127.0.0.1:8080/redoc`

##  Project Objectives

- Learn REST API development using Python.
- Understand HTTP methods and API endpoints.
- Implement API health monitoring.
- Explore FastAPI's automatic documentation.
- Build a foundation for developing a fully functional weather service.

##  Future Improvements

- Integrate a weather data provider API.
- Implement real-time weather information.
- Add city-based weather searches.
- Include temperature, humidity, and wind-speed data.
- Implement error handling and input validation.
- Add API authentication and rate limiting.

##  Author

**Tech Diddie**

GitHub: [Diddie029](https://github.com/Diddie029)

---

*Built with Python and FastAPI.*