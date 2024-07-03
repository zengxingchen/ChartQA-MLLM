
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data into a pandas DataFrame
data = {
    'Movie': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],
    'Rating': [8.2, 7.5, 9.0, 6.8, 7.2, 8.7, 5.9, 6.3, 8.0, 7.8, 9.3, 6.5, 5.5, 7.0, 8.5, 6.0, 8.3, 7.3, 9.1, 6.7],
    'BoxOfficeRevenue': [850, 780, 920, 640, 710, 880, 560, 600, 840, 800, 950, 620, 540, 680, 860, 580, 830, 700, 930, 630]
}

df = pd.DataFrame(data)

# Set the style
sns.set(style="whitegrid")

# Create the scatterplot
plt.figure(figsize=(12, 8))
scatter_plot = sns.scatterplot(x='Rating', y='BoxOfficeRevenue',
                               data=df, color="#E74C3C", s=100)

# Customize the axes and title
scatter_plot.set_title('Movie Ratings vs. Box Office Revenue', fontsize=20)
scatter_plot.set_xlabel('Rating', fontsize=16)
scatter_plot.set_ylabel('Box Office Revenue (in millions)', fontsize=16)

# Show the plot
plt.show()