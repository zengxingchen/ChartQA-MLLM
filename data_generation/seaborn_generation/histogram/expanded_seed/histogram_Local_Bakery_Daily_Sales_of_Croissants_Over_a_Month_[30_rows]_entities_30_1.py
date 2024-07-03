
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Date': '2023-04-01', 'Croissants Sold': 72},
    {'Date': '2023-04-02', 'Croissants Sold': 85},
    {'Date': '2023-04-03', 'Croissants Sold': 60},
    {'Date': '2023-04-04', 'Croissants Sold': 40},
    {'Date': '2023-04-05', 'Croissants Sold': 53},
    {'Date': '2023-04-06', 'Croissants Sold': 69},
    {'Date': '2023-04-07', 'Croissants Sold': 75},
    {'Date': '2023-04-08', 'Croissants Sold': 88},
    {'Date': '2023-04-09', 'Croissants Sold': 91},
    {'Date': '2023-04-10', 'Croissants Sold': 66},
    {'Date': '2023-04-11', 'Croissants Sold': 59},
    {'Date': '2023-04-12', 'Croissants Sold': 34},
    {'Date': '2023-04-13', 'Croissants Sold': 77},
    {'Date': '2023-04-14', 'Croissants Sold': 82},
    {'Date': '2023-04-15', 'Croissants Sold': 99}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to pandas datetime format for easier handling
df['Date'] = pd.to_datetime(df['Date'])

# Setting the style
sns.set(style="whitegrid")

# Creating a histogram with Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Croissants Sold', bins=8, color='skyblue', kde=True)

# Adding more visual details
plt.title('Distribution of Croissants Sold Over Time')
plt.xlabel('Number of Croissants Sold')
plt.ylabel('Frequency')
plt.axvline(df['Croissants Sold'].mean(), color='red', linestyle='--')
plt.text(df['Croissants Sold'].mean()+1, 1, 'Mean', color = 'red')

# Show the plot
plt.show()