
import matplotlib.pyplot as plt

# Provided data
data = [{'Park Name': 'Riverside Park', '0-14 years': '25%', '15-24 years': '20%', '25-44 years': '30%', '45-64 years': '15%', '65+ years': '10%'},
        {'Park Name': 'Central Gardens', '0-14 years': '22%', '15-24 years': '18%', '25-44 years': '35%', '45-64 years': '15%', '65+ years': '10%'},
        {'Park Name': 'Eastside Walkway', '0-14 years': '30%', '15-24 years': '25%', '25-44 years': '25%', '45-64 years': '10%', '65+ years': '10%'},
        {'Park Name': 'Greenbelt Lane', '0-14 years': '15%', '15-24 years': '10%', '25-44 years': '40%', '45-64 years': '25%', '65+ years': '10%'},
        {'Park Name': 'Liberty Trails', '0-14 years': '18%', '15-24 years': '20%', '25-44 years': '30%', '45-64 years': '22%', '65+ years': '10%'},
        {'Park Name': 'Northend Grounds', '0-14 years': '20%', '15-24 years': '22%', '25-44 years': '30%', '45-64 years': '18%', '65+ years': '10%'},
        {'Park Name': 'Lakeview Lands', '0-14 years': '28%', '15-24 years': '18%', '25-44 years': '26%', '45-64 years': '20%', '65+ years': '8%'},
        {'Park Name': 'Hilltop Reserve', '0-14 years': '22%', '15-24 years': '19%', '25-44 years': '33%', '45-64 years': '16%', '65+ years': '10%'}]

# Extract Park Names and create a list of park names
park_names = [item['Park Name'] for item in data]

# Convert percentage strings to floats and store them in separate lists
age_groups = ['0-14 years', '15-24 years', '25-44 years', '45-64 years', '65+ years']
ages_data = {age: [float(park[age].strip('%')) for park in data] for age in age_groups}

# Prepare the figure and bar chart
fig, ax = plt.subplots(figsize=(10, 7))

# Define a function to stack bars
def add_stacked_bar(age_group, bottom):
    return ax.bar(park_names, ages_data[age_group], width=0.6, bottom=bottom, label=age_group)

# Stack the bars
bottoms = [0] * len(park_names)
for age in age_groups:
    bars = add_stacked_bar(age, bottoms)
    # Update bottoms for the next stack
    bottoms = [bottoms[i] + ages_data[age][i] for i in range(len(park_names))]

# Add labels, title, and legend
ax.set_xlabel('Park Name')
ax.set_ylabel('Percentage')
ax.set_title('Age Group Distribution in Parks (Stacked 100%)')
ax.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()