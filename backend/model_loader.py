import tensorflow as tf

MODEL_PATH = "alzheimers_model"

print("Loading model...")

model = tf.saved_model.load(MODEL_PATH)

infer = model.signatures["serving_default"]

print("Model loaded.")
