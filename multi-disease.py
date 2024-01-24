import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
st.set_page_config(page_title='Multi-disease Prediction',  layout = 'wide', initial_sidebar_state = 'auto')
# favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)

diabetes_model = pickle.load(open('Diabetes_RandomForest_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_Adaboost_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_Stacking_Ensemble_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    st.title('Multi-Disease Prediction System')
    st.markdown("---")  # Add a horizontal line for separation
    selected = option_menu('Select Disease',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           "Parkinson's Prediction"
                           ],
                          icons=['activity','heart','person'],
                          default_index=0)
    dataset = "https://drive.google.com/drive/folders/15k-0dPKuYCOP5nirLimBbOS7k0pxDNE4?usp=sharing" 
    parkinsons = "https://www.linkedin.com/in/md-bariul-munshi/"
    st.markdown("[Get User-Guide](%s)" % dataset)
    url = "https://www.linkedin.com/in/md-bariul-munshi/" 
    st.write("Copyright©2023[Md. Bariul Munshi](%s)" % url)
    
    
# Diabetes Prediction Page 
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        Glucose = st.text_input('Glucose Level')
        BloodPressure = st.text_input('Blood Pressure value')
    with col2:
        SkinThickness = st.text_input('Skin Thickness value')
        Insulin = st.text_input('Insulin Level')
        BMI = st.text_input('BMI value')
    with col3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        Age = st.text_input("Age")
    # code for Prediction
    diab_diagnosis = ''
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        if(Pregnancies and Glucose and BloodPressure and SkinThickness and Insulin and BMI and DiabetesPedigreeFunction and Age) : 
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
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
        age = st.text_input("Age")
        sex = st.text_input('Sex (1-M,0-F)')
        cp = st.text_input('Chest Pain types')
        trestbps = st.text_input('Resting Blood Pressure')
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col2:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        restecg = st.text_input('Resting Electrocardiographic results')
        thalach = st.text_input('Maximum Heart Rate achieved')
        exang = st.text_input('Exercise Induced Angina')
        oldpeak = st.text_input('ST depression induced by exercise')
    with col3:
        slope = st.text_input('Slope of the peak exercise ST segment')
        ca = st.text_input('Major vessels colored by flourosopy')        
        thal = st.text_input('thal: 0 = normal; 1 = fixed; 2 = reversable')
     
    # code for Prediction
    heart_diagnosis = ''
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        
        if(age and sex and cp and trestbps and chol and fbs and restecg and thalach and exang and oldpeak and slope and ca and thal) : 
            heart_prediction = heart_disease_model.predict([[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]])
            if (heart_prediction[0] == 1):
                st.error('The person is having heart disease')
            else:
                st.success('The person does not have any heart disease 😊')
            #st.success(heart_diagnosis)
        else : 
            st.warning("Please fill all details")
            
            
#Parkinsons Prediction Page
if(selected == "Parkinson's Prediction"):
    #Page title
    st.title('Parkinsons Prediction using ML')
        # Create columns for better UI with a maximum of 5 inputs per column
    col1, col2, col3, col4, col5 = st.columns(5)

    # Input fields in the first column
    with col1:
        fo = st.text_input('MDVP:Fo (fo)', key='fo')
        fhi = st.text_input('MDVP:Fhi (fhi)', key='fhi')
        Shimmer = st.text_input('MDVP:Shimmer (shimmer)', key='shimmer')
        APQ = st.text_input('MDVP:APQ (apq)', key='apq')
        RPDE = st.text_input('RPDE (rpde)', key='rpde')

    # Input fields in the second column
    with col2:
        flo = st.text_input('MDVP:Flo (flo)', key='flo')
        Jitter_percent = st.text_input('MDVP:Jitter (%) (jitter_percent)', key='jitter_percent')
        Shimmer_dB = st.text_input('MDVP:Shimmer (dB) (shimmer_db)', key='shimmer_db')
        DDA = st.text_input('Shimmer:DDA (dda)', key='dda')
        DFA = st.text_input('DFA (dfa)', key='dfa')

    # Input fields in the third column
    with col3:
        Jitter_Abs = st.text_input('MDVP:Jitter (Abs) (jitter_abs)', key='jitter_abs')
        RAP = st.text_input('MDVP:RAP (rap)', key='rap')
        APQ3 = st.text_input('Shimmer:APQ3 (apq3)', key='apq3')
        NHR = st.text_input('NHR (nhr)', key='nhr')
        spread1 = st.text_input('spread1 (spread1)', key='spread1')

    # Input fields in the fourth column
    with col4:
        PPQ = st.text_input('MDVP:PPQ (ppq)', key='ppq')
        DDP = st.text_input('Jitter:DDP (ddp)', key='ddp')
        APQ5 = st.text_input('Shimmer:APQ5 (apq5)', key='apq5')
        HNR = st.text_input('HNR (hnr)', key='hnr')
        spread2 = st.text_input('spread2 (spread2)', key='spread2')

    # Input fields in the fifth column
    with col5:
        # Additional inputs
        D2 = st.text_input('D2 (d2)', key='d2')
        PPE = st.text_input('PPE (ppe)', key='ppe')

        
    parkinsons_diagnosis = ''

    # Creating a button for prediction
    if st.button('Parkinsons Test Result'):
        if (fo and fhi and flo and Jitter_percent and Jitter_Abs and RAP and PPQ and DDP and Shimmer and Shimmer_dB and APQ3 and APQ5 and APQ and DDA and NHR and HNR and RPDE and DFA and spread1 and spread2 and D2 and PPE):
            parkinsons_prediction = parkinsons_model.predict([[float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB), float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]])

            if (parkinsons_prediction[0] == 1):
                st.error('The person is suffering from Parkinsons disease')
            else:
                st.success('The person is Not suffering from Parkinsons disease 😊')
        else:
            st.warning("Please fill all details")