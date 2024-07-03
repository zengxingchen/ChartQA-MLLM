
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Week': 'Week 1', 'Yoga_Participants': 15, 'Zumba_Participants': 20, 'Pilates_Participants': 10, 'Average_Age': 35},
    {'Week': 'Week 2', 'Yoga_Participants': 18, 'Zumba_Participants': 22, 'Pilates_Participants': 12, 'Average_Age': 34},
    # ... [Rest of the data is omitted for brevity] ...
    {'Week': 'Week 12', 'Yoga_Participants': 27, 'Zumba_Participants': 30, 'Pilates_Participants': 15, 'Average_Age': 34}
]

# Extracting data for the bubble chart
weeks = [d['Week'] for d in data]
yoga = [d['Yoga_Participants'] for d in data]
zumba = [d['Zumba_Participants'] for d in data]
pilates = [d['Pilates_Participants'] for d in data]
average_age = [d['Average_Age'] for d in data]

# Calculating the scale for bubble sizes, 's', using average_age
# This could be adjusted based on desired bubble size appearance
scale_factor = 10  # A parameter to calibrate the bubble sizes
sizes = [age * scale_factor for age in average_age]

# Setting up the chart
plt.figure(figsize=(12, 8))

# Creating a scatter plot for each activity
plt.scatter(weeks, yoga, s=sizes, alpha=0.6, color='blue', edgecolors='w', label='Yoga')
plt.scatter(weeks, zumba, s=sizes, alpha=0.6, color='green', edgecolors='w', label='Zumba')
plt.scatter(weeks, pilates, s=sizes, alpha=0.6, color='red', edgecolors='w', label='Pilates')

# Adding additional chart elements
plt.title('Participants per Activity with Average Age Bubble Size')
plt.xlabel('Week')
plt.ylabel('Number of Participants')
plt.legend(loc='upper right')
plt.grid(True)

# Showing the plot
plt.show()