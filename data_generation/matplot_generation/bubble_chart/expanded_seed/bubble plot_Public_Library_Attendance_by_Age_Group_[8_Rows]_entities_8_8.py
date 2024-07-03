
import matplotlib.pyplot as plt
import numpy as np

# Given table data
table_data = [
    {'Age Group': '0-12', 'Library Name': 'Rivertown Library', 'Visits Last Month': 340, 'Number of Books Loaned': 980, 'Average Loan Duration (Days)': 14},
    {'Age Group': '13-18', 'Library Name': 'Oldtown Library', 'Visits Last Month': 250, 'Number of Books Loaned': 710, 'Average Loan Duration (Days)': 21},
    {'Age Group': '19-25', 'Library Name': 'Liberty Library', 'Visits Last Month': 500, 'Number of Books Loaned': 1450, 'Average Loan Duration (Days)': 17},
    {'Age Group': '26-35', 'Library Name': 'Central Library', 'Visits Last Month': 600, 'Number of Books Loaned': 1260, 'Average Loan Duration (Days)': 20},
    {'Age Group': '36-50', 'Library Name': 'Kingsfield Library', 'Visits Last Month': 450, 'Number of Books Loaned': 1380, 'Average Loan Duration (Days)': 22},
    {'Age Group': '51-65', 'Library Name': 'Westside Library', 'Visits Last Month': 300, 'Number of Books Loaned': 940, 'Average Loan Duration (Days)': 25},
    {'Age Group': '66+', 'Library Name': 'Grand Arc Library', 'Visits Last Month': 230, 'Number of Books Loaned': 620, 'Average Loan Duration (Days)': 28},
    {'Age Group': 'Multiple Ages', 'Library Name': 'Springside Library', 'Visits Last Month': 1100, 'Number of Books Loaned': 4100, 'Average Loan Duration (Days)': 18}
]

# Create a figure and a set of subplots
plt.figure(figsize=(15, 8))

# Age Group labels, mapping to integer values for x-axis placement
age_groups = ['0-12', '13-18', '19-25', '26-35', '36-50', '51-65', '66+', 'Multiple Ages']
age_group_mapping = {age: index for index, age in enumerate(age_groups)}

# Extract data for plotting
x = [age_group_mapping[data['Age Group']] for data in table_data]
y = [data['Visits Last Month'] for data in table_data]
sizes = [data['Number of Books Loaned'] for data in table_data]
colors = [data['Average Loan Duration (Days)'] for data in table_data]

# Normalize the size of the bubbles to make them visible and proportional
size_scaler = 20  # Adjust size_scaler to change bubble sizes
sizes = [size * size_scaler for size in sizes]

# Create a bubble chart
scatter = plt.scatter(x, y, s=sizes, c=colors, alpha=0.6, cmap='viridis')

# Add a color bar
cbar = plt.colorbar(scatter)
cbar.set_label('Average Loan Duration (Days)')

# Set the x-axis to use the Age Group labels
plt.xticks(range(len(age_groups)), age_groups)

# Add labels and a title
plt.xlabel('Age Group')
plt.ylabel('Visits Last Month')
plt.title('Library Usage by Age Group')

# Show the plot
plt.grid(True)
plt.show()