
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Sport': ['Running', 'Swimming', 'Cycling', 'Yoga', 'Weightlifting', 'Tennis', 'Basketball', 'Soccer',
              'Hiking', 'Rowing', 'Boxing', 'Rock Climbing', 'Dancing', 'Skiing', 'Skateboarding', 'Surfing'],
    'Concentration (mg/L)': [8.0, 5.5, 7.2, 3.0, 4.5, 6.0, 7.0, 7.5, 4.8, 9.0, 8.5, 7.8, 4.0, 7.0, 3.5, 5.0],
    'Sample Size': [150, 120, 180, 100, 200, 140, 160, 200, 180, 150, 130, 140, 160, 170, 180, 160],
    'Analysis Duration (min)': [60, 45, 90, 60, 75, 60, 90, 90, 120, 60, 45, 90, 60, 60, 90, 75]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(
    data=df,
    x="Concentration (mg/L)",
    y="Sample Size",
    size="Analysis Duration (min)",
    sizes=(100, 1000),
    hue="Analysis Duration (min)",
    palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FF8333", "#FFBD33", "#33FFBD", "#8333FF",
             "#33A1FF", "#A133FF", "#57FF33", "#A1FF33", "#BD33FF", "#33FF83", "#FF3357", "#5733FF"],
    alpha=0.7,
    legend=True
)

bubble_chart.set_title("Sample Analysis: Concentration vs Sample Size vs Duration", fontsize=16, pad=20)
bubble_chart.set_xlabel("Concentration (mg/L)", fontsize=14)
bubble_chart.set_ylabel("Sample Size", fontsize=14)

plt.show()