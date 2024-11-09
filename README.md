
# Loan Approval Classifier

A Streamlit-based web application that predicts loan approval status based on user-provided information, utilizing a pre-trained machine learning model.

## Dataset
The dataset is used here is [Loan Data Set](https://www.kaggle.com/datasets/burak3ergun/loan-data-set)

## Overview
The Loan Approval Classifier allows users to input personal, financial, and credit history information to determine the likelihood of a loan being approved. The application uses a machine learning model `RandomForestRegressor` saved as `model.pkl`, which evaluates the input data and provides a prediction of either "Approved" or "Not Approved."

## Features
- **User-Friendly Interface**: Designed with Streamlit for ease of use, allowing quick data entry and instant predictions.
- **Data Input Fields**:
  - **Demographic Information**: Collects details such as gender, marital status, dependents, education level, employment type, and property area.
  - **Income Information**: Captures applicant and co-applicant income data.
  - **Loan Information**: Includes loan amount and term.
  - **Credit History**: Allows input of credit history, where 1 indicates good credit, and 0 indicates poor credit.
- **Prediction**: A machine learning model, loaded from `model.pkl`, is applied to the input data to predict loan approval status.


## Evaluation Results
The output of the model evaluation metrics is as follows:

**Precision:** 95%

**F1 Score:** 89%

## License
[MIT License](LICENSE)