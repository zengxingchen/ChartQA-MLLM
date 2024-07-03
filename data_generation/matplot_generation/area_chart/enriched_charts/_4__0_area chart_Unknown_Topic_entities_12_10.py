
import matplotlib.pyplot as plt

# Data
years = range(2010, 2022)
novels_published = [200, 220, 250, 280, 310, 350, 400, 450, 500, 550, 600, 650]
poetry_books = [150, 160, 170, 180, 190, 210, 230, 250, 270, 300, 330, 360]
short_stories = [300, 320, 350, 370, 400, 430, 460, 500, 540, 580, 620, 660]

# Plot
fig, ax = plt.subplots(figsize=(14, 10))

# Plotting the area chart
ax.fill_between(years, novels_published, color="#8A2BE2", alpha=0.6, label='Novels Published')
ax.fill_between(years, poetry_books, color="#DC143C", alpha=0.6, label='Poetry Books')
ax.fill_between(years, short_stories, color="#20B2AA", alpha=0.6, label='Short Stories')

# Titles and labels
ax.set_title('Literature & Writing: Publications from 2010 to 2021', fontsize=18, pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Publications', fontsize=14)

# Customizing the y-axis to get a better understanding of scales
ax.set_yscale('linear')

# Legend
ax.legend(loc='upper left')

# Annotations
ax.annotate('Increase in novels', xy=(2015, 350), xytext=(2013, 400),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
ax.annotate('Steady rise in poetry books', xy=(2018, 270), xytext=(2015, 310),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.show()