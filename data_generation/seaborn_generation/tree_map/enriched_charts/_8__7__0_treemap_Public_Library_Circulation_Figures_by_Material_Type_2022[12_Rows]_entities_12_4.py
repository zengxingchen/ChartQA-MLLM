
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Issue': ['Anxiety', 'Depression', 'PTSD', 'Bipolar Disorder', 'OCD', 'ADHD', 'Eating Disorders', 'Substance Abuse', 'Schizophrenia', 'Phobias'],
    'Prevalence': [0.25, 0.20, 0.10, 0.08, 0.05, 0.12, 0.07, 0.06, 0.03, 0.04]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c4e17f', '#6e6e6e', '#b3b3b3']

# Plot the Treemap
plt.figure(figsize=(16, 12))
squarify.plot(sizes=df['Prevalence'], label=df['Issue'], color=colors, alpha=0.8)
plt.title('Common Mental Health Issues and Their Prevalence', fontsize=22, y=1.05)
plt.axis('off')
plt.show()