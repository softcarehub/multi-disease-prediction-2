

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
st.set_page_config(page_title='Multi-disease Prediction',  layout = 'wide', initial_sidebar_state = 'auto')
# favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
#parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multi-Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'
                           ],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page 
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Name = st.text_input("Name of the patient")
    with col2:
        Age = st.text_input("Age")
    with col3:
        Gender = st.text_input("Gender")
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    # code for Prediction
    diab_diagnosis = ''
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        if(Pregnancies and Glucose and BloodPressure and SkinThickness and Insulin and BMI and DiabetesPedigreeFunction and Age) : 
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            #st.success("sd"+diab_diagnosis)
            st.write("Patient Name : ",Name)
            st.write("Age : ",Age)
            st.write("Gender : ",Gender)
            if (diab_prediction[0] == 1):
                diab_diagnosis = 'The person is diabetic 🥺'
                st.error(diab_diagnosis)
            else:
                diab_diagnosis = 'The person is not diabetic 😊'
                #st.balloons()
                st.success(diab_diagnosis)
        else : 
            st.warning("Please fill all details")
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Name = st.text_input("Name of the patient")
    with col2:
        age = st.text_input("Age")
    # with col3:
    #     Gender = st.text_input("Gender")
    with col3:
        sex = st.text_input('Sex (1-F,0-M)')
    with col1:
        cp = st.text_input('Chest Pain types')
    with col2:
        trestbps = st.text_input('Resting Blood Pressure')
    with col3:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col1:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col2:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col3:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col1:
        exang = st.text_input('Exercise Induced Angina')
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col3:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col1:
        ca = st.text_input('Major vessels colored by flourosopy')        
    #col1, col2= st.columns(2)
    with col2:
        thal = st.text_input('thal: 0 = normal; 1 = fixed; 2 = reversable')
    
    
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        
        if(age and sex and cp and trestbps and chol and fbs and restecg and thalach and exang and oldpeak and slope and ca and thal) : 
            heart_prediction = heart_disease_model.predict([[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]])                          
            st.write("Patient Name : ",Name)
            st.write("Age : ",age)
            if(sex=="1"):
                st.write("Gender : Female")
            else:
                st.write("Gender : Male")
           # st.write("Gender : ",Gender)
            if (heart_prediction[0] == 1):
                st.error('The person is having heart disease')
            else:
                st.success('The person does not have any heart disease 😊')
            #st.success(heart_diagnosis)
        else : 
            st.warning("Please fill all details")



