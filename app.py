import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#Loading th saved model

stroke_model = pickle.load(open("stroke_model.sav", 'rb'))

st.title("Stroke Prediction using Machine Learning")

genderList = ['Select gender',0,1]
hypertensionList = ['Select hypertension', 0, 1]
heartdiseaseList = ['Select heart disease', 0, 1]
evermarriedList = ['Select matrried status', 0, 1]
worktypeList = ["Select work type", 0,1,2,3,4]
residenceList = ['Select residence', 0, 1]
smokingstatusList = ["Select smoking status", 0,1,2,3]

gender = st.selectbox("Gender [ 0 = Male, 1 = Female ]", genderList)
age = st.slider('Age', min_value= 1, max_value= 110, step=1, value= 20)
hypertension = st.selectbox("Hyepertesnion [ 0 = doesn't have hypertension, 1 = has hypertension ]", hypertensionList)
heart_disease = st.selectbox("Heart Disease [ 0 = doesn't have heart disease, 1 = has heart disease ]", heartdiseaseList)
ever_married = st.selectbox('Ever married [ 0 = No, 1 = Yes ]', evermarriedList)
work_type = st.selectbox('Work type [ 0 = Private, 1 = Self-employed, 2 = children, 3 = Govt_job, 4 = Never_worked ]', worktypeList)
Residence_type = st.selectbox('Residence type [ 0 = Rural, 1 = Urban ]', residenceList)
avg_glucose_level = st.slider("Average Glucose Level", min_value= 0.0, max_value= 500.0, step=0.01, value=100.0)
bmi = st.slider("BMI", min_value= 0.0, max_value= 100.0, step=0.01, value=24.0)
smoking_status = st.selectbox('Smoking Status [ 0 = never smoked, 1 = Unknown, 2 = formerly smoked, 3 = smokes]', smokingstatusList)

#code for prediction
stroke_diagnosis = ''

#creating a button for prediction

if st.button('Check your result'):
    stroke_predict = stroke_model.predict([
        [gender,
        age,
        hypertension,
        heart_disease,
        ever_married,
        work_type,
        Residence_type,
        avg_glucose_level,
        bmi,
        smoking_status,

        ]
        ])
    
    if (stroke_predict[0] == 1):
        stroke_diagnosis = 'the patient had a stroke'

    else:
        stroke_diagnosis = 'the patient had not a stroke'

st.success(stroke_diagnosis)
