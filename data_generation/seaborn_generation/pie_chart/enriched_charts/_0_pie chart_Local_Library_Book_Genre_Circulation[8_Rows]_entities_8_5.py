
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data for the pie chart
data = {
    'Energy Source': ['Hydropower', 'Wind Power', 'Solar Power', 'Bioenergy', 'Geothermal', 'Marine'],
    'Energy Usage (TWh)': [4006, 1433, 720, 560, 88, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot Pie Chart
plt.figure(figsize=(10, 8))  # Adjusting the figure size
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#17becf']  # Specific color codes

plt.pie(df['Energy Usage (TWh)'], labels=df['Energy Source'], autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Global Renewable Energy Usage Distribution (TWh)')  # Updated chart topic and title
plt.show()