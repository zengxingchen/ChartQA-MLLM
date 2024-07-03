
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Month': 'January', 'Paintings': 120, 'Sculptures': 80, 'Installations': 50, 'Digital Art': 90, 'Photography': 60},
    {'Month': 'February', 'Paintings': 115, 'Sculptures': 85, 'Installations': 55, 'Digital Art': 92, 'Photography': 65},
    {'Month': 'March', 'Paintings': 130, 'Sculptures': 70, 'Installations': 60, 'Digital Art': 88, 'Photography': 70},
    {'Month': 'April', 'Paintings': 125, 'Sculptures': 78, 'Installations': 62, 'Digital Art': 95, 'Photography': 75},
    {'Month': 'May', 'Paintings': 140, 'Sculptures': 82, 'Installations': 65, 'Digital Art': 100, 'Photography': 80},
    {'Month': 'June', 'Paintings': 135, 'Sculptures': 85, 'Installations': 68, 'Digital Art': 105, 'Photography': 85},
    {'Month': 'July', 'Paintings': 145, 'Sculptures': 90, 'Installations': 70, 'Digital Art': 110, 'Photography': 88},
    {'Month': 'August', 'Paintings': 150, 'Sculptures': 88, 'Installations': 75, 'Digital Art': 115, 'Photography': 90},
    {'Month': 'September', 'Paintings': 155, 'Sculptures': 92, 'Installations': 78, 'Digital Art': 118, 'Photography': 95},
    {'Month': 'October', 'Paintings': 160, 'Sculptures': 95, 'Installations': 80, 'Digital Art': 120, 'Photography': 100},
    {'Month': 'November', 'Paintings': 158, 'Sculptures': 93, 'Installations': 77, 'Digital Art': 117, 'Photography': 98},
    {'Month': 'December', 'Paintings': 165, 'Sculptures': 98, 'Installations': 82, 'Digital Art': 122, 'Photography': 105}
]

# Extracting months
months = [record['Month'] for record in data]

# Extracting data for each type of art
paintings = [record['Paintings'] for record in data]
sculptures = [record['Sculptures'] for record in data]
installations = [record['Installations'] for record in data]
digital_art = [record['Digital Art'] for record in data]
photography = [record['Photography'] for record in data]

# Start plotting
plt.figure(figsize=(16, 10))

# Plotting each type of art
plt.plot(months, paintings, label='Paintings', marker='o', linestyle='-', color='#1e90ff')
plt.plot(months, sculptures, label='Sculptures', marker='X', linestyle='--', color='#ff6347')
plt.plot(months, installations, label='Installations', marker='^', linestyle='-.', color='#32cd32')
plt.plot(months, digital_art, label='Digital Art', marker='s', linestyle=':', color='#8a2be2')
plt.plot(months, photography, label='Photography', marker='D', linestyle='-', color='#ffa500')

# Adding titles and labels
plt.title('Monthly Sales of Artworks in Various Categories', pad=20)
plt.xlabel('Month')
plt.ylabel('Sales (Units)')

# Add a legend
plt.legend(loc='upper right')

# Annotate a specific data point
plt.annotate('Highest Sales', xy=('December', 165), xytext=('November', 170),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()