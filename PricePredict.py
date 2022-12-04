import streamlit as st
import pickle
import numpy as np
from PIL import Image

st.write('# House Pricing')
image = Image.open('house.jpg')
st.image(image, caption='House Pricing Prediction')

#Survey Section
sanatation = st.selectbox('Sanatation Network', ['No', 'Yes'])
area = st.number_input('Building Area', min_value=0)
mainstreet = st.selectbox('Main Street', ['No', 'Yes'])
plot = st.number_input('Plot Size', min_value=0)
year = st.number_input('Building Year', min_value=2015, max_value=2022)
garage = st.number_input('Garage Capacity', min_value=0)
location = st.selectbox('Location', ['Artil', 'Asbahi', 'Bayt Baws', 'Haddah'])

#Mapping characters to numbers
boolean = {'Yes': 1, 'No': 0}
inverseBoolean = {'Yes': 0, 'No': 1}
loc_Artil = {'Artil': 1, 'Asbahi': 0, 'Bayt Baws': 0, 'Haddah': 0}
loc_Asbahi = {'Artil': 0, 'Asbahi': 1, 'Bayt Baws': 0, 'Haddah': 0}
loc_Bayt = {'Artil': 0, 'Asbahi': 0, 'Bayt Baws': 1, 'Haddah': 0}
loc_Haddah = {'Artil': 0, 'Asbahi': 0, 'Bayt Baws': 0, 'Haddah': 1}

#Loading Pre-Trained Model (Linear Regression)
model = pickle.load(open('RegressionModel.sav', 'rb'))

#Predict Button
predict = st.button('Predict Price!')

if predict:
    pred = model.predict(np.array([year, plot, area, garage, loc_Artil[location], loc_Asbahi[location], loc_Bayt[location], loc_Haddah[location], inverseBoolean[mainstreet], boolean[mainstreet], inverseBoolean[sanatation], boolean[sanatation]]).reshape(1,-1))
    if pred < 0:
        st.write('## Do Not Exist! Please Enter Useful Data.')
    else:
        if int(pred/1000000) == 0:
            st.write('## The Price is:  ', str(int(pred/1000)), ',     ', str(int(pred)%1000))
        elif int(pred/1000) == 0:
            st.write('## The Price is:  ', str(int(pred)%1000))
        else:
            st.write('## The Price is:  ', str(int(pred/1000000)), ',     ', str(int(pred/1000)), ',     ', str(int(pred)%1000))
