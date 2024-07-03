
import matplotlib.pyplot as plt

# Data from the provided chart table
data = [
    {'Month': 'January', 'Quantum Computing': 150, 'Artificial Intelligence': 200, 'Blockchain': 180, 'Virtual Reality': 170, 'Cybersecurity': 160},
    {'Month': 'February', 'Quantum Computing': 160, 'Artificial Intelligence': 210, 'Blockchain': 185, 'Virtual Reality': 175, 'Cybersecurity': 165},
    {'Month': 'March', 'Quantum Computing': 170, 'Artificial Intelligence': 220, 'Blockchain': 190, 'Virtual Reality': 180, 'Cybersecurity': 170},
    {'Month': 'April', 'Quantum Computing': 180, 'Artificial Intelligence': 230, 'Blockchain': 195, 'Virtual Reality': 185, 'Cybersecurity': 175},
    {'Month': 'May', 'Quantum Computing': 190, 'Artificial Intelligence': 240, 'Blockchain': 200, 'Virtual Reality': 190, 'Cybersecurity': 180},
    {'Month': 'June', 'Quantum Computing': 200, 'Artificial Intelligence': 250, 'Blockchain': 210, 'Virtual Reality': 195, 'Cybersecurity': 185},
    {'Month': 'July', 'Quantum Computing': 210, 'Artificial Intelligence': 260, 'Blockchain': 215, 'Virtual Reality': 200, 'Cybersecurity': 190},
    {'Month': 'August', 'Quantum Computing': 220, 'Artificial Intelligence': 270, 'Blockchain': 220, 'Virtual Reality': 205, 'Cybersecurity': 195},
    {'Month': 'September', 'Quantum Computing': 230, 'Artificial Intelligence': 280, 'Blockchain': 225, 'Virtual Reality': 210, 'Cybersecurity': 200},
    {'Month': 'October', 'Quantum Computing': 240, 'Artificial Intelligence': 290, 'Blockchain': 230, 'Virtual Reality': 215, 'Cybersecurity': 205}
]

# Extracting month names for the x-axis
months = [entry['Month'] for entry in data]

# Plotting each technology's trend
plt.figure(figsize=(14, 10))
technologies = list(data[0].keys())[1:]  # Get technology names skipping the 'Month' key

# Line style settings and markers for each technology
line_styles = ['-', '--', '-.', ':']
markers = ['o', '^', 's', 'D', 'x']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#57FF33']

for i, tech in enumerate(technologies):
    values = [entry[tech] for entry in data]
    plt.plot(months, values, label=tech, linestyle=line_styles[i % len(line_styles)], marker=markers[i % len(markers)], color=colors[i % len(colors)])
    # Adding annotation for the last data point
    plt.text(months[-1], values[-1], f'{values[-1]}', fontsize=10, color=colors[i % len(colors)])

# Adding titles and labels
plt.title('Monthly Investment Trends in Emerging Technologies', pad=20)
plt.xlabel('Month')
plt.ylabel('Investment (in million USD)')

# Adding grid for readability
plt.grid(True)

# Adding a legend to identify the lines
plt.legend(title='Technologies', loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()