import streamlit as stl
import pandas as pd
import pickle


def welcome(): 
    return 'welcome all'

# defining the function which will make the prediction using  
# the data which the user inputs 
def prediction(Dependents, tenure, OnlineSecurity, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges ):
  with open("best_model.pkl", "rb") as f:
        best_model = pickle.load(f)
  prediction = best_model.predict( 
        [[Dependents, tenure, OnlineSecurity, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges 
          ]]) 
  
  confidence_factor=prediction.squeeze()
  print(prediction) 
  print (confidence_factor)
  return confidence_factor   


# this is the main function in which we define our webpage  
def main(): 
    # giving the webpage a title 
    stl.title("Customer Churn Prediction") 
      
    # here we define some of the front end elements of the web page like  
    # the font and background color, the padding, and the text to be displayed 
    html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Customer Churn Prediction App </h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    stl.markdown(html_temp, unsafe_allow_html=True) 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction    
    tenure = stl.number_input("tenure", 0) 
    MonthlyCharges = stl.number_input("MonthlyCharges", 0)
    TotalCharges = stl.number_input("TotalCharges", 0)

    Dependents = stl.selectbox("Dependents? Enter 0 for no OR 1 for yes", [0, 1])
    OnlineSecurity = stl.selectbox("Online Security? Enter 0 for no OR 1 for no service OR 2 for yes", [0, 1, 2])
    DeviceProtection = stl.selectbox("Device Protection? Enter 0 for no OR 1 for no service OR 2 for yes", [0, 1, 2])
    TechSupport = stl.selectbox("Tech Support? Enter 0 for no OR 1 for no service OR 2 for yes", [0, 1, 2])
    StreamingTV = stl.selectbox("Streaming TV? Enter 0 for no OR 1 for no service OR 2 for yes", [0, 1, 2])
    StreamingMovies = stl.selectbox("Streaming Movies? Enter 0 for no OR 1 for no service OR 2 for yes", [0, 1, 2])
    Contract = stl.selectbox("Contract? Enter 0 for Month-to-month OR 1 for One Year OR 2 for Two Years", [0, 1, 2])
    PaperlessBilling = stl.selectbox("PaperlessBilling? Enter 0 for no OR 1 for yes", [0, 1])
    PaymentMethod = stl.selectbox("Payment Method? Enter 0 for Bank transfer (automatic) OR 1 for Credit card (automatic) OR 2 for Electronic check OR 3 for Mailed check",  [0, 1, 2, 3])

    # Load the model outside the button click
    with open("best_model.pkl", "rb") as f:
        best_model = pickle.load(f)

    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    if stl.button("Predict"):
        result = prediction(Dependents, tenure, OnlineSecurity, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges) 
        stl.write(f'The output is {int(result[0])}')

if __name__ == '__main__': 
    main()
