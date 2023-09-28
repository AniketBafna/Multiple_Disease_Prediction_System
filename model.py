
from audioop import reverse
import re
import pandas as pd
import numpy as np
import streamlit as st
import pickle
import json
from streamlit_option_menu import option_menu

def model():

    with st.sidebar:
        add_checkbox = option_menu('Multiple Disease Prediction System using ML',
                                   ['Heart Disease Prediction',
                                    'Diabetes Prediction',
                                    'Hypertension Prediction'])

    if add_checkbox == "Heart Disease Prediction":
        st.header("Heart Disease Predictor")

        pipe1 = pickle.load(open('pipe1.pkl','rb'))
        df1 = pd.read_csv("Heart_data_clean.csv")

        #st.write(df1)
        #'BMI', 'PhysicalHealth', 'MentalHealth']

        smoke = np.sort(df1['Smoking'].unique())
        alcho = np.sort(df1['AlcoholDrinking'].unique())
        stroke = np.sort(df1['Stroke'].unique())
        walk = np.sort(df1['DiffWalking'].unique())
        sex = np.sort(df1['Sex'].unique())
        age = np.sort(df1['AgeCategory'].unique())
        race = np.sort(df1['Race'].unique())
        diabetic = np.sort(df1['Diabetic'].unique())
        phyact = np.sort(df1['PhysicalActivity'].unique())
        genheal = np.sort(df1['GenHealth'].unique())
        sleep = np.sort(df1['SleepTime'].unique())
        asthma = np.sort(df1['Asthma'].unique())
        kidney = np.sort(df1['KidneyDisease'].unique())
        skin = np.sort(df1['SkinCancer'].unique())

        col1, col2, col3 = st.columns(3)
        with col1:
            bmi = st.number_input("BMI",step=0.1)
        with col2:
            phyheal = st.number_input("Physical Health",step=1)
        with col3:
            menheal = st.number_input("Mental Health",step=1)

        col1, col2 = st.columns(2)
        with col1:
            smoke = st.selectbox("Smoker",smoke)
        with col2:
            alcho = st.selectbox("Alcholic",alcho)

        col3, col4 = st.columns(2)
        with col3:
            stroke = st.selectbox("Stroke",stroke)
        with col4:
            walk = st.selectbox("Difficulty in Walking",walk)

        col5, col6 = st.columns(2)
        with col5:
            sex = st.selectbox("Gender",sex)
        with col6:
            age = st.selectbox("Age Category",age)

        col7, col8 = st.columns(2)
        with col7:
            race = st.selectbox("Race/Ethnicity",race)
        with col8:
            diabetic = st.selectbox("Diabetic",diabetic)

        col9, col10 = st.columns(2)
        with col9:
            phyact = st.selectbox("Physical Activity",phyact)
        with col10:
            genheal = st.selectbox("General Health",genheal)

        col11, col12 = st.columns(2)
        with col11:
            sleep = st.selectbox("Sleep (in Hours)",sleep)
        with col12:
            asthma = st.selectbox("Asthma",asthma)

        col13, col14 = st.columns(2)
        with col13:
            kidney = st.selectbox("Kidney Disease",kidney)
        with col14:
            skin = st.selectbox("Skin Disease",skin)

        if st.button('Predict Score'):
            input_df = pd.DataFrame({'BMI':[bmi], 'Smoking':[smoke], 'AlcoholDrinking':[alcho],'Stroke':[stroke],'PhysicalHealth':[phyheal],
                                'MentalHealth':[menheal], 'DiffWalking':[walk], 'Sex':[sex], 'AgeCategory':[age], 'Race':[race], 
                                'Diabetic':[diabetic], 'PhysicalActivity':[phyact], 'GenHealth':[genheal], 'SleepTime':[sleep], 
                                'Asthma':[asthma], 'KidneyDisease':[kidney], 'SkinCancer':[skin]})
            result = pipe1.predict(input_df)
            #st.write(result)
            if str(result[0]) == 'No':
                st.header("The Patient has No Heart Disease :blush::thumbsup:")
            else:
                st.header("The Patient has Heart Disease :neutral_face::thumbsdown:")

            #23.62	No	No	No	5	7	No	Female	40-44	White	No	Yes	Very good	7	No	No	No



    if add_checkbox == "Diabetes Prediction":
        st.header("Diabetes Disease Predictor")

        pipe2 = pickle.load(open('pipe2.pkl','rb'))
        df2 = pd.read_csv("Diabetes_clean_data.csv")

        sex = np.sort(df2['Sex'].unique())
        coll = np.sort(df2['HighChol'].unique())
        checkk = np.sort(df2['CholCheck'].unique())
        smokee = np.sort(df2['Smoker'].unique())
        heartdiseasee = np.sort(df2['HeartDiseaseorAttack'].unique())
        phyactt = np.sort(df2['PhysActivity'].unique())
        fruit = np.sort(df2['Fruits'].unique())
        veggies = np.sort(df2['Veggies'].unique())
        alcoll = np.sort(df2['HvyAlcoholConsump'].unique())
        genhealt = np.sort(df2['GenHlth'].unique())
        diffwalk = np.sort(df2['DiffWalk'].unique())
        strokes = np.sort(df2['Stroke'].unique())
        bp = np.sort(df2['HighBP'].unique())


        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input("Patient's Age",step=1)
        with col2:
            menhealt = st.number_input("Mental Health",step=1)
        with col3:
            physhealt = st.number_input("Physical Health",step=1)
        

        col5, col6 = st.columns(2)
        with col5:
            sex = st.selectbox("Gender",sex)
        with col6:
            smokee = st.selectbox("Smoker",smokee)

        col7, col8 = st.columns(2)
        with col7:
            bp = st.selectbox("Blood Pressure",bp)
        with col8:
            bmi = st.number_input("BMI")

        col7, col8 = st.columns(2)
        with col7:
            coll = st.selectbox("High Cholestrol",coll)
        with col8:
            checkk = st.selectbox("Cholestrol Check (in 5 years)",checkk)

        col9, col10 = st.columns(2)
        with col9:
            fruit = st.selectbox("Consume Fruits Daily",fruit)
        with col10:
            veggies = st.selectbox("Consume Vegetable Daily",veggies)

        col11, col12 = st.columns(2)
        with col11:
            heartdiseasee = st.selectbox("Suffered Heart Disease",heartdiseasee)
        with col12:
            strokes = st.selectbox("Suffered Stroke",strokes)

        col13, col14 = st.columns(2)
        with col13:
            phyactt = st.selectbox("Physical Activity",phyactt)
        with col14:
            alcoll = st.selectbox("Alcoholic",alcoll)

        col15, col16 = st.columns(2)
        with col15:
            genhealt = st.selectbox("General Health",genhealt)
        with col16:
            diffwalk = st.selectbox("Difficulty in Walking",diffwalk)

        if st.button('Predict Score'):
            input_df = pd.DataFrame({'Age':[age], 'Sex':[sex], 'HighChol':[coll],'CholCheck':[checkk], 'BMI':[bmi],'Smoker':[smokee],
                             'HeartDiseaseorAttack':[heartdiseasee], 'PhysActivity':[phyactt], 'Fruits':[fruit], 'Veggies':[veggies], 
                             'HvyAlcoholConsump':[alcoll], 'GenHlth':[genhealt], 'MentHlth':[menhealt], 'PhysHlth':[physhealt], 
                             'DiffWalk':[diffwalk], 'Stroke':[strokes], 'HighBP':[bp]})
            result = pipe2.predict(input_df)

            if str(int(result[0])) == 0:
                st.header("The Patient has No Diabetes :blush:")
            else:
                st.header("The Patient has Diabetes Disease :neutral_face:")


    if add_checkbox == "Hypertension Prediction":
        st.header("Hypertension Disease Predictor")

        pipe3 = pickle.load(open('pipe3.pkl','rb'))
        df3 = pd.read_csv("hypertension_data_clean.csv")


        sex = np.sort(df3['sex'].unique())
        cp = np.sort(df3['cp'].unique())
        fbs = np.sort(df3['fbs'].unique())
        restecg = np.sort(df3['restecg'].unique())
        exang = np.sort(df3['exang'].unique())
        slope = np.sort(df3['slope'].unique())
        ca = np.sort(df3['ca'].unique())
        thal = np.sort(df3['thal'].unique())

        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Patient's Age",step=1,min_value=10,max_value=100)
        with col2:
            sex = st.selectbox("Sex",sex)

        col3, col4 = st.columns(2)
        with col3:
            cp = st.selectbox("Chest Pain Type",cp)
        with col4:
            trestbps = st.number_input("Resting Blood Pressure (in mm hg)",step=1)

        col5, col6 = st.columns(2)
        with col5:
            chol = st.number_input("Serum Cholestoral (in mm hg)",step=1)
        with col6:
            fbs = st.selectbox("Fasting Sugar (>120mg/dl)",fbs)

        col7, col8 = st.columns(2)
        with col7:
            restecg = st.selectbox("Resting Results",restecg)
        with col8:
            thalach = st.number_input("Maximum Hear Rat Achieved",step=1)

        col9, col10 = st.columns(2)
        with col9:
            exang = st.selectbox("Excercise Induced Angina",exang)
        with col10:
            oldpeak = st.number_input("ST depression induced by Exercise relative to Rest",step=0.1)

        col11, col12, col13 = st.columns(3)
        with col11:
            slope = st.selectbox("Slope of the Peak Exercise ST Segment",slope)
        with col12:
            ca = st.selectbox("Number of major vessels",ca)
        with col13:
            thal = st.selectbox("Thalassemia",thal)

        if st.button('Predict Score'):
            input_df = pd.DataFrame({'age':[age], 'sex':[sex], 'cp':[cp],'trestbps':[trestbps], 'chol':[chol],'fbs':[fbs],
                             'restecg':[restecg], 'thalach':[thalach], 'exang':[exang], 'oldpeak':[oldpeak], 'slope':[slope],
                             'ca':[ca], 'thal':[thal]})
            result = pipe3.predict(input_df)

            if str(int(result[0])) == 0:
                st.header("The Patient has No Hypertension Disease :blush:")
            else:
                st.header("The Patient has Hypertension Disease :neutral_face:")
