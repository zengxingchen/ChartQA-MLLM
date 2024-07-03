
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': ['2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04', 
             '2023-04-05', '2023-04-06', '2023-04-07', '2023-04-08', 
             '2023-04-09', '2023-04-10', '2023-04-11', '2023-04-12', 
             '2023-04-13', '2023-04-14'],
    'Rainfall': [12, 15, 10, 18, 20, 22, 17, 24, 19, 21, 16, 23, 25, 14]
}

df = pd.DataFrame(data)

# Visualization
plt.figure(figsize=(12, 6))
sns.barplot(x='Date', y='Rainfall', data=df,
            palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                     '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                     '#bcbd22', '#17becf', '#aec7e8', '#ffbb78',
                     '#98df8a', '#ff9896'],
            ci=None)

plt.xlabel('Date')
plt.ylabel('Average Daily Rainfall (mm)')
plt.title('Two-week Average Daily Rainfall in Fictitious City')
plt.xticks(rotation=45)
plt.tight_layout()
sns.despine(left=True, bottom=True)

plt.show()