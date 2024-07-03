
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Creating the data as a DataFrame
data = {
    'Activity': ['Running', 'Swimming', 'Cycling', 'Yoga', 'Weightlifting', 'Hiking', 'Tennis', 'Basketball', 'Soccer', 'Pilates'],
    'Participants': [450, 340, 390, 300, 210, 280, 160, 230, 190, 150]
}

df = pd.DataFrame(data)

# Sorting data to make the chart easier to read
df = df.sort_values('Participants', ascending=False)

# Set up the matplotlib figure with changed width and height
plt.figure(figsize=(12, 6))

# Create the bar plot
sns.barplot(
    x='Activity',
    y='Participants',
    data=df,
    palette=[
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
    ],
    linewidth=1.5,
    edgecolor='black'
)

# Adjust the width of the bars
for bar in plt.gca().patches:
    bar.set_width(0.7)

# Adding chart labels and title
plt.ylabel('Number of Participants')
plt.xlabel('Activity')
plt.title('Popularity of Various Sports Activities')

# Show the plot
plt.show()