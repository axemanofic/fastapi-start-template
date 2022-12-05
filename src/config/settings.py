from pydantic import BaseSettings

from .schemas import *
from .utils import toml_config_settings_source


class Settings(BaseSettings):
    app: AppModel = AppModel()
    secrets: SecretsModel

    class Config:
        env_file = '.env'
        env_encoding = 'utf-8'
        env_nested_delimiter = '__'

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings):
            return init_settings, toml_config_settings_source, env_settings, file_secret_settings

# class DeepSubModel(BaseModel):
#     v4: str
#
#
# class SubModel(BaseModel):
#     v1: str
#     v2: bytes
#     v3: int
#     deep: DeepSubModel
#
#
# class Settings(BaseSettings):
#     app: dict
#     v0: str
#     sub_modell: SubModel
#
#     class Config:
#         env_file = '.env'
#         env_file_encoding = 'utf-8'
#         env_nested_delimiter = '__'
#
#         @classmethod
#         def customise_sources(cls, init_settings, env_settings, file_secret_settings):
#             # return init_settings, env_settings, file_secret_settings
#             return init_settings, toml_config_settings_source, env_settings, file_secret_settings


settings = Settings()

settings.json()
