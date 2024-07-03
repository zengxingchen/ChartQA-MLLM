
import matplotlib.pyplot as plt

countries = [
    'USA', 'Brazil', 'Germany', 'France', 'Italy', 'Japan', 'Canada',
    'Russia', 'South Korea', 'Australia', 'Ethiopia', 'Spain', 'India',
    'UK', 'China'
]

average_daily_coffee_consumption = [
    3.1, 2.5, 4.0, 3.5, 3.8, 2.2, 3.0, 1.5, 2.7, 3.4, 2.8, 3.2, 1.0, 2.9, 0.8
]

colors = [
    '#ff5733', '#33ff57', '#3357ff', '#ff33a1', '#a133ff',
    '#33ffa1', '#a1ff33', '#ff8333', '#33a1ff', '#ff33d9',
    '#d933ff', '#33ffd9', '#a133d9', '#d9ff33', '#d9a133'
]

plt.figure(figsize=(14, 8))
plt.barh(countries, average_daily_coffee_consumption, color=colors, height=0.5)
plt.xlabel('Average Daily Coffee Consumption (cups)')
plt.title('Average Daily Coffee Consumption by Country')
plt.xlim(0.5, 4.5)
plt.tight_layout()
plt.show()