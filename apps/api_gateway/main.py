from fastapi import FastAPI
app=FastAPI(title="Enterprise AI API Gateway")
@app.get("/health")
def health():
    return {"status":"ok"}
