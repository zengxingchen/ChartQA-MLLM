
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    'PodcastPlays': [150, 200, 250, 180, 220, 275, 195, 230, 240, 210, 260, 280, 170, 225, 215, 265, 245, 205, 235, 255, 180, 220, 250, 190, 200, 270, 210, 230, 240, 220, 265, 250, 230, 245, 255, 210, 225, 235, 215, 260, 275, 195, 205, 255, 240, 230, 225, 265, 250, 270],
    'OnlineCourseEnrollments': [30, 45, 55, 40, 50, 60, 48, 52, 58, 47, 63, 65, 42, 53, 49, 61, 59, 46, 54, 62, 44, 51, 56, 43, 47, 64, 48, 55, 57, 50, 66, 58, 52, 59, 63, 46, 54, 60, 50, 65, 67, 45, 49, 62, 55, 51, 53, 66, 60, 64]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
scatterplot = sns.scatterplot(x='PodcastPlays', y='OnlineCourseEnrollments', data=df, color='#FF4500')

scatterplot.set_title('Online Course Enrollments vs Podcast Plays', fontsize=20, pad=25)
scatterplot.set_xlabel('Podcast Plays (counts)', fontsize=16)
scatterplot.set_ylabel('Online Course Enrollments (counts)', fontsize=16)

plt.show()