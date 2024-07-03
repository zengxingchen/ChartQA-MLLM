
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Category": ["Technology", "Technology", "Technology", "Technology", 
                 "Technology", "Technology", "Travel", "Travel", 
                 "Travel", "Travel", "Travel", "Travel", "Fitness", 
                 "Fitness", "Fitness", "Fitness", "Fitness", "Fitness"],
    "Age Group": ["13-18", "19-25", "26-35", "36-45", "46-55", "56+", 
                  "13-18", "19-25", "26-35", "36-45", "46-55", "56+", 
                  "13-18", "19-25", "26-35", "36-45", "46-55", "56+"],
    "Popularity Score": [85, 90, 80, 75, 70, 60, 65, 80, 85, 70, 60, 50, 70, 85, 80, 75, 65, 55],
    "Number of Participants": [300000, 500000, 400000, 250000, 150000, 80000, 200000, 600000, 550000, 300000, 200000, 100000, 450000, 600000, 350000, 200000, 100000, 50000],
    "Activity": ["Learning Coding", "Learning Coding", "Learning Coding", "Learning Coding", 
                 "Learning Coding", "Learning Coding", "Adventure Trips", "Adventure Trips", 
                 "Adventure Trips", "Adventure Trips", "Adventure Trips", "Adventure Trips", 
                 "Yoga", "Yoga", "Yoga", "Yoga", "Yoga", "Yoga"]
}

df = pd.DataFrame(data)

activity_colors = {
    'Learning Coding': '#1f77b4',
    'Adventure Trips': '#ff7f0e',
    'Yoga': '#2ca02c'
}

plt.figure(figsize=(14, 9))
for activity in df['Activity'].unique():
    subset = df[df['Activity'] == activity]
    plt.scatter(
        subset['Age Group'], 
        subset['Popularity Score'], 
        s=subset['Number of Participants']/1000, 
        alpha=0.6,
        color=activity_colors[activity],
        label=activity
    )

plt.title('Popularity of Activities by Age Group and Participation')
plt.xlabel('Age Group')
plt.ylabel('Popularity Score')
plt.legend(title='Activity')
plt.grid(True)
plt.show()