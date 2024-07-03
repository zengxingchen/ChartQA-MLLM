
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the data above.
data = {
    'Fruit': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 
              'Fig', 'Grape', 'Honeydew', 'Kiwi', 'Lemon', 
              'Mango', 'Nectarine', 'Orange', 'Papaya', 'Pineapple'],
    'Caloric Content (kcal)': [52, 89, 50, 282, 73, 
                               74, 69, 36, 61, 29, 
                               60, 44, 47, 43, 50],
    'Sugar Content (g)': [10.4, 12.2, 8.0, 66.5, 11.5, 
                          16.3, 16.3, 8.0, 9.0, 2.5,
                          14.8, 8.4, 9.4, 7.8, 9.9],
    'Popularity Index': [8, 9, 7, 5, 6, 
                         4, 10, 5, 7, 6,
                         8, 7, 9, 6, 10]
}

df = pd.DataFrame(data)

# Define the bubble chart
plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=df, x='Caloric Content (kcal)', y='Sugar Content (g)', 
                               hue='Popularity Index', size='Popularity Index', 
                               sizes=(100, 1000), alpha=0.7, 
                               palette=["#FF5733", "#33FF57", "#3357FF", "#FF33FB", "#FFD700"])

# Enhance legend and labels
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Popularity Index')
plt.title('Nutrient Content vs. Popularity of Various Fruits', fontsize=16, pad=20)
plt.xlabel('Caloric Content (kcal)', fontsize=12)
plt.ylabel('Sugar Content (g)', fontsize=12)

# Create the visualization
plt.show()