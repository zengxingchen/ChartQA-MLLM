
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Preparing the dataset
data = {
    "Year": [i for i in range(2000, 2021)],
    "MarathonParticipants": [
        45000, 47000, 48000, 50000, 52000, 54000, 55000, 57000, 60000, 62000, 
        65000, 67000, 69000, 71000, 73000, 75000, 77000, 79000, 81000, 83000, 
        85000
    ]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Create the area chart
plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")
area_chart = sns.lineplot(x="Year", y="MarathonParticipants", data=df)
area_chart.fill_between(df['Year'], df['MarathonParticipants'], alpha=0.3, color='#FF6347')

# Customize the plot with labels and change in visual aspects
plt.title('Marathon Participation Over Time', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Participants', fontsize=14)

# Annotate the last data point
plt.annotate(f'{df.iloc[-1]["MarathonParticipants"]}',
             xy=(df.iloc[-1]['Year'], df.iloc[-1]['MarathonParticipants']),
             xytext=(df.iloc[-2]['Year'], df.iloc[-1]['MarathonParticipants'] + 2000),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12)

sns.despine(left=True, bottom=True)
plt.show()