import tensorflow as tf

MODEL_PATH = "alzheimers_model"

print("Loading TensorFlow model...")

# Load SavedModel
model = tf.saved_model.load(MODEL_PATH)

# Get inference signature
infer = model.signatures["serving_default"]

print("Model loaded successfully.")

