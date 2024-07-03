
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points
data_points = {
    'finish_time': [240, 255, 270, 300, 315, 330, 345, 360, 375, 390, 405, 
                    420, 435, 450, 465, 480, 495, 510, 525, 540, 555, 570]
}

# Convert to DataFrame
df = pd.DataFrame(data_points)

# Set the style
sns.set(style="whitegrid")

# Size of the figure
plt.figure(figsize=(10, 8))

# Create the histogram
sns.histplot(data=df, y="finish_time", color="#3498db", binwidth=30, orientation="horizontal")

# Set the title and labels
plt.title('Distribution of Marathon Finish Times', fontsize=16, pad=20)
plt.xlabel('Frequency')
plt.ylabel('Finish Time (minutes)')

# Show the plot
plt.show()