from fastapi import FastAPI
from app.router import api_router


app = FastAPI(debug=True, title='Music tag editor',
              version='0.0.1', description="Music tag editor")

app.include_router(router=api_router, prefix='/api')
