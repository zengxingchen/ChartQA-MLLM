
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Condition': ['Depression', 'Anxiety', 'Bipolar Disorder', 'Schizophrenia', 'Eating Disorders', 
                  'PTSD', 'OCD', 'ADHD', 'Autism Spectrum Disorder'],
    'Prevalence (Millions)': [264, 284, 46, 20, 70, 100, 40, 300, 75]
}

df = pd.DataFrame(data)

# Color scheme for better clarity and visual appeal
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', 
          '#FF69B4', '#CD5C5C', '#87CEEB', '#48D1CC']

# Plotting the Treemap
plt.figure(figsize=(18, 10))  # Change width and height reasonably
squarify.plot(sizes=df['Prevalence (Millions)'], label=df['Condition'], color=colors, alpha=0.8)
plt.title('Prevalence of Mental Health Conditions Worldwide (Millions of People)', fontsize=18)
plt.axis('off')
plt.show()