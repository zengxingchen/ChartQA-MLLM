
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points in pandas DataFrame
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
             'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
             'Fort Worth', 'Columbus', 'Charlotte', 'Detroit', 'El Paso', 'Seattle',
             'Denver', 'Washington', 'Nashville', 'Boston', 'Memphis', 'Portland',
             'Oklahoma City', 'Las Vegas', 'Louisville', 'Baltimore', 'Milwaukee',
             'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Kansas City', 'Long Beach',
             'Mesa', 'Atlanta', 'Virginia Beach', 'Omaha', 'Colorado Springs'],
    'Revenue': [900, 850, 700, 650, 600, 580, 570, 560, 550, 540, 530, 520, 510, 500, 490, 
                480, 470, 460, 450, 440, 430, 420, 410, 400, 390, 380, 370, 360, 350, 340, 
                330, 320, 310, 300, 290, 280, 270, 260, 250, 240],
    'Expenditure': [850, 800, 680, 600, 550, 540, 530, 520, 510, 500, 490, 480, 470, 460, 
                    450, 440, 430, 420, 410, 400, 390, 380, 370, 360, 350, 340, 330, 320, 
                    310, 300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200]
}

df = pd.DataFrame(data)

# Setting sns theme and figure size
sns.set_theme()
plt.figure(figsize=(16, 10))

# Creating scatterplot with customized color scheme
scatterplot = sns.scatterplot(x='Revenue', y='Expenditure', data=df,
                              palette=['#1E90FF', '#FF4500', '#32CD32', '#FFD700', '#8A2BE2'])

# Customize further details of the plot
scatterplot.axes.set_title('City Financial Overview: Revenue vs Expenditure', fontsize=16, weight='bold')
scatterplot.set_xlabel('Revenue ($ in millions)', fontsize=14)
scatterplot.set_ylabel('Expenditure ($ in millions)', fontsize=14)
scatterplot.figure.set_size_inches(16, 10)  # Change width and height of the chart

plt.show()