
import matplotlib.pyplot as plt

# Define the data
data = [
    {'Participant_Name': 'John Smith', 'Age_Group': '18-25', 'Steps_Count': 32000, 'Challenge_Duration_Days': 30},
    {'Participant_Name': 'Laura Adams', 'Age_Group': '26-35', 'Steps_Count': 45000, 'Challenge_Duration_Days': 30},
    {'Participant_Name': 'Michael Brown', 'Age_Group': '36-45', 'Steps_Count': 39000, 'Challenge_Duration_Days': 30},
    {'Participant_Name': 'Chloe Johnson', 'Age_Group': '46-55', 'Steps_Count': 31000, 'Challenge_Duration_Days': 30},
    {'Participant_Name': 'Harold Miller', 'Age_Group': '56-65', 'Steps_Count': 25000, 'Challenge_Duration_Days': 30},
    {'Participant_Name': 'Samantha Wilson', 'Age_Group': '26-35', 'Steps_Count': 47000, 'Challenge_Duration_Days': 30},
    {'Participant_Name': 'Mark Taylor', 'Age_Group': '36-45', 'Steps_Count': 36000, 'Challenge_Duration_Days': 30},
    {'Participant_Name': 'Jennifer Davis', 'Age_Group': '18-25', 'Steps_Count': 42000, 'Challenge_Duration_Days': 30},
    {'Participant_Name': 'Lucas Moore', 'Age_Group': '46-55', 'Steps_Count': 33000, 'Challenge_Duration_Days': 30},
    {'Participant_Name': 'Emma Lee', 'Age_Group': '56-65', 'Steps_Count': 28500, 'Challenge_Duration_Days': 30},
    {'Participant_Name': 'Olivia Jones', 'Age_Group': '26-35', 'Steps_Count': 41000, 'Challenge_Duration_Days': 30},
    {'Participant_Name': 'Noah White', 'Age_Group': '18-25', 'Steps_Count': 44000, 'Challenge_Duration_Days': 30}
]

# Initialize x, y, sizes and colors lists
names = [d['Participant_Name'] for d in data]
x = list(range(len(names)))
y = [d['Steps_Count'] for d in data]
sizes = [d['Steps_Count'] / 1000 for d in data]  # Normalize sizes for bubble size representation
age_groups = [d['Age_Group'] for d in data]
colors = {'18-25': 'blue', '26-35': 'green', '36-45': 'red', '46-55': 'orange', '56-65': 'purple'}  # Age group colors
color_list = [colors[age.strip()] for age in age_groups]  # getColor for each participant

# Create the plot
plt.figure(figsize=(10, 8))

bubble = plt.scatter(x, y, s=sizes, c=color_list, alpha=0.5)  # Adding the alpha for transparency

# Adding labels and title
plt.title('Steps Count by Participants')
plt.xlabel('Participants')
plt.ylabel('Steps Count')

# Set x ticks
plt.xticks(x, names, rotation=45, ha='right')

# Add a color legend for age groups
from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], marker='o', color='w', label=age_group, markerfacecolor=color, markersize=10) for age_group, color in colors.items()]
plt.legend(handles=legend_elements, title="Age Groups")

# Show the plot
plt.tight_layout()
plt.show()