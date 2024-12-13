import pandas as pd
from datetime import datetime,timezone

file_path = r"C:\Users\SOHAIL\OneDrive\Desktop\DataEngineeringQ2.json"  
data = pd.read_json(file_path)

patient_details = pd.json_normalize(data['patientDetails'])

def calculate_age(birth_date):
    if pd.isnull(birth_date):
        return None
    nw=datetime.now(timezone.utc)
    return int((nw - pd.to_datetime(birth_date)).days / 365.25)

patient_details['age'] = patient_details['birthDate'].apply(calculate_age)

def age_group(age):
    if pd.isnull(age):
        return None
    elif age <= 12:
        return 'Child'
    elif 13 <= age <= 19:
        return 'Teen'
    elif 20 <= age <= 59:
        return 'Adult'
    else:
        return 'Senior'

patient_details['ageGroup'] = patient_details['age'].apply(age_group)

adult_count = patient_details['ageGroup'].value_counts().get('Adult', 0)

print(adult_count)
