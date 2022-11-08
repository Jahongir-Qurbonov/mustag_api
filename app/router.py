from fastapi import APIRouter, status, UploadFile, File
# from fastapi.routing import APIRoute
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.db_models import FileDBModel
from app.models import UpdateModel, UploadModel
from app.utils import get_fname_uuid
from mutagen.easyid3 import EasyID3


api_router = APIRouter()


@api_router.get("/")
async def apis():
    """Hello apis"""
    content = jsonable_encoder(obj={"message": "Hello World"})
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)


@api_router.post("/upload", operation_id='file_upload', response_description='OK')
async def music_upload(
    music_file: UploadFile = File(..., media_type='audio/mpeg'),
    parameters: UploadModel = None,
    *args, **kwargs,
):
    """Musiqani yuklash"""
    m_fname = music_file.filename
    fname, ext, m_id = get_fname_uuid(m_fname)
    filename = fname + m_id + '.' + ext

    try:
        contents = music_file.file.read()
        with open(f"mus_tmp/{filename}", 'wb') as f:
            f.write(contents)
    except Exception as e:
        contents = jsonable_encoder(obj={"error": e})
        return JSONResponse(
            content=contents,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    else:
        db_f = FileDBModel(
            filename=filename,
            m_id=m_id,
        )
        if hasattr(parameters, 'time_second'):
            db_f.timestamp_sec = parameters.time_second
        db_f.save(force_insert=True)
    finally:
        music_file.file.close()

    obj = {"music_filename": m_fname, "music_id": m_id}
    contents = jsonable_encoder(obj=obj)

    return JSONResponse(content=contents, status_code=status.HTTP_200_OK)

@api_router.get('/get_valid_tags')
def get_valid_tags():
    valid_k = EasyID3.valid_keys
    print(valid_k.keys())

    obj = {
        'valid_keys': list(valid_k.keys()),
    }
    contents = jsonable_encoder(obj=obj)

    return JSONResponse(content=contents, status_code=status.HTTP_200_OK)

@api_router.get('/get_tags')
def get_tags(music_id: str):
    q = FileDBModel.get_or_none(m_id=music_id)
    if q is None:
        obj = {'doesn\'t exists': 'None'}
        contents = jsonable_encoder(obj=obj)
        return JSONResponse(content=contents, status_code=status.HTTP_204_NO_CONTENT)
    else:
        mus = EasyID3(filename=f'mus_tmp/{q.filename}')
        tags = mus

    obj = {
        'Music file name': q,
        'music_id': q.m_id,
        'tags':tags,
    }
    contents = jsonable_encoder(obj=obj)
    return JSONResponse(content=contents, status_code=status.HTTP_200_OK)


@api_router.post("/update_music")
def update_tags(update_music: UpdateModel):
    """Musiqani yangilash"""
    q = FileDBModel.get_or_none(m_id=update_music.music_id)
    if q is None:
        obj = {'doesn\'t exists': 'None'}
        contents = jsonable_encoder(obj=obj)
        return JSONResponse(content=contents)
    else:
        mus = EasyID3(filename=f'mus_tmp/{q.filename}')
        tags = mus

        if hasattr(update_music, 'update'):
            mus.update(update_music.update)
            mus.save()
            new_tags = mus

    obj = {
        'music_id': q.m_id,
        'tags':tags,
    }
    contents = jsonable_encoder(obj=obj)
    return JSONResponse(content=contents)


# def use_route_names_as_operation_ids(app: FastAPI) -> None:

#     Simplify operation IDs so that generated API clients have
#     simpler function names.

#     Should be called only after all routes have been added.


#     for route in app.routes:
#         if isinstance(route, APIRoute):
#             route.operation_id = route.name  # in this case, 'read_items'


# use_route_names_as_operation_ids(api_router)
