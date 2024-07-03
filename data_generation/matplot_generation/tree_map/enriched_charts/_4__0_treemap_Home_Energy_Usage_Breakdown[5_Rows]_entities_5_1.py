
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataset
data = {
    'Disorder': ['Depression', 'Anxiety', 'Bipolar Disorder', 'Eating Disorders', 'Schizophrenia', 
                 'OCD', 'PTSD', 'ADHD', 'Autism Spectrum Disorder', 'Borderline Personality Disorder', 
                 'Panic Disorder', 'Social Anxiety Disorder'],
    'Prevalence': [4.4, 3.6, 1.0, 0.7, 0.3, 1.2, 3.9, 2.5, 1.5, 1.4, 2.2, 1.3]
}

df = pd.DataFrame(data)

# Define the color scheme
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', 
          '#FFB266', '#FF6666', '#99CCCC', '#FF9933', 
          '#CCCC99', '#99CCFF', '#FF66B2', '#6699FF']

# Create the figure with specified figure size
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, aspect="auto")

# Create a treemap
squarify.plot(sizes=df['Prevalence'], label=df['Disorder'], color=colors, alpha=0.7)

# Set the title of the plot
plt.title('Prevalence of Mental Health Disorders', fontsize=22)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()