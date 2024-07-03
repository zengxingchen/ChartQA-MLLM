
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    'Pet Type': ['Dogs', 'Cats', 'Birds', 'Fish', 'Reptiles'],
    'Count': [500, 320, 150, 100, 30]
}

# Create DataFrame
df = pd.DataFrame(data)

# Generate colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#C2F0C2']

# Make the pie chart
plt.figure(figsize=(10, 8))
plt.pie(df['Count'], labels=df['Pet Type'], autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Preferred Pet Types Distribution')

# Show the plot
plt.show()