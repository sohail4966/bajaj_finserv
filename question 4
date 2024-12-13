import pandas as pd
file_path = r"C:\Users\SOHAIL\OneDrive\Desktop\DataEngineeringQ2.json" 
data = pd.read_json(file_path)

patient_details = pd.json_normalize(data['patientDetails'])

columns_to_check = ['firstName', 'lastName', 'birthDate']

missing_percentage = (patient_details[columns_to_check].isnull().sum() / len(patient_details)) * 100

print(missing_percentage.round(2))
