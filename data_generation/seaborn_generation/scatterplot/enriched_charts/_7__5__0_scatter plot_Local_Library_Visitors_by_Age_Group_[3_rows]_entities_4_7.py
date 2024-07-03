
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
             'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
             'Fort Worth', 'Columbus', 'Charlotte', 'Detroit', 'El Paso', 'Seattle',
             'Denver', 'Washington', 'Nashville', 'Boston', 'Memphis', 'Portland',
             'Oklahoma City', 'Las Vegas', 'Louisville', 'Baltimore', 'Milwaukee',
             'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Kansas City', 'Long Beach',
             'Mesa', 'Atlanta', 'Virginia Beach', 'Omaha', 'Colorado Springs'],
    'Popularity': [98, 95, 92, 85, 83, 80, 78, 77, 75, 74, 73, 72, 71, 70, 69, 
                   68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 
                   53, 52, 51, 50, 49, 48, 47, 46, 45, 44],
    'Attendance': [94000, 87000, 78000, 72000, 68000, 67000, 64000, 63000, 62000, 
                   61000, 60000, 59000, 58000, 57000, 56000, 55000, 54000, 53000, 
                   52000, 51000, 50000, 49000, 48000, 47000, 46000, 45000, 44000, 
                   43000, 42000, 41000, 40000, 39000, 38000, 37000, 36000, 35000, 
                   34000, 33000, 32000, 31000]
}

df = pd.DataFrame(data)

sns.set_theme()
plt.figure(figsize=(14, 8))

scatterplot = sns.scatterplot(x='Popularity', y='Attendance', data=df,
                              palette=['#FF6347', '#4682B4', '#8B008B', '#32CD32', '#FFD700'])

scatterplot.axes.set_title('City Event Popularity vs Attendance', fontsize=18, weight='bold')
scatterplot.set_xlabel('Popularity (%)', fontsize=14)
scatterplot.set_ylabel('Attendance (in thousands)', fontsize=14)
scatterplot.figure.set_size_inches(14, 8)

plt.show()