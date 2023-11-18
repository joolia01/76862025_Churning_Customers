# Customer Churn Prediction Model

# Problem
Customer churn is a major problem and one of the most important concerns for large companies. Customer churning is when a customer decides to stop using a company's product or service. It is the rate at which businesses lose customers. It directly affects the revenues of the companies, especially in the telecom field. 

# Solution
Therefore, finding factors that increase customer churn is important to take necessary actions to reduce this churn. This is a churn prediction model that assists telecom operators in predicting customers who are most likely subject to churn.

# Dataset
The Customer Churn dataset was provided by the Faculty. It consisted of 20 independent variables and one dependent variable. 
The independent variables were: 
- Customer ID (the ID of the customer)
- Gender(male or female)
- Senior Citizen (whether the customer is a senior citizen-a choice between yes or no)
- Partner(whether the customer has a partner-a choice between yes or no)
- Dependents (whether the customer has dependents-a choice between yes or no)
- Tenure (number of months that an employee has been continuously employed by a company or organization
- Phone Service (whether the customer has a phone service- choice between yes or no)
- Multiple Lines (whether the customer has multiple lines- choice between yes or no or no phone service)
- Internet Service(whether the customer has an internet service- choice between no or DSL or fibre optic)
- Online Security (Whether the customer has online security- choice between yes or no or no internet service)
- Online Backup (Whether the customer has online backup- choice between yes or no or no internet service)
- Device Protection (Whether the customer has online backup- choice between yes or no or no internet service)
- Tech Support (Whether the customer has online backup- choice between yes or no or no internet service)
- Streaming TV (Whether the customer has online backup- choice between yes or no or no internet service)
- Streaming Movies (Whether the customer has online backup- choice between yes or no or no internet service)
- Contract (the contract term of the customer- choice between month-to-month or one year or two year)
- Paperless Billing (Whether the customer has paperless billing- choice between yes or no)
- PaymentMethod  (the payment method of the customer- choice between electronic check or mailed check or bank transfer (automatic) or credit card (automatic))
- Monthly Charge (the amount charged to the customer monthly)
- Total Charges (the total amount charged to the customer)
- Churn (whether the customer churned- choice between yes or no)

# Operations
- Label Encoding
- Imputation (the TotalCharges column only)
- Correlation Analysis
- Scaling
- Exploratory Data Analysis (EDA): Compared each categorical independent variable to 'Churn' and created bar charts; Compared each quantitative variable to 'Churn' and created box plots
- Training a Multi-Layer Perceptron model using the Functional API, using features from the feature extraction process, with cross-validation and GridSearchCV
- Evaluated the model’s accuracy, calculated the AUC score, optimised the model, trained and tested again
- Created a web-based platform using Streamlit to host the model
- Allowed users to use the application to enter new data. However, my the model was not able to predict churn and print the confidence factor of the model

# Extracted Features to Predict Customer Churn
- Dependents
- Tenure
- OnlineSecurity
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaperlessBilling
- PaymentMethod
- MonthlyCharges
- TotalCharges

# Demo Link
- Demo link: https://youtu.be/e0skNxTVdCY
