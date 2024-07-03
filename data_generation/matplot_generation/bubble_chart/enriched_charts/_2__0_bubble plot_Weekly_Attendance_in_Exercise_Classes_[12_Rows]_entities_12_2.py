
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Age Group": ["13-18", "13-18", "13-18", "19-25", "19-25", "19-25", 
                  "26-35", "26-35", "26-35", "36-45", "36-45", "36-45",
                  "46-55", "46-55", "46-55", "56+", "56+", "56+"],
    "Hours per day": [1, 2, 0.5, 3, 2.5, 2, 2.5, 1.5, 1, 1.5, 1, 0.8, 1, 0.6, 0.4, 0.5, 0.3, 0.2],
    "Number of Users": [500000, 400000, 200000, 800000, 700000, 300000, 
                        650000, 500000, 250000, 350000, 250000, 180000,
                        120000, 90000, 60000, 70000, 40000, 30000],
    "Platform": ["TikTok", "Instagram", "Twitter", "TikTok", 
                 "Instagram", "Twitter", "TikTok", "Instagram", 
                 "Twitter", "TikTok", "Instagram", "Twitter", 
                 "TikTok", "Instagram", "Twitter", "TikTok", 
                 "Instagram", "Twitter"]
}
df = pd.DataFrame(data)

platform_colors = {
    'TikTok': '#FF5733',
    'Instagram': '#C70039',
    'Twitter': '#900C3F'
}

plt.figure(figsize=(16, 10))
for platform in df['Platform'].unique():
    subset = df[df['Platform'] == platform]
    plt.scatter(
        subset['Age Group'], 
        subset['Hours per day'], 
        s=subset['Number of Users']/1000, 
        alpha=0.6,
        color=platform_colors[platform],
        label=platform
    )

plt.title('Social Media Engagement by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Hours per Day')
plt.legend(title='Platform', loc='upper right')
plt.grid(True)
plt.show()