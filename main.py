from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

 
update_info = {
  "android": {
    "version": "1.1",
    "store_url": "https://play.google.com/store/apps/details?id=in.deerikaexpress.djtretailers"
  },
  "ios": {
    "version": "1.2",
    "store_url": "https://apps.apple.com/app/deerika-hypermart/id1509418088"
  }
}

@app.get("/check-update")
async def check_update():
    """
    Endpoint to return app update information.
    """
    return JSONResponse(content=update_info)

