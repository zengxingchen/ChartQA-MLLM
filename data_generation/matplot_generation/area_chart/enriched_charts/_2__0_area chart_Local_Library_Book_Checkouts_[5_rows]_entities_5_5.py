
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Date': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01', '2024-06-01', 
             '2024-07-01', '2024-08-01', '2024-09-01', '2024-10-01', '2024-11-01', '2024-12-01'],
    'Attendance': [150, 180, 220, 300, 400, 450, 480, 470, 420, 350, 250, 200]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(14, 8))
sns.set(style="whitegrid")

sns.lineplot(data=df, x='Date', y='Attendance', color="#FF6347")
plt.fill_between(df['Date'], df['Attendance'], alpha=0.3, color="#FF6347")

max_attendance = df['Attendance'].max()
max_attendance_date = df.loc[df['Attendance'] == max_attendance, 'Date'].iloc[0]
plt.text(x=max_attendance_date, y=max_attendance, s='Peak\n{} Attendees'.format(max_attendance), color="black",
         horizontalalignment='left', size='medium', style='italic')

plt.title("Monthly Event Attendance in 2024", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Attendance")

plt.show()