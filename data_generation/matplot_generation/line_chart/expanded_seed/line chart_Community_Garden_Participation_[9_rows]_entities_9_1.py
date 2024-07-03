
import matplotlib.pyplot as plt

# Data provided in the table
data = [
    {'Month': 'January', 'Participants': 12, 'Location': 'Parkside'},
    {'Month': 'February', 'Participants': 15, 'Location': 'Parkside'},
    {'Month': 'March', 'Participants': 20, 'Location': 'Parkside'},
    {'Month': 'April', 'Participants': 25, 'Location': 'Parkside'},
    {'Month': 'May', 'Participants': 30, 'Location': 'Parkside'},
    {'Month': 'June', 'Participants': 27, 'Location': 'Parkside'},
    {'Month': 'July', 'Participants': 26, 'Location': 'Parkside'},
    {'Month': 'August', 'Participants': 28, 'Location': 'Parkside'},
    {'Month': 'September', 'Participants': 22, 'Location': 'Parkside'}
]

# Extracting the months and the number of participants
months = [entry['Month'] for entry in data]
participants = [entry['Participants'] for entry in data]

# Creating the line chart
plt.figure(figsize=(10, 6))  # Setting the figure size

# Plotting the data with various visual encodings
plt.plot(months, participants, color='blue', linestyle='-', linewidth=2, 
         marker='o', markersize=6, markerfacecolor='red', markeredgewidth=2, 
         markeredgecolor='black', label='Participants at Parkside')

# Adding titles and labels
plt.title('Monthly Participants at Parkside')
plt.xlabel('Month')
plt.ylabel('Number of Participants')

# Adding a legend
plt.legend()

# Adding a grid
plt.grid(True)

# Adding customization with font size and style for x and y ticks
plt.xticks(fontsize=9, fontweight='bold', rotation=45)
plt.yticks(fontsize=9, fontweight='bold')

# Show plot
plt.show()