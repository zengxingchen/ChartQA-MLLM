
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the chart table data
data = [
    {'Month': 'January 2023', 'New Members': 50, 'Membership Cancellations': 30},
    {'Month': 'February 2023', 'New Members': 45, 'Membership Cancellations': 25},
    {'Month': 'March 2023', 'New Members': 60, 'Membership Cancellations': 20},
    {'Month': 'April 2023', 'New Members': 70, 'Membership Cancellations': 15},
    {'Month': 'May 2023', 'New Members': 80, 'Membership Cancellations': 40},
    {'Month': 'June 2023', 'New Members': 75, 'Membership Cancellations': 35},
    {'Month': 'July 2023', 'New Members': 85, 'Membership Cancellations': 25},
    {'Month': 'August 2023', 'New Members': 90, 'Membership Cancellations': 20},
    {'Month': 'September 2023', 'New Members': 95, 'Membership Cancellations': 18},
    {'Month': 'October 2023', 'New Members': 100, 'Membership Cancellations': 15},
    {'Month': 'November 2023', 'New Members': 110, 'Membership Cancellations': 10},
    {'Month': 'December 2023', 'New Members': 120, 'Membership Cancellations': 12}
]

df = pd.DataFrame(data)

# Convert the 'Month' column to datetime to make sure the plot is in the correct order
df['Month'] = pd.to_datetime(df['Month'])

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the line plot for "New Members"
sns.lineplot(data=df, x='Month', y='New Members', label='New Members', 
             color='blue', linestyle='-', marker='o')

# Create the line plot for "Membership Cancellations"
sns.lineplot(data=df, x='Month', y='Membership Cancellations', label='Membership Cancellations', 
             color='red', linestyle='--', marker='x')

# Improve the readability of the x-axis labels
plt.xticks(rotation=45)

# Setting the plot title and labels
plt.title('Monthly New Members and Membership Cancellations in 2023')
plt.xlabel('Month')
plt.ylabel('Count')

# Display the legend
plt.legend()

# Adjust plot to ensure the x-axis date labels fit well
plt.tight_layout()

# Show the plot
plt.show()