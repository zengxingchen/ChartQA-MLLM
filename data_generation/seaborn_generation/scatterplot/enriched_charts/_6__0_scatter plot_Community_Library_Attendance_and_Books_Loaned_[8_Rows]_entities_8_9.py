
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with the provided data
data = {
    'City': ['London', 'New York', 'Los Angeles', 'Tokyo', 'Paris', 'Berlin', 'Moscow', 'Beijing', 'Sydney', 'Rio de Janeiro', 'Cairo', 'Mumbai', 'Chicago', 'Toronto', 'Mexico City', 'Seoul', 'Madrid', 'Johannesburg', 'Dubai', 'Singapore'],
    'Average_Movie_Rating': [7.5, 8.0, 8.5, 7.0, 6.5, 7.2, 6.8, 7.9, 7.3, 6.7, 6.2, 8.1, 7.6, 7.8, 6.9, 8.2, 7.1, 6.4, 7.7, 7.4],
    'Box_Office_Earnings_Million': [150, 200, 250, 180, 120, 130, 90, 220, 160, 110, 50, 210, 170, 140, 95, 230, 125, 70, 155, 145]
}

df = pd.DataFrame(data)

# Plotting the scatterplot
plt.figure(figsize=(12, 8))
scatterplot = sns.scatterplot(data=df, x='Average_Movie_Rating', y='Box_Office_Earnings_Million', palette=['#4B0082', '#FF4500'])

scatterplot.set_title('Average Movie Ratings and Box Office Earnings by City', fontsize=14)
scatterplot.set_xlabel('Average Movie Rating', fontsize=12)
scatterplot.set_ylabel('Box Office Earnings (Million $)', fontsize=12)
plt.show()