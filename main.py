from crispr_efficacy import data, features, model, evaluate
import pandas as pd

# Load and preprocess data
data_path = "crispr_data.csv"  # Replace with your data file path
raw_data = data.load_data(data_path)
if raw_data is not None:
    processed_data = data.preprocess_data(raw_data)
    featured_data = features.engineer_features(processed_data)

    # Split data into features (X) and target (y)
    X = featured_data.drop(["efficacy", "gRNA_sequence", "target_sequence"], axis=1)
    y = featured_data["efficacy"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    trained_model = model.train_model(X_train, y_train)

    # Make predictions
    y_pred = model.make_predictions(trained_model, X_test)

    # Evaluate the model
    mse, rmse, r2 = evaluate.evaluate_model(y_test, y_pred)
    print(f"MSE: {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R-squared: {r2:.2f}")
