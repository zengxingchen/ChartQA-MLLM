
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'University': ['Harvard', 'Stanford', 'MIT', 'Caltech', 'Princeton', 'Yale', 'Columbia', 'Chicago',
                   'UPenn', 'Northwestern', 'Duke', 'Dartmouth', 'Brown', 'Vanderbilt', 'Rice', 'Notre Dame',
                   'Washington_St_Louis', 'Cornell', 'UCLA', 'Johns_Hopkins'],
    'Average_Ranking': [2, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'Graduation_Rate': [98, 94, 92, 91, 97, 95, 93, 94, 95, 92, 95, 97, 94, 93, 94, 95, 94, 93, 91, 93],
    'Student_Faculty_Ratio': [7, 5, 3, 3, 5, 6, 6, 5, 6, 6, 7, 7, 6, 7, 6, 8, 8, 9, 18, 7],
    'Total_Enrollment': [21000, 17000, 11000, 2200, 8200, 12500, 32000, 15000, 26000, 21000, 16000, 6600, 10000, 13000, 7800, 12300, 15000, 24000, 44000, 27000]
})

sns.set(style="whitegrid")
palette = sns.color_palette(["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"])

plt.figure(figsize=(16, 12))
bubble = sns.scatterplot(x="Average_Ranking", y="Graduation_Rate", size="Total_Enrollment",
                         sizes=(100, 2500), hue="University", palette=palette, data=data, legend=False)

plt.title('University Rankings and Graduation Rates', fontsize=20)
plt.xlabel('Average Ranking', fontsize=16)
plt.ylabel('Graduation Rate (%)', fontsize=16)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, color='gray', linestyle='--', linewidth=0.5)

plt.show()