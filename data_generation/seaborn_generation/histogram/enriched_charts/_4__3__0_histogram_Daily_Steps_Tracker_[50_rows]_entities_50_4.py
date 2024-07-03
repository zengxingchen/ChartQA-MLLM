
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load data into a pandas DataFrame
data_values = [
    10, 15, 22, 24, 28, 32, 36, 38, 42, 44, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86,
    90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170,
    175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250,
    255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330,
    335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400, 405, 410,
    415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495, 500
]

# Create the dataframe
df = pd.DataFrame(data_values, columns=['Age'])

# Set up the matplotlib figure
sns.set(style="whitegrid")
plt.figure(figsize=(14, 10))

# Plot a horizontal histogram with specified bin width and color
sns.histplot(df['Age'], color='#e74c3c', binwidth=30, kde=False, orientation='horizontal')

# Customize the plot with title, labels, and limits
plt.title('Age Distribution in Community')
plt.xlabel('Frequency')
plt.ylabel('Age')

# Show the plot
plt.show()