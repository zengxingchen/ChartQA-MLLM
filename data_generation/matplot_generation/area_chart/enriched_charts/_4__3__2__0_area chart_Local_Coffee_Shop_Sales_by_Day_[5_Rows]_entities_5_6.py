
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Category': ['Fiction', 'Non-Fiction', 'Science', 'Biography', 'Fantasy', 'Mystery', 'Romance', 'History', 'Horror', 'Poetry', 'Self-Help', 'Children'],
    'AverageRating': [85, 75, 92, 70, 88, 81, 78, 65, 74, 82, 80, 90]
}
df = pd.DataFrame(data)

# Convert 'Category' to categorical type with proper order
df['Category'] = pd.Categorical(df['Category'], categories=data['Category'], ordered=True)

# Create the area chart
plt.figure(figsize=(14, 8))
plt.plot(df['Category'], df['AverageRating'], lw=2, color='#ff6347')

# Filling the area under the line
plt.fill_between(x=df['Category'], y1=df['AverageRating'], color='#ffa07a', alpha=0.6)

# Annotate the chart with text labels
for i in range(df.shape[0]):
    plt.text(df['Category'][i], df['AverageRating'][i] + 1, str(df['AverageRating'][i]) + ' pts', horizontalalignment='center')

# Customize the axes
plt.xlabel('Book Category')
plt.ylabel('Average Rating')
plt.title('Average Ratings of Different Book Categories', pad=20)

# Show the final plot
plt.show()