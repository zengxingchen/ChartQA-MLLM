
import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Define the table data as pandas DataFrame
data = {
    "Age Group": ["13-18", "13-18", "13-18", "19-25", "19-25", "19-25", 
                  "26-35", "26-35", "26-35", "36-45", "36-45", "36-45",
                  "46-55", "46-55", "46-55", "56+", "56+", "56+"],
    "Hours per day": [1.2, 2.1, 0.7, 3.2, 2.7, 2.1, 2.5, 1.8, 1.2, 1.5, 1.1, 0.9, 0.8, 0.4, 0.3, 0.4, 0.2, 0.1],
    "Number of Users": [520000, 420000, 210000, 820000, 710000, 320000, 
                        620000, 510000, 260000, 320000, 220000, 170000,
                        120000, 90000, 60000, 55000, 35000, 25000],
    "Platform": ["TikTok", "Instagram", "Twitter", "TikTok", 
                 "Instagram", "Twitter", "TikTok", "Instagram", 
                 "Twitter", "TikTok", "Instagram", "Twitter", 
                 "TikTok", "Instagram", "Twitter", "TikTok", 
                 "Instagram", "Twitter"]
}
df = pd.DataFrame(data)

# Step 2: Prepare the color mapping
platform_colors = {
    'TikTok': '#FF4500',
    'Instagram': '#FFD700',
    'Twitter': '#1E90FF'
}

# Step 3: Generate the bubble chart
plt.figure(figsize=(16, 10))  # Change width and height reasonably
for platform in df['Platform'].unique():
    subset = df[df['Platform'] == platform]
    plt.scatter(
        subset['Age Group'], 
        subset['Hours per day'], 
        s=subset['Number of Users']/1000,  # Bubble sizes
        alpha=0.5,
        color=platform_colors[platform],
        label=platform
    )

# Step 4: Chart formatting and topic/headline changes
plt.title('Social Media Usage by Age Group', pad=20)
plt.xlabel('Age Group')
plt.ylabel('Average Hours per Day')
plt.legend(title='Platform', loc='upper right')
plt.grid(True)
plt.show()