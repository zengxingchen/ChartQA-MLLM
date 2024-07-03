
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a data frame with new data
df = pd.DataFrame({
    'category': ['Mental Health', 'Mental Health', 'Mental Health', 'Mental Health', 
                 'Physical Health', 'Physical Health', 'Physical Health', 'Physical Health', 
                 'Nutrition', 'Nutrition', 'Nutrition', 'Nutrition', 
                 'Exercise', 'Exercise', 'Exercise', 'Exercise', 
                 'Sleep Disorders', 'Sleep Disorders', 'Sleep Disorders', 'Sleep Disorders', 
                 'Addictions', 'Addictions', 'Addictions', 'Addictions'],
    'sub_category': ['Depression', 'Anxiety', 'Bipolar Disorder', 'Schizophrenia', 
                     'Heart Disease', 'Diabetes', 'Asthma', 'Cancer', 
                     'Diet Plans', 'Supplements', 'Organic Foods', 'Processed Foods', 
                     'Aerobics', 'Strength Training', 'Yoga', 'Pilates', 
                     'Insomnia', 'Apnea', 'Restless Legs', 'Narcolepsy', 
                     'Substance Abuse', 'Alcoholism', 'Smoking', 'Overeating'],
    'value': [1500, 1200, 800, 600, 
              1800, 1600, 1400, 1200, 
              900, 700, 500, 300, 
              800, 600, 400, 200, 
              1000, 800, 600, 400, 
              1500, 1200, 1000, 800]
})

# Create a color list
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', 
          '#33FFA1', '#A133FF', '#FF8333', '#FF3380', 
          '#33FFB5', '#5733FF', '#FF57A1', '#57FFA1', 
          '#3380FF', '#FF5733', '#33FF57', '#3357FF', 
          '#FF33A1', '#33FFA1', '#A133FF', '#FF8333', 
          '#FF3380', '#33FFB5', '#5733FF', '#FF57A1']

# Plot
plt.figure(figsize=(24, 12))
squarify.plot(sizes=df['value'], label=df['sub_category'], color=colors, alpha=.7)
plt.title('Prevalence of Health & Psychological Issues', fontsize=23)
plt.axis('off')
plt.show()