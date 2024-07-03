
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the data table
data = {
    'Disorder': ['Depression', 'Anxiety', 'Schizophrenia', 'Bipolar Disorder', 'PTSD', 'OCD', 'Eating Disorders', 
                 'Substance Use Disorder', 'ADHD', 'Autism Spectrum Disorder', 'Alzheimer\'s Disease', 
                 'Parkinson\'s Disease', 'Sleep Disorders', 'Personality Disorders', 'Panic Disorder', 
                 'Borderline Personality Disorder', 'Hoarding Disorder', 'Phobias'],
    'Prevalence (%)': [4.4, 3.6, 0.3, 1.0, 1.9, 1.2, 1.5, 3.0, 5.0, 1.7, 0.6, 0.3, 4.0, 1.5, 1.0, 1.6, 2.5, 3.2],
    'Average Treatment Cost (USD)': [800, 600, 5000, 3000, 700, 1500, 2500, 2000, 1000, 2500, 4500, 2500, 500, 
                                     2000, 800, 1500, 700, 400],
    'Economic Burden (Billion USD)': [210, 250, 155, 200, 120, 100, 90, 450, 180, 60, 290, 100, 70, 50, 40, 35, 25, 30]
}

df = pd.DataFrame(data)

# Plotting the bubble chart with customized colors and sizes
plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(
    data=df,
    x="Prevalence (%)",
    y="Average Treatment Cost (USD)",
    size="Economic Burden (Billion USD)",
    sizes=(100, 2000),
    hue="Economic Burden (Billion USD)",
    palette=["#4B0082", "#FF6347", "#4682B4", "#32CD32", "#FFD700", "#DC143C", "#FF1493", "#1E90FF",
             "#FF4500", "#00FA9A", "#FFDAB9", "#ADFF2F", "#FF00FF", "#8B008B", "#B22222", "#FF69B4", "#FFA500", "#40E0D0"],
    alpha=0.8,
    legend="full"
)

bubble_chart.set_title("Prevalence, Treatment Cost, and Economic Burden of Mental Health Disorders", fontsize=16, pad=20)
bubble_chart.set_xlabel("Prevalence (%)", fontsize=12)
bubble_chart.set_ylabel("Average Treatment Cost (USD)", fontsize=12)

plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Economic Burden (Billion USD)')
plt.show()