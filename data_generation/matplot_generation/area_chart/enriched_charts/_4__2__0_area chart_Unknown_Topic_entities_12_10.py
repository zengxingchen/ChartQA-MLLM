
import matplotlib.pyplot as plt

# Data
years = range(2010, 2031)
art_gallery_visits = [1500, 1700, 1900, 2100, 2500, 2800, 3200, 3700, 4300, 5000, 5800, 6700, 7700, 8900, 10300, 11900, 13700, 15700, 18000, 20500, 23200]

# Plot
fig, ax = plt.subplots(figsize=(16, 12))

# Plotting the area chart
ax.fill_between(years, art_gallery_visits, color="#FF6347", alpha=0.7, label='Art Gallery Visits')

# Titles and labels
ax.set_title('Annual Art Gallery Visits from 2010 to 2030', fontsize=18, pad=20)
ax.set_xlabel('Year', fontsize=15)
ax.set_ylabel('Number of Visits', fontsize=15)

# Customizing the y-axis to get a better understanding of scales
ax.set_yscale('linear')

# Annotation
for i, txt in enumerate(art_gallery_visits):
    ax.annotate(txt, (years[i], art_gallery_visits[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Legend
ax.legend(loc='upper left')

plt.show()