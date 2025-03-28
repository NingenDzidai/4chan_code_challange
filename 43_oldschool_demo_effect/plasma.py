# the whole idea described in the link below
# https://web.archive.org/web/20210922045757/https://www.bidouille.org/prog/plasma
 
import math as m
import numpy as np
import matplotlib.pyplot as plt

def sin_vert(arr, time):
    val_array = [m.sin(arr[i] * 10 + time) for i in range(size)]
    image_array = np.tile(val_array, (size, 1))
    return image_array

def sin_angle(X, Y, time):
    return np.sin(10 * (X * np.sin(time / 2)) + Y * np.cos(time / 3) + time)

def sin_rotate(X, Y, time):
    cx = X + 0.5*np.sin(time/5)
    cy = Y + 0.5*np.cos(time/3)
    return np.sin(np.sqrt(100*(cx*cx+cy*cy)+1) + time)

def on_key(event):
    global running
    if event.key == 'q':
        running = False

time = 0
size = 128 
x = np.linspace(-0.5, 0.5, size)
y = np.linspace(-0.5, 0.5, size)
X, Y = np.meshgrid(x, y, indexing='ij')

plt.ion()
fig, ax = plt.subplots()

sin_angle_arr = sin_angle(x, y, time)  
sin_vert_arr = sin_vert(x, time)  
sin_rotate_arr = sin_rotate(x, y, time)

image_array = sin_rotate_arr + sin_vert_arr + sin_angle_arr
im = ax.imshow(image_array, cmap="gray", animated=True)
im.set_clim(-3, 3) # Fixed color range

running = True
fig.canvas.mpl_connect('key_press_event', on_key) # connecting keyboard event to the canvas


while running:
    time += 0.3

    sin_angle_arr = sin_angle(X, Y, time)  
    sin_vert_arr = sin_vert(x, time)  
    sin_rotate_arr = sin_rotate(X, Y, time)

    image_array = sin_rotate_arr + sin_vert_arr + sin_angle_arr 
    im.set_data(image_array) # fun fuct: .imcshow creates and rendres a new object evety time it is calle, .set_data simply updates colors 

    plt.pause(0.01)  

plt.ioff()