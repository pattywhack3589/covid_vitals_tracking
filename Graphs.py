import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

# customizing runtime configuration stored
# in matplotlib.rcParams
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.arange(0, 15, 0.1)

# list oxygen saturation
o2 = [96, 99, 98, 97, 99, 100, 97, 97, 99, 98]

# plot O2
fig1 = plt.figure()
plt.plot(o2, 'black')

# Filling regions
plt.fill_between(x, 95, 100, color='green',
                 alpha=0.5)
plt.fill_between(x, 92, 94.99, color='yellow',
                 alpha=0.5)
plt.fill_between(x, 85, 91.99, color='red',
                 alpha=0.5)
plt.title('Oxygen Saturation (SpO2)')
plt.xlabel('Measurement #')
plt.ylabel('SpO2 [%]')

# list temperature
temp = [99.8, 99.5, 98.1, 97.4, 97.6, 97.9, 97.5, 97.4, 97.3, 97.5, 97.5]

# plot temperature
fig2 = plt.figure()
plt.plot(temp, 'black')

# Filling regions
plt.fill_between(x, 96, 100.49, color='green',
                 alpha=0.5)
plt.fill_between(x, 100.5, 102.19, color='yellow',
                 alpha=0.5)
plt.fill_between(x, 102.2, 103.99, color='orange',
                 alpha=0.5)
plt.fill_between(x, 104, 107, color='red',
                 alpha=0.5)
plt.title('Temperature')
plt.xlabel('Measurement #')
plt.ylabel('Temperature [deg F]')

# list systolic blood pressure
sys = [120, 108, 102, 125, 102, 127, 104, 114, 104, 112, 104]

# plot systolic blood pressure
fig3 = plt.figure()
plt.plot(sys, 'black')

# Filling regions
plt.fill_between(x, 60, 90.99, color='red',
                 alpha=0.5)
plt.fill_between(x, 91, 119.99, color='green',
                 alpha=0.5)
plt.fill_between(x, 120, 139.99, color='yellow',
                 alpha=0.5)
plt.fill_between(x, 140, 179.99, color='orange',
                 alpha=0.5)
plt.fill_between(x, 180, 210, color='red',
                 alpha=0.5)
plt.title('Systolic Blood Pressure (Top #)')
plt.xlabel('Measurement #')
plt.ylabel('Pressure [mmHg]')

# list diastolic blood pressure
dia = [80, 55, 53, 54, 65, 78, 61, 62, 49, 68, 66]

# plot diastolic blood pressure
fig4 = plt.figure()
plt.plot(dia, 'black')

# Filling regions
plt.fill_between(x, 30, 59.99, color='red',
                 alpha=0.5)
plt.fill_between(x, 60, 79.99, color='green',
                 alpha=0.5)
plt.fill_between(x, 80, 89.99, color='yellow',
                 alpha=0.5)
plt.fill_between(x, 90, 119.99, color='orange',
                 alpha=0.5)
plt.fill_between(x, 120, 150, color='red',
                 alpha=0.5)
plt.title('Diastolic Blood Pressure (Bottom #)')
plt.xlabel('Measurement #')
plt.ylabel('Pressure [mmHg]')

# list MAP
map = [93, 73, 69, 78, 77, 94, 75, 79, 67, 83, 79]

# plot MAP
fig5 = plt.figure()
plt.plot(map, 'black')

# Filling regions
plt.fill_between(x, 65, 100, color='green',
                 alpha=0.5)
plt.fill_between(x, 30, 64.99, color='red',
                 alpha=0.5)
plt.title('Mean Arterial Pressure (MAP)')
plt.xlabel('Measurement #')
plt.ylabel('Pressure [mmHg]')


def save_image(filename):
    # PdfPages is a wrapper around pdf
    # file so there is no clash and create
    # files with no error.
    p = PdfPages(filename)

    # get_fignums Return list of existing
    # figure numbers
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]

    # iterating over the numbers in list
    for fig in figs:
        # and saving the files
        fig.savefig(p, format='pdf')

        # close the object
    p.close()


# name pdf file
filename = "COVID Tracking.pdf"

# call the function
save_image(filename)


