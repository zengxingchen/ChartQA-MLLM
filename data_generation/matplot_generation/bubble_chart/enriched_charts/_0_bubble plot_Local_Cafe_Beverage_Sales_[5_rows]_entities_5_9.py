
import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ['13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
facebook_users = [45, 120, 160, 110, 80, 60, 40]
twitter_users = [30, 50, 80, 60, 40, 20, 10]
instagram_users = [75, 110, 95, 60, 50, 25, 10]
youtube_users = [65, 95, 130, 120, 75, 50, 30]

# Bubble sizes
bubble_scale = 200
facebook_sizes = np.array(facebook_users) * bubble_scale
twitter_sizes = np.array(twitter_users) * bubble_scale
instagram_sizes = np.array(instagram_users) * bubble_scale
youtube_sizes = np.array(youtube_users) * bubble_scale

fig, ax = plt.subplots(figsize=(14, 9))  # Set the width and height of the chart

# Create scatter points for each social media platform
ax.scatter(age_groups, facebook_users, s=facebook_sizes, color='#3b5998', alpha=0.6, label='Facebook')
ax.scatter(age_groups, twitter_users, s=twitter_sizes, color='#1da1f2', alpha=0.6, label='Twitter')
ax.scatter(age_groups, instagram_users, s=instagram_sizes, color='#c32aa3', alpha=0.6, label='Instagram')
ax.scatter(age_groups, youtube_users, s=youtube_sizes, color='#ff0000', alpha=0.6, label='YouTube')

# Chart title and labels
ax.set_title('Social Media Users by Age Group and Platform', fontsize=18)
ax.set_xlabel('Age Group', fontsize=14)
ax.set_ylabel('Number of Users (in millions)', fontsize=14)

# Legend
ax.legend(loc='upper right', title='Platforms')

plt.tight_layout()
plt.show()