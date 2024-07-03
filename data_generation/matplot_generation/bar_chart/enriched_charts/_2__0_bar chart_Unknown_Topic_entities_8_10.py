
import matplotlib.pyplot as plt

# Data
events = [
    'Open Mic Night', 'Book Reading', 'Comedy Show', 'Theater Play', 
    'Dance Performance', 'Jazz Concert', 'Poetry Slam', 'Art Exhibition', 
    'Film Screening', 'Music Festival', 'Circus Show', 'Magic Show'
]
attendees = [75, 45, 60, 90, 80, 85, 55, 70, 65, 120, 110, 50]

# Plotting the bar chart
plt.figure(figsize=(12, 7))
plt.bar(events, attendees, width=0.6, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
    '#bcbd22', '#17becf', '#9edae5', '#f7b6d2'
])

# Customizing the plot
plt.ylabel('Number of Attendees')
plt.title('Event Attendance Statistics')
plt.ylim(0, 130)

# Show the plot
plt.show()