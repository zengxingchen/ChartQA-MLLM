
import matplotlib.pyplot as plt

# Given data
data = [
    {'Year': 2018, 'Member Count': 1200},
    {'Year': 2019, 'Member Count': 1350},
    {'Year': 2020, 'Member Count': 1110},
    {'Year': 2021, 'Member Count': 1500},
    {'Year': 2022, 'Member Count': 1650}
]

# Extracting data for plotting
years = [item['Year'] for item in data]
member_counts = [item['Member Count'] for item in data]

# Create an area chart
plt.fill_between(years, member_counts, color="skyblue", alpha=0.4)

# Add a line chart in the same figure to highlight the area boundaries
plt.plot(years, member_counts, color="Slateblue", alpha=0.6, marker='o')

# Annotate each data point with its value
for i, txt in enumerate(member_counts):
    plt.annotate(txt, (years[i], member_counts[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Set the title and labels
plt.title('Member Count Over Years')
plt.xlabel('Year')
plt.ylabel('Member Count')

# Customize the y-axis grid
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Enhance layout
plt.tight_layout()

# Show the figure
plt.show()