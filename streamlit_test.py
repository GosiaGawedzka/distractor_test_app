#%% Import packages.

import streamlit as st
import os
import pandas as pd
import ast
import re



#Set webapp title.
st.title("Distractor Generator")

#Initiate drop-down box for selection of IGCSE subject.
subject_long = st.selectbox('Select IGCSE syllabus', ('Biology 0610', 'Chemistry 0620', 'Physics 0625'))
subject = subject_long.translate({ord(ch): None for ch in '0123456789'}).strip()#this strips out the syllabus code.
#st.write('Selected subject:', subject)

#Load the syllabus topics and subtopics for Biology, Chemisty and Physics.
syllabus_topics = pd.read_csv(r'Combined_Syllabus_Topics.csv')
single_subject_syllabus_topics = syllabus_topics[syllabus_topics['Subject'] == subject]

#Set up prompt panels for stem and key text.
stem = st.text_area(label="Enter stem:", value="", height=5)
key = st.text_area(label="Enter key:", value="", height=5)

#Define a button which generates the distractors.
button_clicked = st.button("Submit")


