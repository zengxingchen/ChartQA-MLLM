
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'Month': 'January', "Children's Books": 350, 'Novels': 200, 'Non-Fiction': 150, 'Comics': 100},
    {'Month': 'February', "Children's Books": 400, 'Novels': 180, 'Non-Fiction': 160, 'Comics': 120},
    {'Month': 'March', "Children's Books": 450, 'Novels': 210, 'Non-Fiction': 170, 'Comics': 130},
    {'Month': 'April', "Children's Books": 300, 'Novels': 160, 'Non-Fiction': 180, 'Comics': 110},
    {'Month': 'May', "Children's Books": 500, 'Novels': 220, 'Non-Fiction': 200, 'Comics': 140},
    {'Month': 'June', "Children's Books": 550, 'Novels': 240, 'Non-Fiction': 210, 'Comics': 150},
    {'Month': 'July', "Children's Books": 600, 'Novels': 250, 'Non-Fiction': 220, 'Comics': 160},
    {'Month': 'August', "Children's Books": 650, 'Novels': 260, 'Non-Fiction': 230, 'Comics': 170}
]

# Extracting the month labels for the X-axis
months = [item['Month'] for item in data]

# Extracting the sales data for each book category
childrens_books = [item["Children's Books"] for item in data]
novels = [item['Novels'] for item in data]
non_fiction = [item['Non-Fiction'] for item in data]
comics = [item['Comics'] for item in data]

# Creating line chart
plt.figure(figsize=(10, 7))  # Setting the figure size

plt.plot(months, childrens_books, marker='o', label="Children's Books", linestyle='-', linewidth=2, color='skyblue', markersize=8)
plt.plot(months, novels, marker='s', label='Novels', linestyle='--', linewidth=2, color='olive', markersize=8)
plt.plot(months, non_fiction, marker='^', label='Non-Fiction', linestyle='-.', linewidth=2, color='coral', markersize=8)
plt.plot(months, comics, marker='D', label='Comics', linestyle=':', linewidth=2, color='purple', markersize=8)

# Adding a title and axis labels
plt.title('Monthly Sales Data', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales (units)', fontsize=12)

# Adding a legend to the chart
plt.legend(loc='upper left', frameon=False)

# Setting the grid
plt.grid(True, linestyle='--', alpha=0.5)

# Displaying the chart
plt.tight_layout()  # Adjust layout to fit all components
plt.show()