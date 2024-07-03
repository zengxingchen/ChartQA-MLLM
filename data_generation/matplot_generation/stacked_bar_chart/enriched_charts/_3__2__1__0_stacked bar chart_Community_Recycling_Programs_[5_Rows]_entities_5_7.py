
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
research_papers = [800, 950, 1100, 1300, 1500, 1800, 2100]
books_published = [300, 350, 400, 450, 500, 550, 600]
magazines = [150, 200, 250, 300, 350, 400, 450]

# Bottom data for stacking
books_published_bottom = research_papers
magazines_bottom = [i + j for i, j in zip(research_papers, books_published)]

# Figure and Axes
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked Bars
ax.bar(years, research_papers, color='#4b8bbe', edgecolor='white', width=0.5, label='Research Papers')
ax.bar(years, books_published, bottom=books_published_bottom, color='#d9534f', edgecolor='white', width=0.5, label='Books Published')
ax.bar(years, magazines, bottom=magazines_bottom, color='#5cb85c', edgecolor='white', width=0.5, label='Magazines')

# Labels and Title
ax.set_ylabel('Number of Publications')
ax.set_xlabel('Year')
ax.set_title('Annual Publications Overview (2015-2021)', pad=20)

# Adding numerical labels
for i in range(len(years)):
    ax.text(i, research_papers[i] / 2, str(research_papers[i]), va='center', ha='center', color='white', fontsize=8, fontweight='bold')
    ax.text(i, books_published_bottom[i] + (books_published[i] / 2), str(books_published[i]), va='center', ha='center', color='white', fontsize=8, fontweight='bold')
    ax.text(i, magazines_bottom[i] + (magazines[i] / 2), str(magazines[i]), va='center', ha='center', color='white', fontsize=8, fontweight='bold')

# Legend
ax.legend(loc='upper left')

# Display the plot
plt.show()