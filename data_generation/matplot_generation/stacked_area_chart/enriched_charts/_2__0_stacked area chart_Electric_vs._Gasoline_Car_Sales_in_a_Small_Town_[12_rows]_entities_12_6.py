
import matplotlib.pyplot as plt

# Data
years = list(range(2001, 2021))
science_papers = [2.1, 2.4, 2.7, 3.1, 3.4, 3.7, 4.0, 4.4, 4.7, 5.0, 5.4, 5.7, 6.0, 6.3, 6.7, 7.0, 7.3, 7.6, 8.0, 8.3]
tech_innovations = [1.4, 1.7, 2.0, 2.4, 2.7, 3.0, 3.4, 3.7, 4.0, 4.3, 4.6, 5.0, 5.3, 5.6, 6.0, 6.3, 6.6, 7.0, 7.3, 7.6]
research_funding = [0.9, 1.1, 1.3, 1.5, 1.8, 2.0, 2.2, 2.5, 2.7, 2.9, 3.2, 3.4, 3.6, 3.8, 4.1, 4.3, 4.5, 4.8, 5.0, 5.2]

# Plotting the stacked area chart
plt.figure(figsize=(14, 9))  # Change the size of the chart (width, height)
plt.stackplot(years, science_papers, tech_innovations, research_funding, colors=['#66c2a5', '#fc8d62', '#8da0cb'])

# Annotations
for year, sp, ti, rf in zip(years, science_papers, tech_innovations, research_funding):
    plt.text(year, sp/2, f"{sp}", va='center', ha='center', color='black', fontsize=8)
    plt.text(year, sp + ti/2, f"{ti}", va='center', ha='center', color='black', fontsize=8)
    plt.text(year, sp + ti + rf/2, f"{rf}", va='center', ha='center', color='black', fontsize=8)

# Titles and labels
plt.title('Scientific Research Trends (2001-2020)', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Count/Amount (in Billion $)', fontsize=12)

# Customize the legend
plt.legend(['Science Papers', 'Tech Innovations', 'Research Funding'], loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()