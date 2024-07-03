
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the DataFrame from the data above
data = {
    'Activity': ['Yoga', 'Meditation', 'Running', 'Cycling', 'Hiking', 'Weightlifting', 'Cardio Workouts', 
                 'Pilates', 'CrossFit', 'Boxing', 'Zumba', 'Dancing', 'Swimming', 'Martial Arts', 'Tai Chi', 
                 'Rowing', 'Rock Climbing', 'Skating', 'Skiing', 'Snowboarding'],
    'Participants': [200, 180, 300, 250, 150, 130, 280, 100, 90, 70, 60, 110, 170, 80, 60, 50, 40, 45, 35, 30],
    'Events': [3000, 2500, 3500, 3300, 2700, 2000, 3100, 2200, 2400, 2100, 1800, 2600, 2800, 2300, 1700, 
               1600, 1500, 1400, 1300, 1200],
    'Popularity': [5000, 4500, 4800, 4700, 4600, 4200, 4900, 4300, 4400, 4100, 4000, 4500, 4600, 4200, 3900, 
                   3800, 3700, 3600, 3500, 3400]
}

df = pd.DataFrame(data)

# Adjusting the figure size
plt.figure(figsize=(20, 14))

# Creating the bubble chart
sns.scatterplot(data=df, x="Participants", y="Events", size="Popularity", sizes=(100, 1000),
                hue="Popularity", palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#33FFA1", 
                                           "#A133FF", "#FF9633", "#33FF96", "#9633FF", "#96FF33"])

# Customizing the appearance
plt.title("Popularity of Health & Psychology Activities: Participants, Events, and Popularity", fontsize=20, pad=20)
plt.xlabel("Number of Participants (in thousands)", fontsize=16)
plt.ylabel("Number of Events", fontsize=16)

# Adjusting legend to avoid covering data points
plt.legend(title="Popularity (in thousands)", loc='upper right', bbox_to_anchor=(1.2, 1), fontsize=14)

# Showing the final result
plt.show()