
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Month': 'January', 'Visitors': 1200, 'Books Checked Out': 850, 'eBooks Downloaded': 400, 'Public Computer Use': 300, 'Event Attendance': 150},
    {'Month': 'February', 'Visitors': 1100, 'Books Checked Out': 760, 'eBooks Downloaded': 380, 'Public Computer Use': 280, 'Event Attendance': 140},
    # ... include all the data points provided
    {'Month': 'December', 'Visitors': 1250, 'Books Checked Out': 870, 'eBooks Downloaded': 420, 'Public Computer Use': 310, 'Event Attendance': 150},
    {'Month': 'January(Next Year)', 'Visitors': 1300, 'Books Checked Out': 910, 'eBooks Downloaded': 430, 'Public Computer Use': 330, 'Event Attendance': 160},
    {'Month': 'February(Next Year)', 'Visitors': 1180, 'Books Checked Out': 880, 'eBooks Downloaded': 420, 'Public Computer Use': 325, 'Event Attendance': 158}
]

# Prepare data
months = [d['Month'] for d in data]
visitors = [d['Visitors'] for d in data]
books_checked_out = [d['Books Checked Out'] for d in data]
ebooks_downloaded = [d['eBooks Downloaded'] for d in data]
public_computer_use = [d['Public Computer Use'] for d in data]
event_attendance = [d['Event Attendance'] for d in data]

# Define figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Stacked area chart
ax.stackplot(months, visitors, books_checked_out, ebooks_downloaded, public_computer_use, event_attendance, 
             labels=['Visitors', 'Books Checked Out', 'eBooks Downloaded', 'Public Computer Use', 'Event Attendance'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
             alpha=0.6)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add legend
plt.legend(loc='upper left')

# Add titles and labels
plt.title('Library Usage Statistics by Month')
plt.xlabel('Month')
plt.ylabel('Number of People/Actions')

# Adjust layout to make room for the rotated x-axis labels
plt.tight_layout()

# Show the plot
plt.show()