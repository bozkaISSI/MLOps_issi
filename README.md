# ML API - Production-Ready Machine Learning Application

---

## 🚀 Features

- 🔧 Fast dependency management with [`uv`](https://astral.sh/blog/uv/)
- 📚 Code versioning with Git & GitHub
- ✅ Pre-commit hooks: Ruff (lint/format), Xenon (complexity)
- ⚙️ Configuration via environment variables and `.env` files
- 🔐 Secrets management using `sops` and GPG
- 🧪 Testing with `pytest`
- ⚡ Webserver using FastAPI
- 🤖 ML model served via REST API
- 📦 Containerization with Docker & Docker Compose

---

## 📁 Project Structure

```
lab/
├── app.py                   # FastAPI app
├── api/
│   └── models/
│       └── iris.py          # Request/response models
├── config/
│   ├── .env.dev
│   ├── .env.test
│   └── .env.prod
├── inference.py            # Inference logic
├── main.py                 # Env loader
├── secrets.yaml            # Encrypted secrets
├── settings.py             # App settings
├── tests/
│   └── test_settings.py    # Unit tests
├── training.py             # Model training script
├── pyproject.toml
├── uv.lock
├── .pre-commit-config.yaml
└── Dockerfile
```

## 🛠️ Setup & Usage

### 1. Install `uv` and Set Python Version

```bash
uv venv --python 3.12.8
uv init
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 2. Git & GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

### 3. Add Dependencies

```bash
uv add fastapi uvicorn scikit-learn pydantic-settings python-dotenv pre-commit ruff pytest sops pyyaml
```

---

## ✅ Pre-commit Hooks

Install and configure:

```bash
pre-commit install
pre-commit run --all-files
```

`.pre-commit-config.yaml` includes:
- Ruff (linter + formatter)
- Xenon (complexity checker)

---

## ⚙️ Environment Management

- Store config in `.env.dev`, `.env.test`, `.env.prod`
- Use `pydantic-settings` for typed config
- Load with:

```bash
uv run python main.py --environment dev
```

---

## 🔐 Secrets Management with `sops`

1. Generate GPG key:  
   `gpg --gen-key`

2. Encrypt secrets:

```bash
sops --encrypt --in-place secrets.yaml
```

3. Decrypt when needed:

```bash
sops --decrypt --in-place secrets.yaml
```

Secrets are loaded via `pyyaml` into environment variables.

---

## 🧪 Testing

```bash
uv run pytest tests -rP
```

- Test settings loading
- API route responses

---

## 🧠 Machine Learning Model

Train the model:

```bash
uv run python training.py
```

Make predictions via API:

```bash
uv run uvicorn app:app --reload --port=8000
```

- POST `/predict` with:
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

---

## 🐳 Docker & Compose

### Build & Run

```bash
docker build -t ml-app .
docker run --rm -p 8000:8000 ml-app
```

### With Docker Compose

```bash
docker compose up
```

- Access at: [http://localhost:8000](http://localhost:8000)
- Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)

