
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Month': 'January', "Children's Books (borrows)": 450, 'Young Adult (borrows)': 350, 'Adult Fiction (borrows)': 300, 'Adult Non-fiction (borrows)': 200, 'Total Visitors': 2000, 'Location': 'Springfield'},
    # ... (Include the rest of the months data here)
    {'Month': 'December', "Children's Books (borrows)": 500, 'Young Adult (borrows)': 370, 'Adult Fiction (borrows)': 320, 'Adult Non-fiction (borrows)': 295, 'Total Visitors': 2400, 'Location': 'Springfield'}
]

# Prepare data for plotting
months = [entry['Month'] for entry in data]
childrens_books_borrows = [entry["Children's Books (borrows)"] for entry in data]
young_adult_borrows = [entry['Young Adult (borrows)'] for entry in data]
adult_fiction_borrows = [entry['Adult Fiction (borrows)'] for entry in data]
adult_non_fiction_borrows = [entry['Adult Non-fiction (borrows)'] for entry in data]
total_visitors = [entry['Total Visitors'] for entry in data]

# Calculate total borrows for the color of the bubbles
total_borrows = [children + ya + fiction + non_fiction for children, ya, fiction, non_fiction in zip(childrens_books_borrows, young_adult_borrows, adult_fiction_borrows, adult_non_fiction_borrows)]

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Create bubble plot
bubble = ax.scatter(months, total_borrows, s=total_visitors, c=total_borrows, cmap='viridis', alpha=0.6, edgecolors='w', linewidth=0.5)

# Create a color bar
cbar = plt.colorbar(bubble)
cbar.set_label('Total Borrows')

# Label axis
ax.set_xlabel('Month')
ax.set_ylabel('Total Borrows')
ax.set_title('Library Usage Statistics (Bubble Size Represents Total Visitors)')

# Show grid
plt.grid(True)

# Rotate the x-axis month labels for better readability
plt.xticks(rotation=45)

# Include total visitor count in the bubbles
for i in range(len(months)):
    ax.text(months[i], total_borrows[i], total_visitors[i], ha='center', va='center', fontsize=9)

# Show the plot
plt.show()