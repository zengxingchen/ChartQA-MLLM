
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
web_development = [3000, 3200, 3400, 3300, 3500, 3700, 3800, 3900, 4100, 4200, 4300, 4400]
data_science = [4000, 4200, 4300, 4400, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300]
machine_learning = [3500, 3600, 3800, 3700, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600]

plt.figure(figsize=(16, 10))
plt.stackplot(months, web_development, data_science, machine_learning, 
              labels=['Web Development', 'Data Science', 'Machine Learning'],
              colors=['#FF5733', '#33FF57', '#3357FF'])

plt.title('Monthly Online Course Enrollment in Technology Fields', y=1.08)
plt.xlabel('Month')
plt.ylabel('Number of Enrollments')
plt.legend(loc='upper left')
plt.xticks(rotation=45)

peak_ds_sales = max(data_science)
peak_month = months[data_science.index(peak_ds_sales)]
plt.annotate(f'Peak Data Science Enrollments\n{peak_ds_sales} Enrollments',
             xy=(peak_month, peak_ds_sales),
             xytext=(peak_month, peak_ds_sales + 1000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

plt.tight_layout()
plt.show()