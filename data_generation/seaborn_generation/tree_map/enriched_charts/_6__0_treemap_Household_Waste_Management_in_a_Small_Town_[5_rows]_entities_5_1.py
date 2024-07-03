import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2021', '2021', '2021', '2021', '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022', '2022', '2022', '2022', '2022',
             '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023'],
    "Condition": ['Hypertension', 'Diabetes', 'Asthma', 'Depression', 'Anxiety', 'Cancer', 'Obesity', 'Arthritis', 'Heart Disease',
                  'Hypertension', 'Diabetes', 'Asthma', 'Depression', 'Anxiety', 'Cancer', 'Obesity', 'Arthritis', 'Heart Disease',
                  'Hypertension', 'Diabetes', 'Asthma', 'Depression', 'Anxiety', 'Cancer', 'Obesity', 'Arthritis', 'Heart Disease'],
    "Prevalence": [45.0, 8.5, 6.3, 11.1, 13.2, 5.6, 30.4, 15.9, 8.4,
                   46.2, 8.7, 6.5, 11.5, 13.5, 5.8, 31.0, 16.2, 8.6,
                   47.0, 8.9, 6.7, 11.8, 13.8, 6.0, 32.0, 16.5, 8.9]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(16, 10))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4', '#ff9ff3']

# Treemap plot
squarify.plot(sizes=df["Prevalence"], label=df["Condition"], color=colors, alpha=0.8)
plt.title("Health Conditions Prevalence (2021-2023)", fontsize=18, color='#555555', pad=20)
plt.axis('off')
plt.show()