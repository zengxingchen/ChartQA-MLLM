
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Age Group": ["13-18", "13-18", "13-18", "19-25", "19-25", "19-25", 
                  "26-35", "26-35", "26-35", "36-45", "36-45", "36-45",
                  "46-55", "46-55", "46-55", "56+", "56+", "56+"],
    "Average Trips per Year": [2, 1.5, 0.8, 3.5, 2.5, 1.2, 4, 3, 1.5, 3.5, 2.5, 1.2, 3, 2, 1, 2.5, 1.5, 0.8],
    "Number of Travelers": [400000, 300000, 150000, 600000, 500000, 250000, 
                            700000, 600000, 300000, 500000, 400000, 200000,
                            300000, 250000, 120000, 200000, 150000, 80000],
    "Platform": ["TripAdvisor", "Expedia", "Booking", "TripAdvisor", 
                 "Expedia", "Booking", "TripAdvisor", "Expedia", 
                 "Booking", "TripAdvisor", "Expedia", "Booking", 
                 "TripAdvisor", "Expedia", "Booking", "TripAdvisor", 
                 "Expedia", "Booking"]
}
df = pd.DataFrame(data)

platform_colors = {
    'TripAdvisor': '#1f77b4',
    'Expedia': '#ff7f0e',
    'Booking': '#2ca02c'
}

plt.figure(figsize=(18, 12))
for platform in df['Platform'].unique():
    subset = df[df['Platform'] == platform]
    plt.scatter(
        subset['Age Group'], 
        subset['Average Trips per Year'], 
        s=subset['Number of Travelers']/1000, 
        alpha=0.6,
        color=platform_colors[platform],
        label=platform
    )

plt.title('Travel Frequency by Age Group and Platform')
plt.xlabel('Age Group')
plt.ylabel('Average Trips per Year')
plt.legend(title='Platform', loc='upper left')
plt.grid(True)
plt.show()