import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

st.set_page_config(
    page_title='Predict',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Load All Files of Logistic Regression after hyperparameter tuning
with open('logreg_best_estimator.pkl', 'rb') as file_1:
  logreg_best_estimator = pickle.load(file_1)

def run ():
    with st.form(key='form_tour_package'):
        Age = st.number_input('Age', min_value=1, max_value=100, value=25, step=1, help='Age of customer')
        CityTier = st.number_input('City Tier', min_value=1, max_value=3, value=1)
        NumberOfPersonVisiting = st.number_input('Number Of Person Visiting', min_value=1, max_value=5, value=3)
        PreferredPropertyStar = st.number_input('Preferred Property Star', min_value=2, max_value=5, value=3)
        NumberOfTrips = st.number_input('Number Of Trips', min_value=1, max_value=22, value=3)
        NumberOfChildrenVisiting = st.number_input('Number Of Children Visiting', min_value=0, max_value=5, value=3)
        MonthlyIncome = st.number_input('Monthly Income', min_value=1000, max_value=100000, value=23000)
        st.markdown('---')

        TypeofContact = st.radio('Type of Contact', ('Self Enquiry', 'Company Invited'), index=1)
        Occupation = st.radio('Occupation', ('Salaried', 'Small Business', 'Large Business', 'Free Lancer'), index=1)
        Gender = st.radio('Gender', ('Male', 'Female'), index=1)
        MaritalStatus = st.radio('Marital Status', ('Married', 'Divorced', 'Single', 'Unmarried'), index=1)
        Passport = st.radio('Passport', ('0', '1'), index=1, help='No, Yes')
        OwnCar = st.radio('OwnCar', ('0', '1'), index=1, help='No, Yes')
        Designation = st.radio('Designation', ('Executive', 'Manager', 'Senior Manager', 'AVP', 'VP'), index=1)
        st.markdown('---')

        PitchSatisfactionScore = st.number_input('Pitch Satisfaction Score', min_value=1, max_value=5, value=3)
        ProductPitched = st.radio('Product Pitched', ('Basic', 'Deluxe', 'Standard', 'Super Deluxe', 'King'), index=1)
        NumberOfFollowups = st.number_input('Number Of Followups', min_value=1, max_value=6, value=4)
        DurationOfPitch = st.slider('Duration Of Pitch', 5, 130, 20)

        submitted = st.form_submit_button('Predict')

    data_inf = {
        'age': Age,
        'typeofcontact': TypeofContact,
        'citytier': CityTier,
        'durationofpitch': DurationOfPitch,
        'occupation': Occupation,
        'gender': Gender,
        'numberofpersonvisiting': NumberOfPersonVisiting,
        'numberoffollowups': NumberOfFollowups,
        'productpitched': ProductPitched,
        'preferredpropertystar': PreferredPropertyStar,
        'maritalstatus': MaritalStatus,
        'numberoftrips': NumberOfTrips,
        'passport': Passport,
        'pitchsatisfactionscore': PitchSatisfactionScore,
        'owncar': OwnCar,
        'numberofchildrenvisiting': NumberOfChildrenVisiting,
        'designation': Designation,
        'monthlyincome': MonthlyIncome
        }

    df_inf = pd.DataFrame([data_inf])
    st.dataframe(df_inf)

    if submitted:
        # Dropping unnecessary columns from the inference-set, which we'll use going forward
        df_inf.drop(columns=['numberoffollowups', 'productpitched', 'durationofpitch', 'numberoftrips', 'typeofcontact', 'gender', 'pitchsatisfactionscore', 'numberofpersonvisiting', 'owncar', 'numberofchildrenvisiting'], inplace=True)

        # Mapping values to the expected output
        df_inf['citytier']=df_inf['citytier'].map({1: 'Tier 1', 2: 'Tier 2', 3: 'Tier 3'})
        df_inf['passport']=df_inf['passport'].map({0: 'No', 1: 'Yes'})

        # Predict using Logistic Regression
        y_pred_inf = logreg_best_estimator.predict(df_inf)
        st.write('# Product_Taken : ', str(int(y_pred_inf)))

if __name__=='__app__':
    run()