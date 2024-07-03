
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'VR Headsets Sold': 120, 'AR Glasses Sold': 200, 'Smart Speakers Sold': 150, 'Robot Assistants Sold': 80},
    {'Month': 'February', 'VR Headsets Sold': 140, 'AR Glasses Sold': 190, 'Smart Speakers Sold': 160, 'Robot Assistants Sold': 85},
    {'Month': 'March', 'VR Headsets Sold': 160, 'AR Glasses Sold': 210, 'Smart Speakers Sold': 170, 'Robot Assistants Sold': 90},
    {'Month': 'April', 'VR Headsets Sold': 180, 'AR Glasses Sold': 220, 'Smart Speakers Sold': 180, 'Robot Assistants Sold': 95},
    {'Month': 'May', 'VR Headsets Sold': 200, 'AR Glasses Sold': 230, 'Smart Speakers Sold': 190, 'Robot Assistants Sold': 100},
    {'Month': 'June', 'VR Headsets Sold': 220, 'AR Glasses Sold': 240, 'Smart Speakers Sold': 200, 'Robot Assistants Sold': 105},
    {'Month': 'July', 'VR Headsets Sold': 240, 'AR Glasses Sold': 250, 'Smart Speakers Sold': 210, 'Robot Assistants Sold': 110},
    {'Month': 'August', 'VR Headsets Sold': 260, 'AR Glasses Sold': 260, 'Smart Speakers Sold': 220, 'Robot Assistants Sold': 115},
    {'Month': 'September', 'VR Headsets Sold': 280, 'AR Glasses Sold': 270, 'Smart Speakers Sold': 230, 'Robot Assistants Sold': 120},
    {'Month': 'October', 'VR Headsets Sold': 300, 'AR Glasses Sold': 280, 'Smart Speakers Sold': 240, 'Robot Assistants Sold': 125},
    {'Month': 'November', 'VR Headsets Sold': 320, 'AR Glasses Sold': 290, 'Smart Speakers Sold': 250, 'Robot Assistants Sold': 130},
    {'Month': 'December', 'VR Headsets Sold': 340, 'AR Glasses Sold': 300, 'Smart Speakers Sold': 260, 'Robot Assistants Sold': 135}
]

months = [entry['Month'] for entry in data]
vr_headsets_sold = [entry['VR Headsets Sold'] for entry in data]
ar_glasses_sold = [entry['AR Glasses Sold'] for entry in data]
smart_speakers_sold = [entry['Smart Speakers Sold'] for entry in data]
robot_assistants_sold = [entry['Robot Assistants Sold'] for entry in data]

plt.figure(figsize=(16, 10))

plt.plot(months, vr_headsets_sold, label='VR Headsets Sold', color='#1f77b4', linestyle='-', marker='o')
plt.plot(months, ar_glasses_sold, label='AR Glasses Sold', color='#ff7f0e', linestyle='--', marker='s')
plt.plot(months, smart_speakers_sold, label='Smart Speakers Sold', color='#2ca02c', linestyle='-.', marker='^')
plt.plot(months, robot_assistants_sold, label='Robot Assistants Sold', color='#d62728', linestyle=':', marker='x')

plt.title('Monthly Sales of Tech Gadgets in 2023', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Units Sold', fontsize=14)

plt.legend(loc='upper left')
plt.grid(True)

plt.xticks(rotation=45)
plt.yticks(range(0, 400, 50))

# Adding annotations
for i, txt in enumerate(vr_headsets_sold):
    plt.annotate(txt, (months[i], vr_headsets_sold[i]), textcoords="offset points", xytext=(0,5), ha='center')
for i, txt in enumerate(ar_glasses_sold):
    plt.annotate(txt, (months[i], ar_glasses_sold[i]), textcoords="offset points", xytext=(0,5), ha='center')
for i, txt in enumerate(smart_speakers_sold):
    plt.annotate(txt, (months[i], smart_speakers_sold[i]), textcoords="offset points", xytext=(0,5), ha='center')
for i, txt in enumerate(robot_assistants_sold):
    plt.annotate(txt, (months[i], robot_assistants_sold[i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.tight_layout()
plt.show()