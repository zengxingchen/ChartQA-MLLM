
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Country': ['United States', 'Canada', 'United Kingdom', 'France', 'Germany', 'India', 'China', 'Japan', 
                'South Korea', 'Australia', 'Mexico', 'Brazil', 'Italy', 'Spain', 'Russia', 'Argentina', 
                'Saudi Arabia', 'South Africa', 'Turkey', 'New Zealand'],
    'Number of Movies': [120, 45, 70, 55, 40, 150, 110, 65, 50, 30, 35, 45, 25, 30, 40, 20, 10, 15, 25, 10],
    'Average Rating': [7.8, 7.5, 8.0, 7.2, 7.0, 8.3, 7.6, 8.1, 7.9, 7.4, 7.1, 7.3, 7.0, 7.2, 7.4, 6.9, 6.5, 7.0, 7.1, 7.8],
    'Budget (Millions)': [150, 70, 120, 50, 40, 90, 130, 80, 60, 30, 25, 35, 20, 28, 50, 18, 15, 10, 22, 12],
    'Box Office (Millions)': [1000, 600, 750, 500, 450, 1100, 900, 650, 500, 350, 300, 400, 250, 275, 450, 200, 150, 180, 240, 140],
    'Year of Release': [2023, 2022, 2021, 2020, 2019, 2023, 2022, 2021, 2020, 2019, 2023, 2022, 2021, 2020, 2019, 2023, 2022, 2021, 2020, 2019]
})

plt.figure(figsize=(18, 12))

for i in range(len(data)):
    plt.scatter(data['Budget (Millions)'][i], data['Average Rating'][i], 
                s=data['Box Office (Millions)'][i] * 0.5, 
                alpha=0.6, 
                c=[(data['Year of Release'][i] - 2019) * 0.2, 0.3, 0.7])

plt.xlabel('Budget (Millions)')
plt.ylabel('Average Rating')
plt.title('Entertainment & Leisure: Movie Ratings vs Budget by Country')

plt.show()