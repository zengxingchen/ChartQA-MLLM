
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data in a pandas DataFrame
data = pd.DataFrame({
    'Daily_Temperature': [24, 22, 23, 25, 27, 26, 23, 22, 24, 21, 28, 30, 29, 31, 34, 33, 32, 31, 29, 28,
                          27, 26, 25, 27, 28, 29, 27, 25, 24, 23, 26, 28, 30, 32, 33, 29, 27, 26, 25, 24,
                          22, 23, 25, 26, 28, 31, 30, 29, 28, 27, 25, 24, 26, 28, 31, 33, 34, 32, 30, 29,
                          28, 27, 25, 23, 24, 22, 21, 20, 18, 19, 20, 22, 25, 26, 27, 29, 31, 32, 34, 35,
                          36, 37, 38, 36, 34, 32, 30, 28, 27, 26, 25, 24, 22, 20, 19, 18, 17, 16, 18, 20,
                          23, 25, 27, 30, 32, 31, 29, 28, 27, 25, 23, 21, 20, 19, 18, 21, 23, 25, 27, 29,
                          31, 30, 28, 26, 27, 29, 32, 34, 36, 35, 33, 31, 29, 27, 26, 25, 24, 22, 21, 23,
                          25, 28, 30, 32, 33, 31, 29, 28, 26, 24, 23, 21, 22, 24, 27, 29, 31, 33, 32, 30,
                          28, 27, 25, 24, 22, 23, 25, 28, 31, 34, 36, 35, 33, 31, 30, 28, 27, 25, 24, 23,
                          21, 20, 22, 24, 27, 29, 31, 30, 28, 27, 25, 23, 22, 20, 21, 23, 26, 28, 31, 33,
                          35, 34, 32, 30, 29, 28, 26, 25, 24, 23, 22, 21, 19, 20, 22, 25, 27, 29, 28, 26,
                          25, 23, 22]
})

# Set the size of the seaborn plot
plt.figure(figsize=(10, 6))

# Plot a horizontal histogram with specified bin width and color
sns.histplot(data, x='Daily_Temperature', binwidth=1, color="#3498db", orientation='horizontal')

# Set chart title and labels
plt.title('Yearly Temperature Distribution in City X')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')

# Show the plot
plt.show()