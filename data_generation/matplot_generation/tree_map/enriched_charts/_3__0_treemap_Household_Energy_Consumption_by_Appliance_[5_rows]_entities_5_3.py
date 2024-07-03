
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "City": ["New York", "New York", "New York", "Los Angeles", "Los Angeles", "Los Angeles",
             "Chicago", "Chicago", "Chicago", "Houston", "Houston", "Houston",
             "Phoenix", "Phoenix", "Phoenix", "Philadelphia", "Philadelphia", "Philadelphia",
             "San Antonio", "San Antonio", "San Antonio", "San Diego", "San Diego", "San Diego",
             "Dallas", "Dallas", "Dallas", "San Jose", "San Jose", "San Jose"],
    "Education Level": ["High School", "Undergraduate", "Graduate", "High School", "Undergraduate", "Graduate",
                        "High School", "Undergraduate", "Graduate", "High School", "Undergraduate", "Graduate",
                        "High School", "Undergraduate", "Graduate", "High School", "Undergraduate", "Graduate",
                        "High School", "Undergraduate", "Graduate", "High School", "Undergraduate", "Graduate",
                        "High School", "Undergraduate", "Graduate", "High School", "Undergraduate", "Graduate"],
    "Number of Students": [450, 320, 150, 400, 300, 120, 350, 280, 100, 320, 260, 90,
                           290, 240, 80, 270, 220, 70, 250, 200, 60, 230, 180, 50,
                           210, 160, 40, 190, 140, 30]
}

df = pd.DataFrame(data)

grouped_data = df.groupby("Education Level").sum().reset_index()

colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A5", "#57FF33", "#5733FF", "#33FFA5", "#A533FF", "#33FF57"]

plt.figure(figsize=(14, 10))
squarify.plot(sizes=grouped_data['Number of Students'], label=grouped_data['Education Level'], alpha=0.8, color=colors)
plt.title('Number of Students by Education Level in Major Cities')
plt.axis('off')
plt.show()