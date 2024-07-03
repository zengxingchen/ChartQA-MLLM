
import matplotlib.pyplot as plt

# Given table data
data = [
    {'Age Group': '0-12', 'Number of Books Checked Out': 450, 'Visitors': 300},
    {'Age Group': '13-18', 'Number of Books Checked Out': 550, 'Visitors': 200},
    {'Age Group': '19-24', 'Number of Books Checked Out': 300, 'Visitors': 150},
    {'Age Group': '25-34', 'Number of Books Checked Out': 400, 'Visitors': 220},
    {'Age Group': '35-44', 'Number of Books Checked Out': 380, 'Visitors': 180},
    {'Age Group': '45-54', 'Number of Books Checked Out': 420, 'Visitors': 190},
    {'Age Group': '55-64', 'Number of Books Checked Out': 390, 'Visitors': 210},
    {'Age Group': '65+', 'Number of Books Checked Out': 360, 'Visitors': 230}
]

# Extract the required information for plotting
age_groups = [entry['Age Group'] for entry in data]
books_checked_out = [entry['Number of Books Checked Out'] for entry in data]
visitors = [entry['Visitors'] for entry in data]

# Create the scatter plot using diversified visual encoding
plt.figure(figsize=(10, 6))
scatter = plt.scatter(books_checked_out, visitors, alpha=0.6, 
                      c=range(len(age_groups)), cmap='viridis', 
                      s=[n / 2 for n in books_checked_out])  # Use number of books to determine size

# Add a color bar for the age groups
cbar = plt.colorbar(scatter)
cbar.set_label('Age Group Index')
cbar.set_ticks(range(len(age_groups)))
cbar.set_ticklabels(age_groups)

# Add labels and title
plt.xlabel('Number of Books Checked Out')
plt.ylabel('Visitors')
plt.title('Library Data: Number of Books Checked Out vs. Visitors by Age Group')

# Show grid
plt.grid(True)

# Show the plot
plt.show()