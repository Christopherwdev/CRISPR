from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(y_true, y_pred):
    """Evaluates the model's performance."""
    mse = mean_squared_error(y_true, y_pred)
    rmse = mse**0.5
    r2 = r2_score(y_true, y_pred)
    return mse, rmse, r2
