import uvicorn
from app.main import app
from multiprocessing import freeze_support


if __name__ == '__main__':
    freeze_support()
    uvicorn.run('app.main:app', debug=True, reload=True, workers=True)
