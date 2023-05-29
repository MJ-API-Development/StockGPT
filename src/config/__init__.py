from functools import lru_cache

from pydantic import BaseSettings, Field


class APPSettings(BaseSettings):
    APP_NAME: str = Field(default="StockGPT")
    TITLE: str = Field(default="StockGPT - Business Intelligence")
    DESCRIPTION: str = Field(default="Analyze Financial Data, Business & Financial Data with chatGPT")
    VERSION: str = Field(default="1.0.0")
    TERMS: str = Field(default="https://stockGPT.site/terms")
    CONTACT_NAME: str = Field(default="MJ API Development")
    CONTACT_URL: str = Field(default="https://stockGPT.site/contact")
    CONTACT_EMAIL: str = Field(default="info@stockGPT.site")
    LICENSE_NAME: str = Field(default="Apache 2.0")
    LICENSE_URL: str = Field(default="https://www.apache.org/licenses/LICENSE-2.0.html")
    DOCS_URL: str = Field(default='/docs')
    OPENAPI_URL: str = Field(default='/openapi')
    REDOC_URL: str = Field(default='/redoc')


class Settings(BaseSettings):
    application: APPSettings = APPSettings()
    class Config:
        env_file = '.env.development'
        env_file_encoding = 'utf-8'


@lru_cache(maxsize=1, typed=True)
def config_instance() -> Settings:
    return Settings()
