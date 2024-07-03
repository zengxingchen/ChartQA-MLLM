
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2019', '2019', '2019', '2019', '2019', '2019', '2019',
             '2020', '2020', '2020', '2020', '2020', '2020', '2020',
             '2021', '2021', '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022', '2022', '2022'],
    "Disorder": ['Anxiety', 'Depression', 'PTSD', 'Schizophrenia', 'OCD', 'Bipolar', 'ADHD',
                 'Anxiety', 'Depression', 'PTSD', 'Schizophrenia', 'OCD', 'Bipolar', 'ADHD',
                 'Anxiety', 'Depression', 'PTSD', 'Schizophrenia', 'OCD', 'Bipolar', 'ADHD',
                 'Anxiety', 'Depression', 'PTSD', 'Schizophrenia', 'OCD', 'Bipolar', 'ADHD'],
    "Patients": [40.2, 33.8, 15.5, 5.7, 12.4, 10.2, 8.1,
                 42.5, 36.0, 16.2, 6.0, 13.0, 11.0, 9.3,
                 45.8, 39.1, 18.5, 6.5, 14.2, 12.5, 10.8,
                 48.3, 42.3, 19.8, 7.0, 15.3, 13.6, 12.1]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(18, 12))
colors = ['#4B0082', '#FF6347', '#4682B4', '#9ACD32', '#FFD700', '#FF1493', '#8A2BE2']

# Treemap plot
squarify.plot(sizes=df["Patients"], label=df["Disorder"], color=colors, alpha=0.8)
plt.title("Mental Health Disorder Statistics (2019-2022)", fontsize=18, color='#333333', y=1.08)
plt.axis('off')
plt.show()