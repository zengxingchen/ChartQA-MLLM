
import matplotlib.pyplot as plt

# Data for the stacked area chart
quarters = ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 
            'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022']
north_america_revenue = [120, 130, 140, 150, 160, 170, 180, 190]
europe_revenue = [90, 100, 110, 120, 130, 140, 150, 160]
asia_pacific_revenue = [70, 80, 90, 100, 110, 120, 130, 140]

# Modify the dimensions of the plot
plt.figure(figsize=(10, 6))

# Creating the stacked area chart
plt.stackplot(quarters, north_america_revenue, europe_revenue, asia_pacific_revenue,
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'],
              labels=['North America', 'Europe', 'Asia-Pacific'])

# Adding the legend
plt.legend(loc='upper left')

# Adding titles and labels
plt.title('Tech Company Quarterly Revenue by Region')
plt.xlabel('Quarter')
plt.ylabel('Revenue (Millions USD)')

# Add annotation
for i, na in enumerate(north_america_revenue):
    total_revenue = na + europe_revenue[i] + asia_pacific_revenue[i]
    plt.text(quarters[i], total_revenue, f'{total_revenue}M', ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()