import pandas as pd

file_path = r"C:\Users\SOHAIL\OneDrive\Desktop\DataEngineeringQ2.json"  # Replace with your actual file path
data = pd.read_json(file_path)

medicines_list = data['consultationData'].apply(lambda x: x['medicines'])

medicine_names = [medicine['medicineName'] for sublist in medicines_list for medicine in sublist]

medicine_freq = pd.Series(medicine_names).value_counts()

third_most_frequent_medicine = medicine_freq.index[2]

print(third_most_frequent_medicine)
