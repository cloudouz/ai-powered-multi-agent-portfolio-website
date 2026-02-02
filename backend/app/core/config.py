from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    ENV: str = Field("development", env="ENV")
    API_PREFIX: str = "/api"
    CORS_ORIGINS: str = Field("http://localhost:3000", env="CORS_ORIGINS")

    # Security
    JWT_SECRET: str = Field("CHANGE_ME", env="JWT_SECRET")
    JWT_ALG: str = "HS256"
    JWT_EXPIRES_MINUTES: int = 30

    # Providers
    LLM_PROVIDER: str = Field("gemini", env="LLM_PROVIDER")  # gemini|openai
    GEMINI_API_KEY: str | None = Field(None, env="GEMINI_API_KEY")
    OPENAI_API_KEY: str | None = Field(None, env="OPENAI_API_KEY")

    # Search
    TAVILY_API_KEY: str | None = Field(None, env="TAVILY_API_KEY")

    # DB/Cache (optional)
    DATABASE_URL: str | None = Field(None, env="DATABASE_URL")
    REDIS_URL: str | None = Field(None, env="REDIS_URL")

settings = Settings()
