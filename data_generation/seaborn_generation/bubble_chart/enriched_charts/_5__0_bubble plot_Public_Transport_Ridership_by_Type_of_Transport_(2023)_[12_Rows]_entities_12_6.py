
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the above data
data = {
    'Company': ['Gold\'s Gym', '24 Hour Fitness', 'Planet Fitness', 'LA Fitness', 'Anytime Fitness', 
                'Equinox', 'Crunch Fitness', 'YMCA', 'Snap Fitness', 'Lifetime Fitness'],
    'MembershipCount': [150.2, 130.5, 200.3, 110.4, 90.3, 75.6, 60.4, 50.2, 40.3, 30.4],
    'WorkoutSessions': [340.1, 290.8, 320.7, 220.5, 150.2, 120.1, 80.5, 60.8, 50.7, 40.2],
    'Revenue': [180.3, 160.4, 210.5, 140.8, 100.9, 90.7, 70.2, 60.1, 50.0, 45.3]
}
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(14, 10))

# Create the bubble chart
bubble = sns.scatterplot(data=df, x='WorkoutSessions', y='MembershipCount', size='Revenue', 
                         hue='Company', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', 
                                                 '#33FFFB', '#FFFB33', '#FBFF33', '#837FF3',
                                                 '#8FF73F', '#3FF786'],
                         sizes=(100, 1500), alpha=0.7, edgecolor='w', linewidth=1)
bubble.set_title('Fitness Club Membership and Workout Sessions', weight='bold', size=18)
bubble.set_xlabel('Workout Sessions (in thousands)', weight='bold', size=14)
bubble.set_ylabel('Membership Count (in thousands)', weight='bold', size=14)

# Adjust legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# Show the plot
plt.show()