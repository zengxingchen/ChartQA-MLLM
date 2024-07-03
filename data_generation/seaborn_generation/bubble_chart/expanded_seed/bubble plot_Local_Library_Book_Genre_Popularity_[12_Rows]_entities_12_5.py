
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data provided
data = [
    {'Genre': 'Mystery', 'Month': 'January', 'Checkouts': 220, 'New Memberships': 30, 'Average Reading Time (Hours)': 5.2},
    {'Genre': 'Science Fiction', 'Month': 'January', 'Checkouts': 180, 'New Memberships': 24, 'Average Reading Time (Hours)': 6.5},
    {'Genre': 'Romance', 'Month': 'January', 'Checkouts': 240, 'New Memberships': 21, 'Average Reading Time (Hours)': 4.1},
    {'Genre': 'History', 'Month': 'January', 'Checkouts': 300, 'New Memberships': 15, 'Average Reading Time (Hours)': 7.0},
    {'Genre': 'Biography', 'Month': 'January', 'Checkouts': 150, 'New Memberships': 12, 'Average Reading Time (Hours)': 5.5},
    {'Genre': 'Fantasy', 'Month': 'January', 'Checkouts': 270, 'New Memberships': 35, 'Average Reading Time (Hours)': 6.2},
    {'Genre': 'Mystery', 'Month': 'February', 'Checkouts': 250, 'New Memberships': 28, 'Average Reading Time (Hours)': 5.5},
    {'Genre': 'Science Fiction', 'Month': 'February', 'Checkouts': 190, 'New Memberships': 20, 'Average Reading Time (Hours)': 6.8},
    {'Genre': 'Romance', 'Month': 'February', 'Checkouts': 200, 'New Memberships': 18, 'Average Reading Time (Hours)': 3.9},
    {'Genre': 'History', 'Month': 'February', 'Checkouts': 320, 'New Memberships': 16, 'Average Reading Time (Hours)': 7.5},
    {'Genre': 'Biography', 'Month': 'February', 'Checkouts': 160, 'New Memberships': 10, 'Average Reading Time (Hours)': 5.0},
    {'Genre': 'Fantasy', 'Month': 'February', 'Checkouts': 290, 'New Memberships': 40, 'Average Reading Time (Hours)': 6.3}
]

# Converting the data into a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(12, 6))

# Bubble sizes are better to be scaled, this avoids very small or large bubbles
bubble_size_factor = 10
df['Scaled Checkouts'] = df['Checkouts'] / bubble_size_factor

# Create the bubble chart using seaborn's scatterplot() method
bubble_chart = sns.scatterplot(
    data=df,
    x="Genre", 
    y="New Memberships",
    size="Scaled Checkouts", 
    hue="Average Reading Time (Hours)", 
    sizes=(20, 800),  # Control the range of bubble sizes
    alpha=0.6,  # Transparency of bubbles
    palette="coolwarm",  # Color palette for hue
    legend='full'
)

# Adjust the legend for bubble sizes
h, l = bubble_chart.get_legend_handles_labels()
legend_sizes = df['Checkouts'].drop_duplicates().sort_values().tolist()
legend_scaled_sizes = [x / bubble_size_factor for x in legend_sizes]

# This custom legend shows the actual 'Checkouts' numbers
for i in range(len(legend_sizes)):
    l[i+1] = str(legend_sizes[i])

plt.legend(h[0:len(legend_sizes)+1], l[0:len(legend_sizes)+1], title="Checkouts", borderaxespad=1)

# Set labels and title
plt.xlabel("Genre")
plt.ylabel("New Memberships")
plt.title("Library Genre Popularity and Reading Time")

# Show the plot
plt.tight_layout()
plt.show()