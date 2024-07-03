
import seaborn as sns
import matplotlib.pyplot as plt

# Data: Marathon finish times in minutes
finish_times = [
    120, 150, 165, 170, 200, 210, 230, 245, 260, 275, 290, 305, 315, 330, 345, 
    360, 375, 390, 405, 420, 435, 450, 465, 480, 495, 510, 525, 540, 555, 570, 
    585, 600, 615, 630, 645, 660, 675, 690, 705, 720, 735, 750, 765, 780, 795, 
    810, 825, 840, 855, 870, 885, 900, 915, 930, 945, 960, 975, 990, 1005, 
    1020, 1035, 1050, 1065, 1080, 1095, 1110, 1125, 1140, 1155, 1170, 1185, 1200
]

# Set the size of the chart
plt.figure(figsize=(10, 8))

# Create a histogram with vertical orientation
sns.histplot(data=finish_times, kde=False, color="#e74c3c", binwidth=30, orientation='vertical')

# Set chart title and labels
plt.title('Distribution of Marathon Finish Times (in minutes)', fontsize=15, pad=20)
plt.xlabel('Finish Time (minutes)')
plt.ylabel('Frequency')

# Show the plot
plt.show()