
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Exercise_Duration": [
        10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 
        110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 
        190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 
        270, 275, 280, 285, 290, 295, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 
        400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(12, 8))

# Create a histogram with specified bin width, color, and other properties
sns.histplot(df['Exercise_Duration'], bins=20, color='#1f77b4', kde=False, binwidth=25, orientation='vertical')

# Set title and labels for the plot
plt.title("Distribution of Daily Exercise Duration", pad=20)
plt.xlabel("Exercise Duration (minutes)")
plt.ylabel("Frequency")

# Show the plot
plt.show()