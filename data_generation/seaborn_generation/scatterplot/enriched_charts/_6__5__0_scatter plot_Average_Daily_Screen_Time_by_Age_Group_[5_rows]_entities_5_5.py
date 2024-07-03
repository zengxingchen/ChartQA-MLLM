
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'WritingTime': [1.5, 2.0, 1.0, 3.0, 2.5, 1.8, 2.2, 2.0, 1.7, 3.5, 2.8, 1.2, 2.6, 1.9, 3.2, 2.1, 2.4, 1.6, 3.3, 2.7, 1.4, 2.3, 3.0, 1.1, 2.9, 1.3, 2.5, 3.4, 2.0, 1.7],
    'WordsWritten': [300, 450, 200, 600, 500, 380, 440, 400, 360, 700, 560, 240, 520, 380, 640, 420, 480, 320, 660, 540, 280, 460, 600, 220, 580, 260, 500, 680, 400, 340]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
scatterplot = sns.scatterplot(x='WritingTime', y='WordsWritten', data=df, color='#1E90FF')

scatterplot.set_title('Writing Time vs Words Written', fontsize=20, pad=20)
scatterplot.set_xlabel('Writing Time (hours)', fontsize=16)
scatterplot.set_ylabel('Words Written', fontsize=16)

plt.show()