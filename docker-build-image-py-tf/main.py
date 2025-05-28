import tensorflow as tf

# Verifica della versione
print("TensorFlow version:", tf.__version__)

# Creazione di un modello semplice
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(1)
])

model.summary()