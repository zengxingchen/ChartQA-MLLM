
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {
    "Score": [
        78, 81, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 95, 96, 97, 98, 98, 99, 
        100, 101, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 
        113, 114, 115, 116, 117, 118, 119, 120
    ]
}

df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(10, 8))

# Create the histogram
sns.histplot(df['Score'], 
             bins=8, 
             kde=False, 
             color='#e74c3c', 
             binwidth=3,
             orientation='horizontal')

# Set titles and labels
plt.title('Distribution of Student Test Scores')
plt.xlabel('Frequency')
plt.ylabel('Score')

# Display the plot
plt.show()