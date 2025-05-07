import pandas as pd


df = pd.read_csv(r"C:\Users\USER\Downloads\Assignment_1_introduction_to_py_for_data_science_01-05-025 - Assign ment 1 Educonect.csv.csv")
print("Dataset loaded successfully!")

print(df.head)
# 1. How many rows and columns?
num_rows, num_cols = df.shape
print(f"\nNumber of Rows: {num_rows}, Number of Columns: {num_cols}")

# 2. What are the data types of each column?
print("\nData Types of Each Column:")
print(df.dtypes)

# 3. Which columns contain numerical data? Which ones are categorical?
numerical_cols = df.select_dtypes(include=['number']).columns
categorical_cols = df.select_dtypes(exclude=['number']).columns
print("\nNumerical Columns:", list(numerical_cols))
print("Categorical Columns:", list(categorical_cols))

# 4. What are the top 2 most frequent values in the Customer Segment column?
print("\nTop 2 Most Frequent Customer Segments:")
print(df['Customer Segment'].value_counts().head(2))

# 5. List the unique values in the Loan Type, Risk Type, and Risk Level columns.
print("\nUnique Values in Loan Type:")
print(df['Loan Type'].unique())
print("\nUnique Values in Risk Type:")
print(df['Risk Type'].unique())
print("\nUnique Values in Risk Level:")
print(df['Risk Level'].unique())

# 6. Which columns might be useful for customer profitability analysis?
print("\nColumns useful for Customer Profitability Analysis: Revenue, Expense, Customer Profitability, Customer Lifetime Value (CLV)")

# 7. Which columns can be grouped together for risk analysis?
print("\nColumns for Risk Analysis: Risk Type, Risk Level, Risk Mitigation")