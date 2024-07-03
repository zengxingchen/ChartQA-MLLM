
import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Define the table data as pandas DataFrame
data = {
    "Age Group": ["13-18", "13-18", "13-18", "19-25", "19-25", "19-25", 
                  "26-35", "26-35", "26-35", "36-45", "36-45", "36-45",
                  "46-55", "46-55", "46-55", "56+", "56+", "56+"],
    "Hours per day": [1, 2, 0.5, 3, 2.5, 2, 2, 1.5, 1, 1, 0.7, 0.5, 0.5, 0.3, 0.2, 0.2, 0.1, 0.1],
    "Number of Users": [500000, 400000, 200000, 800000, 700000, 300000, 
                        600000, 500000, 250000, 300000, 200000, 150000,
                        100000, 80000, 50000, 50000, 30000, 20000],
    "Platform": ["TikTok", "Instagram", "Twitter", "TikTok", 
                 "Instagram", "Twitter", "TikTok", "Instagram", 
                 "Twitter", "TikTok", "Instagram", "Twitter", 
                 "TikTok", "Instagram", "Twitter", "TikTok", 
                 "Instagram", "Twitter"]
}
df = pd.DataFrame(data)

# Step 2: Prepare the color mapping
platform_colors = {
    'TikTok': '#1DA1F2',
    'Instagram': '#E1306C',
    'Twitter': '#4AB3F4'
}

# Step 3: Generate the bubble chart
plt.figure(figsize=(14, 8))  # Change width and height reasonably
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
plt.title('Social Media Usage by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Hours per Day')
plt.legend(title='Platform')
plt.grid(True)
plt.show()