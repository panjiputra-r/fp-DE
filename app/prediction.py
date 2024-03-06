# import library
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Set Page Config
st.set_page_config(
    page_title="Predicting Customer Churn",
)

# # Load Model
with open('/app/models/model.pkl', 'rb') as model:
    model = pickle.load(model)

# Function to generate dummy data
def generate_dummy_data():
    dummy_age = np.random.randint(18, 100)
    dummy_occupation = np.random.choice(['Housemaid', 'Services', 'Admin', 'Blue-collar', 'Technician',
                                         'Retired', 'Management', 'Unemployed', 'Self-employed', 'Entrepreneur', 'Student'])
    dummy_marital_status = np.random.choice(['Married', 'Single', 'Divorced'])
    dummy_education_level = np.random.choice(['Basic (4 Years)', 'High School', 'Basic (6 Years)', 'Basic (9 Years)',
                                              'Professional Course', 'University Degree', 'Illiterate'])
    dummy_credit_default = np.random.choice(['No', 'Yes'])
    dummy_housing_loan = np.random.choice(['No', 'Yes'])
    dummy_personal_loan = np.random.choice(['No', 'Yes'])
    dummy_contact_method = np.random.choice(['Telephone', 'Cellular'])
    dummy_last_contact_month = np.random.randint(1, 12)
    dummy_last_contact_day_of_week = np.random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
    dummy_last_contact_duration = np.random.randint(1, 5000)
    dummy_campaign_contacts = np.random.randint(1, 100)
    dummy_days_since_previous_contact = np.random.randint(1, 999)
    dummy_previous_contacts = np.random.randint(1, 10)
    dummy_previous_campaign_outcome = np.random.choice(['Non-existent', 'Failure', 'Success'])
    dummy_employment_variation_rate = np.random.uniform(-5.0, 5.0)
    dummy_consumer_price_index = np.random.uniform(-100.0, 100.0)
    dummy_consumer_confidence_index = np.random.uniform(-50.0, 100.0)
    dummy_euribor_3_month_rate = np.random.uniform(0.000, 9.999)
    dummy_number_employed = np.random.randint(1000, 99999)

    return {'age': dummy_age,
            'occupation': dummy_occupation,
            'marital_status': dummy_marital_status,
            'education_level': dummy_education_level,
            'credit_default': dummy_credit_default,
            'housing_loan': dummy_housing_loan,
            'personal_loan': dummy_personal_loan,
            'contact_method': dummy_contact_method,
            'last_contact_month': dummy_last_contact_month,
            'last_contact_day_of_week': dummy_last_contact_day_of_week,
            'last_contact_duration': dummy_last_contact_duration,
            'campaign_contacts': dummy_campaign_contacts,
            'days_since_previous_contact': dummy_days_since_previous_contact,
            'previous_contacts': dummy_previous_contacts,
            'previous_campaign_outcome': dummy_previous_campaign_outcome,
            'employment_variation_rate': dummy_employment_variation_rate,
            'consumer_price_index': dummy_consumer_price_index,
            'consumer_confidence_index': dummy_consumer_confidence_index,
            'euribor_3_month_rate': dummy_euribor_3_month_rate,
            'number_employed': dummy_number_employed
            }

