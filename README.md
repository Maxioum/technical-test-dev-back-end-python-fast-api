## Installation

1. clone the repository

```
git clone https://github.com/Maxioum/{repo}.git && cd {repo}
```

1. install [uv](https://docs.astral.sh/uv/)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Download dependencies

```bash
uv sync
```

## Starting the server

```bash
uv run uvicorn app.main:app --reload
```

Example requests:

Here’s a set of simple curl examples you can use to interact with the app once it’s running (default at http://localhost:8000):

1. Create a User

```bash
curl -X POST "http://localhost:8000/api/v1/tickets" -H "Content-Type: application/json" -d '{"title": "Feature: Add Ticket Type", "description": "Add different types of ticket, such as feature, bug etc"}'
```

2. Get All Users

```bash
curl -X GET "http://localhost:8000/api/v1/tickets"
```

3. Get a Ticket by ID

(Replace 1 with the actual ID from the create response)

```bash

curl -X GET "http://localhost:8000/api/v1/tickets/1"
```

4️. Update a Ticket

```bash
curl -X PUT "http://localhost:8000/api/v1/tickets/1" -H "Content-Type: application/json" -d '{"title": "Feature: Add Ticket Types"}'
```

5. Mark a Ticket as closed

```bash
curl -X PATCH "http://localhost:8000/api/v1/tickets/1/close" \
     -H "Content-Type: application/json" \
```

## Documentation

While the app is running visit:

http://localhost:8000/docs

## Docker

```bash
docker compose up --build tickets-api
```

## Unit Tests

1. Install dev dependencies

```bash
uv sync --dev
```

2. Run tests

```bash
uv run pytest
```

3. Run test with coverage

```bash
uv run pytest . --cov
```

# Check linting

```bash
uvx ruff check
```
