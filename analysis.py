import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', engine='python')


column_name = 'Sales'
print("First 5 rows:")
print(df.head())

print("\nBasic Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

if column_name in df.columns:
    avg_value = df[column_name].mean()
    print(f"\nAverage of {column_name}: {avg_value:.2f}")

if 'Category' in df.columns and column_name in df.columns:
    category_avg = df.groupby('Category')[column_name].mean()

    plt.figure()
    category_avg.plot(kind='bar')
    plt.title('Average Sales per Category')
    plt.xlabel('Category')
    plt.ylabel('Average Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
if 'Sales' in df.columns and 'Profit' in df.columns:
    plt.figure()
    df = pd.read_csv('data.csv', on_bad_lines='skip', engine='python')
    plt.scatter(df['Sales'], df['Profit'])
    plt.title('Sales vs Profit')    
    plt.xlabel('Sales')
    plt.ylabel('Profit')
    plt.tight_layout()
    plt.show()

corr = df.corr(numeric_only=True)

plt.figure()
plt.imshow(corr, interpolation='nearest')
plt.title('Correlation Heatmap')
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.tight_layout()
plt.show()
print("\nInsights:")

if column_name in df.columns:
    print(f"- The average {column_name} is {avg_value:.2f}.")

if 'Sales' in df.columns and 'Profit' in df.columns:
    correlation = df['Sales'].corr(df['Profit'])
    print(f"- Correlation between Sales and Profit: {correlation:.2f}")
    
    if correlation > 0:
        print("- Positive relationship: Higher sales tend to generate higher profit.")
    else:
        print("- Negative relationship: Higher sales may not always mean higher profit.")

print("- Check the heatmap to identify strong correlations between variables.")
print("- Bar chart helps compare category performance.")
print("- Scatter plot reveals trends and outliers.")
