# Online Store API

A FastAPI-based RESTful API for managing users and products in an online store.

## Requirements

- Python 3.8+
- pip (Python package installer)

## Setup

1. Clone the repository:
```bash
git clone git@github.com:voltai-inc/swe-interview-coding-agent.git
cd swe-interview-coding-agent
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:

- On macOS/Linux:
```bash
source venv/bin/activate
```

- On Windows:
```bash
venv\Scripts\activate
```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server with auto-reload enabled:
```bash
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000

## Running Tests

```bash
pytest tests.py
```
