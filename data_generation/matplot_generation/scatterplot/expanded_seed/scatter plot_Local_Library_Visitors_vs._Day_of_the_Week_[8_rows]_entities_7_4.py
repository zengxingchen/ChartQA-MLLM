
import matplotlib.pyplot as plt

# Data
data = [
    {'Day of the Week': 'Monday', 'Average Visitors': 75, 'Average Books Checked Out': 120},
    {'Day of the Week': 'Tuesday', 'Average Visitors': 50, 'Average Books Checked Out': 80},
    {'Day of the Week': 'Wednesday', 'Average Visitors': 60, 'Average Books Checked Out': 95},
    {'Day of the Week': 'Thursday', 'Average Visitors': 80, 'Average Books Checked Out': 140},
    {'Day of the Week': 'Friday', 'Average Visitors': 90, 'Average Books Checked Out': 160},
    {'Day of the Week': 'Saturday', 'Average Visitors': 200, 'Average Books Checked Out': 300},
    {'Day of the Week': 'Sunday', 'Average Visitors': 180, 'Average Books Checked Out': 250}
]

# Extracting information for plotting
days_of_week = [entry['Day of the Week'] for entry in data]
visitors = [entry['Average Visitors'] for entry in data]
books_checked_out = [entry['Average Books Checked Out'] for entry in data]

# Size based on visitors (scaled to be more visually appealing)
sizes = [v * 5 for v in visitors]

# Colors (unique for each day of the week)
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink']

# Creating scatterplot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(visitors, books_checked_out, s=sizes, c=colors, alpha=0.7)

# Annotating each point with the day of the week
for i, txt in enumerate(days_of_week):
    plt.annotate(txt, (visitors[i], books_checked_out[i]))

# Adding chart details
plt.title('Library Traffic: Average Visitors vs. Average Books Checked Out')
plt.xlabel('Average Visitors')
plt.ylabel('Average Books Checked Out')

# Setting the legend to show the days of the week
legend_labels = days_of_week
legend_scatter = plt.scatter(visitors, books_checked_out, s=0)  # Dummy scatter for legend
plt.legend(handles=legend_scatter.legend_elements()[0], labels=legend_labels, title="Days of the Week")

# Displaying the scatterplot
plt.grid(True)
plt.tight_layout()
plt.show()