from pydantic import BaseSettings, BaseModel, Field, Extra

from .utils import toml_config_settings_source


class AppModel(BaseModel):
    title: str = ''
    version: str = ''
    description: str = ''


class SecretsModel(BaseModel):
    allowed_host_env: str = Field('', alias='allowed_hosts')
    cors_allow_origins_env: str = Field('', alias='cors_allow_origins')

    DEBUG: int = Field(10, alias='debug', ge=0, le=1)
    SECRET_KEY: str = Field('', alias='secret_key')

    @property
    def ALLOWED_HOSTS(self):
        return self.allowed_host_env.split(',')

    @property
    def CORS_ALLOW_ORIGINS(self):
        list_hosts = self.cors_allow_origins_env.split(',')
        return [f'http://{address}' for address in list_hosts]


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
