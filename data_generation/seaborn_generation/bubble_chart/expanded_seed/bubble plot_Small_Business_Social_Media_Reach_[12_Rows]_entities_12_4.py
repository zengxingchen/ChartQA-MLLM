
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = [
    {'Week': 1, 'Bakery Page Likes': 150, 'Florist Page Likes': 135, 'Bookstore Page Shares': 40, 'Restaurant Check-ins': 50, 'Week Highlight Promotion': 'None', 'Social Media Engagement Score': 220},
    {'Week': 2, 'Bakery Page Likes': 160, 'Florist Page Likes': 140, 'Bookstore Page Shares': 45, 'Restaurant Check-ins': 55, 'Week Highlight Promotion': 'Bookstore', 'Social Media Engagement Score': 230},
    # ... add all the other weeks data
    {'Week': 12, 'Bakery Page Likes': 210, 'Florist Page Likes': 220, 'Bookstore Page Shares': 110, 'Restaurant Check-ins': 105, 'Week Highlight Promotion': 'Restaurant', 'Social Media Engagement Score': 390}
]
df = pd.DataFrame(data)

# Create a color palette for the 'Week Highlight Promotion' categories
promotion_palette = {
    'None': 'gray',
    'Bookstore': 'blue',
    'Bakery': 'orange',
    'Restaurant': 'green',
    'Florist': 'red'
}

# Create the bubble chart
plt.figure(figsize=(12, 8))
bubble_chart = sns.scatterplot(
    data=df,
    x="Week",
    y="Social Media Engagement Score",
    size="Restaurant Check-ins",
    hue="Week Highlight Promotion",
    palette=promotion_palette,
    sizes=(100, 1000),  # Control the range of bubble sizes
    alpha=0.7,
    legend='full'
)

# Add annotations for Bakery and Florist Page Likes
for line in range(0, df.shape[0]):
    bubble_chart.text(df.Week[line]+0.2, df["Social Media Engagement Score"][line], 
                      f"Bakery: {df['Bakery Page Likes'][line]}, Florist: {df['Florist Page Likes'][line]}", 
                      horizontalalignment='left', 
                      size='small', color='black')

# Finalize and display the bubble chart
plt.title('Social Media Engagement vs. Week with Bubble Sizes for Restaurant Check-ins')
plt.xlabel('Week')
plt.ylabel('Social Media Engagement Score')
plt.legend(title='Week Highlight Promotion', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()