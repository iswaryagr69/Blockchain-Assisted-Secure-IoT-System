import tensorflow as tf
from tensorflow.keras import layers, models

def build_attention_model(input_dim):
    inputs = layers.Input(shape=(input_dim,))

    # Attention-like mechanism
    attention = layers.Dense(input_dim, activation='softmax')(inputs)
    attended = layers.multiply([inputs, attention])

    x = layers.Dense(64, activation='relu')(attended)
    x = layers.Dense(32, activation='relu')(x)
    outputs = layers.Dense(1, activation='sigmoid')(x)

    model = models.Model(inputs, outputs)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return model