import pandas as pd
import numpy as np

# hard coded paths - this could easily be changed to
# get dynamically from another application, or to accept
# command line arguments
json_location = './bmi.json'
csv_location = './table1.csv'


def build_dataframe(json_path, csv_path):
    df = pd.read_json(json_path)
    lookup_df = pd.read_csv(csv_path)

    df['BMI'] = df.apply(lambda row: row.WeightKg/((row.HeightCm/100) ** 2), axis=1)

    conditions = [
        df['BMI'] <= 18.4,
        (df['BMI'] >= 18.5) & (df['BMI'] <= 24.9),
        (df['BMI'] >= 25) & (df['BMI'] <= 29.9),
        (df['BMI'] >= 30) & (df['BMI'] <= 34.9),
        (df['BMI'] >= 35) & (df['BMI'] <= 39.9),
        df['BMI'] >= 40
    ]

    bmi_category_values = list(lookup_df['BMI Category'])

    health_risk_values = list(lookup_df['Health risk'])

    df['BMI Category'] = np.select(conditions, bmi_category_values, default=0)
    df['Health Risk'] = np.select(conditions, health_risk_values, default=0)

    return df


def get_weight_category_count(input_df, overweight_category):
    return input_df['BMI Category'].value_counts().get(overweight_category)


completed_dataframe = build_dataframe(json_location, csv_location)
overweight_count = get_weight_category_count(completed_dataframe, 'Overweight')

print(completed_dataframe)
print('\n')
print('The number of overweight people is: ' + str(overweight_count))
