
    
#Parkinsons Prediction Page
if(selected == "Parkinson's Prediction"):
    
    #Page title
    st.title('Parkinsons Prediction using ML')
    

        # Create columns for better UI with a maximum of 5 inputs per column
    col1, col2, col3, col4, col5 = st.columns(5)

    # Input fields in the first column
    with col1:
        fo = st.number_input('MDVP:Fo (fo)', key='fo')
        fhi = st.number_input('MDVP:Fhi (fhi)', key='fhi')
        Shimmer = st.number_input('MDVP:Shimmer (shimmer)', key='shimmer')
        APQ = st.number_input('MDVP:APQ (apq)', key='apq')
        RPDE = st.number_input('RPDE (rpde)', key='rpde')

    # Input fields in the second column
    with col2:
        flo = st.number_input('MDVP:Flo (flo)', key='flo')
        Jitter_percent = st.number_input('MDVP:Jitter (%) (jitter_percent)', key='jitter_percent')
        Shimmer_dB = st.number_input('MDVP:Shimmer (dB) (shimmer_db)', key='shimmer_db')
        DDA = st.number_input('Shimmer:DDA (dda)', key='dda')
        DFA = st.number_input('DFA (dfa)', key='dfa')

    # Input fields in the third column
    with col3:
        Jitter_Abs = st.number_input('MDVP:Jitter (Abs) (jitter_abs)', key='jitter_abs')
        RAP = st.number_input('MDVP:RAP (rap)', key='rap')
        APQ3 = st.number_input('Shimmer:APQ3 (apq3)', key='apq3')
        NHR = st.number_input('NHR (nhr)', key='nhr')
        spread1 = st.number_input('spread1 (spread1)', key='spread1')

    # Input fields in the fourth column
    with col4:
        PPQ = st.number_input('MDVP:PPQ (ppq)', key='ppq')
        DDP = st.number_input('Jitter:DDP (ddp)', key='ddp')
        APQ5 = st.number_input('Shimmer:APQ5 (apq5)', key='apq5')
        HNR = st.number_input('HNR (hnr)', key='hnr')
        spread2 = st.number_input('spread2 (spread2)', key='spread2')

    # Input fields in the fifth column
    with col5:
        # Additional inputs
        D2 = st.number_input('D2 (d2)', key='d2')
        PPE = st.number_input('PPE (ppe)', key='ppe')

        
    #Code for prediction
    parkinsons_diagnosis = ''
        
    #Creating a button for prediction
        
    if st.button('Parkinsons Test Result'):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            
            if (parkinsons_prediction[0]==1):
                parkinsons_diagnosis = 'The person is suffering from Parkinsons disease'
                
            else:
                parkinsons_diagnosis = 'The person is Not suffering from Parkinsons disease'
                
                
    st.success(parkinsons_diagnosis)