#Function to run streamlit model predictor
def run():
   # Set title
    st.title("Classification Model for Predicting Customer.")

    # Sub title
    st.subheader("Predicting the Possibility Customer Will Be Subscribe.")
    st.markdown('---')
    st.image("https://png.pngtree.com/png-vector/20230525/ourmid/pngtree-bank-workers-providing-service-to-clients-vector-financial-banner-vector-png-image_52210830.jpg")

    # Create Form for data inference
    st.markdown('## Input Data')
    with st.form('my_form'):
        age = st.number_input(label='Enter your age', min_value = 18, max_value= 100, step=1)
        occupation = st.selectbox(label='Select your occupation', options=['Housemaid', 'Services', 'Admin', 'Blue-collar', 'Technician','Retired', 'Management', 'Unemployed', 'Self-employed','Entrepreneur', 'Student'])
        marital_status = st.selectbox(label='Select your gender', options=['Married', 'Single', 'Divorced'])
        education_level = st.selectbox(label='Select your education level', options=['Basic (4 Years)', 'High School', 'Basic (6 Years)','Basic (9 Years)', 'Professional Course', 'University Degree','Illiterate'])
        credit_default = st.selectbox(label='Select your credit default', options=['No', 'Yes'])
        housing_loan = st.selectbox(label='Select your housing loan', options=['No', 'Yes'])
        personal_loan = st.selectbox(label='Select your personal loan', options=['No', 'Yes'])
        contact_method = st.selectbox(label='Select your contact method', options=['Telephone', 'Cellular'])
        last_contact_month = st.selectbox(label='Select your last contact month', options=[1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12])
        last_contact_day_of_week = st.selectbox(label='Select your last contact day of week', options=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        last_contact_duration = st.number_input(label='Enter your last contact duration', min_value = 1, max_value= 5000, step=1)
        campaign_contacts = st.number_input(label='Enter your campaign contacts', min_value = 1, max_value= 100, step=1)
        days_since_previous_contact = st.number_input(label='Enter days since previous contact', min_value = 1, max_value= 999, step=1)
        previous_contacts = st.number_input(label='Enter previous contacts', min_value = 1, max_value= 10, step=1)
        previous_campaign_outcome = st.selectbox(label='Select your previous campaign outcome', options=['Non-existent', 'Failure', 'Success'])
        employment_variation_rate = st.number_input(label='Enter employment variation rate', min_value = -5.0, max_value= 5.0, step=0.1)
        consumer_price_index = st.number_input(label='Enter consumer price index', min_value = -100.0, max_value= 100.0, step=0.1)
        consumer_confidence_index = st.number_input(label='Enter consumer confidence index', min_value = -50.0, max_value= 100.0, step=0.10)
        euribor_3_month_rate = st.number_input(label='Enter euribor 3 month rate', min_value = 0.000, max_value= 9.999, step=0.100)
        number_employed = st.number_input(label='Enter number employed', min_value = 1000, max_value= 99999, step=100)

        # Create a button
        dummy_button = st.form_submit_button("Generate Dummy Data")
        submitted = st.form_submit_button("Let's Predict!")

    if 'dummy_data' in st.session_state:
        dummy_data = st.session_state['dummy_data']
        age = dummy_data['age']
        occupation = dummy_data['occupation']
        marital_status = dummy_data['marital_status']
        education_level = dummy_data['education_level']
        credit_default = dummy_data['credit_default']
        housing_loan = dummy_data['housing_loan']
        personal_loan = dummy_data['personal_loan']
        contact_method = dummy_data['contact_method']
        last_contact_month = dummy_data['last_contact_month']
        last_contact_day_of_week = dummy_data['last_contact_day_of_week']
        last_contact_duration = dummy_data['last_contact_duration']
        campaign_contacts = dummy_data['campaign_contacts']
        days_since_previous_contact = dummy_data['days_since_previous_contact']
        previous_contacts = dummy_data['previous_contacts']
        previous_campaign_outcome = dummy_data['previous_campaign_outcome']
        employment_variation_rate = dummy_data['employment_variation_rate']
        consumer_price_index = dummy_data['consumer_price_index']
        consumer_confidence_index = dummy_data['consumer_confidence_index']
        euribor_3_month_rate = dummy_data['euribor_3_month_rate']
        number_employed = dummy_data['number_employed']
    
    # dataframe
    data = {'age' : age,
            'occupation' : occupation,
            'marital_status' : marital_status,
            'education_level' : education_level,
            'credit_default' : credit_default,
            'housing_loan' : housing_loan,
            'personal_loan' : personal_loan,
            'contact_method' : contact_method,
            'last_contact_month' : last_contact_month,
            'last_contact_day_of_week' : last_contact_day_of_week,
            'last_contact_duration' : last_contact_duration,
            'campaign_contacts' : campaign_contacts,
            'days_since_previous_contact' : days_since_previous_contact,
            'previous_contacts' : previous_contacts,
            'previous_campaign_outcome' : previous_campaign_outcome,
            'employment_variation_rate' : employment_variation_rate,
            'consumer_price_index' : consumer_price_index,
            'consumer_confidence_index' : consumer_confidence_index,
            'euribor_3_month_rate' : euribor_3_month_rate,
            'number_employed' : number_employed,
            }

    df = pd.DataFrame([data])
    st.dataframe(df)
    
    if dummy_button:
        dummy_data = generate_dummy_data()
        st.session_state['dummy_data'] = dummy_data
        st.experimental_rerun()

    if submitted:
        y_pred_inf = model.predict(df)
        if y_pred_inf[0] == 0:
            st.write('Customers Will Not Subscribe')
        else:
            st.write('Customer Will Subscribe')

if __name__== '__main__':
    generate_dummy_data()
    run()