import streamlit as st
from PIL import Image
def page_four():
    st.title("Result of Prediction")
    
    Heart,Diabete = st.columns(2)
    
    
    with Heart.expander("The Result of Heart disease Prediction "): 
        f_heart = open('Heart_result.csv','r')
        Heart_data = f_heart.read().split(',')
        
        if int(Heart_data[0]) == 1:
            st.error('!Heart disease Detected.!')
        else:
            st.info("!Heart disease Not Detected.!")
        st.markdown(f'Age : {Heart_data[1]} years old')
        
        if int(Heart_data[2]) == 1:
            st.markdown("Sex : Man")
        else:
            st.markdown("Sex : Woman") 
        image = Image.open('Stage-of-CHF-Infographic.jpg')
        st.image(image, caption='Stage of CHF') 
    
        
    with Diabete.expander("The Result of Diabete Prediction"):
        f_diabete = open('Diabete_result.csv','r')
        Diabete_data = f_diabete.read().split(',')
        if int(Diabete_data[0]) == 1:
            st.error('!Diabete Detected!') 
        else:
            st.info("!Diabete Not Detected!")   
        
        st.markdown(f'Name : {Diabete_data[-1]}')
        st.markdown(f'Age : {Diabete_data[-2]} years old.')
        image2 = Image.open('Diabetes.jpg')
        st.image(image2,caption='Diabetes')