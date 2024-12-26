import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def train_model(X_train, y_train):
    """Trains a RandomForestRegressor model."""
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    pipeline.fit(X_train, y_train)
    return pipeline

def make_predictions(model, X_test):
    """Makes predictions using the trained model."""
    return model.predict(X_test)
