
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'Person': 'Alice', 'Date': '2023-03-01', 'Step Count': 5400},
    {'Person': 'Bob', 'Date': '2023-03-01', 'Step Count': 7300},
    {'Person': 'Charlie', 'Date': '2023-03-01', 'Step Count': 9100},
    {'Person': 'Diana', 'Date': '2023-03-01', 'Step Count': 4100},
    {'Person': 'Ethan', 'Date': '2023-03-01', 'Step Count': 6200}
]

# Convert raw data to pandas DataFrame
df = pd.DataFrame(data)

# Convert Date to datetime and ensure 'Step Count' is an integer
df['Date'] = pd.to_datetime(df['Date'])
df['Step Count'] = df['Step Count'].astype(int)

# Create scatterplot
plt.figure(figsize=(10, 6))  # Set the size of the plot
sns.scatterplot(data=df, x='Person', y='Step Count', size='Step Count', hue='Person', style='Person', sizes=(100, 500), palette='viridis')

# Customize the plot
plt.title('Daily Step Count per Person')
plt.xlabel('Person')
plt.ylabel('Step Count')
plt.legend(title='Person', bbox_to_anchor=(1.05, 1), loc='upper left')  # Move the legend outside the plot

# Display the plot
plt.tight_layout()
plt.show()