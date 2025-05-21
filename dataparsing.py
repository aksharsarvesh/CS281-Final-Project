import pandas as pd

def analyze_diabetes_medication():
    # Read the CSV file
    df = pd.read_csv('data/diabetic_data.csv')
    total = len(df)
    
    # Count patients on and off diabetes medication
    yes_count = (df['diabetesMed'] == 'Yes').sum()
    no_count = (df['diabetesMed'] == 'No').sum()
    
    # Print results
    print("\nDiabetes Medication Analysis:")
    print(f"Total patients: {total}")
    print(f"Patients on diabetes medication: {yes_count} ({yes_count/total*100:.2f}%)")
    print(f"Patients not on diabetes medication: {no_count} ({no_count/total*100:.2f}%)")

def analyze_readmission():
    # Read the CSV file
    df = pd.read_csv('data/diabetic_data.csv')
    total = len(df)
    
    # Count patients based on readmission status
    # "<30" is considered readmitted, "NO" and ">30" are considered not readmitted
    yes_count = (df['readmitted'] == '<30').sum()
    no_count = ((df['readmitted'] == 'NO') | (df['readmitted'] == '>30')).sum()
    
    # Print results
    print("\nReadmission Analysis:")
    print(f"Total patients: {total}")
    print(f"Patients readmitted within 30 days: {yes_count} ({yes_count/total*100:.2f}%)")
    print(f"Patients not readmitted or readmitted after 30 days: {no_count} ({no_count/total*100:.2f}%)")

def diabetes_analyze_category_sizes():
    # Read the CSV file
    df = pd.read_csv('data/diabetic_data.csv')
    total = len(df)
    
    # Count patients in each category
    for col in df.columns:
        unique_count = df[col].nunique()
        
        print(f"\n{col}:")

        print(f"Unique values: {unique_count}") 
        print(df[col].value_counts())
        
def income_analyze_category_sizes():
    # Read the CSV file
    df = pd.read_csv('data/income_data.csv')
    total = len(df)
    
    # Count patients in each category
    for col in df.columns:
        unique_count = df[col].nunique()
        
        print(f"\n{col}:")

        print(f"Unique values: {unique_count}") 
        print(df[col].value_counts())

def loan_analyze_category_sizes():
    # Read the CSV file
    df = pd.read_csv('data/loan_data.csv')
    total = len(df)
    categorical_features = ['derived_dwelling_category', 'conforming_loan_limit', 'derived_race', 'derived_sex', 'purchaser_type', 'loan_type', 'loan_purpose', 'lien_status',
                        'reverse_mortgage', 'open-end_line_of_credit', 'business_or_commercial_purpose', 'hoepa_status', 'negative_amortization', 'interest_only_payment',
                        'balloon_payment', 'other_nonamortizing_features', 'occupancy_type', 'manufactured_home_secured_property_type', 'manufactured_home_land_property_interest',
                        'debt_to_income_ratio', 'applicant_credit_score_type', 'applicant_race_observed', 'applicant_sex_observed', 'applicant_age', 'denial_reason-1']

    # Count in each category
    col = "action_taken"
    unique_count = df[col].nunique()
        
    print(f"\n{col}:")

    print(f"Unique values: {unique_count}") 
    print(df[col].value_counts())
    for col in categorical_features:
        unique_count = df[col].nunique()
        
        print(f"\n{col}:")

        print(f"Unique values: {unique_count}") 
        print(df[col].value_counts())
if __name__ == "__main__":
    # analyze_diabetes_medication()
    # analyze_readmission()
    # diabetes_analyze_category_sizes()
    # income_analyze_category_sizes()
    loan_analyze_category_sizes()