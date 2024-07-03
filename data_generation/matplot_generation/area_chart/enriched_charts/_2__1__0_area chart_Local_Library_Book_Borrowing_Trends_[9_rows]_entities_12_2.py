
import matplotlib.pyplot as plt
import pandas as pd

# Create the data
data = {
    'Date': pd.date_range(start='2023-05-01', periods=61, freq='D'),
    'Visitors': [
        150, 160, 155, 170, 180, 190, 185, 195, 200, 210, 220, 230, 225, 235,
        245, 255, 265, 260, 270, 280, 290, 300, 310, 320, 315, 325, 335, 345,
        340, 350, 360, 370, 380, 390, 395, 405, 415, 425, 435, 445, 450, 460,
        470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600,
        610, 620, 630, 640, 650
    ]
}

df = pd.DataFrame(data)

# Plot the data
plt.figure(figsize=(14, 7))
plt.fill_between(df['Date'], df['Visitors'], color='#FF5733', alpha=0.6)
plt.plot(df['Date'], df['Visitors'], color='#C70039', alpha=0.9)

# Title and labels
plt.title('Museum Visitors Over Time', fontsize=18, pad=25)
plt.xlabel('Date')
plt.ylabel('Number of Visitors')

# Annotations
plt.annotate('Peak Attendance', xy=(pd.Timestamp('2023-06-30'), 650), xytext=(pd.Timestamp('2023-06-20'), 580),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, ha='center')

# Display the plot
plt.tight_layout()
plt.show()