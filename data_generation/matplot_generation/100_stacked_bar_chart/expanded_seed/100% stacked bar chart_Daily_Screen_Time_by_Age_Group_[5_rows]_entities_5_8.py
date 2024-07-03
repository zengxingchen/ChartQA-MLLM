
import matplotlib.pyplot as plt
import numpy as np

# Provided data
data = [
    {'Age Group': '0-8', 'TV': 50, 'Computer': 10, 'Mobile Device': 30, 'Gaming': 10},
    {'Age Group': '9-13', 'TV': 30, 'Computer': 20, 'Mobile Device': 40, 'Gaming': 10},
    {'Age Group': '14-18', 'TV': 20, 'Computer': 30, 'Mobile Device': 45, 'Gaming': 5},
    {'Age Group': '19-25', 'TV': 15, 'Computer': 35, 'Mobile Device': 40, 'Gaming': 10},
    {'Age Group': '26-35', 'TV': 20, 'Computer': 40, 'Mobile Device': 30, 'Gaming': 10}
]

# Sort the data by Age Group for visual consistency
data.sort(key=lambda x: x['Age Group'])

# Extracting the Age Groups
age_groups = [x['Age Group'] for x in data]

# Extract individual categories of data
tv = np.array([x['TV'] for x in data])
computer = np.array([x['Computer'] for x in data])
mobile = np.array([x['Mobile Device'] for x in data])
gaming = np.array([x['Gaming'] for x in data])

# Calculating the percentage
total = tv + computer + mobile + gaming
tv_pct = tv / total * 100
computer_pct = computer / total * 100
mobile_pct = mobile / total * 100
gaming_pct = gaming / total * 100

# Bottom offsets for each bar segment
bottom_computer = tv_pct
bottom_mobile = bottom_computer + computer_pct
bottom_gaming = bottom_mobile + mobile_pct

fig, ax = plt.subplots()

# Plotting the stacked bars
ax.bar(age_groups, tv_pct, label='TV')
ax.bar(age_groups, computer_pct, bottom=tv_pct, label='Computer')
ax.bar(age_groups, mobile_pct, bottom=bottom_computer, label='Mobile Device')
ax.bar(age_groups, gaming_pct, bottom=bottom_mobile, label='Gaming')

# Adding labels and title
ax.set_ylabel('Percentage')
ax.set_xlabel('Age Group')
ax.set_title('Device Usage by Age Group - 100% Stacked Bar Chart')

# Adding the legend
ax.legend()

# Displaying the values on the bars for better readability
for i, (tv, comp, mob, game) in enumerate(zip(tv_pct, computer_pct, mobile_pct, gaming_pct)):
    ax.text(i, tv/2, f'{tv:.1f}%', ha='center', va='center', color='white')
    ax.text(i, tv + comp/2, f'{comp:.1f}%', ha='center', va='center', color='white')
    ax.text(i, tv + comp + mob/2, f'{mob:.1f}%', ha='center', va='center', color='white')
    ax.text(i, tv + comp + mob + game/2, f'{game:.1f}%', ha='center', va='center', color='white')

# Adjusting the layout
plt.tight_layout()

# Show the plot
plt.show()