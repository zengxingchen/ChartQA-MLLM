
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Renewable Energy': 250, 'Quantum Computing': 100, 'AI Development': 300, 'Space Exploration': 400, 'Green Architecture': 150},
    {'Month': 'February', 'Renewable Energy': 270, 'Quantum Computing': 110, 'AI Development': 320, 'Space Exploration': 420, 'Green Architecture': 160},
    {'Month': 'March', 'Renewable Energy': 290, 'Quantum Computing': 120, 'AI Development': 340, 'Space Exploration': 440, 'Green Architecture': 170},
    {'Month': 'April', 'Renewable Energy': 310, 'Quantum Computing': 130, 'AI Development': 360, 'Space Exploration': 460, 'Green Architecture': 180},
    {'Month': 'May', 'Renewable Energy': 330, 'Quantum Computing': 140, 'AI Development': 380, 'Space Exploration': 480, 'Green Architecture': 190},
    {'Month': 'June', 'Renewable Energy': 350, 'Quantum Computing': 150, 'AI Development': 400, 'Space Exploration': 500, 'Green Architecture': 200},
    {'Month': 'July', 'Renewable Energy': 370, 'Quantum Computing': 160, 'AI Development': 420, 'Space Exploration': 520, 'Green Architecture': 210},
    {'Month': 'August', 'Renewable Energy': 390, 'Quantum Computing': 170, 'AI Development': 440, 'Space Exploration': 540, 'Green Architecture': 220},
    {'Month': 'September', 'Renewable Energy': 410, 'Quantum Computing': 180, 'AI Development': 460, 'Space Exploration': 560, 'Green Architecture': 230},
    {'Month': 'October', 'Renewable Energy': 430, 'Quantum Computing': 190, 'AI Development': 480, 'Space Exploration': 580, 'Green Architecture': 240},
    {'Month': 'November', 'Renewable Energy': 450, 'Quantum Computing': 200, 'AI Development': 500, 'Space Exploration': 600, 'Green Architecture': 250},
    {'Month': 'December', 'Renewable Energy': 470, 'Quantum Computing': 210, 'AI Development': 520, 'Space Exploration': 620, 'Green Architecture': 260}
]

months = [entry['Month'] for entry in data]
renewable_energy = [entry['Renewable Energy'] for entry in data]
quantum_computing = [entry['Quantum Computing'] for entry in data]
ai_development = [entry['AI Development'] for entry in data]
space_exploration = [entry['Space Exploration'] for entry in data]
green_architecture = [entry['Green Architecture'] for entry in data]

plt.figure(figsize=(14, 7))
plt.plot(months, renewable_energy, marker='o', linestyle='-', color='#1f78b4', label='Renewable Energy')
plt.plot(months, quantum_computing, marker='s', linestyle='--', color='#33a02c', label='Quantum Computing')
plt.plot(months, ai_development, marker='^', linestyle='-.', color='#e31a1c', label='AI Development')
plt.plot(months, space_exploration, marker='x', linestyle=':', color='#ff7f00', label='Space Exploration')
plt.plot(months, green_architecture, marker='d', linestyle='-', color='#6a3d9a', label='Green Architecture')

plt.title('Future Technologies & Society: Monthly Research Investment Trends', pad=20)
plt.xlabel('Month')
plt.ylabel('Investment (in Million USD)')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()