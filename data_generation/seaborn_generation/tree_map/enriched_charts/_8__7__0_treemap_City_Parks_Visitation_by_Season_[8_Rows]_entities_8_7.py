
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Let's define our dataframe
data = {
    'Topic': ['Startups', 'Marketing', 'Investment', 'Leadership', 'Innovation', 'E-commerce', 'Business Strategy', 
              'Customer Service', 'Entrepreneurship', 'Human Resources', 'Public Relations', 'Consulting', 
              'Sales', 'Supply Chain', 'Finance'],
    'Percentage': [10, 15, 12, 8, 14, 9, 7, 6, 5, 4, 3, 2, 5, 7, 3]
}

df = pd.DataFrame(data)

# Define color list
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#FF6F61', '#92A8D1', '#955251', '#B565A7', '#009B77', 
          '#DD4124', '#D65076', '#45B8AC', '#EFC050', '#5B5EA6', '#9B2335', '#DFCFBE']

# Plot
plt.figure(figsize=(20, 10))
squarify.plot(sizes=df['Percentage'], label=df['Topic'], color=colors, alpha=0.8)

plt.title('Business & Entrepreneurship Topics in 2023', fontsize=18)
plt.axis('off')

plt.show()