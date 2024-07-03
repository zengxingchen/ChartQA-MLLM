
import matplotlib.pyplot as plt
import seaborn as sns

# Data provided
data = [{'Age Group': '0-2', 'Hours Per Day': 0.5},
        {'Age Group': '3-5', 'Hours Per Day': 1.5},
        {'Age Group': '6-8', 'Hours Per Day': 2.0},
        {'Age Group': '9-12', 'Hours Per Day': 3.0},
        {'Age Group': '13-18', 'Hours Per Day': 4.5},
        {'Age Group': '19-30', 'Hours Per Day': 3.7},
        {'Age Group': '31-45', 'Hours Per Day': 3.5},
        {'Age Group': '46-60', 'Hours Per Day': 3.0},
        {'Age Group': '61+', 'Hours Per Day': 2.5}]

# Convert the data into a format that can be used by Matplotlib
age_groups = [entry['Age Group'] for entry in data]
hours_per_day = [entry['Hours Per Day'] for entry in data]

# Seaborn styles
sns.set(style="whitegrid")  # Use seaborn style aesthetics

# Create a pie chart
plt.figure(figsize=(10, 8))  # Specify the size of the figure

# Create the pie chart
plt.pie(hours_per_day, labels=age_groups, autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Title and other customizations can be done here
plt.title('Daily Screen Time by Age Group', fontsize=16)

# Show the plot
plt.show()