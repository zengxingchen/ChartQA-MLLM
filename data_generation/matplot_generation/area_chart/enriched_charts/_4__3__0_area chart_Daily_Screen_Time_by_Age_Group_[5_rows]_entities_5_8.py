
import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame directly
data = pd.DataFrame({
    'Day': range(1, 32),
    'TouristVisits': [450, 470, 490, 510, 530, 550, 570, 590, 610, 630, 
                      650, 670, 690, 710, 730, 750, 770, 790, 810, 830, 
                      850, 870, 890, 910, 930, 950, 970, 990, 1010, 1030, 1050]
})

plt.figure(figsize=(12, 6))

# Creating an area chart
plt.fill_between(data['Day'], data['TouristVisits'], color="#FFA07A", alpha=0.6, label='Tourist Visits')
plt.plot(data['Day'], data['TouristVisits'], color="#FF6347")

# Annotating the highest tourist visits
highest_visits = data['TouristVisits'].max()
highest_day = data['Day'][data['TouristVisits'].idxmax()]
plt.annotate(f'Highest\n{highest_visits} visits', xy=(highest_day, highest_visits), xytext=(highest_day+1, highest_visits+100),
             arrowprops=dict(facecolor='#4682B4', shrink=0.05))

# Adding chart title and labels
plt.title('Daily Tourist Visits in January', fontsize=16)
plt.xlabel('Day')
plt.ylabel('Tourist Visits')
plt.legend()

# Display the chart
plt.show()