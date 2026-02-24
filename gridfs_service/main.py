from fastapi import FastAPI,UploadFile,File
from GridFSStorage import GridFSStorage
import uvicorn

gridfs_storage = GridFSStorage()
app = FastAPI()

@app.post("/image")
async def upload_image(file:UploadFile = File(...)):
    content = await file.read()
    res = gridfs_storage.gridfs_storage(content)
    if res:
        return {"the image stored in mongo successfully."}
    else:
        return {"the image not stored in mongo :)"}
    
if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8080)
    