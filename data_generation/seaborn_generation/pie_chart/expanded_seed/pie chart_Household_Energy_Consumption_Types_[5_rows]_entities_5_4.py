
import matplotlib.pyplot as plt
import seaborn as sns

# Given chart data
data = [
    {'Energy Source': 'Natural Gas', 'Percentage': 44},
    {'Energy Source': 'Electricity', 'Percentage': 36},
    {'Energy Source': 'Heating Oil', 'Percentage': 12},
    {'Energy Source': 'Renewable Resources', 'Percentage': 5},
    {'Energy Source': 'Propane', 'Percentage': 3}
]

# Extract 'Energy Source' and 'Percentage' for pie chart
labels = [item['Energy Source'] for item in data]
sizes = [item['Percentage'] for item in data]

# Apply seaborn style
sns.set(style="whitegrid")

# Create a new matplotlib figure and axis object
fig, ax = plt.subplots()

# Create the pie chart with Matplotlib using the seaborn style
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("tab10"))

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Set the title of the plot
plt.title('Energy Source Distribution', pad=20)

# Display the plot
plt.show()