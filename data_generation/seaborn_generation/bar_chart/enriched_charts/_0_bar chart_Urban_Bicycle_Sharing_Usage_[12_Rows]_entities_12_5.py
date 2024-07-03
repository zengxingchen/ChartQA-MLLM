
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': ['2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04', 
             '2023-04-05', '2023-04-06', '2023-04-07', '2023-04-08', 
             '2023-04-09', '2023-04-10', '2023-04-11', '2023-04-12', 
             '2023-04-13', '2023-04-14'],
    'Temperature': [56, 58, 61, 64, 60, 67, 68, 70, 72, 65, 63, 69, 71, 74]
}

df = pd.DataFrame(data)

# Visualization
plt.figure(figsize=(10, 8))
sns.barplot(x='Temperature', y='Date', data=df,
            palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB',
                     '#57FFC1', '#FF7333', '#5733FF', '#F3FF33',
                     '#33FFF8', '#F833FF', '#33FF8D', '#FFF833',
                     '#8D33FF', '#33C6FF'],
            orient='h',
            dodge=False)

plt.xlabel('Average Daily Temperature (°F)')
plt.ylabel('Date')
plt.title('Two-week Average Daily Temperature in Fictitious City')
sns.despine(left=True, bottom=True)

plt.show()