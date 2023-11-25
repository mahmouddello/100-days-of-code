import pandas as pd

data_dict = {
    "students": ["Mahmoud", "Anas", "Perihan"],
    "scores": [96, 88, 99]
}

df = pd.DataFrame(data_dict)
print(df)

df.to_csv("students_data.csv")  # Creating csv file from the DataFrame we have
