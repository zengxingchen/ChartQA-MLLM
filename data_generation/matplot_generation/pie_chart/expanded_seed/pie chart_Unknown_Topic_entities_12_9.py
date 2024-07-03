
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Activity': 'Soccer', 'Percentage': '18%'},
    {'Activity': 'Basketball', 'Percentage': '15%'},
    {'Activity': 'Swimming', 'Percentage': '12%'},
    {'Activity': 'Gym Workouts', 'Percentage': '10%'},
    {'Activity': 'Yoga', 'Percentage': '9%'},
    {'Activity': 'Cycling', 'Percentage': '8%'},
    {'Activity': 'Running Clubs', 'Percentage': '7%'},
    {'Activity': 'Tennis', 'Percentage': '6%'},
    {'Activity': 'Dance Classes', 'Percentage': '5%'},
    {'Activity': 'Hiking', 'Percentage': '4%'},
    {'Activity': 'Martial Arts', 'Percentage': '3%'},
    {'Activity': 'Others', 'Percentage': '3%'}
]

# Extracting activities and corresponding percentage values
activities = [item['Activity'] for item in data]
percentages = [int(item['Percentage'].strip('%')) for item in data]

# Colors for each slice
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1f77b4', '#ff7f0e'
]

# Exploding the first slice (Soccer)
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Plotting the pie chart
plt.figure(figsize=(10, 8))
plt.pie(percentages, explode=explode, labels=activities, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 9})

# Adding a title
plt.title('Popularity of Activities', pad=20)

# Display the plot
plt.show()