# import libraries
import pandas as pd
import numpy as np


def preprocessing(): 
    ''' fungsi untuk membersihkan data'''
    # mengambil data dari csv
    df = pd.read_csv("/opt/airflow/dags/bank-additional-full_new.csv")

    ## Mengubah value pada data
    # Cleaning value pada kolom 'job'
    jobCol_categories = df['job'].unique().tolist()
    newJobCol_cats = []

    for each in jobCol_categories:
        newEach = each.capitalize()
        newEach = newEach.replace('.','')
        newJobCol_cats.append(newEach)
        
    jobColReplace_Dict = dict(zip(jobCol_categories, newJobCol_cats))

    df['job'] = df['job'].replace(jobColReplace_Dict)

    # Cleaning value pada kolom 'marital'
    maritalCol_categories = df['marital'].unique().tolist()
    newmaritalCol_cats = []

    for each in maritalCol_categories:
        newEach = each.capitalize()
        newmaritalCol_cats.append(newEach)
    
    maritalColReplace_Dict= dict(zip(maritalCol_categories, newmaritalCol_cats))

    df['marital'] = df['marital'].replace(maritalColReplace_Dict)

    # Cleaning value pada kolom 'education'
    educationCol_categories = df['education'].unique().tolist()
    neweducationCol_cats = []

    for each in educationCol_categories:
        newEach = each.replace('.', ' ')
        newEach = newEach.replace('4y', '(4 years)') if '4y' in newEach else newEach
        newEach = newEach.replace('6y', '(6 years)') if '6y' in newEach else newEach
        newEach = newEach.replace('9y', '(9 years)') if '9y' in newEach else newEach
        newEach = newEach.title()
        neweducationCol_cats.append(newEach)
    
    educationColReplace_Dict= dict(zip(educationCol_categories, neweducationCol_cats))
    df['education'] = df['education'].replace(educationColReplace_Dict)

    # Cleaning value pada kolom 'default'
    defaultCol_categories = df['default'].unique().tolist()
    newdefaultCol_cats = []

    for each in defaultCol_categories:
        newEach = each.capitalize()
        newdefaultCol_cats.append(newEach)
        
    defaultColReplace_Dict= dict(zip(defaultCol_categories, newdefaultCol_cats))

    df['default'] = df['default'].replace(defaultColReplace_Dict)


    # Cleaning value pada kolom 'housing'
    housingCol_categories = df['housing'].unique().tolist()
    newhousingCol_cats = []

    for each in housingCol_categories:
        newEach = each.capitalize()
        newhousingCol_cats.append(newEach)
        
    housingColReplace_Dict= dict(zip(housingCol_categories, newhousingCol_cats))

    df['housing'] = df['housing'].replace(housingColReplace_Dict)


    # Cleaning value pada kolom 'contact'
    contactCol_categories = df['contact'].unique().tolist()
    newcontactCol_cats = []

    for each in contactCol_categories:
        newEach = each.capitalize()
        newcontactCol_cats.append(newEach)
        
    contactColReplace_Dict= dict(zip(contactCol_categories, newcontactCol_cats))

    df['contact'] = df['contact'].replace(contactColReplace_Dict)

    # Cleaning value pada kolom 'loan'
    loanCol_categories = df['loan'].unique().tolist()
    newLoanCol_cats = []

    for each in loanCol_categories:
        newEach = each.capitalize()
        newLoanCol_cats.append(newEach)
        
    loanColReplace_Dict= dict(zip(loanCol_categories, newLoanCol_cats))

    df['loan'] = df['loan'].replace(loanColReplace_Dict)

    # Cleaning value pada kolom 'month'
    monthCol_categories = ['mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    newmonthCol_cats = [3,4,5,6,7,8,9,10,11,12]
        
    monthColReplace_Dict= dict(zip(monthCol_categories, newmonthCol_cats))

    df['month'] = df['month'].replace(monthColReplace_Dict)

    # Cleaning value pada kolom 'day_of_week'
    day_of_weekCol_categories = ['mon', 'tue', 'wed', 'thu', 'fri']
    newday_of_weekCol_cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    day_of_weekColReplace_Dict= dict(zip(day_of_weekCol_categories, newday_of_weekCol_cats))

    df['day_of_week'] = df['day_of_week'].replace(day_of_weekColReplace_Dict)

    # Cleaning value pada kolom 'poutcome'
    poutcomeCol_categories = df['poutcome'].unique().tolist()
    newpoutcomeCol_cats = []

    for each in poutcomeCol_categories:
        newEach = each.replace('non', 'non-') if 'non' in each else each
        newEach = newEach.capitalize()
        newpoutcomeCol_cats.append(newEach)
        
    poutcomeColReplace_Dict= dict(zip(poutcomeCol_categories, newpoutcomeCol_cats))

    df['poutcome'] = df['poutcome'].replace(poutcomeColReplace_Dict)

    # Cleaning value pada kolom 'y'
    yCol_categories = df['y'].unique().tolist()
    newyCol_cats = []

    for each in yCol_categories:
        newEach = each.capitalize()
        newyCol_cats.append(newEach)
        
    yColReplace_Dict= dict(zip(yCol_categories, newyCol_cats))

    df['y'] = df['y'].replace(yColReplace_Dict)


    ## Rename columns
    df.rename(columns={
    'age': 'age',
    'job': 'occupation',
    'marital': 'marital_status',
    'education': 'education_level',
    'default': 'credit_default',
    'housing': 'housing_loan',
    'loan': 'personal_loan',
    'contact': 'contact_method',
    'month': 'last_contact_month',
    'day_of_week': 'last_contact_day_of_week',
    'duration': 'last_contact_duration',
    'campaign': 'campaign_contacts',
    'pdays': 'days_since_previous_contact',
    'previous': 'previous_contacts',
    'poutcome': 'previous_campaign_outcome',
    'emp.var.rate': 'employment_variation_rate',
    'cons.price.idx': 'consumer_price_index',
    'cons.conf.idx': 'consumer_confidence_index',
    'euribor3m': 'euribor_3_month_rate',
    'nr.employed': 'number_employed',
    'y': 'subscription_status'
    }, inplace=True)


    # Replace 'Unknown' dengan NaN
    df.replace('unknown', np.nan, inplace=True)
    df.replace('Unknown', np.nan, inplace=True)

    # Drop rows with any NaN value
    df.dropna(inplace=True)

    # melakukan drop duplicate
    df.drop_duplicates(inplace=True)

    # menyimpan data bersih ke file csv baru
    df.to_csv('/opt/airflow/dags/bank-additional-full_clean.csv', index=False)
    df.to_csv('/opt/airflow/app/data/bank-additional-full_clean.csv', index=False)