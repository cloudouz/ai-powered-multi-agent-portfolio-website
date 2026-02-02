FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml /app/
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir fastapi uvicorn[standard] python-dotenv pydantic-settings httpx slowapi python-jose[cryptography] argon2-cffi sqlalchemy sqlmodel redis markdown-it-py langchain-core langchain-community langchain-openai langchain-google-genai google-generativeai tavily-python
COPY app /app/app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
