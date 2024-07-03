
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load data into a pandas DataFrame
data_values = [
    5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145,
    155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275,
    285, 295, 305, 315, 325, 335, 345, 355, 365, 375, 385, 395, 405,
    415, 425, 435, 445, 455, 465, 475, 485, 495, 505, 515, 525, 535,
    545, 555, 565, 575, 585, 595, 605, 615, 625, 635, 645, 655, 665,
    675, 685, 695, 705, 715, 725, 735, 745, 755, 765, 775, 785, 795,
    805, 815, 825, 835, 845, 855, 865, 875, 885, 895, 905, 915, 925,
    935, 945, 955, 965, 975, 985, 995, 1005, 1015, 1025, 1035, 1045,
    1055, 1065, 1075, 1085, 1095
]

# Create the dataframe
df = pd.DataFrame(data_values, columns=['Value'])

# Set up the matplotlib figure
sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))

# Plot a vertical histogram with specified bin height and color
sns.histplot(df['Value'], color='#1abc9c', binwidth=20, kde=False)

# Customize the plot with title, labels, and limits
plt.title('Distribution of Income Levels')
plt.xlabel('Income Level')
plt.ylabel('Frequency')

# Show the plot
plt.show()