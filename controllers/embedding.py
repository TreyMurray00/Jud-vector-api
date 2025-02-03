from deepface import DeepFace

def get_embedding(image_path: str):
    try:
        embedding = DeepFace.represent(image_path)
        return embedding[0]["embedding"]
    except Exception as e:
        return None# no face detected