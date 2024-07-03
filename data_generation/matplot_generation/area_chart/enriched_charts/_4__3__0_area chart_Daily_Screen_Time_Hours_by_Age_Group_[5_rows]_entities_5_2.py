
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Day": list(range(1, 32)),
    "Calories_Burned": [300, 320, 310, 330, 340, 360, 350, 370, 380, 400, 410, 430, 420, 440, 450, 460, 470, 490, 480, 500, 510, 530, 520, 540, 550, 560, 580, 570, 590, 600, 610]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create the area plot
plt.figure(figsize=(16, 9))
area_chart = plt.plot(df['Day'], df['Calories_Burned'], color="#1f77b4")
plt.fill_between(df['Day'], df['Calories_Burned'], color="#1f77b4", alpha=0.3)

# Annotate a specific day
plt.annotate('Peak Burn',
             xy=(31, 610),
             xytext=(20, 550),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05),
             )

# Add chart title and labels
plt.title('Daily Calories Burned in January', fontsize=18, pad=30)
plt.xlabel('Day of the Month')
plt.ylabel('Calories Burned')

# Show the plot
plt.show()