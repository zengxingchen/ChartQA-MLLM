
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Provided data
data = [
    {'Category': 'Compostable', 'Percentage': 32},
    {'Category': 'Recyclable', 'Percentage': 44},
    {'Category': 'Electronic Waste', 'Percentage': 11},
    {'Category': 'Hazardous', 'Percentage': 7},
    {'Category': 'Other', 'Percentage': 6}
]

# Convert list of dictionaries into a DataFrame
df = pd.DataFrame(data)

# Set Seaborn style for the plot
sns.set(style="whitegrid")

# Create a Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(df['Percentage'], labels=df['Category'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))

# This is additional styling to make the chart more aesthetically pleasing
plt.title('Waste Categories Distribution')

# Show the plot
plt.show()