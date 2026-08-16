from pathlib import Path
import joblib
import numpy as np
import pandas as pd
import sklearn

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "final_random_forest_pipeline.joblib.gz"

model = joblib.load(MODEL_PATH)

sample = pd.DataFrame([{
    "Building_Function": "Heritage",
    "Structural_System": "Traditional/Heritage Masonry",
    "Building_Age_Years": 101,
    "Number_of_Floors": 2,
    "DI": 39.825979319063485,
    "PLI": 38.26864389830388,
    "TRI": np.nan,
    "TRI_Availability_Flag": 0,
    "SI": 13.32,
}])

prediction = float(model.predict(sample)[0])
print(f"scikit-learn: {sklearn.__version__}")
print(f"Model file: {MODEL_PATH}")
print(f"B02 smoke-test prediction: {prediction:.4f}")
print("Expected approximately: 39.98")
