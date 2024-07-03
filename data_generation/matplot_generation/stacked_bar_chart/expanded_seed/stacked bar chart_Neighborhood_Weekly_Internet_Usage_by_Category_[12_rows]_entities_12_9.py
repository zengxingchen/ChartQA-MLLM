
import matplotlib.pyplot as plt

# Data provided as a list of dictionaries
data = [
    {'Week': '2022-W01', ' Streaming (hours)': 350, ' Gaming (hours)': 150, ' Social Media (hours)': 200, ' Work (hours)': 600, ' Other (hours)': 100},
    {'Week': '2022-W02', ' Streaming (hours)': 360, ' Gaming (hours)': 160, ' Social Media (hours)': 210, ' Work (hours)': 590, ' Other (hours)': 110},
    {'Week': '2022-W03', ' Streaming (hours)': 370, ' Gaming (hours)': 170, ' Social Media (hours)': 220, ' Work (hours)': 580, ' Other (hours)': 120},
    {'Week': '2022-W04', ' Streaming (hours)': 380, ' Gaming (hours)': 175, ' Social Media (hours)': 230, ' Work (hours)': 570, ' Other (hours)': 125},
    {'Week': '2022-W05', ' Streaming (hours)': 390, ' Gaming (hours)': 180, ' Social Media (hours)': 240, ' Work (hours)': 560, ' Other (hours)': 130},
    {'Week': '2022-W06', ' Streaming (hours)': 400, ' Gaming (hours)': 185, ' Social Media (hours)': 250, ' Work (hours)': 550, ' Other (hours)': 135},
    {'Week': '2022-W07', ' Streaming (hours)': 410, ' Gaming (hours)': 190, ' Social Media (hours)': 260, ' Work (hours)': 540, ' Other (hours)': 140},
    {'Week': '2022-W08', ' Streaming (hours)': 420, ' Gaming (hours)': 195, ' Social Media (hours)': 270, ' Work (hours)': 530, ' Other (hours)': 145},
    {'Week': '2022-W09', ' Streaming (hours)': 430, ' Gaming (hours)': 200, ' Social Media (hours)': 280, ' Work (hours)': 520, ' Other (hours)': 150},
    {'Week': '2022-W10', ' Streaming (hours)': 440, ' Gaming (hours)': 205, ' Social Media (hours)': 290, ' Work (hours)': 510, ' Other (hours)': 155},
    {'Week': '2022-W11', ' Streaming (hours)': 450, ' Gaming (hours)': 210, ' Social Media (hours)': 300, ' Work (hours)': 500, ' Other (hours)': 160},
    {'Week': '2022-W12', ' Streaming (hours)': 460, ' Gaming (hours)': 215, ' Social Media (hours)': 310, ' Work (hours)': 490, ' Other (hours)': 165}
]

# Preparing the data
weeks = [item['Week'] for item in data]
streaming_hours = [item[' Streaming (hours)'] for item in data]
gaming_hours = [item[' Gaming (hours)'] for item in data]
social_media_hours = [item[' Social Media (hours)'] for item in data]
work_hours = [item[' Work (hours)'] for item in data]
other_hours = [item[' Other (hours)'] for item in data]

# Stacking the bars for each activity
plt.figure(figsize=(10, 8))
plt.bar(weeks, streaming_hours, label='Streaming')
plt.bar(weeks, gaming_hours, bottom=streaming_hours, label='Gaming')
plt.bar(weeks, social_media_hours, bottom=[i+j for i,j in zip(streaming_hours, gaming_hours)], label='Social Media')
plt.bar(weeks, work_hours, bottom=[i+j+k for i,j,k in zip(streaming_hours, gaming_hours, social_media_hours)], label='Work')
plt.bar(weeks, other_hours, bottom=[i+j+k+l for i,j,k,l in zip(streaming_hours, gaming_hours, social_media_hours, work_hours)], label='Other')

# Adding titles and labels
plt.title('Weekly Activity Distribution')
plt.xlabel('Week')
plt.ylabel('Hours')
plt.xticks(rotation=45)
plt.legend()

# Display the stacked bar chart
plt.tight_layout()
plt.show()