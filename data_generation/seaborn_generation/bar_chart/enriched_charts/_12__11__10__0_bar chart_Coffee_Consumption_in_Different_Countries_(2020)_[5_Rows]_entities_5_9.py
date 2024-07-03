
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average Temperature (°C)': [2, 3, 8, 13, 18, 23, 27, 26, 22, 16, 9, 4]
}

df = pd.DataFrame(data)

f, ax = plt.subplots(figsize=(14, 10))

sns.barplot(y="Average Temperature (°C)", x="Month", data=df,
            palette=['#FF6347', '#FFD700', '#90EE90', '#87CEEB', '#9370DB', 
                     '#FF69B4', '#FFA07A', '#20B2AA', '#778899', '#4682B4', 
                     '#8B0000', '#808000'], edgecolor=".6", linewidth=2)

ax.set_ylabel('Average Temperature (°C)')
ax.set_xlabel('Month')
ax.set_title('Monthly Average Temperatures')

for container in ax.containers:
    plt.setp(container, width=0.6)

plt.show()