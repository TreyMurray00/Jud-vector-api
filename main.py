import os
from fastapi import Depends, FastAPI, HTTPException, UploadFile, Form

from contextlib import asynccontextmanager
from controllers.init_utils.database import get_session
from controllers import register_user, search as user_search
from models import UserData
from sqlmodel import select


app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startup")
    # configure_milvus()
    # Connect to Redis on startup
    
    yield
    print("Shutdown")

@app.get("/")
async def live(session=Depends(get_session)):
    all = await session.exec(select(UserData)).all()
    return {"stats":all}

@app.post("/register")
async def register(image: UploadFile, name: str = Form(...), id: int = Form(...), session = Depends(get_session)):
    image_cache_dir = "image_cache"
    os.makedirs(image_cache_dir, exist_ok=True)
    image_path = os.path.join(image_cache_dir, image.filename)
    
    with open(image_path, "wb") as buffer:
        buffer.write(await image.read())
    
    result = register_user(session=session, image=image_path, name= name, id=id)
    os.remove(image_path)
    if not isinstance(result,bool):
        raise HTTPException(status_code=400, detail=result)
    return {"status": "success" , "embedding": result}


@app.post("/search")
async def search(image: UploadFile, session = Depends(get_session)):
    image_cache_dir = "image_cache"
    os.makedirs(image_cache_dir, exist_ok=True)
    image_path = os.path.join(image_cache_dir, image.filename)
    
    with open(image_path, "wb") as buffer:
        buffer.write(await image.read())
    
    result = await user_search.search(session=session, image=image_path)
    os.remove(image_path)
    if result is None:
        raise HTTPException(status_code=400, detail="No face detected")
    return {"status": "success" , "embedding": result}



# @app.delete("/delete/{id}")
# async def delete(id: str):

#     result = await delete_user(id)
#     if result == []:
#         raise HTTPException(status_code=400, detail="Failed to delete")
#     return {"status": "success"}

# @app.put("/update")
# async def update(image: UploadFile, id: str = Form(...)):
#     image_cache_dir = "image_cache"
#     os.makedirs(image_cache_dir, exist_ok=True)
#     image_path = os.path.join(image_cache_dir, image.filename)

#     with open(image_path, "wb") as buffer:
#         buffer.write(await image.read())

#     result = await update_user(image_path, id)
#     os.remove(image_path)
#     # if result is None:
#     #     raise HTTPException(status_code=400, detail="No face detected")
#     return {"status": "success", "data": result}
