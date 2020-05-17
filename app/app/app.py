'''Create an API using FastAPI
'''

# API framework
from fastapi import FastAPI
# ASGI server
import uvicorn

app = FastAPI()

@app.get('/')
async def ping():
  '''Ping the API
  '''
  return {'ping': 'pong'}

if __name__ == '__main__':
  # Run uvicorn directly from the application
  uvicorn.run(
    'app:app', 
    host='127.0.0.1', 
    port=5000, 
    log_level='info'
  )
