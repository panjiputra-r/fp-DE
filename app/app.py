
import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox(label='Menu:', options=['Home', 'Exploration Data Analysis', 'Model Inference'])

if page == 'Home':
    st.image("BankMarketingImage.jpg")
    st.title('Welcome to Final Project Team 2')
    st.header('')

    col1, col2 = st.columns(2)

    # ======================= Columns 1 =======================
    col1.write('**Project Name             :**')
    col1.write('**Batch            :**')
    col1.write('**Team Member            :**')
    for _ in range(5):
        col1.empty()

    # ======================= Columns 2 =======================
    col2.write('Prospect Predictor')
    col2.write('HCK-012')
    col2.write('Samuel Tatang Surja - Data Scientist')
    col2.write('Ogi Hadicahyo - Data Scientist')
    col2.write('Panji Putra Rianto - Data Engineer')
    col2.write('Nicku Rendy Perdana - Data Analyst')

    st.header('')
    st.write('**You can select another menu in the Select Box on the left of your screen**')
    st.write('')
    with st.expander("**Short Description**"):
        st.caption('**Prospect Predictor** is a predictive model designed to anticipate term deposit subscriptions based on telemarketing interactions. By analyzing customer behavior and engagement during calls, this model helps banks efficiently target potential subscribers, optimizing telemarketing campaigns for greater success and enhanced customer acquisition.')
    
    with st.expander("**Problem Statement**"):
        st.caption("A banking client (name withheld due to non-disclosure agreement or NDA) based in Europe seeks assistance in gaining deeper insights into its bank customers regarding the launch of their latest term deposit subscription service. The bank aims to understand customer trends in deciding to adopt and follow the bank's new term deposit subscription service. Therefore, the bank has enlisted our help, a team from the Business Intelligence division of a renowned management consulting firm in Jakarta, to provide insights into predicting customer acquisition success rates for the term deposit subscription service based on telemarketing campaign efforts. In this regard, the bank has provided us with a sample dataset containing customer information gathered by a European bank, anonymized for privacy, during the telemarketing campaign period, along with information regarding the customers' final decisions to subscribe or not subscribe to the term deposit service.")

    with st.expander("**SMART Goal Identification**"):
        st.caption("**Specific**")
        st.caption("- Our client, a European-based bank, requires assistance from our Business Intelligence division to classify customers when contacted by the bank's telemarketing team, determining whether they subscribe to the bank's term deposit service or not.")
        st.caption("**Measurable**")
        st.caption("- Develop a model algorithm capable of predicting customer decisions to subscribe to term deposit services accurately.")
        st.caption("**Actionable**")
        st.caption("- Access raw data provided by the client.")
        st.caption("- Clean accessible raw data.")
        st.caption("- Perform visualization analysis and identify insights from cleaned data.")
        st.caption("- Determine the appropriate model algorithm and conduct modeling with it.")
        st.caption("- Produce predictive model.")
        st.caption("- Deploy model to local server.")
        st.caption("**Realistic**")
        st.caption("- Investment is currently a hot topic across various demographics.")
        st.caption("- Investment serves as a means for the current generation to save and manage their assets.")
        st.caption("- The bank (client) aims to accommodate this trend through term deposit services.")
        st.caption("- The bank requires tools that can enhance the effectiveness of their campaigns in marketing term deposit products to attract customers who are willing to subscribe to term deposit services.")
        st.caption("**Time-bound**")
        st.caption("- The model should be deployable and usable by the client's sales team to predict the probability of customers joining the term deposit program after being contacted by telemarketing team within approximately the first 3 months (1st quarter) since the initial inception of the model into the bank's marketing system.")


elif page == 'Exploration Data Analysis':
    eda.run()
else:
    prediction.run()