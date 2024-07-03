
import matplotlib.pyplot as plt

# Data
years = list(range(2001, 2021))
cbt = [1.2, 1.5, 1.8, 2.1, 2.5, 2.9, 3.4, 3.9, 4.5, 5.0, 5.6, 6.2, 6.9, 7.5, 8.2, 8.9, 9.6, 10.4, 11.1, 11.9]
art_therapy = [0.5, 0.7, 0.8, 0.9, 1.0, 1.2, 1.5, 1.8, 2.1, 2.5, 2.8, 3.2, 3.6, 4.0, 4.4, 4.8, 5.2, 5.7, 6.2, 6.7]
music_therapy = [0.3, 0.5, 0.7, 0.9, 1.1, 1.4, 1.7, 2.0, 2.4, 2.7, 3.0, 3.3, 3.7, 4.1, 4.5, 4.9, 5.4, 5.9, 6.4, 7.0]

# Plotting the stacked area chart
plt.figure(figsize=(14, 9))  # Change the size of the chart (width, height)
plt.stackplot(years, cbt, art_therapy, music_therapy, colors=['#FF5733', '#33FFCE', '#335BFF'])

# Annotations
for year, cb, at, mt in zip(years, cbt, art_therapy, music_therapy):
    plt.text(year, cb/2, f"{cb}", va='center', ha='center', color='black', fontsize=8)
    plt.text(year, cb + at/2, f"{at}", va='center', ha='center', color='black', fontsize=8)
    plt.text(year, cb + at + mt/2, f"{mt}", va='center', ha='center', color='black', fontsize=8)

# Titles and labels
plt.title('Trends in Therapy Sessions (2001-2020)', fontsize=16, loc='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Sessions (Millions)', fontsize=12)

# Customize the legend
plt.legend(['CBT', 'Art Therapy', 'Music Therapy'], loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()