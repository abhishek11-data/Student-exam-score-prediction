import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("Student Exam Mark Prediction")

st.divider()

st.write("This app uses machine learning to predict a student exam score based on their daily habbit performance")

st.divider()

age=st.number_input("Age",min_value=0,value=0)
gender=st.number_input("Gender",min_value=0,value=0)
study_hours_per_day=st.number_input("Study Hour Per Day",min_value=0,value=0)
social_media_hours=st.number_input("Social Media Hours",min_value=0,value=0)
netflix_hours=st.number_input("Netflix Hours",min_value=0,value=0)
part_time_job=st.number_input("Part Time Job",min_value=0,value=0)
attendance_percentage=st.number_input("Attendance Percentage",min_value=0,value=0)
sleep_hours=st.number_input("Sleep Hours",min_value=0,value=0)
diet_quality=st.number_input("Diet Quality",min_value=0,value=0)
exercise_frequency=st.number_input("Exercise Frequency",min_value=0,value=0)
parental_education_level=st.number_input("Parental Educational Level",min_value=0,value=0)
internet_quality=st.number_input("Internet Quality",min_value=0,value=0)
mental_health_rating=st.number_input("Mental Health Rating",min_value=0,value=0)
extracurricular_participation=st.number_input("Extracurricular Participation",min_value=0,value=2)

st.divider()

X=[[age,gender,study_hours_per_day,social_media_hours,netflix_hours,part_time_job,attendance_percentage,sleep_hours,diet_quality,exercise_frequency,parental_education_level,internet_quality, mental_health_rating,extracurricular_participation]]

predictbutton=st.button("Predict!")

if predictbutton:

    st.balloons()

    X_array=np.array(X)

    Prediction=model.predict(X_array)

    st.write(f"Price Prediction is {Prediction}")

else:
    st.write("Please use predict button after entering value")





# order of x ['age', 'gender', 'study_hours_per_day', 'social_media_hours',
    #    'netflix_hours', 'part_time_job', 'attendance_percentage',
    #    'sleep_hours', 'diet_quality', 'exercise_frequency',
    #    'parental_education_level', 'internet_quality', 'mental_health_rating',
    #    'extracurricular_participation']

