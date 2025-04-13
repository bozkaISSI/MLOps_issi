from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_KEY: str = "default-api-key"  # <-- Provide a fallback value

    @field_validator('ENVIRONMENT')
    def validate_environment(cls, value):
        allowed_environments = ['dev', 'test', 'prod']
        if value not in allowed_environments:
            raise ValueError(f"ENVIRONMENT must be one of {allowed_environments}")
        return value

    class Config:
        env_file = ".env"
