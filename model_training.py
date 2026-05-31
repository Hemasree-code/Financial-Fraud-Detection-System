import pandas as pd
from sklearn.ensemble import RandomForestClassifier

print("Financial Fraud Detection Model Training")

# Load Dataset
df = pd.read_csv("dataset/fraud.csv")

print("Dataset Loaded Successfully")
print(df.head())

# Dummy model creation
model = RandomForestClassifier()

print("Model Created Successfully")
