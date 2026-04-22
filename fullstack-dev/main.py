from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'FinGuard API is running'}

@app.post('/check-transaction')
def check_transaction(amount: float, hour: int, location: str):
    # AI model will connect here in Week 2
    return {
        'risk_score': 0,
        'explanation': 'Model not connected yet'
    }



if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")