
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided table data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'Visitors': [
        100, 150, 130, 170, 180, 160, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420
    ]
}

df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(12, 8))

# Create an area plot
plt.plot(df['Date'], df['Visitors'], color="#007ACC")
plt.fill_between(df['Date'], df['Visitors'], color="#007ACC", alpha=0.4)

# Assign annotation
for index, value in df.iterrows():
    if index % 3 == 0:  # Annotate every 3 days
        plt.text(value['Date'], value['Visitors'] + 10, f"{value['Visitors']} Visitors", ha='center')

# Set the chart title and labels
plt.title('Daily Visitors to National Park in January 2023', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Visitors', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()