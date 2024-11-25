import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# File path to your existing Excel file
file_path = r"C:\Users\jamih\Desktop\Phyton data analsys\Synthetic_Customer_Data.xlsx"

# Load the dataset
df = pd.read_excel(file_path)

# Display first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Summary statistics for numerical columns
print("\nSummary statistics:")
print(df.describe())

# Distribution of 'Age' feature
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True, bins=15)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Distribution of 'Income' feature
plt.figure(figsize=(10, 6))
sns.histplot(df['Income'], kde=True, bins=15, color='green')
plt.title('Distribution of Income')
plt.xlabel('Income (in $1000s)')
plt.ylabel('Frequency')
plt.show()

# Correlation heatmap for numerical features
corr_matrix = df[['Age', 'Income', 'Loan_Amount', 'Loan_Duration', 'Credit_History', 'Default']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Analysis of Default based on Credit History
default_by_credit_history = df.groupby('Credit_History')['Default'].mean()
print("\nDefault rate by Credit History:")
print(default_by_credit_history)

# Analysis of Default based on Loan Amount / Income ratio
df['Loan_Income_Ratio'] = df['Loan_Amount'] / df['Income']
loan_income_default = df.groupby('Loan_Income_Ratio')['Default'].mean().reset_index()

# Plotting Default vs Loan/Income ratio
plt.figure(figsize=(10, 6))
sns.lineplot(x='Loan_Income_Ratio', y='Default', data=loan_income_default)
plt.title('Default Rate vs Loan/Income Ratio')
plt.xlabel('Loan/Income Ratio')
plt.ylabel('Default Rate')
plt.show()

