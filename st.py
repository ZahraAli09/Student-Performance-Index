import streamlit as st
import pickle
import numpy as np

file=open('performance.pkl', 'rb')
model=pickle.load(file)
st.title("Welcome Students !! Get your performance index ")

hrs=st.number_input('hours_studied')
Prev_score=st.number_input('Previous_Score')


sleep_hrs=st.number_input('Sleep_Hours')
papers_solved=st.number_input('Sample Papers Solved')

activity=st.radio('Activty', ['yes', 'No'])

n1= 1 if activity=='yes' else 0
n2=0 if activity=='no' else 1
input=np.array([hrs,  Prev_score,  sleep_hrs, papers_solved, n1, n2 ])

if st.button('Performance Index'):
    pred=model.predict([input])    #in this step it is converted into 2d array
    st.write(f'performance Index: {(pred[0])}')

