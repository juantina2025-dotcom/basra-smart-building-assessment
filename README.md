# Basra Smart Building Assessment — Deployment Package

This folder contains the deployable Streamlit application and the trained Random Forest pipeline.

## Files

- `app.py` — main Streamlit application.
- `models/final_random_forest_pipeline.joblib` — trained Stage 5 Random Forest pipeline.
- `requirements.txt` — Python dependencies for local/cloud deployment.
- `verify_model.py` — smoke test for the model environment.
- `.streamlit/config.toml` — Streamlit runtime configuration.

## Important model compatibility

The saved model was created with **scikit-learn 1.7.2**. Keep `scikit-learn==1.7.2` in `requirements.txt` to avoid persistence incompatibilities.

Recommended deployment Python version: **Python 3.12**.

## Local test (Windows)

```bat
cd PATH_TO_THIS_FOLDER
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python verify_model.py
python -m streamlit run app.py
```

The verification script should report a B02 smoke-test prediction of approximately `39.98`.

## Streamlit Community Cloud deployment

1. Create a GitHub repository.
2. Upload the complete contents of this folder, including the `models` folder.
3. Open Streamlit Community Cloud and choose **Create app / Deploy app**.
4. Select the GitHub repository and set the main file to `app.py`.
5. In **Advanced settings**, choose **Python 3.12**.
6. Deploy the app.
7. Streamlit will provide a permanent `*.streamlit.app` URL.

## Phone / computer access

The deployed URL opens in any modern browser. On a phone, use **Add to Home Screen** to create an app-like icon. On Windows, Edge/Chrome can create a desktop shortcut or install the site as an app.
