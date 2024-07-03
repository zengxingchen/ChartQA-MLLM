
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Topic": ["Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", 
              "Beauty", "Beauty", "Beauty", "Beauty", "Beauty", "Beauty", 
              "Accessories", "Accessories", "Accessories", "Accessories", "Accessories", "Accessories"],
    "Age Group": ["13-18", "19-25", "26-35", "36-45", "46-55", "56+", 
                  "13-18", "19-25", "26-35", "36-45", "46-55", "56+", 
                  "13-18", "19-25", "26-35", "36-45", "46-55", "56+"],
    "Interest Level": [90, 85, 75, 70, 65, 60, 88, 92, 82, 75, 68, 58, 85, 90, 78, 72, 65, 55],
    "Participants": [150000, 200000, 180000, 120000, 80000, 40000, 180000, 220000, 200000, 140000, 90000, 50000, 160000, 210000, 170000, 110000, 70000, 30000],
    "Activity": ["Clothing Trends", "Clothing Trends", "Clothing Trends", "Clothing Trends", 
                 "Clothing Trends", "Clothing Trends", "Skincare Routines", "Skincare Routines", 
                 "Skincare Routines", "Skincare Routines", "Skincare Routines", "Skincare Routines", 
                 "Fashion Accessories", "Fashion Accessories", "Fashion Accessories", "Fashion Accessories", 
                 "Fashion Accessories", "Fashion Accessories"]
}

df = pd.DataFrame(data)

activity_colors = {
    'Clothing Trends': '#ff6347',
    'Skincare Routines': '#4682b4',
    'Fashion Accessories': '#32cd32'
}

plt.figure(figsize=(16, 10))
for activity in df['Activity'].unique():
    subset = df[df['Activity'] == activity]
    plt.scatter(
        subset['Age Group'], 
        subset['Interest Level'], 
        s=subset['Participants']/1000, 
        alpha=0.6,
        color=activity_colors[activity],
        label=activity
    )

plt.title('Interest in Fashion & Beauty Activities by Age Group and Participation', pad=20)
plt.xlabel('Age Group')
plt.ylabel('Interest Level')
plt.legend(title='Activity')
plt.grid(True)
plt.show()