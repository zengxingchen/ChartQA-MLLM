
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Constructing a DataFrame from our dataset
data = {
    'BooksRead': [
        63, 72, 58, 45, 80, 67, 59, 75, 62, 78, 70, 64, 83, 68, 54, 60, 76, 55, 
        66, 74, 61, 79, 65, 82, 56, 73, 69, 71, 77, 57, 50, 81, 51, 52, 53, 47, 
        46, 49, 48
    ]
}
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create the histogram
plt.figure(figsize=(10, 8))
sns.histplot(data=df, y="BooksRead", color="#ff5733", binwidth=5)

# Additional customizations
plt.title('Histogram of Books Read by Students in a Year')
plt.xlabel('Frequency')
plt.ylabel('Books Read')

# Show the plot
plt.show()