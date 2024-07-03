
import matplotlib.pyplot as plt

countries = [
    'Canada', 'Russia', 'Germany', 'United Kingdom', 'France', 'Spain', 
    'Italy', 'Greece', 'Turkey', 'Australia', 'Brazil', 'India', 
    'China', 'Japan', 'South Korea'
]

average_physical_activity = [
    4.5, 3.8, 5.2, 6.0, 4.7, 5.1, 4.3, 3.5, 4.8, 
    6.2, 5.5, 2.9, 3.4, 4.0, 3.6
]

colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF',
    '#FF8333', '#33FFF6', '#8D33FF', '#33FF92', '#FF5733',
    '#33A1FF', '#FF33F6', '#5733FF', '#33FF83', '#FF338D'
]

plt.figure(figsize=(12, 10))

plt.barh(countries, average_physical_activity, color=colors, height=0.6)
plt.xlabel('Average Physical Activity (hours/week)')
plt.title('Average Weekly Physical Activity by Country')

plt.xlim(2, 7)

plt.show()