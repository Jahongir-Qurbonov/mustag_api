import pydantic


class UploadModel(pydantic.BaseModel):
    time_second: int = 300


class UpdateModel(pydantic.BaseModel):
    music_id: str
    update: dict | None = None
    download: bool = None