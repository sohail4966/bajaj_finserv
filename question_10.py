import pandas as pd

file_path = r"C:\Users\SOHAIL\OneDrive\Desktop\DataEngineeringQ2.json"  
data = pd.read_json(file_path)

def is_valid_phone_number(phone_number):
    
    phone_number = str(phone_number)

    if phone_number.startswith('+91') and len(phone_number) == 13:
        return phone_number[3:].isdigit() and phone_number[3] in '6789'
    elif phone_number.startswith('91') and len(phone_number) == 12:
        return phone_number[2:].isdigit() and phone_number[2] in '6789'
    elif len(phone_number) == 10 and phone_number.isdigit() and phone_number[0] in '6789':
        return True
    return False

data['isValidMobile'] = data['phoneNumber'].apply(is_valid_phone_number)

valid_phone_count = data['isValidMobile'].sum()

print(valid_phone_count)
