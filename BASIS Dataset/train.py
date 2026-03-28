import pandas as pd
from attention_model import build_attention_model
from sklearn.model_selection import train_test_split

X = pd.read_csv("../data/processed/X.csv")
y = pd.read_csv("../data/processed/y.csv")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = build_attention_model(X.shape[1])

model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

model.save("../results/model.h5")