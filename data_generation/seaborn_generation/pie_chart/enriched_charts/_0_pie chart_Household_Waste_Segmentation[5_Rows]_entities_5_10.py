
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    'Transportation Mode': ['Bicycle', 'Car', 'Bus', 'Train', 'Walking', 'Motorcycle'],
    'Count': [120, 740, 360, 440, 230, 90]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Color scheme using specific hex color codes
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251']

# Seaborn style
sns.set(style="whitegrid")

# Create the pie chart
plt.figure(figsize=(10, 6))
plt.pie(df['Count'], labels=df['Transportation Mode'], colors=colors, startangle=140, autopct='%1.1f%%')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  

# Chart title
plt.title('Commuting Preferences in Fictional City')

# Show the plot
plt.show()