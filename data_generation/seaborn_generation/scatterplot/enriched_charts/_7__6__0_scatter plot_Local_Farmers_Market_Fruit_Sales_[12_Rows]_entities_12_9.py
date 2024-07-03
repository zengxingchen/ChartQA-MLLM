
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Visitors': [200, 180, 220, 230, 210, 240, 260, 250, 270, 290,
                 300, 280, 310, 330, 320, 340, 360, 350, 370, 390,
                 380, 400, 410, 430, 420, 440, 460, 450, 470, 480],
    'Distance': [15, 17, 14, 18, 16, 19, 20, 21, 23, 25,
                 22, 24, 27, 29, 28, 30, 32, 31, 33, 35,
                 34, 37, 36, 39, 38, 41, 43, 42, 44, 45]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 10))
scatterplot = sns.scatterplot(x='Visitors', y='Distance',
                              data=df, palette=['#2E8B57', '#FF6347'])

scatterplot.set_title('Relationship Between Visitors and Distance Traveled on Adventure Trips')
scatterplot.set_xlabel('Number of Visitors')
scatterplot.set_ylabel('Distance Traveled (km)')
plt.show()