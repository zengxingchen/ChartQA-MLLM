
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Sport': ['Running', 'Swimming', 'Cycling', 'Yoga', 'Weightlifting', 'Tennis', 'Basketball', 'Soccer',
              'Hiking', 'Rowing', 'Boxing', 'Rock Climbing', 'Dancing', 'Skiing', 'Skateboarding', 'Surfing'],
    'Calories Burned (cal/hr)': [600, 500, 700, 300, 400, 550, 650, 700, 450, 800, 750, 600, 400, 700, 350, 500],
    'Cost of Equipment (USD)': [100, 150, 200, 30, 500, 120, 80, 60, 40, 250, 150, 300, 50, 400, 150, 350],
    'Duration (min)': [60, 45, 90, 60, 75, 60, 90, 90, 120, 60, 45, 90, 60, 60, 90, 75]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
bubble_chart = sns.scatterplot(
    data=df,
    x="Calories Burned (cal/hr)",
    y="Cost of Equipment (USD)",
    size="Duration (min)",
    sizes=(100, 1000),
    hue="Duration (min)",
    palette=["#ff6347", "#4682b4", "#32cd32", "#ffa500", "#8a2be2", "#5f9ea0", "#d2691e", "#6495ed",
             "#dc143c", "#00fa9a", "#ff4500", "#8b0000", "#ffd700", "#ff69b4", "#c71585", "#ffb6c1"],
    alpha=0.7,
    legend=True
)

bubble_chart.set_title("Sports: Calories Burned vs Cost of Equipment vs Duration", fontsize=16, pad=20)
bubble_chart.set_xlabel("Calories Burned (cal/hr)", fontsize=14)
bubble_chart.set_ylabel("Cost of Equipment (USD)", fontsize=14)

plt.show()