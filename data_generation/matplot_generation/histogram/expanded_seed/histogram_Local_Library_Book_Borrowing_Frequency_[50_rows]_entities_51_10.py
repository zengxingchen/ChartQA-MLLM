
import matplotlib.pyplot as plt

# Input data
data = [
    {'Day': 'Monday', 'Books Borrowed': 52},
    {'Day': 'Tuesday', 'Books Borrowed': 47},
    {'Day': 'Wednesday', 'Books Borrowed': 63},
    {'Day': 'Thursday', 'Books Borrowed': 58},
    {'Day': 'Friday', 'Books Borrowed': 36},
    {'Day': 'Saturday', 'Books Borrowed': 81},
    {'Day': 'Sunday', 'Books Borrowed': 29},
    {'Day': 'Monday', 'Books Borrowed': 54},
    {'Day': 'Tuesday', 'Books Borrowed': 49},
    {'Day': 'Wednesday', 'Books Borrowed': 65},
    {'Day': 'Thursday', 'Books Borrowed': 59},
    {'Day': 'Friday', 'Books Borrowed': 38},
    {'Day': 'Saturday', 'Books Borrowed': 83},
    {'Day': 'Sunday', 'Books Borrowed': 31},
    {'Day': 'Monday', 'Books Borrowed': 56}
]

# Aggregating the total books borrowed for each day
books_per_day = {}
for entry in data:
    if entry['Day'] in books_per_day:
        books_per_day[entry['Day']] += entry['Books Borrowed']
    else:
        books_per_day[entry['Day']] = entry['Books Borrowed']

# Sorting the data by days of the week for consistent ordering
sorted_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sorted_books_borrowed = [books_per_day[day] for day in sorted_days]

# Creating the histogram
plt.figure(figsize=(10, 6))  # Set the figure size
plt.bar(sorted_days, sorted_books_borrowed, color='skyblue')  # Create a bar chart

# Adding titles and labels
plt.title('Total Books Borrowed Each Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Total Books Borrowed')

# Customize the y-axis to show the actual number of books borrowed
plt.yticks(range(0, max(sorted_books_borrowed) + 10, 10))  # Assuming the maximum is round up to the nearest ten

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add numerical labels on top of each bar
for i, value in enumerate(sorted_books_borrowed):
    plt.text(i, value + 2, str(value), ha='center')

# Show the plot
plt.show()