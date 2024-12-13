import pandas as pd
from datetime import datetime,timezone

file_path = r"C:\Users\SOHAIL\OneDrive\Desktop\DataEngineeringQ2.json"  
data = pd.read_json(file_path)

patient_details = pd.json_normalize(data['patientDetails'])

def calculate_age(birth_date):
    if pd.isnull(birth_date):
        return None
    now = datetime.now(timezone.utc)  # Current date
    return int((now - pd.to_datetime(birth_date)).days / 365.25)

patient_details['age'] = patient_details['birthDate'].apply(calculate_age)

medicines_list = data['consultationData'].apply(lambda x: x['medicines'])
num_medicines_per_patient = medicines_list.apply(len)

correlation = num_medicines_per_patient.corr(patient_details['age'])

print(round(correlation, 2))
