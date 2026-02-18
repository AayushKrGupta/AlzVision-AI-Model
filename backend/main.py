from fastapi import FastAPI, UploadFile, File
from model_loader import infer
from preprocess import preprocess_image
import tensorflow as tf

app = FastAPI()

CLASS_NAMES = [
    "Non_Demented",
    "Very_Mild_Demented",
    "Mild_Demented",
    "Moderate_Demented"
]

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image = preprocess_image(file.file)

    prediction = infer(tf.constant(image))

    output = list(prediction.values())[0].numpy()

    predicted_index = output.argmax()

    result = CLASS_NAMES[predicted_index]

    confidence = float(output[0][predicted_index])

    return {
        "prediction": result,
        "confidence": confidence
    }
