
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'UK', 'France', 'Italy', 'Brazil', 'Canada', 
                'Russia', 'South_Korea', 'Australia', 'Spain', 'Mexico', 'Indonesia', 'Netherlands', 
                'Saudi_Arabia', 'Turkey', 'Switzerland'],
    'GDP_Trillions': [21.43, 14.34, 5.08, 3.84, 2.87, 2.83, 2.72, 2.00, 1.84, 1.74, 
                      1.63, 1.63, 1.39, 1.39, 1.27, 1.12, 0.91, 0.79, 0.75, 0.71],
    'Population_Millions': [331, 1441, 126, 83, 1380, 68, 67, 60, 212, 38, 
                            146, 52, 25, 47, 128, 273, 17, 35, 84, 9],
    'Internet_Penetration': [89, 61, 92, 88, 43, 96, 88, 87, 70, 91, 
                             80, 95, 88, 91, 64, 53, 95, 96, 75, 94],
    'Total_Enrollment': [21000, 17000, 11000, 2200, 8200, 12500, 32000, 15000, 26000, 21000, 
                         16000, 6600, 10000, 13000, 7800, 12300, 15000, 24000, 44000, 27000]
})

sns.set(style="whitegrid")
palette = ["#8B0000", "#FF4500", "#32CD32", "#1E90FF", "#FFD700", "#8A2BE2", "#00CED1", "#FF1493", "#7CFC00", "#DA70D6", 
           "#FF69B4", "#FF6347", "#ADFF2F", "#20B2AA", "#DB7093", "#3CB371", "#4682B4", "#D2B48C", "#EE82EE", "#D2691E"]

plt.figure(figsize=(18, 14))
bubble = sns.scatterplot(x="GDP_Trillions", y="Internet_Penetration", size="Population_Millions",
                         sizes=(100, 2500), hue="Country", palette=palette, data=data, legend="brief")

plt.title('Global GDP and Internet Penetration Rates', fontsize=20, pad=20)
plt.xlabel('GDP in Trillions (USD)', fontsize=16)
plt.ylabel('Internet Penetration Rate (%)', fontsize=16)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, color='gray', linestyle='--', linewidth=0.5)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Country", fontsize=12)

plt.show()