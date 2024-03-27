from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

@app.get('/items/')
async def get_items():
    return 'Aplicação rodando'

if __name__ == '__main__':
    run(app=app)