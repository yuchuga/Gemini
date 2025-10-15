FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy application into container
COPY . /app

# Install dependencies, sync packages from .venv with .toml file
WORKDIR /app
RUN uv sync --frozen --no-cache

# Run
CMD ['/app/.venv/bin/fastapi', 'run', 'app/main.py', '--port', '8080', '--host', '127.0.0.1']