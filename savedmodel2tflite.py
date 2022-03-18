import tensorflow as tf

# Convert the model.
converter = tf.compat.v1.lite.TFLiteConverter.from_saved_model('/home/stanik/repos/TensorFlow_1.13/workspace/training_demo/training/tf_0/saved_model')
tflite_model = converter.convert()

# Save the model.
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)