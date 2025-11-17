import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pickle

# ------------------------------------------
# LOAD DATA
# ------------------------------------------
df = pd.read_csv("Housing.csv")
print(df.head())
print(df.info())

# ------------------------------------------
# PREPROCESSING
# ------------------------------------------
df_encoded = pd.get_dummies(df, drop_first=True)

# Save column names for API
columns = df_encoded.drop("price", axis=1).columns.tolist()

X = df_encoded.drop("price", axis=1).values
y = df_encoded["price"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ------------------------------------------
# BUILD MODEL
# ------------------------------------------
model = keras.Sequential([
    layers.Dense(128, activation="relu", input_shape=(X_train.shape[1],)),
    layers.Dense(64, activation="relu"),
    layers.Dense(1)
])

model.compile(optimizer="adam", loss="mse", metrics=["mae"])

# ------------------------------------------
# TRAIN
# ------------------------------------------
history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=100,
    batch_size=32,
    verbose=1
)

# ------------------------------------------
# EVALUATE
# ------------------------------------------
loss, mae = model.evaluate(X_test, y_test, verbose=0)
print(f"Test MAE: {mae:,.2f}")

# ------------------------------------------
# SAVE MODEL + SCALER + COLUMNS
# ------------------------------------------
model.save("house_model.h5")

# Save scaler
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

# Save columns
with open("columns.pkl", "wb") as f:
    pickle.dump(columns, f)

print("\nSaved: house_model.h5, scaler.pkl, columns.pkl")

