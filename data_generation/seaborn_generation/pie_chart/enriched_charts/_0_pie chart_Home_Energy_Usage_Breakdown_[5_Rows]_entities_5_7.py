
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    'Task': ['Research', 'Planning', 'Design', 'Development', 'Testing', 'Deployment', 'Maintenance', 'Documentation'],
    'Time Spent': [20, 30, 25, 60, 40, 15, 10, 10]
}

df = pd.DataFrame(data)

# Colors
colors = ['#3498db', '#2ecc71', '#f1c40f', '#e74c3c', '#8e44ad', '#2980b9', '#16a085', '#d35400']

# Pie chart
plt.figure(figsize=(12, 8))
plt.pie(df['Time Spent'], labels=df['Task'], colors=colors, autopct='%.1f%%', startangle=140)
plt.title('Distribution of Time Spent on Software Project Tasks')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()