
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Beach': [400, 420, 450, 480, 500, 550, 580, 600, 570, 550, 530, 510],
    'Mountains': [700, 720, 750, 780, 800, 850, 870, 890, 860, 840, 820, 800],
    'City': [500, 520, 540, 560, 600, 650, 680, 700, 670, 650, 630, 610],
}

df = pd.DataFrame(data)
x = df['Month']

plt.figure(figsize=(18, 12))
plt.stackplot(x, df['Beach'], df['Mountains'], df['City'], 
              colors=['#1E90FF', '#3CB371', '#FF8C00'])

plt.title('Monthly Tourist Visits to Different Attractions', fontsize=20)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Number of Tourists', fontsize=16)

plt.annotate('Peak Season for Beaches', xy=(7, df['Beach'][7] + df['Mountains'][7] + df['City'][7]), 
             xytext=(5, 1800), arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.annotate('Mountain Tourism Decline', xy=(11, df['Mountains'][11]), 
             xytext=(9, 900), arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.show()