import streamlit as st
import pickle

st.title("Play Golf???")
#streamlit run app.py

temp_dict = {'Hot': 1, 'Cool': 0,'Mild' : 2}
outlook_dict = {'Overcast': 0, 'Rainy': 1,'Sunny' : 2}
humid_dict = {'High': 0, 'Normal': 1}
windy_dict = {'True': True, 'False': False}


outlook = st.selectbox('Outlook', outlook_dict)
temp = st.selectbox('Temperature', temp_dict)
humidity = st.selectbox('Humidity', humid_dict)
windy = st.selectbox('Windy', windy_dict)

model =  pickle.load(open('model.sav','rb'))
x = model.predict([[outlook_dict[outlook],temp_dict[temp],humid_dict[humidity],windy_dict[windy]]])
st.header("Output")
st.write(x[0])