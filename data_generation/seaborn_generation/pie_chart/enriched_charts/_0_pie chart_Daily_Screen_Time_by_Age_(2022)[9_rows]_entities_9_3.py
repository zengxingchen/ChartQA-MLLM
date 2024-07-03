
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data preparation
data = {
    'Language': ['Python', 'JavaScript', 'Java', 'C#', 'Ruby', 'C++'],
    'Users': [30, 25, 20, 15, 5, 5]
}

df = pd.DataFrame(data)

# Create a pie chart
plt.figure(figsize=(10, 8))

# Specifying custom colors for the slices
colors = ['#FF6347', '#4682B4', '#FFD700', '#ADFF2F', '#FF4500', '#00CED1']

# Using seaborn style
sns.set(style="whitegrid")

# Explode the 1st slice (Python)
explode = (0.1, 0, 0, 0, 0, 0)

# Plotting the pie chart
plt.pie(df['Users'], labels=df['Language'], colors=colors, explode=explode,
        autopct='%1.1f%%', startangle=140)

# Customizing the title
plt.title('Programming Language Popularity')

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()