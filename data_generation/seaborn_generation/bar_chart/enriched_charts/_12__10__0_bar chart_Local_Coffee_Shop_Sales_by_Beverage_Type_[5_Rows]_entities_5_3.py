
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the dataset
data = pd.DataFrame({
    'Age Group': ['18-25', '18-25', '26-35', '26-35', '36-45', '36-45', '46-55', '46-55', '56-65', '56-65', '66+', '66+'],
    'Workout Hours (Hours)': [5.5, 6.0, 4.8, 5.1, 4.2, 4.5, 3.8, 3.6, 3.0, 2.8, 2.5, 2.3],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
})

# Set the style and color palette of the plot
sns.set_style('whitegrid')
sns.set_palette(['#3498DB', '#E74C3C', '#2ECC71', '#9B59B6', '#F1C40F', '#E67E22'])

# Create a horizontal bar chart
plt.figure(figsize=(12, 8))  # Width and height of the chart
chart = sns.barplot(y='Age Group', x='Workout Hours (Hours)', hue='Gender', data=data, dodge=True, saturation=0.8)

chart.set_ylabel('Age Group', fontsize=12)
chart.set_xlabel('Average Weekly Workout Hours (Hours)', fontsize=12)
chart.set_title('Average Weekly Workout Hours by Age Group and Gender', fontsize=16, pad=20)

# Change the height of bars
for bar in chart.patches:
    bar.set_height(0.5)

plt.show()