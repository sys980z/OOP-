import streamlit as st
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib 
import numpy as np
import time as t
def load_heart_data():
    return pd.read_excel('heart.xlsx')

def save_model(model):
    joblib.dump(model, 'model.joblib')

def load_model():
    return joblib.load('model.joblib')
def page_one():
    global t0,X,Y
    st.title("🩸Heart disease Prediction🩸")
    st.caption("This is a Heart disease prediction machine learning system.") 
    st.markdown("Attention Please,Please do by step by step 1 to 4 your final step is :red[go!!!]")
    col1, col2 = st.columns(2) 
    option = col1.selectbox(
'How would you like to be contacted?',
('Let start!!!', '👀 Load your Dataset 👀', '👾Training!👾',"go!!!"))
    if option == 'Let start!!!': # Create model fuction
        t0 = int(t.time())
        with st.spinner('generating. . .'):
            t1 = int(t.time())
            t.sleep(1+t1 - t0)
            data = pd.read_csv('heart.csv')
            data = pd.DataFrame(data)
            X = data.drop(columns= 'target',axis= 1)
            Y = data['target']
            data.to_excel('heart.xlsx')
        col1.success("Generating Complete. . .")
    if option == '👀 Load your Dataset 👀': # Load model fucntions
        t0 = int(t.time())
        with st.spinner('Loading. . .'):
            t1 = int(t.time())
            t.sleep(1+t1 - t0)
            df = pd.read_excel('heart.xlsx', index_col=0)
            pd.DataFrame(df)
            st.write(df.head())
        col1.success("Loading complete . . .")
    if option == '👾Training!👾': #training model
        with st.spinner('Training. . .'):
            t.sleep(5)
        col1.success("Training Complete . . .")
        x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size= 0.2,stratify=Y,random_state= 2)
        model = LogisticRegression()
        model.fit(x_train,y_train) 
        save_model(model)
    
    if option == 'go!!!':
        pass
    age = col2.slider("Input your age",0,100) 
    sex = 0
    genre_sex = col2.radio(
    "What\'s your sex?",
    ('Female', 'Male'))
    if genre_sex == 'Male':sex = 1 
    cp = col2.slider("Chest pain level",0,3)
    col2.caption("typical = 0 ,asymptotic = 1 ,nonanginal = 2 ,nontypical = 3") 
    trestbps = col2.slider("Resting blood pressure",90,210) 
    chol = col2.slider('Serum cholestoral in mg/dl',110,570)
    fbs = 1
    genre_fbs = col2.radio(
    "Fasting blood sugar > 120 mg/dl?",
    ('Yes', 'No'))
    if genre_fbs == 'No':sex = 0 
    RestECG = col2.slider('Resting electrocardiographic results',0,2) 
    thalach = col2.slider('Maximum heart rate achieved',70,210)
    exang = 1
    genre_exang = col2.radio(
    "Exercise induced angina?",
    ('Yes', 'No'))
    if genre_exang == 'No':exang = 0 
    oldpeak = col2.number_input('ST depression induced by exercise relative to rest') 
    slope = col2.slider('Slope of the peak exercise ST segment',0,2)
    Ca = col2.slider('Number of major vessels colored by flourosopy',0,3) 
    Thal = col2.slider('(0 = normal; 1 = fixed defect; 2 = reversable defect',0,2,1)  
    Pred = col2.button('Press here to Prediction')
    if Pred:
        model = load_model() 
        Pred_data = (age,sex,cp,trestbps,chol,fbs,RestECG,thalach,exang,oldpeak,slope,Ca,Thal) 
        Pred_data_array = np.asarray(Pred_data)
        Pred_data_array_re = Pred_data_array.reshape(1,-1)
        predict_Heart = model.predict(Pred_data_array_re)
        result = predict_Heart[0]
        if result == 1:
            col1.error('I\'m sorry to say that You probably have a Heart disease.Take care yourself.')
        else:
            col1.info('You don\'t have a Heart disease') 
        predict_Heart.to_excel("Heart_result.xlsx") 
        f_Heart = open('Heart_result.csv','w')
        f_Heart.write(f'{result},{age},{sex},{cp},{trestbps},{RestECG},{thalach},{exang},{oldpeak},{slope},{Ca},{Thal}')
        f_Heart.close