from unittest import mock

import pytest
from pydantic import ValidationError

from settings import Settings


# Test for successful loading of settings from .env file
def test_settings_loads_from_env():
    # Set up environment variables
    with mock.patch.dict('os.environ', {
        'ENVIRONMENT': 'dev',
        'APP_NAME': 'MyApp',
        'API_KEY': 'my-api-key',
    }):
        settings = Settings()

    assert settings.ENVIRONMENT == 'dev'
    assert settings.APP_NAME == 'MyApp'
    assert settings.API_KEY == 'my-api-key'


# Test for default value of API_KEY
def test_settings_default_api_key():
    # Set up environment variables without API_KEY
    with mock.patch.dict('os.environ', {
        'ENVIRONMENT': 'test',
        'APP_NAME': 'MyApp',
    }):
        settings = Settings()

    assert settings.API_KEY == 'default-api-key'  # Check that default value is used


# Test validation for ENVIRONMENT field (valid values)
@pytest.mark.parametrize("env_value", ["dev", "test", "prod"])
def test_validate_environment_valid_values(env_value):
    # Set up environment variables with valid ENVIRONMENT
    with mock.patch.dict('os.environ', {
        'ENVIRONMENT': env_value,
        'APP_NAME': 'MyApp',
    }):
        settings = Settings()

    assert settings.ENVIRONMENT == env_value


# Test validation for ENVIRONMENT field (invalid value should raise an error)
def test_validate_environment_invalid_value():
    # Set up environment variables with invalid ENVIRONMENT
    with mock.patch.dict('os.environ', {
        'ENVIRONMENT': 'staging',  # Invalid environment
        'APP_NAME': 'MyApp',
    }):
        with pytest.raises(ValidationError):
            Settings()


# Test if missing environment variable for APP_NAME causes an error
def test_missing_app_name():
    with mock.patch.dict('os.environ', {
        'ENVIRONMENT': 'dev',
        'API_KEY': 'my-api-key',
    }):
        with pytest.raises(ValidationError):
            Settings()


# Test if Settings class uses .env file correctly (for real-world testing)
def test_settings_load_from_file():
    with mock.patch.dict('os.environ', {
        'ENVIRONMENT': 'prod',
        'APP_NAME': 'ProductionApp',
        'API_KEY': 'prod-api-key',
    }):
        settings = Settings()

    assert settings.ENVIRONMENT == 'prod'
    assert settings.APP_NAME == 'ProductionApp'
    assert settings.API_KEY == 'prod-api-key'
