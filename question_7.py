import pandas as pd

file_path = r"C:\Users\SOHAIL\OneDrive\Desktop\DataEngineeringQ2.json" 
data = pd.read_json(file_path)

num_medicines_per_consultation = data['consultationData'].apply(lambda x: len(x['medicines']))

average_medicines = num_medicines_per_consultation.mean()

print( round(average_medicines, 2))
