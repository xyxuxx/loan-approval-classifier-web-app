import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title='Loan Approval',
    page_icon='./img/favicon.png',
    layout='wide',
)

gender = ['Male', 'Female']
married = ['No', 'Yes']
dependents =['None', 'One', 'Two', 'More than two']
education = ['Graduate', 'Not Graduate']
self_employed = ['No', 'Yes']
loan_amount_term = [360, 120, 240, 180,  60, 300, 480,  36,  84,  12]
credit_history=[1, 0]
property_area = ['Urban', 'Rural', 'Semiurban']

st.header('Loan Approval Classifier')

st.markdown('`Demographics Info:`')
col1, col2, col3 = st.columns(3)
with col1:
    inp_name = st.text_input('Input your name: ')
with col2:
    inp_gender = st.selectbox('Applicant gender: ', gender)
with col3:
    inp_married = st.selectbox('Applicant marital status:', married)

col1, col2 = st.columns(2)
with col1:
    inp_education = st.selectbox('Select Education Level: ', education)
with col2:
    inp_self_employed = st.selectbox('Is the applicant Self Employed?: ', self_employed)

col1, col2 = st.columns(2)
with col1:
    inp_dependents = st.selectbox('Applicant\'s Family Member: ', dependents)
with col2:
    inp_property_area = st.selectbox('Location of the property: ', property_area)

st.markdown('`Income Info:`')
col1, col2 = st.columns(2)
with col1:
    inp_applicant_income = st.number_input('Applicant\'s monthly income (in thousand $)')
with col2:
    inp_coapplicant_income = st.number_input('Co-applicant\'s monthly income (in thousand $)')

st.markdown('`Loan Information:`')
col1, col2 = st.columns(2)
with col1:
    inp_loan_amount_term = st.selectbox('The loan\'s repayment period (in days) ', loan_amount_term)
with col2:
    inp_loan_amount = st.number_input('Input Loan Amount (in thousand $): ')

st.markdown('`Previous Credit History:`')
inp_credit_history = st.selectbox('Records of previous credit history(0: bad credit history, 1: good credit history): ', credit_history)


if st.button('Predict'):
    if not all([
        inp_name
    ]):
        st.warning("Please provide Name.")
    else:
        df = pd.DataFrame({'Gender':[inp_gender], 'Married':[inp_married], 'Dependents':[inp_dependents], 'Education':[inp_education], 'Self_Employed':[inp_self_employed],
            'ApplicantIncome':[inp_applicant_income], 'CoapplicantIncome':[inp_coapplicant_income], 'LoanAmount':[inp_loan_amount],
            'Loan_Amount_Term':[inp_loan_amount_term], 'Credit_History':[inp_credit_history], 'Property_Area':[inp_property_area]})

        model = pickle.load(open('./model.pkl', 'rb'))

        y_pred = model.predict(df)

        if y_pred[0] == 1:
            approval = 'Approved'
        else:
            approval = 'Not Approved'
        st.subheader(f'{inp_name}\'s Loan is {approval}')