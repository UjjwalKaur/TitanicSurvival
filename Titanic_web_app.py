import streamlit as st
import pickle
import os
import numpy as np
import pandas as pd
import random
import sklearn
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

#Pclass, Sex, Age, SibSp, Parch, Fare, Embarked

def model_pred(user_info):
    pickled_model = pickle.load(open('/Users/ujjwalkaur/PycharmProjects/Titanic/regmodel.pkl', 'rb'))
    y_pred = pickled_model.predict(pd.DataFrame(user_info))
    return(y_pred)

st.title('Would You Survive the Titanic?')

Pclass = st.text_input('What class do you belong to?')
gender = st.radio('Gender',("Male", "Female", "Other"))
if(gender == 'Male'):
    Sex = 0
elif(gender == 'Female' or gender == 'Other'):
    Sex = 1

Age = st.slider('How old are you?', 0, 40, 80)
SibSp = st.number_input('Do you have siblings or a spouse? How many?',max_value=5)
Embarked = random.choice([1, 2, 3])

user_info1 = [{'Pclass': Pclass, 'Sex': Sex, 'Age':Age, 'SibSp': SibSp, 'Parch':0, 'Fare': 700, 'Embarked': Embarked}]


def make_predict(user_info):
    prediction = model_pred(user_info1)
    if prediction == 1:
        st.write('Omgg you totally would')
    elif prediction == 0:
        st.write('Babe....you wouldn\'t survive. It\'s a good thing you weren\'t on board')

if st.button('Work your data magic!'):
    make_predict(user_info1)