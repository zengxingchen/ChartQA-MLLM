
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the data above.
data = {
    'Book': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E', 
             'Book F', 'Book G', 'Book H', 'Book I', 'Book J', 
             'Book K', 'Book L', 'Book M'],
    'Total Pages': [350, 420, 310, 280, 390, 
                    460, 330, 300, 370, 410, 
                    360, 440, 320],
    'Reading Time (hours)': [10, 12, 8, 7, 11, 
                             13, 9, 8.5, 10.5, 12, 
                             10, 13.5, 9],
    'Reader Satisfaction': [8.5, 9.0, 7.8, 7.5, 8.7, 
                            9.3, 8.0, 7.9, 8.6, 8.9, 
                            8.2, 9.1, 7.7]
}

df = pd.DataFrame(data)

# Define the bubble chart
plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=df, x='Total Pages', y='Reading Time (hours)', 
                               hue='Reader Satisfaction', size='Reader Satisfaction', 
                               sizes=(100, 1000), alpha=0.7, 
                               palette=["#FF6347", "#4682B4", "#3CB371", "#FFD700", 
                                        "#DA70D6", "#CD5C5C", "#40E0D0", "#FF69B4",
                                        "#8B4513", "#7B68EE", "#6A5ACD", "#D2691E", "#9ACD32"])

# Enhance legend and labels
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Reader Satisfaction')
plt.title('Total Pages vs. Reading Time by Book with Reader Satisfaction', fontsize=16, pad=20)
plt.xlabel('Total Pages', fontsize=12)
plt.ylabel('Reading Time (hours)', fontsize=12)

# Create the visualization
plt.show()