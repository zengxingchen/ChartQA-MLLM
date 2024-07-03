
import matplotlib.pyplot as plt
from pandas import DataFrame

# Data in a structured form
data = [
    {'Month': 'January', 'Rainfall (inches)': 5.5},
    {'Month': 'February', 'Rainfall (inches)': 3.2},
    {'Month': 'March', 'Rainfall (inches)': 3.7},
    {'Month': 'April', 'Rainfall (inches)': 2.0},
    {'Month': 'May', 'Rainfall (inches)': 1.5},
    {'Month': 'June', 'Rainfall (inches)': 1.1},
    {'Month': 'July', 'Rainfall (inches)': 0.7},
    {'Month': 'August', 'Rainfall (inches)': 0.6},
    {'Month': 'September', 'Rainfall (inches)': 1.5},
    {'Month': 'October', 'Rainfall (inches)': 3.4},
    {'Month': 'November', 'Rainfall (inches)': 6.1},
    {'Month': 'December', 'Rainfall (inches)': 5.8}
]

# Converting data to DataFrame for easier plotting
df = DataFrame(data)

# Set the index to the 'Month' column for plotting
df.set_index('Month', inplace=True)

# Create an area chart
plt.fill_between(df.index, df['Rainfall (inches)'], color="skyblue", alpha=0.4)
plt.plot(df.index, df['Rainfall (inches)'], color="Slateblue", alpha=0.6)

# Beautifications
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.title('Monthly Rainfall (Inches)')  # Chart title
plt.xlabel('Month')  # X-axis label
plt.ylabel('Rainfall (inches)')  # Y-axis label
plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Adding gridlines for readability

# Shading the area under the curve makes it more visually appealing
ax = plt.gca()  # Get current axes
ax.fill_between(df.index, 0, df['Rainfall (inches)'], facecolor="lightblue", alpha=0.3)

# Show the plot
plt.tight_layout()  # Fit the plot within the figure neatly
plt.show()