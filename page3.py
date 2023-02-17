import streamlit as st 
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.model_selection import train_test_split 
from sklearn import svm
import numpy as np
def load_diabetes_data():
    return pd.read_excel('Diabetes.xlsx',index_col=0)

def save_model(model):
    joblib.dump(model, 'model_diabete.joblib')

def load_model():
    return joblib.load('model_diabete.joblib')



def page_three():
    global X,Y,scal
    st.title("🩸Diabetes Prediction🩸")
    st.caption("This is a Diabetes prediction machine learning system.") 
    st.markdown("Attention Please,Please do by step by step 1 to 4 your final step is :red[prediction]") 
    name = st.text_input("Enter your name")
    col1,col2 = st.columns(2)
    Button = col1.button('1.Let\'s Start!')
    
    if Button: #creating model
        scal = StandardScaler()
        data = pd.read_csv('diabetes.csv')
        data_Frame = pd.DataFrame(data) 
        #creating X and Y
        X = data_Frame.drop(columns= 'Outcome',axis= 1)
        Y = data_Frame['Outcome']
        X_for_used = scal.fit_transform(X)
        data_Frame.to_excel('Diabetes.xlsx') 
    Load_button = col2.button('2.Showing Data')
    if Load_button: # loading model
        df = load_diabetes_data()
        pd.DataFrame(df)
        st.write(df.head()) 
    if name: # training bot
        Training_button = col1.button(f"3.Traning {name}'s bot") 
        if Training_button:
            x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size= 0.2,stratify=Y )
            model = svm.SVC()
            model.fit(x_train,y_train) 
            save_model(model)   
    
    Pred_Button = col2.button("4.prediction")    
    Pregnancies = st.slider('The Number of pregnancies',0,17,8)
    Glucose = st.slider('The Glucose level in blood',0,200,100)
    BloodPressure = st.slider('The Blood pressure measurement',0,150,75) 
    SkinThickness = st.number_input('Express the thickness of the skin')
    Insulin = st.slider('express the Insulin level in blood',0,900,450)
    B_M_I =st.number_input('express the Body mass index',key=1) 
    DiabetesPedigreeFunction = st.number_input('To express the Diabetes percentage',key=2) 
    Age = st.slider('Express the age',0,100)
    if Pred_Button:
        model = load_model()
        Data_input = (Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,B_M_I,DiabetesPedigreeFunction,Age)
        array_data_input = np.asarray(Data_input)
        reshape_array_data_input = array_data_input.reshape(1,-1)
        std = scal.transform(reshape_array_data_input)
        predict_Diabtete = model.predict(std)
        result = predict_Diabtete[0]
        if result == 1:
            st.error('I\'m sorry to say that You probably have a Diabetes.Please take care yourself.')
        else:
            st.info('You don\'t have a Diabetes')
        f = open('Diabete_result.csv','w')
        f.write(str(result) +"," + str(Pregnancies) +","+ str(Glucose) +","+ str(BloodPressure) +","+ str(SkinThickness) +","+ str(Insulin) +","+ str(B_M_I) +","+ str(DiabetesPedigreeFunction) +","+ str(Age)+','+ str(name))
        f.close() 
