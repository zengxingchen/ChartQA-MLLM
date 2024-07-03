
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Topic': ['Poetry', 'Novel', 'Essay', 'Short Story', 'Play', 'Biography', 'Memoir', 'Satire', 
              'Speech', 'Criticism', 'Journalism', 'Literary Theory'],
    'Value': [3200, 5800, 2300, 4100, 3400, 5200, 4800, 2900, 3700, 2400, 2700, 1900]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(18, 12))
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#33FFA1", "#A133FF", "#FFA133", "#57FF33", "#33A1FF", "#A1FF33", "#5733FF", "#FF5733"]
squarify.plot(sizes=df['Value'], label=df['Topic'], alpha=0.8, color=colors)
plt.title('Participation in Various Literary Activities', fontsize=22)
plt.axis('off')
plt.show()