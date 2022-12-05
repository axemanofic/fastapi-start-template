from pydantic import BaseModel, Field, HttpUrl, EmailStr


class LicenseModel(BaseModel):
    name: str = 'MIT License'
    url: HttpUrl = 'https://mit-license.org/'


class ContactModel(BaseModel):
    name: str = ''
    url: HttpUrl = 'http://some.example/'
    email: EmailStr = 'some.example@mail.com'


class AppModel(BaseModel):
    title: str = ''
    version: str = ''
    description: str = ''
    contact: ContactModel = ContactModel()
    license_info: LicenseModel = LicenseModel()
    tags: list[dict[str, str]] = []


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