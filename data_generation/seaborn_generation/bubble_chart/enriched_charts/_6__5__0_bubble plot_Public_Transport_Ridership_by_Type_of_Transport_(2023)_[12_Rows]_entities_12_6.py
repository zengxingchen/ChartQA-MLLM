
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Company': ['Gold\'s Gym', '24 Hour Fitness', 'Planet Fitness', 'LA Fitness', 'Anytime Fitness', 
                'Equinox', 'Crunch Fitness', 'YMCA', 'Snap Fitness', 'Lifetime Fitness',
                'Yoga Studio', 'Pilates Center', 'Zumba Class', 'CrossFit Gym', 'Cycle Studio'],
    'MembershipCount': [150.2, 130.5, 200.3, 110.4, 90.3, 75.6, 60.4, 50.2, 40.3, 30.4, 70.1, 55.2, 45.7, 80.9, 60.5],
    'WorkoutSessions': [340.1, 290.8, 320.7, 220.5, 150.2, 120.1, 80.5, 60.8, 50.7, 40.2, 100.3, 75.4, 65.8, 130.6, 90.1],
    'Revenue': [180.3, 160.4, 210.5, 140.8, 100.9, 90.7, 70.2, 60.1, 50.0, 45.3, 85.4, 65.3, 55.2, 95.7, 75.4]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))

bubble = sns.scatterplot(data=df, x='WorkoutSessions', y='MembershipCount', size='Revenue', 
                         hue='Company', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', 
                                                 '#33FFFB', '#FFFB33', '#FBFF33', '#837FF3',
                                                 '#8FF73F', '#3FF786', '#B36A5E', '#6AB35E',
                                                 '#5E6AB3', '#A3B35E', '#B35EA3'],
                         sizes=(100, 1500), alpha=0.7, edgecolor='w', linewidth=1)

bubble.set_title('Membership and Workout Sessions of Various Fitness Clubs', weight='bold', size=18)
bubble.set_xlabel('Workout Sessions (in thousands)', weight='bold', size=14)
bubble.set_ylabel('Membership Count (in thousands)', weight='bold', size=14)

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
plt.show()