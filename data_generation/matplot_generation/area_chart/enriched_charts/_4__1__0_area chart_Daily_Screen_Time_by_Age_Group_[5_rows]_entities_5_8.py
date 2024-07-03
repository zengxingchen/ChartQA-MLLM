
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Day": list(range(1, 31)),
    "Visitors": [120, 135, 145, 150, 160, 175, 190, 205, 220, 240, 260, 280, 295, 310, 325, 340, 360, 380, 400, 420, 450, 470, 490, 510, 530, 550, 575, 600, 625, 650]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 10))
ax.fill_between(df["Day"], df["Visitors"], color="#FF5733", alpha=0.7)

ax.set_title("Daily Museum Visitors Over a Month", fontsize=20, pad=20)
ax.set_xlabel("Day", fontsize=16)
ax.set_ylabel("Number of Visitors", fontsize=16)
ax.grid(True, linestyle='--', alpha=0.5)

for i, txt in enumerate(df["Visitors"]):
    ax.annotate(txt, (df["Day"][i], df["Visitors"][i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.show()