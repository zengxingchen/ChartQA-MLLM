
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Topic': ['Literature', 'Writing', 'Poetry', 'Fiction', 'Non-Fiction', 'Drama', 'Criticism', 
              'Memoir', 'Biography', 'Creative Writing', 'Literary Theory', 'Short Stories', 
              'Essays', 'Journalism', 'Screenwriting', 'Playwriting', 'Prose'],
    'Participants': [500, 400, 350, 300, 250, 200, 150, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],
    'Percentage': [0.20, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06, 0.04, 0.036, 0.032, 0.028, 0.024, 
                   0.020, 0.016, 0.012, 0.008, 0.004]
}

df = pd.DataFrame(data)

colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f', '#e67e22', '#1abc9c', 
          '#34495e', '#f39c12', '#d35400', '#7f8c8d', '#2980b9', '#c0392b', '#27ae60', 
          '#8e44ad', '#bdc3c7', '#2c3e50']

plt.figure(figsize=(16, 12))
squarify.plot(sizes=df['Percentage'], label=df['Topic'], color=colors, alpha=0.8)
plt.title('Interest in Various Literature & Writing Topics among Participants', fontsize=22, pad=20)
plt.axis('off')
plt.show()