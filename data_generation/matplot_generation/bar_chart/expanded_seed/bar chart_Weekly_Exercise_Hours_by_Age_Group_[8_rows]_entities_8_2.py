
import matplotlib.pyplot as plt

# Data from your chart table
data = [
    {'Age Group': '16-24', ' Average Exercise Hours per Week': 4.5},
    {'Age Group': '25-34', ' Average Exercise Hours per Week': 3.8},
    {'Age Group': '35-44', ' Average Exercise Hours per Week': 3.5},
    {'Age Group': '45-54', ' Average Exercise Hours per Week': 3.0},
    {'Age Group': '55-64', ' Average Exercise Hours per Week': 2.5},
    {'Age Group': '65-74', ' Average Exercise Hours per Week': 2.0},
    {'Age Group': '75-84', ' Average Exercise Hours per Week': 1.5},
    {'Age Group': '85+', ' Average Exercise Hours per Week': 1.0}
]

# Separate the Age Group labels and their corresponding Average Exercise Hours
age_groups = [item['Age Group'] for item in data]
exercise_hours = [item[' Average Exercise Hours per Week'] for item in data]

# Creating the bar chart
plt.figure(figsize=(10, 6))  # Set the figure size
bars = plt.bar(age_groups, exercise_hours, color=['#1f77b4', '#ff7f0e', '#2ca02c', 
                                                  '#d62728', '#9467bd', '#8c564b', 
                                                  '#e377c2', '#7f7f7f'])  # Use different colors for each bar

# Add data labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, round(yval, 1), 
             ha='center', va='bottom')

# Add the title and labels
plt.title('Average Exercise Hours per Week by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Exercise Hours per Week')

# Adding a grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()