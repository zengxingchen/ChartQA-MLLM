
import matplotlib.pyplot as plt
import squarify

# Data
data = [
    {'Sport': 'Soccer', 'Number of Participants': 120, 'Age Group': '16-30', 'Session Length (minutes)': 90},
    {'Sport': 'Basketball', 'Number of Participants': 75, 'Age Group': '16-30', 'Session Length (minutes)': 60},
    {'Sport': 'Volleyball', 'Number of Participants': 50, 'Age Group': '31-45', 'Session Length (minutes)': 60},
    {'Sport': 'Swimming', 'Number of Participants': 40, 'Age Group': '46-60', 'Session Length (minutes)': 45},
    {'Sport': 'Yoga', 'Number of Participants': 60, 'Age Group': '31-45', 'Session Length (minutes)': 60},
    {'Sport': 'Running', 'Number of Participants': 100, 'Age Group': '16-30', 'Session Length (minutes)': 30},
    {'Sport': 'Cycling', 'Number of Participants': 80, 'Age Group': '31-45', 'Session Length (minutes)': 45},
    {'Sport': 'Tennis', 'Number of Participants': 30, 'Age Group': '46-60', 'Session Length (minutes)': 60}
]

# Extracting necessary information for the treemap
labels = [f"{entry['Sport']}\n({entry['Number of Participants']} participants)" for entry in data]
sizes = [entry['Number of Participants'] for entry in data]
age_group = [entry['Age Group'] for entry in data]

# Color mapping based on Age Group
colors = {
    '16-30': 'skyblue',
    '31-45': 'lightgreen',
    '46-60': 'salmon'
}
color_list = [colors[age] for age in age_group]

# Create a figure and axis
fig, ax = plt.subplots(1, figsize=(12, 8))

# Treemap parameters
squarify.plot(sizes=sizes, label=labels, color=color_list, alpha=0.8)

# Remove the axis
plt.axis('off')

# Add a title
plt.title('Treemap of Participants in Different Sports', fontsize=18)

# Show the plot
plt.show()