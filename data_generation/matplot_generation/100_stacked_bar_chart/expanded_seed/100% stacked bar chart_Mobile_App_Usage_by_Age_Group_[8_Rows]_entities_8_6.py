
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Age Group': '16-25', 'Communication Apps': '30%', 'Social Media Apps': '25%', 'Games': '20%', 'Productivity Apps': '5%', 'Health & Fitness Apps': '5%', 'News & Reading Apps': '5%', 'Music & Audio Apps': '5%', 'Shopping Apps': '5%'},
    {'Age Group': '26-35', 'Communication Apps': '25%', 'Social Media Apps': '20%', 'Games': '15%', 'Productivity Apps': '10%', 'Health & Fitness Apps': '10%', 'News & Reading Apps': '5%', 'Music & Audio Apps': '10%', 'Shopping Apps': '5%'},
    {'Age Group': '36-45', 'Communication Apps': '20%', 'Social Media Apps': '15%', 'Games': '10%', 'Productivity Apps': '15%', 'Health & Fitness Apps': '15%', 'News & Reading Apps': '10%', 'Music & Audio Apps': '10%', 'Shopping Apps': '5%'},
    {'Age Group': '46-55', 'Communication Apps': '15%', 'Social Media Apps': '10%', 'Games': '5%', 'Productivity Apps': '20%', 'Health & Fitness Apps': '20%', 'News & Reading Apps': '15%', 'Music & Audio Apps': '10%', 'Shopping Apps': '5%'},
    {'Age Group': '56-65', 'Communication Apps': '10%', 'Social Media Apps': '5%', 'Games': '3%', 'Productivity Apps': '25%', 'Health & Fitness Apps': '25%', 'News & Reading Apps': '20%', 'Music & Audio Apps': '7%', 'Shopping Apps': '5%'},
    {'Age Group': '66-75', 'Communication Apps': '5%', 'Social Media Apps': '3%', 'Games': '2%', 'Productivity Apps': '20%', 'Health & Fitness Apps': '25%', 'News & Reading Apps': '25%', 'Music & Audio Apps': '10%', 'Shopping Apps': '10%'},
    {'Age Group': '76-85', 'Communication Apps': '2%', 'Social Media Apps': '1%', 'Games': '1%', 'Productivity Apps': '15%', 'Health & Fitness Apps': '20%', 'News & Reading Apps': '30%', 'Music & Audio Apps': '15%', 'Shopping Apps': '15%'},
    {'Age Group': '85+', 'Communication Apps': '3%', 'Social Media Apps': '2%', 'Games': '1%', 'Productivity Apps': '10%', 'Health & Fitness Apps': '10%', 'News & Reading Apps': '15%', 'Music & Audio Apps': '20%', 'Shopping Apps': '25%'}
]

# Convert percentage strings to numbers and find the categories
categories = list(data[0].keys())[1:]  # Exclude 'Age Group'
age_groups = [entry['Age Group'] for entry in data]
numeric_data = [{cat: float(entry[cat].strip('%')) for cat in categories} for entry in data]

# Create a list of bottom values for stacking
bottoms = [0] * len(age_groups)

fig, ax = plt.subplots()

# Loop through each category and stack bars
for category in categories:
    values = [entry[category] for entry in numeric_data]
    ax.bar(age_groups, values, label=category, bottom=bottoms)
    # Update bottoms for the next stack
    bottoms = [bottoms[i] + values[i] for i in range(len(age_groups))]

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel('Age Group')
ax.set_ylabel('Percentage')
ax.set_title('100% Stacked Bar Chart of App Usage by Age Group')
ax.legend()

# Rotate X-axis labels for better readability
plt.xticks(rotation=45)

# Display the stacked bar chart
plt.show()