# CRISPR-Cas9 Editing Efficacy Prediction: A Python Package

This project is my attempt at building a robust and reusable Python package for predicting the on-target efficacy of CRISPR-Cas9 gene editing.  I've always been fascinated by the power and precision of CRISPR technology, and this project represents a personal endeavor to contribute to its advancement through data-driven approaches.

The package utilizes a RandomForestRegressor model, chosen for its balance of predictive power and interpretability.  This makes it suitable for both research and practical applications where understanding the factors influencing editing efficacy is crucial.

**Key Features:**

* **Modular Design:** The code is structured into clearly defined modules for data loading (`data.py`), feature engineering (`features.py`), model training (`model.py`), and evaluation (`evaluate.py`).  This promotes reusability and maintainability.
* **Data Preprocessing:** The package includes functions for basic data preprocessing, handling missing values, and data type conversions.  These functions are designed to be easily adaptable to different datasets.
* **Feature Engineering:**  The `features.py` module provides functions for calculating relevant features from gRNA and target sequences (currently, GC content is implemented; more features can be easily added).
* **Random Forest Model:** A scikit-learn RandomForestRegressor is used for prediction.  The model is trained and evaluated using standard machine learning techniques.
* **Comprehensive Evaluation:** The `evaluate.py` module provides functions to calculate key performance metrics (MSE, RMSE, R-squared) for a thorough assessment of the model's accuracy.
* **Easy Installation:**  The package can be easily installed using pip.


**Getting Started:**

1. **Install dependencies:** `pip install -r requirements.txt` (You'll need to create a `requirements.txt` file listing `pandas` and `scikit-learn`).
2. **Install the package:** `pip install .` (from the root directory)
3. **Prepare your data:** Create a CSV file named `crispr_data.csv` with columns for gRNA sequence, target sequence, and efficacy score.
4. **Run the main script:** `python main.py` (You'll likely need to modify the `main.py` script to point to your data file).

**Future Improvements:**

* **Advanced Feature Engineering:** Incorporate more sophisticated features like off-target scores, structural features of the gRNA-target complex, and sequence motifs known to influence cutting efficiency.
* **Model Optimization:** Explore other machine learning models (e.g., Gradient Boosting, Neural Networks) to potentially improve predictive performance.
* **Hyperparameter Tuning:**  Implement a robust hyperparameter tuning strategy to optimize the RandomForestRegressor's performance.
* **Visualization:** Add data visualization capabilities to better understand the model's predictions and feature importance.


This project is a work in progress, and I welcome contributions and suggestions from the community.  I believe this package has the potential to become a valuable tool for researchers and developers working in the field of CRISPR-Cas9 gene editing.  I hope you find it useful!


You can learn more about my coding projects here: [https://sites.google.com/view/wong-kin-on-christopher/computer-science](https://sites.google.com/view/wong-kin-on-christopher/computer-science)
