
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Visitors': [120, 130, 150, 160, 170, 180, 190, 200, 210, 220,
                 230, 240, 250, 260, 270, 280, 290, 300, 310, 320,
                 330, 340, 350, 360, 370, 380, 390, 400, 410, 420],
    'Sales': [300, 320, 330, 340, 360, 370, 380, 390, 400, 410,
              420, 430, 440, 450, 460, 470, 480, 490, 500, 510,
              520, 530, 540, 550, 560, 570, 580, 590, 600, 610]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 8))
scatterplot = sns.scatterplot(x='Visitors', y='Sales',
                              data=df, palette=['#FF4500', '#1E90FF'])

scatterplot.set_title('Relationship Between Visitors and Sales in a Store')
scatterplot.set_xlabel('Number of Visitors')
scatterplot.set_ylabel('Sales ($)')
plt.show()