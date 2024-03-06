import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Exploration Data Analysis (EDA)')
    st.write('Further data analysis to gain in-depth insight into the dataset used.')   

    # Load Picture
    st.image("EdaImage.jpg")
    st.markdown('---')

    # Load csv Data 
    data = pd.read_csv('/app/bank-additional-full_clean.csv')

    # Displays the data
    st.header('Displays the data')
    st.dataframe(data)
    st.markdown ('---')
    
    # EDA1
    st.header('1. Last Contact Month')
    image = Image.open('figure_1_last_contact_month.png')
    st.image(image, caption='Figure 1:Last Contact Month')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            From this visualization, Both graphs above indicate that the majority of respondents have been contacted by the marketing team most frequently in the month of May.
            There is a very prominent trend among those who decide not to take the deposit service. In this group, almost 3 out of 4 people who were contacted and then chose to decline the service were contacted in May.
            ''')
    st.markdown('---')
    
    # Distribution of Chustomer Churn
    st.header('2. Subscription Status')
    image = Image.open('figure_2_subscription_status.png')
    st.image(image, caption='Figure 2:Subscription Status')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            It is noted that 88 percent of respondents contacted by the bank's marketing team decided not to take the bank's deposit service. Meanwhile, only 11 percent of those contacted were interested and willing to use the deposit service offered by the bank.
            ''')
    st.markdown('---')

    # Relationship of exited customer and Gender
    st.header('3. Age')
    image = Image.open('figure_3_age.png')
    st.image(image, caption='Figure 3:Age')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            The age column tends to be positively skewed, as evidenced by the chart leaning towards the left side of the graph. Twelve percent of all records were detected as outliers.
            Respondents who decide to subscribe to banking deposit services tend to be older compared to those who decline the offer.
            ''')
    st.markdown('---')

    # Age Group That Prefer To Churn
    st.header('4. Occupation')
    image = Image.open('figure_4_occupation.png')
    st.image(image, caption='Figure 4: Occupation')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            The most commonly mentioned occupations by respondents are related to administration and private employees. This is consistently found among respondents who ultimately choose to deposit or not to deposit. Both groups also similarly have the third most frequent occupation, which is technicians.**
            ''')
    st.markdown('---')

    # Distribution in Various Countries
    st.header('5. Last Contact Duration')
    image = Image.open('figure_5_last_contact_duration.png')
    st.image(image, caption='Figure 5: Last Contact Duration')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - The `duration` variable tends to be positively skewed; more than 15 percent of all records were considered outliers.  
            - Respondents who experienced a short duration tend to decline banking offers, while those engaged in long contact durations tend to become the next banking subscribers.  
            - It's also worth noting that this tendency can indicate that those who already have disinterest in banking offers tend not to further engage in marketer conversations.  
            ''')
    st.markdown('---')

    # Impact of Estimated Salary on customer churn
    st.header('6. Marital Status')
    image = Image.open('figure_6_marital_status.png')
    st.image(image, caption='Figure 6: Marital Status')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            Based on the identification of marital status characteristics between those who choose to deposit and those who do not, it is found that there is no significant difference, considering that the majority of both groups are respondents who are already married.
            ''')
    st.markdown('---')

    # Impact of Estimated Salary on customer churn
    st.header('7. Campaign Contact')
    image = Image.open('figure_7_campaign_contact.png')
    st.image(image, caption='Figure 7: Campaign Contact')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - Most respondents experienced fewer than 10 banking campaigns and interactions with telemarketers.
            - Respondents who decided to subscribe to banking offers tended to experience fewer campaign occurrences. This could be due to their inherent interest, which may make them more responsive and quicker to decide to apply for the subscription.
            - Conversely, most respondents who decided they were not interested in banking offers tended to experience prolonged campaign interactions, possibly due to delayed decision-making, extended follow-ups, and the inconvenience of being over-contacted by telemarketers.
            ''')
    st.markdown('---')

    st.header('8. Education Level')
    image = Image.open('figure_8_education_level.png')
    st.image(image, caption='Figure 8: Education Level')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - Respondents who eventually deposit assets into the bank after the campaign tend to be focused on the university education demographic category.
            - On the other hand, respondents who choose not to deposit tend to come from a more diverse demographic category. This group has a larger proportion of basic and secondary education backgrounds.
            - This indicates that the level of education contributes significantly to their decision to deposit or pass up this opportunity.
            ''')
    st.markdown('---')

    st.header('9. Personal Loan')
    image = Image.open('figure_9_personal_loan.png')
    st.image(image, caption='Figure 9: Personal Loan')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            Demographically overall, the majority of respondents do not have existing loans in their accounts. The following proportions can be said to be the same between respondents who subscribe to the default term subscription and those who reject the following offer.
            ''')
    st.markdown('---')

    st.header('10. Housing Loan')
    image = Image.open('figure_10_housing_loan.png')
    st.image(image, caption='Figure 10: Housing Loan')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            The majority of respondents have home construction loans. This is indicated by data showing that more than half of the respondents, specifically those who take term deposit services at the bank and those who reject the offer, claim to have a home mortgage program.    
            ''')
    st.markdown('---')

    st.header('11. Contact Method')
    image = Image.open('figure_11_contact_method.png')
    st.image(image, caption='Figure 11: Contact Method')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
        - The majority of respondents who choose not to subscribe to the bank's deposit service are respondents contacted via mobile phone, as are those who ultimately subscribe to the term deposit service.
        - There is an interesting pattern where respondents who reject the offer have a proportion of responses via landline phone. This indicates that respondents may tend not to continue contact related to marketing through the following medium.
            ''')
    st.markdown('---')

if __name__== '__main__':
    run()