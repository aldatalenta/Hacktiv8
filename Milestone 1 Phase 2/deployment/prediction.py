import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model

st.set_page_config(
    page_title='Predict',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Load All Files of Functional API (Improvement)

with open('final_pipeline.pkl', 'rb') as file_1:
  final_pipeline = pickle.load(file_1)

model_ann = load_model('churn_risk_model.h5')

def run ():
    with st.form(key='form_customer_telco'):
        age = st.number_input('Age', min_value=10, max_value=100, value=37, step=1, help='Age of customer')
        gender = st.radio('Gender', ('M', 'F'), index=1, help='Gender of customer (Male, Female)')
        region_category = st.radio('Region Category', ('Town', 'City', 'Village'), index=1, help='Region of customer')

        st.markdown('---')

        membership_category	 = st.radio('Membership Category', ('Basic Membership', 'No Membership', 'Gold Membership', 'Silver Membership', 'Premium Membership', 'Platinum Membership'), index=1, help='Membership type of customer')
        joined_through_referral = st.radio('Joined Through Referral', ('No', 'Yes'), index=1, help='Whether a cust joined using any referral code')
        preferred_offer_types = st.radio('Preferred Offer Types', ('Gift Vouchers/Coupons', 'Credit/Debit Card Offers', 'Without Offers'), index=1, help='Type of offer that a cust prefers')
        medium_of_operation	 = st.radio('Medium of Operation', ('Desktop', 'Smartphone', 'Both'), index=1, help='Medium of operation that a cust uses for transactions')
        internet_option	 = st.radio('Internet Option', ('Wi-Fi', 'Mobile_Data', 'Fiber_Optic'), index=1, help='Type of internet service a cust uses')

        st.markdown('---')

        days_since_last_login = st.number_input('Days Since Last Login', min_value=1, max_value=30, value=13, step=1, help='Number of days since a cust last logged into the website')
        avg_time_spent = st.number_input('Average Time Spent', min_value=0, max_value=3500, value=160, step=1, help='Average time spent by a cust on the website')
        avg_transaction_value = st.number_input('Average Transaction Value', min_value=800, max_value=100000, value=27000, step=1, help='Average transaction value of a cust')
        avg_frequency_login_days = st.number_input('Average Frequency Login Days', min_value=0, max_value=75, value=14, step=1, help='Number of times a cust has logged in to the website')
        points_in_wallet = st.number_input('Points in Wallet', min_value=0, max_value=3000, value=680, step=1, help='Points awarded to a cust on each transaction')
        used_special_discount = st.radio('Used Special Discount', ('No', 'Yes'), index=1, help='Whether a cust uses special discount offer')
        offer_application_preference = st.radio('Offer Application Preference', ('No', 'Yes'), index=1, help='Whether a cust prefers offers')
        
        st.markdown('---')

        past_complaint = st.radio('Past Complaint', ('No', 'Yes'), index=1, help='Whether a cust has raised any complaints')
        complaint_status = st.radio('Complaint Status', ('Not Applicable', 'Unsolved', 'Solved', 'Solved in Follow-up', 'No Information Available'), index=1, help='Whether the complaints was resolved')
        feedback = st.radio('Feedback', ('Poor Product Quality', 'No reason specified', 'Too many ads', 'Poor Website', 'Poor Customer Service', 'Reasonable Price', 'User Friendly Website', 'Products always in Stock', 'Quality Customer Care'), index=1, help='Feedback provided by a cust')

        submitted = st.form_submit_button('Predict')

    data_inf = {
        'age': age,
        'gender': gender,
        'region_category': region_category,
        'membership_category': membership_category,
        'joined_through_referral': joined_through_referral,
        'preferred_offer_types': preferred_offer_types,
        'medium_of_operation': medium_of_operation,
        'internet_option': internet_option,
        'days_since_last_login': days_since_last_login,
        'avg_time_spent': avg_time_spent,
        'avg_transaction_value': avg_transaction_value,
        'avg_frequency_login_days': avg_frequency_login_days,
        'points_in_wallet': points_in_wallet,
        'used_special_discount': used_special_discount,
        'offer_application_preference': offer_application_preference,
        'past_complaint': past_complaint,
        'complaint_status': complaint_status,
        'feedback': feedback
        }

    df_inf = pd.DataFrame([data_inf])
    st.dataframe(df_inf)

    if submitted:
        # Transform Inference-Set
        data_inf_transform = final_pipeline.transform(df_inf)

        # Predict using Artificial Neural Network
        y_pred_inf = model_ann.predict(data_inf_transform)
        y_pred_inf = np.where (y_pred_inf>=0.5, 1, 0)
        
        if y_pred_inf == 1: 
            st.write('# Churn Risk Score  : ', "Churn")
        else:
            st.write('# Churn Risk Score  : ', "Not Churn")

if __name__=='__app__':
    run()