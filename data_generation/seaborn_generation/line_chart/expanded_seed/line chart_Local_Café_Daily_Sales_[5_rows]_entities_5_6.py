
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given table data
data = [
    {'Date': '2023-03-01', 'Number of Coffees Sold': 157, 'Number of Pastries Sold': 134},
    {'Date': '2023-03-02', 'Number of Coffees Sold': 165, 'Number of Pastries Sold': 145},
    {'Date': '2023-03-03', 'Number of Coffees Sold': 172, 'Number of Pastries Sold': 138},
    {'Date': '2023-03-04', 'Number of Coffees Sold': 180, 'Number of Pastries Sold': 150},
    {'Date': '2023-03-05', 'Number of Coffees Sold': 190, 'Number of Pastries Sold': 160}
]

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime for proper plotting
df['Date'] = pd.to_datetime(df['Date'])

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the line plot
plt.figure(figsize=(10, 6))

# Plot the "Number of Coffees Sold" line
sns.lineplot(data=df, x='Date', y='Number of Coffees Sold', label='Coffees Sold', 
             color="blue", marker="o", linestyle='-', linewidth=2.5)

# Plot the "Number of Pastries Sold" line
sns.lineplot(data=df, x='Date', y='Number of Pastries Sold', label='Pastries Sold', 
             color="green", marker="s", linestyle='--', linewidth=2.5)

# Customize the plot with titles and labels
plt.title('Number of Coffees and Pastries Sold in March 2023', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number Sold', fontsize=14)
plt.xticks(rotation=45) # Rotate the x-axis labels for better readability

# At this point, seaborn automatically adds a legend. 
# But in case you want to customize it further, you can use the following:
plt.legend(title='Items Sold')

# Show the plot
plt.tight_layout() # Adjust layout for better fit
plt.show() # This will display the plot in a window