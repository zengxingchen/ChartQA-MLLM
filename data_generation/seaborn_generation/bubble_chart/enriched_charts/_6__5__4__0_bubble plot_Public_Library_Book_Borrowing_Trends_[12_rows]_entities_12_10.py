
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'UK', 'France', 'Italy', 'Brazil', 'Canada', 
                'Russia', 'South_Korea', 'Australia', 'Spain', 'Mexico', 'Indonesia', 'Netherlands', 
                'Saudi_Arabia', 'Turkey', 'Switzerland'],
    'Medals_Won': [113, 88, 58, 46, 7, 65, 33, 40, 21, 24, 
                   71, 20, 46, 17, 10, 5, 36, 2, 13, 14],
    'Population_Millions': [331, 1441, 126, 83, 1380, 68, 67, 60, 212, 38, 
                            146, 52, 25, 47, 128, 273, 17, 35, 84, 9],
    'Participation_Rate': [90, 45, 85, 80, 25, 88, 82, 78, 65, 88, 
                           77, 90, 92, 80, 55, 23, 88, 38, 70, 85],
    'Total_Athletes': [613, 406, 552, 434, 120, 376, 383, 371, 302, 371, 
                       335, 206, 296, 322, 115, 71, 286, 47, 190, 108]
})

sns.set(style="whitegrid")
palette = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FF8633", "#B533FF", "#FF3388", "#33FFDD", "#FF5733", "#33FF57", 
           "#3357FF", "#FF33A1", "#FF8633", "#B533FF", "#FF3388", "#33FFDD", "#FF5733", "#33FF57", "#3357FF", "#FF33A1"]

plt.figure(figsize=(20, 16))
bubble = sns.scatterplot(x="Medals_Won", y="Participation_Rate", size="Population_Millions",
                         sizes=(100, 2500), hue="Country", palette=palette, data=data, legend="brief")

plt.title('Olympic Medals Won and Participation Rates', fontsize=20, pad=20)
plt.xlabel('Medals Won', fontsize=16)
plt.ylabel('Participation Rate (%)', fontsize=16)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, color='gray', linestyle='--', linewidth=0.5)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Country", fontsize=12)

plt.show()