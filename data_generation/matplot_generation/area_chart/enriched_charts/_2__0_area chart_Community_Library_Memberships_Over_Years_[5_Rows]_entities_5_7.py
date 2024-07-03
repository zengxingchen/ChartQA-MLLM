
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data for monthly visitor count to a national park
data = {
    "Month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Visitor_Count": [15000, 16000, 17500, 20000, 22000, 30000, 35000, 34000, 28000, 25000, 21000, 18000]
}

data_df = pd.DataFrame(data)

# Plotting using Seaborn
plt.figure(figsize=(14, 8))
sns_line = sns.lineplot(data=data_df, x="Month", y="Visitor_Count", color="#2ca02c")
sns_line.fill_between(data_df.Month, data_df.Visitor_Count, color="#2ca02c", alpha=0.3)

# Annotating the chart
plt.annotate('Peak Season', xy=(7, data_df.loc[6, 'Visitor_Count']),
             xytext=(8, data_df.Visitor_Count.max() + 2000),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Customize the appearance
sns_line.set_title('Monthly Visitor Count to National Park', fontsize=16)
sns_line.set_xlabel('Month')
sns_line.set_ylabel('Visitor Count')
plt.show()