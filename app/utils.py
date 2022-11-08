from uuid import uuid4


def fname_getter(filename, get_ext=False):
    dot = str(filename).rfind('.')
    fname_no_ext = filename[:dot]
    if not get_ext:
        return fname_no_ext
    ext = filename[dot + 1:]
    return fname_no_ext, ext


def get_fname_uuid(filename: str):
    fname_no_ext, ext = fname_getter(filename, get_ext=True)
    uuid = str(uuid4())
    return fname_no_ext, ext, uuid
