
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = [
    {'Month': 'January', 'Total Rides': 6720, 'Subscribed Users': 4400, 'Casual Users': 2320, 'Average Ride Duration(minutes)': 15},
    {'Month': 'February', 'Total Rides': 6890, 'Subscribed Users': 4500, 'Casual Users': 2390, 'Average Ride Duration(minutes)': 14},
    {'Month': 'March', 'Total Rides': 10450, 'Subscribed Users': 6987, 'Casual Users': 3463, 'Average Ride Duration(minutes)': 18},
    {'Month': 'April', 'Total Rides': 15230, 'Subscribed Users': 10325, 'Casual Users': 4905, 'Average Ride Duration(minutes)': 22},
    {'Month': 'May', 'Total Rides': 17025, 'Subscribed Users': 11597, 'Casual Users': 5428, 'Average Ride Duration(minutes)': 24},
    {'Month': 'June', 'Total Rides': 19075, 'Subscribed Users': 12800, 'Casual Users': 6280, 'Average Ride Duration(minutes)': 27},
    {'Month': 'July', 'Total Rides': 20790, 'Subscribed Users': 13865, 'Casual Users': 6925, 'Average Ride Duration(minutes)': 29},
    {'Month': 'August', 'Total Rides': 21500, 'Subscribed Users': 14500, 'Casual Users': 7000, 'Average Ride Duration(minutes)': 30},
    {'Month': 'September', 'Total Rides': 19870, 'Subscribed Users': 13460, 'Casual Users': 6410, 'Average Ride Duration(minutes)': 26},
    {'Month': 'October', 'Total Rides': 15200, 'Subscribed Users': 10290, 'Casual Users': 4910, 'Average Ride Duration(minutes)': 22},
    {'Month': 'November', 'Total Rides': 11840, 'Subscribed Users': 8000, 'Casual Users': 3840, 'Average Ride Duration(minutes)': 17},
    {'Month': 'December', 'Total Rides': 7510, 'Subscribed Users': 5150, 'Casual Users': 2360, 'Average Ride Duration(minutes)': 14}
]

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Plotting
# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the plot
plt.figure(figsize=(12, 8))

# Stacked bar chart for Subscribed Users and Casual Users
bottom_bar = sns.barplot(x='Month', y='Subscribed Users', data=df, color='skyblue', label='Subscribed Users')
top_bar = sns.barplot(x='Month', y='Total Rides', data=df, color='navy', label='Casual Users')

# Add a legend
plt.legend()

# Secondary Y-axis for Average Ride Duration
ax2 = plt.twinx()
sns.lineplot(data=df, x='Month', y='Average Ride Duration(minutes)', ax=ax2, color='green', marker="o", label='Average Ride Duration')

# Add labels for the axes and title
bottom_bar.set_xlabel('Month', fontsize=14)
bottom_bar.set_ylabel('Number of Rides', fontsize=14)
ax2.set_ylabel('Average Ride Duration (minutes)', fontsize=14)
plt.title('Monthly Ride Statistics', fontsize=16)

# Customize the tick labels on the primary y-axis
plt.yticks(fontsize=12)
ax2.yaxis.label.set_color('green')
ax2.tick_params(axis='y', colors='green')

# Show plot with grid
plt.grid(True)
plt.show()