
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

# The provided chart table data
data = [
    {'Month': '2023-01', 'New_Books': 120},
    {'Month': '2023-02', 'New_Books': 135},
    {'Month': '2023-03', 'New_Books': 110},
    {'Month': '2023-04', 'New_Books': 150},
    {'Month': '2023-05', 'New_Books': 165},
    {'Month': '2023-06', 'New_Books': 140},
    {'Month': '2023-07', 'New_Books': 155},
    {'Month': '2023-08', 'New_Books': 130},
    {'Month': '2023-09', 'New_Books': 180},
    {'Month': '2023-10', 'New_Books': 175},
    {'Month': '2023-11', 'New_Books': 160},
    {'Month': '2023-12', 'New_Books': 190}
]

# Convert string dates to datetime and extract New_Books values
dates = [datetime.strptime(d['Month'], "%Y-%m") for d in data]
new_books = [d['New_Books'] for d in data]

fig, ax = plt.subplots(figsize=(10, 6))  # Create figure and axes with a specified size

# Plot area chart
ax.fill_between(dates, new_books, color="skyblue", alpha=0.4)
ax.plot(dates, new_books, color="Slateblue", alpha=0.6, linewidth=2)

# Highlight the data points with markers
ax.plot(dates, new_books, 'o', color="DarkSlateblue")

# Set the title and labels
ax.set_title("New Books Added Each Month in 2023", fontsize=16)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Number of New Books", fontsize=14)

# Improve formatting of the x-axis dates
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))  # Set major ticks interval to 1 month
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))  # Set major ticks format
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Add grid lines and set limits
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.set_xlim(min(dates), max(dates))  # Set the x-axis limits to min and max dates

# Annotate the highest point on the plot
max_books_idx = np.argmax(new_books)
ax.annotate(f'Max: {new_books[max_books_idx]}',
            xy=(dates[max_books_idx], new_books[max_books_idx]),
            xytext=(dates[max_books_idx], new_books[max_books_idx] + 10),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Show plot
plt.tight_layout()
plt.show()