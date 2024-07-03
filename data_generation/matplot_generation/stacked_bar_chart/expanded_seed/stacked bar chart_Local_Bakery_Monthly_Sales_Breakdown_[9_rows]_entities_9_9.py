
import matplotlib.pyplot as plt

# Sample data
data = [
    {'Month': 'January', ' Bread (units)': 1200, ' Cakes (units)': 300, ' Pastries (units)': 450, ' Pies (units)': 200},
    {'Month': 'February', ' Bread (units)': 1150, ' Cakes (units)': 320, ' Pastries (units)': 460, ' Pies (units)': 210},
    {'Month': 'March', ' Bread (units)': 1300, ' Cakes (units)': 350, ' Pastries (units)': 470, ' Pies (units)': 220},
    {'Month': 'April', ' Bread (units)': 1280, ' Cakes (units)': 370, ' Pastries (units)': 480, ' Pies (units)': 230},
    {'Month': 'May', ' Bread (units)': 1350, ' Cakes (units)': 400, ' Pastries (units)': 490, ' Pies (units)': 240},
    {'Month': 'June', ' Bread (units)': 1400, ' Cakes (units)': 420, ' Pastries (units)': 500, ' Pies (units)': 250},
    {'Month': 'July', ' Bread (units)': 1450, ' Cakes (units)': 430, ' Pastries (units)': 510, ' Pies (units)': 260},
    {'Month': 'August', ' Bread (units)': 1500, ' Cakes (units)': 440, ' Pastries (units)': 520, ' Pies (units)': 270},
    {'Month': 'September', ' Bread (units)': 1550, ' Cakes (units)': 450, ' Pastries (units)': 530, ' Pies (units)': 280}
]

# Extracting data
months = [item['Month'] for item in data]
bread_units = [item[' Bread (units)'] for item in data]
cakes_units = [item[' Cakes (units)'] for item in data]
pastries_units = [item[' Pastries (units)'] for item in data]
pies_units = [item[' Pies (units)'] for item in data]

# Stacking values for the stacked bar chart
bars_bread = bread_units
bars_cakes = [i + j for i, j in zip(bread_units, cakes_units)]
bars_pastries = [i + j for i, j in zip(bars_cakes, pastries_units)]
bars_pies = [i + j for i, j in zip(bars_pastries, pies_units)]

# Create the figure and the bar chart
fig, ax = plt.subplots(figsize=(10, 7))

# Plotting the bars
ax.bar(months, bars_bread, color='brown', edgecolor='white', label='Bread')
ax.bar(months, cakes_units, bottom=bread_units, color='pink', edgecolor='white', label='Cakes')
ax.bar(months, pastries_units, bottom=bars_cakes, color='orange', edgecolor='white', label='Pastries')
ax.bar(months, pies_units, bottom=bars_pastries, color='yellow', edgecolor='white', label='Pies')

# Adding labels and title
ax.set_xlabel('Months', fontweight='bold')
ax.set_ylabel('Units Sold', fontweight='bold')
ax.set_title('Monthly Sales Data (Units Sold)', fontweight='bold')

# Add legend
ax.legend()

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()