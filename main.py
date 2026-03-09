from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

 
update_info = {
    "latestVersion": "1.2",
    "forceUpdate": True,
    "updateUrl": "https://play.google.com/store/apps/details?id=com.djtmyhr"
}

@app.get("/check-update")
async def check_update():
    """
    Endpoint to return app update information.
    """
    return JSONResponse(content=update_info)

