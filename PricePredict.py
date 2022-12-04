import streamlit as st
import pickle
import numpy as np
from PIL import Image

st.markdown("<h1 style='text-align: center; color: red;'>House Pricing</h1>", unsafe_allow_html=True)
image = Image.open('house.jpg')
st.image(image, caption='House Pricing Prediction')

#Survey Section
location = st.selectbox('Location', ['Artil', 'Asbahi', 'Bayt Baws', 'Haddah'])
mainstreet = st.selectbox('Main Street', ['No', 'Yes'])
area = st.number_input('Building Area', min_value=0)
plot = st.number_input('Plot Size', min_value=0)
garage = st.number_input('Garage Capacity', min_value=0)
sanitation = st.selectbox('Sanitation Network', ['No', 'Yes'])
grade = st.selectbox('Finishing Grade', ['Commercial', 'Delux'])


#Mapping characters to numbers
boolean = {'Yes': 1, 'No': 0}
inverseBoolean = {'Yes': 0, 'No': 1}
loc_Artil = {'Artil': 1, 'Asbahi': 0, 'Bayt Baws': 0, 'Haddah': 0}
loc_Asbahi = {'Artil': 0, 'Asbahi': 1, 'Bayt Baws': 0, 'Haddah': 0}
loc_Bayt = {'Artil': 0, 'Asbahi': 0, 'Bayt Baws': 1, 'Haddah': 0}
loc_Haddah = {'Artil': 0, 'Asbahi': 0, 'Bayt Baws': 0, 'Haddah': 1}
grade_Com = {'Commercial': 1, 'Delux': 0}
grade_Del = {'Commercial': 0, 'Delux': 1}

#Loading Pre-Trained Model (Linear Regression)
model = pickle.load(open('LinRegModel.sav', 'rb'))

#Predict Button
predict = st.button('Predict Price!')

if predict:
    pred = model.predict(np.array([plot, area, garage, loc_Artil[location], loc_Asbahi[location], loc_Bayt[location], loc_Haddah[location], inverseBoolean[mainstreet], boolean[mainstreet], inverseBoolean[sanitation], boolean[sanitation], grade_Com[grade], grade_Del[grade]]).reshape(1,-1))
    if pred < 0:
        st.write('## Do Not Exist! Please Enter Useful Data.')
    else:
        x = str(int(pred))
        l = [ x[len(x)-i-3:len(x)-i] for i in range(0, len(x), 3) ]
        if len(l) == 2:
            st.write('## The Price is:  {},  {}'.format(l[1], l[0]))
        else:
            if len(x) == 8:
                st.write('## The Price is:  {}{},  {},  {}'.format(x[1], x[0], l[1], l[0]))
            else:
                st.write('## The Price is:    {},  {},  {}'.format(x[0], l[1], l[0])) 
            
st.write('\n')            
st.write('## Thank you for your visit!')
