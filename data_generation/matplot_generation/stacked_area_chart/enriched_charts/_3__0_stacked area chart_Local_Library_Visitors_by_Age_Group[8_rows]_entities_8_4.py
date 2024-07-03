
import matplotlib.pyplot as plt

# Data for the stacked area chart
quarters = ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 
            'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
            'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023']
north_america_revenue = [120, 135, 150, 160, 175, 190, 200, 210, 220, 230, 240, 250]
europe_revenue = [90, 95, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
asia_pacific_revenue = [70, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175]

# Modify the dimensions of the plot
plt.figure(figsize=(12, 7))

# Creating the stacked area chart
plt.stackplot(quarters, north_america_revenue, europe_revenue, asia_pacific_revenue,
              colors=['#1E90FF', '#FF4500', '#32CD32'],
              labels=['North America', 'Europe', 'Asia-Pacific'])

# Adding the legend
plt.legend(loc='upper left')

# Adding titles and labels
plt.title('Quarterly Revenue by Region for a Tech Company', pad=20)
plt.xlabel('Quarter')
plt.ylabel('Revenue (Millions USD)')

# Add annotation
for i, na in enumerate(north_america_revenue):
    total_revenue = na + europe_revenue[i] + asia_pacific_revenue[i]
    plt.text(quarters[i], total_revenue, f'{total_revenue}M', ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()