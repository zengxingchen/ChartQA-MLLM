
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day": list(range(1, 32)),
    "Visitor_Count": [
        8000, 9000, 10000, 11000, 13000, 15000, 18000, 20000, 22000, 25000,
        27000, 30000, 32000, 35000, 38000, 40000, 38000, 35000, 33000, 30000,
        28000, 26000, 24000, 22000, 20000, 18000, 17000, 15000, 13000, 12000,
        10000
    ]
}

data_df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
sns_line = sns.lineplot(data=data_df, x="Day", y="Visitor_Count", color="#1f77b4")
sns_line.fill_between(data_df.Day, data_df.Visitor_Count, color="#1f77b4", alpha=0.3)

plt.annotate('Peak Day', xy=(16, data_df.loc[15, 'Visitor_Count']),
             xytext=(20, data_df.Visitor_Count.max() + 2000),
             arrowprops=dict(facecolor='black', shrink=0.05))

sns_line.set_title('Daily Visitor Count to Art Exhibition', fontsize=20, pad=20)
sns_line.set_xlabel('Day')
sns_line.set_ylabel('Visitor Count')

plt.show()