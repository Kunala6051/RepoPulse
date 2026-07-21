FROM python:3.11-slim

ARG AGENT_MODULE

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/

ENV AGENT_MODULE=${AGENT_MODULE}

CMD ["python", "-m", "backend.agents.worker"]
