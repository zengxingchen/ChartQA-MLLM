
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
             'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
             'Fort Worth', 'Columbus', 'Charlotte'],
    'temperature': [95, 100, 97, 99, 104, 96, 98, 94, 101, 92, 98, 95, 96, 93, 94]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 8))
barplot = sns.barplot(
    x='temperature',
    y='city',
    data=df,
    palette=['#FF5733', '#33FF57', '#3357FF', '#57FFF3', '#F3FF57', '#FF5733', '#33FF57', '#3357FF', '#57FFF3',
             '#F3FF57', '#FF5733', '#33FF57', '#3357FF', '#57FFF3', '#F3FF57'],
    orient='h',
    dodge=False
)

# Customize bars width
for bar in barplot.patches:
    bar.set_height(0.6)

plt.title('Maximum Temperatures Recorded During Heatwave')
plt.xlabel('Temperature (°F)')
plt.ylabel('City')

plt.show()