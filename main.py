from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

 
update_info = {
    "version": "0.9",
}

@app.get("/check-update")
async def check_update():
    """
    Endpoint to return app update information.
    """
    return JSONResponse(content=update_info)

