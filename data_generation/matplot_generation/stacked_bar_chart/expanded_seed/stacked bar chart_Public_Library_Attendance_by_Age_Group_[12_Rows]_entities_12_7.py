
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Month': 'January', ' Children (0-12)': 230, ' Teens (13-18)': 120, ' Adults (19-64)': 459, ' Seniors (65+)': 178},
    {'Month': 'February', ' Children (0-12)': 210, ' Teens (13-18)': 110, ' Adults (19-64)': 400, ' Seniors (65+)': 190},
    # ... (other data points)
    {'Month': 'December', ' Children (0-12)': 250, ' Teens (13-18)': 130, ' Adults (19-64)': 480, ' Seniors (65+)': 230}
]

# Extract month names for x-axis labels
months = [entry['Month'] for entry in data]

# Extract values for each age group
children = [entry[' Children (0-12)'] for entry in data]
teens = [entry[' Teens (13-18)'] for entry in data]
adults = [entry[' Adults (19-64)'] for entry in data]
seniors = [entry[' Seniors (65+)'] for entry in data]

# Create a figure and an axes object
fig, ax = plt.subplots(figsize=(10, 7))  # Adjust the figure size as needed

# Plot stacked bars for each age group
ax.bar(months, children, label='Children (0-12)')
ax.bar(months, teens, bottom=children, label='Teens (13-18)')
ax.bar(months, adults, bottom=[i+j for i,j in zip(children, teens)], label='Adults (19-64)')
ax.bar(months, seniors, bottom=[i+j+k for i,j,k in zip(children, teens, adults)], label='Seniors (65+)')

# Customize the plot with titles and labels
ax.set_title('Monthly Distribution of Age Groups', fontsize=16)
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Number of People', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add a legend to the plot
ax.legend(title='Age Groups')

# Add grid to the y-axis for better readability of the stacked bars
ax.yaxis.grid(True)

# Show the plot
plt.tight_layout()  # Adjust layout to fit elements
plt.show()