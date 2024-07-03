
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points in pandas DataFrame
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
             'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
             'Fort Worth', 'Columbus', 'Charlotte', 'Detroit', 'El Paso', 'Seattle',
             'Denver', 'Washington', 'Nashville', 'Boston', 'Memphis', 'Portland',
             'Oklahoma City', 'Las Vegas', 'Louisville', 'Baltimore', 'Milwaukee',
             'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Kansas City', 'Long Beach',
             'Mesa', 'Atlanta', 'Virginia Beach', 'Omaha', 'Colorado Springs'],
    'AverageTemperature': [16, 19, 13, 23, 28, 15, 25, 18, 22, 20, 24, 26, 21, 14, 20, 12,
                           27, 13, 12, 18, 19, 12, 20, 15, 19, 30, 18, 17, 11, 25, 27, 24,
                           22, 20, 21, 29, 20, 19, 15, 14],
    'Humidity': [73, 65, 70, 80, 23, 72, 66, 68, 64, 60, 68, 88, 65, 70, 75, 78, 23, 82,
                 55, 71, 69, 76, 74, 83, 64, 22, 72, 70, 77, 45, 35, 47, 61, 69, 63, 25,
                 71, 72, 69, 54]
}

df = pd.DataFrame(data)

# Setting sns theme and figure size
sns.set_theme()
plt.figure(figsize=(12, 8))

# Creating scatterplot with customized color scheme
scatterplot = sns.scatterplot(x='AverageTemperature', y='Humidity', data=df,
                              palette=['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2'])

# Customize further details of the plot
scatterplot.axes.set_title('City Climate: Average Temperature vs Humidity', fontsize=14, weight='bold')
scatterplot.set_xlabel('Average Temperature (°C)', fontsize=12)
scatterplot.set_ylabel('Humidity (%)', fontsize=12)
scatterplot.figure.set_size_inches(14, 10)  # Change width and height of the chart
plt.show()