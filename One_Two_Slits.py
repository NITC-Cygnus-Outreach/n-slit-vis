import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox

# The electric field
screen = np.arange(-0.005, 0.005, 0.00001)

# The screen size
s = 0.01

# Distance between slits
a = 1 * 10 ** -3
# Distance between the plane containing slits and the screen
l2 = 50 * (10 ** -2)

# Slit width
sw = 100 * (10 ** -6)

# Wavelength
lmb = 500 * (10 ** -9)

# No of Slits
n = 1


def double_slit(slit_width, wavelength, screen_distance, distance_between_slits, X):
    """
    Takes in slit_width, wavelength, screen distance, distance between the two strings and a numpy array X(an array of distances from the center).
    Outputs an array of normalized intensities corresponding to X.
  """
    return ((np.cos((np.pi * distance_between_slits * X) / (wavelength * screen_distance))) ** 2)


def single_slit(slit_width, wavelength, screen_distance, X):
    """
    Takes in slit_width, wavelength, screen distance and a numpy array X(an array of distances from the center).
    Outputs an array of normalized intensities corresponding to X.
  """
    return ((np.sin((np.pi * slit_width * X) / (wavelength * screen_distance))) / (
                (np.pi * slit_width * X) / (wavelength * screen_distance))) ** 2


def slit(n, slit_width, wavelength, screen_distance, distance_between_slits, X):
    if n == 1:
        return single_slit(slit_width, wavelength, screen_distance, X)
    elif n == 2:
        return double_slit(slit_width, wavelength, screen_distance, distance_between_slits, X)
    else:
        print('Wrong n value')


intensity = slit(n, sw, lmb, l2, a, screen)

plot, = plt.plot(screen, intensity)
plt.xlabel("Distance from center")
plt.ylabel("Intensity")

axis = (plt.axes([0.72, 0.75, 0.14, 0.05]))
if n == 1:
    axis2 = (plt.axes([0.72, 0.65, 0.14, 0.05]))
axis3 = (plt.axes([0.72, 0.55, 0.14, 0.05]))
axis4 = (plt.axes([0.72, 0.45, 0.14, 0.05]))

axis5 = (plt.axes([0.72, 0.35, 0.14, 0.05]))

wavelength_slider = Slider(axis, 'Wavelength(nm)', 100, 1000, valinit=lmb * 10 ** 9)
if n == 1:
    slit_width_slider = Slider(axis2, "Slit Width(micrometers)", 10, 1000, valinit=sw * 10 ** 6)
screen_distance_slider = Slider(axis3, "Screen Distance(cm)", 10, 100, valinit=l2 * 10 ** 2)
distance_between_slits_slider = Slider(axis4, "Distance b/w slits(mm)", 0.1, 10, valinit=a * 10 ** 3)

no_of_slits_slider = Slider(axis5, "No of slits", 1, 2, valinit=n,valstep=1.0)
#no_of_slits_box = TextBox(axis5, "No of Slits ", '1')


def update(val):
    wavelength = wavelength_slider.val * (10 ** -9)
    slit_width = slit_width_slider.val * (10 ** -6)
    screen_distance = screen_distance_slider.val * (10 ** -2)
    distance_between_slits = distance_between_slits_slider.val * (10 ** -3)
    no_of_slits = no_of_slits_slider.val
    intensity = slit(no_of_slits, slit_width, wavelength, screen_distance, distance_between_slits, screen)

    plot.set_ydata(intensity)



wavelength_slider.on_changed(update)
slit_width_slider.on_changed(update)
screen_distance_slider.on_changed(update)
distance_between_slits_slider.on_changed(update)
no_of_slits_slider.on_changed(update)

plt.show()
