from pydantic import BaseSettings, Field
import os


class RDS_Settings(BaseSettings):
    RDS_URL: str = Field(..., env="RDS_URL")
    RDS_BDD: str = Field(..., env="RDS_BDD")
    RDS_USER: str = Field(..., env="RDS_USER")
    RDS_PW: str = Field(..., env="RDS_PW")
    RDS_PORT: str = Field(..., env="RDS_PORT")
    RDS_TABLE: str = Field(..., env="RDS_TABLE")
    RDS_REGION: str = Field(..., env="RDS_REGION")


rds_settings = RDS_Settings(
    _env_file=os.environ.get("ENV_FILE", ".env")
)
