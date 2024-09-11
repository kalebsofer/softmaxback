# Softmax Backend

This is the backend for the Softmax dashboard generation and ChatGPT integration.

## Setup

1. Install dependencies:
   ```
   poetry install
   ```

2. Set up environment variables:
   Copy `.env.example` to `.env` and fill in the required values.

3. Run the server:
   ```
   poetry run uvicorn app.main:app --reload
   ```

## API Endpoints

- `POST /generate-dashboard`: Generate a dashboard based on the selected dataset
- `POST /ask-question`: Ask a question about the dashboard data using ChatGPT
- `POST /login`: User login (to be implemented)
- `POST /logout`: User logout (to be implemented)

## Docker

To build and run the Docker container:
