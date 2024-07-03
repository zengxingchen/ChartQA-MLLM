
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create dataframe
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']*4,
    'Year': [2010]*10 + [2011]*10 + [2012]*10 + [2013]*10,
    'Mental_Health_Score': [
        70, 65, 75, 60, 68, 64, 72, 66, 71, 69,
        73, 67, 78, 62, 70, 66, 75, 68, 74, 71,
        76, 69, 80, 65, 73, 68, 78, 70, 77, 73,
        78, 72, 83, 67, 75, 70, 81, 72, 79, 76
    ]
}
df = pd.DataFrame(data)

# Scatterplot
plt.figure(figsize=(16, 12))
scatter_plot = sns.scatterplot(
    x='Year', 
    y='Mental_Health_Score', 
    data=df, 
    hue='City', 
    palette=[
        '#FF5733', '#33FF57', '#3357FF', '#57FFFF', 
        '#FF33FF', '#FFFF33', '#FF8333', '#33FF83', 
        '#8333FF', '#FF3383'
    ]
)

# Customizing the chart
plt.title('Yearly Mental Health Survey Scores in Various Cities', pad=20)
plt.xlabel('Year')
plt.ylabel('Mental Health Score')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()