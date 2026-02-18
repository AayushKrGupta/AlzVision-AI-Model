from fastapi import FastAPI, UploadFile, File
import tensorflow as tf
import numpy as np

from model_loader import infer
from preprocess import preprocess_image

app = FastAPI()

# CLASS LABELS
CLASS_NAMES = [
    "Non_Demented",
    "Very_Mild_Demented",
    "Mild_Demented",
    "Moderate_Demented"
]

@app.get("/")
def root():
    return {"message": "AlzVision AI Backend Running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Preprocess image
    image = preprocess_image(file.file)

    print("Image shape:", image.shape)

    # Convert to tensor
    input_tensor = tf.constant(image, dtype=tf.float32)

    # IMPORTANT FIX HERE
    prediction = infer(keras_tensor=input_tensor)

    print("Raw prediction:", prediction)

    output = next(iter(prediction.values())).numpy()

    predicted_index = np.argmax(output)

    result = CLASS_NAMES[predicted_index]

    confidence = float(output[0][predicted_index])

    return {
        "prediction": result,
        "confidence": confidence
    }
