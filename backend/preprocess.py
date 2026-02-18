from PIL import Image
import numpy as np

IMAGE_SIZE = (160, 160)

def preprocess_image(file):

    # Open image
    image = Image.open(file).convert("RGB")

    # Resize
    image = image.resize(IMAGE_SIZE)

    # Convert to numpy + normalize + FORCE float32
    image = np.array(image).astype("float32") / 255.0

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    return image
