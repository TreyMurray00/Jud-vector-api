from deepface import DeepFace

def get_embedding(image_path, model_name="VGG-Face", model=None):
    try:
        embedding = DeepFace.represent(image_path)
        return embedding[0]['embedding']
    except Exception as e:
        return e
    
# print(get_embedding("image_cache/tony_Reg.jpg"))
vec = get_embedding("image_cache/tony_Reg.jpg")



import numpy as np

print(np.array(vec).shape)