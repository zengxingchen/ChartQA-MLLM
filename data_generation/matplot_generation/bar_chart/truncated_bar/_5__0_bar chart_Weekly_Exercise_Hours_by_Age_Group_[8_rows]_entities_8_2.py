
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
website_visits = [350, 400, 450, 480, 500, 520, 530, 550, 580, 600, 620, 650]
social_media_engagements = [300, 320, 330, 350, 360, 380, 390, 400, 410, 420, 430, 440]
email_subscribers = [250, 280, 310, 320, 330, 350, 360, 370, 380, 390, 400, 420]

# Plot setup
fig, ax = plt.subplots(figsize=(10, 12))

# Create bar chart
bar_width = 0.2
bar_locations_a = range(len(website_visits))
bar_locations_b = [x + bar_width for x in bar_locations_a]
bar_locations_c = [x + bar_width for x in bar_locations_b]

bars1 = ax.bar(bar_locations_a, website_visits, bar_width, label='Website Visits', color='#FF5733')
bars2 = ax.bar(bar_locations_b, social_media_engagements, bar_width, label='Social Media Engagements', color='#33FF57')
bars3 = ax.bar(bar_locations_c, email_subscribers, bar_width, label='Email Subscribers', color='#3357FF')

# Set the position of the x ticks
ax.set_xticks([r + bar_width for r in range(len(website_visits))])
ax.set_xticklabels(months)

# Adding labels and title
plt.ylabel('Counts')
plt.title('Monthly Digital Marketing Metrics')
ax.legend()

# Set y-axis limits to truncate the chart
ax.set_ylim(200, 700)

# Display the plot
plt.tight_layout()
plt.show()