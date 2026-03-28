import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score, precision_score, recall_score

X = pd.read_csv("../data/processed/X.csv")
y = pd.read_csv("../data/processed/y.csv")

model = load_model("../results/model.h5")

pred = (model.predict(X) > 0.5).astype(int)

print("Accuracy:", accuracy_score(y, pred))
print("Precision:", precision_score(y, pred))
print("Recall:", recall_score(y, pred))