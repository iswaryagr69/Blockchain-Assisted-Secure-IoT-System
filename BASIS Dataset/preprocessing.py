import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(path):
    return pd.read_csv(path)

def preprocess(df):
    df = df.dropna()

    # Encode categorical columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = LabelEncoder().fit_transform(df[col])

    X = df.drop("label", axis=1)
    y = df["label"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y

if __name__ == "__main__":
    df = load_data("../data/raw/dataset.csv")
    X, y = preprocess(df)

    pd.DataFrame(X).to_csv("../data/processed/X.csv", index=False)
    pd.DataFrame(y).to_csv("../data/processed/y.csv", index=False)