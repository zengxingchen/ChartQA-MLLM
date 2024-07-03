
import matplotlib.pyplot as plt

# Data
data = [
    {'Year': 2017, 'Adults_Attendance': 3200, 'Youths_Attendance': 1500, 'Total_Books_Checked_Out': 7800, 'Population': 15000},
    {'Year': 2018, 'Adults_Attendance': 3100, 'Youths_Attendance': 1600, 'Total_Books_Checked_Out': 8000, 'Population': 15200},
    {'Year': 2019, 'Adults_Attendance': 3300, 'Youths_Attendance': 1700, 'Total_Books_Checked_Out': 8150, 'Population': 15500},
    {'Year': 2020, 'Adults_Attendance': 2950, 'Youths_Attendance': 1100, 'Total_Books_Checked_Out': 4250, 'Population': 15700},
    {'Year': 2021, 'Adults_Attendance': 3050, 'Youths_Attendance': 1200, 'Total_Books_Checked_Out': 6450, 'Population': 15800}
]

# Prepare data for plotting
years = [d['Year'] for d in data]
adults_attendance = [d['Adults_Attendance'] for d in data]
youths_attendance = [d['Youths_Attendance'] for d in data]
books_checked_out = [d['Total_Books_Checked_Out'] for d in data]
population = [d['Population'] for d in data]

# Normalize books_checked_out for bubble sizes
max_books = max(books_checked_out)
bubble_sizes = [(x / max_books) * 1000 for x in books_checked_out]

# Normalize population for color map
max_population = max(population)
min_population = min(population)
population_norm = [(x - min_population) / (max_population - min_population) for x in population]

# Create bubble chart
plt.scatter(years, adults_attendance, s=bubble_sizes, c=population_norm, cmap='viridis', alpha=0.6, edgecolors='w', linewidth=0.5)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Adults Attendance')
plt.title('Library Attendance and Book Check-outs Over Time')
plt.colorbar(label='Population (normalized)')

# Additional customization
for i, txt in enumerate(years):
    plt.annotate(txt, (years[i], adults_attendance[i]))

# Display the plot
plt.tight_layout()
plt.show()