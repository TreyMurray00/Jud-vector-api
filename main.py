import os
from fastapi import Depends, FastAPI, HTTPException, UploadFile, Form

from contextlib import asynccontextmanager
from controllers.init_utils.database import get_session
from controllers import register_user, search as user_search , delete_user
from models import UserData
from sqlmodel import select

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startup")
    
    yield
    print("Shutdown")



@app.get("/test")
async def read_root():
    return {"Hello": "World"}

@app.get("/users")
async def get_users(session = Depends(get_session)):
    result = session.exec(select(UserData))
    data = result.all()
    result = {}
    for row in data:
        result[row.id] = row.name
        
    return result

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
    return result



@app.delete("/delete/{id}")
async def delete(id: int, session = Depends(get_session)):

    result = delete_user(id=id, session=session)
    if result == False:
        raise HTTPException(status_code=400, detail="Failed to delete")
    return {"status": "success"}

# @app.put("/update")
# async def update(image: UploadFile, id: int = Form(...)):
#     image_cache_dir = "image_cache"
#     os.makedirs(image_cache_dir, exist_ok=True)
#     image_path = os.path.join(image_cache_dir, image.filename)

#     with open(image_path, "wb") as buffer:
#         buffer.write(await image.read())

#     # result = await update_user(image_path, id)
#     os.remove(image_path)
#     # if result is None:
#     #     raise HTTPException(status_code=400, detail="No face detected")
#     # return {"status": "success", "data": result}
