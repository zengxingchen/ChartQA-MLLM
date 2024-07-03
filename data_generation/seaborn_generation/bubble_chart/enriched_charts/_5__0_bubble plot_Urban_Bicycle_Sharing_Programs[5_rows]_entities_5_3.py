
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Campaign': ['Awareness2020', 'Therapy2020', 'Support2020',
                 'Awareness2021', 'Therapy2021', 'Support2021',
                 'Awareness2022', 'Therapy2022', 'Support2022'],
    'Year': [2020, 2020, 2020, 2021, 2021, 2021, 2022, 2022, 2022],
    'Participants': [1000, 850, 700, 1100, 900, 750, 1150, 950, 800],
    'Impact': [80, 65, 50, 85, 70, 55, 90, 75, 60]
}

# Converting data to DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(16, 8))
bubble_chart = sns.scatterplot(data=df, x="Year", y="Participants",
                               hue="Campaign", size="Impact",
                               palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#A133FF"],
                               sizes=(50, 1500), alpha=0.8)

# Adjust the legend and plot titles
plt.title('Participation in Mental Health Awareness Campaigns', fontsize=18)
bubble_chart.legend(loc='upper right', bbox_to_anchor=(1.25, 1), title='Campaign')
bubble_chart.set_xlabel('Year', fontsize=14)
bubble_chart.set_ylabel('Number of Participants', fontsize=14)

plt.tight_layout()
plt.show()