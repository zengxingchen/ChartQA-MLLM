
import matplotlib.pyplot as plt

# Data
countries = ['USA', 'UK', 'Germany', 'France', 'Japan', 'China']
research_papers = [300, 250, 200, 180, 220, 270]
book_publications = [280, 220, 190, 160, 200, 250]
online_articles = [260, 210, 180, 150, 190, 240]

# Color codes for each type of publication
colors = ['#FF5733', '#33FF57', '#3357FF']

# Plot stacked horizontal bar chart
plt.figure(figsize=(10, 8)) # Width and height of the chart in inches
bar_height = 0.6 # Height of the bars

plt.barh(countries, research_papers, color=colors[0], edgecolor='white', height=bar_height, label='Research Papers')
plt.barh(countries, book_publications, left=research_papers, color=colors[1], edgecolor='white', height=bar_height, label='Book Publications')
plt.barh(countries, online_articles, left=[i+j for i,j in zip(research_papers, book_publications)], color=colors[2], edgecolor='white', height=bar_height, label='Online Articles')

# Add numerical labels
for i in range(len(countries)):
    plt.text(research_papers[i] / 2, i, str(research_papers[i]), ha='center', va='center', color='white', fontweight='bold')
    plt.text(research_papers[i] + book_publications[i] / 2, i, str(book_publications[i]), ha='center', va='center', color='white', fontweight='bold')
    plt.text(research_papers[i] + book_publications[i] + online_articles[i] / 2, i, str(online_articles[i]), ha='center', va='center', color='white', fontweight='bold')

# Add labels and title
plt.xlabel('Number of Publications')
plt.ylabel('Country')
plt.title('Publications in Different Formats by Country')
plt.legend(loc='upper right')

# Display the final result
plt.show()