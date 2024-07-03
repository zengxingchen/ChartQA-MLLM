
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Age Group': '0-2', 'Hours Spent': 0.5},
    {'Age Group': '3-4', 'Hours Spent': 1.5},
    {'Age Group': '5-8', 'Hours Spent': 2.0},
    {'Age Group': '9-12', 'Hours Spent': 3.0},
    {'Age Group': '13-18', 'Hours Spent': 4.5},
    {'Age Group': '19-25', 'Hours Spent': 6.0},
    {'Age Group': '26+', 'Hours Spent': 7.5}
]

# Extracting the 'Age Group' and 'Hours Spent' for the pie chart
age_groups = [entry['Age Group'] for entry in data]
hours_spent = [entry['Hours Spent'] for entry in data]

# Define colors and explode values for the pie chart
colors = plt.cm.Paired(range(len(age_groups)))
explode = [0.05 for _ in age_groups]  # Slightly offset each slice for better visibility
autopct = lambda pct: "{:.1f}%".format(pct) if pct > 0 else ''  # Only show percentage if greater than 0

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(hours_spent, labels=age_groups, autopct=autopct, startangle=90, colors=colors, explode=explode)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Customizing chart with title
plt.title('Hours Spent by Age Group')

# Show the pie chart
plt.show()