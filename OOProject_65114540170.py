import streamlit as st
import page1 as p1
import time as t
import page3 as p3
import page4 as p4

with st.sidebar:
    genre = st.selectbox(
    "Choose your Prediction",
    ('Introduction', 'Heart disease Prediction', 'Diabetes prediction','Result'))

if genre == 'Introduction':
    
    with st.spinner():
        t.sleep(5)
    
    st.title("Introduction Page") 
    st.caption("Welcome to my project Let me introduce myself My name is Natthachai Sisai 65114540170 UBU science student")
    st.markdown("")
    
    Heart_bar = st.progress(0)
    for Heart_bar_percent in range(100):
        t.sleep(0.00000000001)
        Heart_bar.progress(Heart_bar_percent + 1)
    
    with st.expander("What is Heart disease Prediction?"):
        st.success('Cardiovascular diseases (CVDs)')
        st.info('are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worldwide. Four out of 5CVD deaths are due to heart attacks and strokes, and one-third of these deaths occur prematurely in people under 70 years of age. Heart failure is a common event caused by CVDs and this dataset contains 11 features that can be used to predict a possible heart disease.') 
        st.markdown('    ')
        st.info('People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.') 
        st.markdown('       ')
        st.success('Attribute Information')
        st.text('Age: age of the patient (years) \nSex: sex of the patient (M: Male, F: Female) \nChestPain: Chest pain (typical, asymptotic, nonanginal, nontypical) \nRestBP: Resting blood pressure \n  Chol: Serum cholestoral in mg/dl \n  Fbs: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false) \n  RestECG: Resting electrocardiographic results \n  MaxHR: Maximum heart rate achieved \n  ExAng: Exercise induced angina (1 = yes; 0 = no) \n  Oldpeak: ST depression induced by exercise relative to rest \n  Slope: Slope of the peak exercise ST segment \n  Ca: Number of major vessels colored by flourosopy (0 - 3) \n  Thal: (0 = normal; 1 = fixed defect; 2 = reversable defect)') 
        st.markdown("   ")
        st.success("Creators of Datasets that I used")
        st.text('Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D. \nUniversity Hospital, Zurich, Switzerland: William Steinbrunn, M.D. \nUniversity Hospital, Basel, Switzerland: Matthias Pfisterer, M.D. \nV.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.')
        st.markdown(" ")
        st.success('Data Set Information')
        st.text('This database contains attributes, but all published experiments refer to using a subset of 14 of them. In particular, the Cleveland database is the only one that has been used by ML researchers to this date. \nThe "goal" field refers to the presence of heart disease in the patient. \nIt is integer valued from 0 (no presence) to 4. \nExperiments with the Cleveland database have concentrated on simply attempting to distinguish presence from absence (value 0).\nThe names and social security numbers of the patients were recently removed from the database, replaced with dummy values.')
    
    Diabete_bar = st.progress(0)
    for Diabete_bar_percent in range(100):
        t.sleep(0.00000000001)
        Diabete_bar.progress(Diabete_bar_percent + 1)
    
    with st.expander('What is Diabete Prediction?'):
        st.success('Diabetes')
        st.info('is a chronic medical condition characterized by high levels of sugar (glucose) in the blood. The body needs insulin, a hormone produced by the pancreas, to transport glucose from the bloodstream into the cells where it can be used for energy. In people with diabetes, the body either doesn\'t produce enough insulin (Type 1 diabetes) or is unable to use it effectively (Type 2 diabetes).\n Type 1 diabetes typically develops in childhood or adolescence and is thought to be an autoimmune disorder in which the immune system attacks and destroys the cells in the pancreas that produce insulin. Type 2 diabetes, on the other hand, typically develops in adulthood and is often associated with factors such as obesity, a sedentary lifestyle, and a family history of the disease.\nIf left untreated, high blood sugar levels over time can lead to a range of serious health complications, including cardiovascular disease, nerve damage, kidney disease, eye problems, and more. Treatment for diabetes often involves lifestyle changes such as diet and exercise, as well as medications or insulin therapy as needed to help manage blood sugar levels.') 
        st.markdown(" ")
        st.success("About Datasets")
        st.info('This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether a patient has diabetes,based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.2 From the data set in the (.csv) File We can find several variables, some of them are independent (several medical predictor variables) and only one target dependent variable (Outcome).')
        st.markdown(" ")
        st.success("Attributes")
        st.text('Pregnancies: To express the Number of pregnancies \nGlucose: To express the Glucose level in blood \nBloodPressure: To express the Blood pressure measurement \nSkinThickness: To express the thickness of the skin \nInsulin: To express the Insulin level in blood \nBMI: To express the Body mass index \nDiabetesPedigreeFunction: To express the Diabetes percentage \nAge: To express the age \nOutcome: To express the final result 1 is Yes and 0 is No')
        st.success("Source")
        st.error('Michael Kahn, MD, PhD, Washington University, St. Louis, MO')
    
    Diabete_bar = st.progress(0)
    for Diabete_bar_percent in range(100):
        t.sleep(0.00000000001)
        Diabete_bar.progress(Diabete_bar_percent + 1)
    
    with st.expander('What is Result?'):
        st.success('Result page is a result of Heart Disease Prediction and Diabetes Prediction')
        
if genre == 'Heart disease Prediction':
    p1.page_one()

    
if genre == 'Diabetes prediction': 
    with st.spinner():
        t.sleep(1)
        p3.page_three() 
    st.success("Complete . . .")
    
if genre == 'Result':
    with st.spinner():
        t.sleep(3)
    p4.page_four()
