
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Constants
v_ball_train = -20  # Velocity of the ball as measured by the observer inside the train (m/s)
v_train = 40  # Velocity of the train (m/s)
t_max = 5  # Maximum time (s)
dt = 0.1  # Time step (s)

# Derived quantities
v_ball_platform = v_ball_train + v_train  # Velocity of the ball as measured by the stationary observer on the platform (m/s)

# Create figure and axis
fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(8, 8))

# Set up the axis for observer inside the train
ax1.set_xlabel('Distance (m)')
ax1.set_ylabel('Position (m)')
ax1.set_title('Ball Motion as Observed from Inside the Train')

# Set up the axis for observer on the platform
ax2.set_xlabel('Distance (m)')
ax2.set_ylabel('Position (m)')
ax2.set_title('Ball Motion as Observed from the Platform')

# Adjust layout to create space between subplots
plt.subplots_adjust(hspace=0.5)

# Initialize ball and train positions
ball_x_train = [0]
ball_y_train = [0]
train_x = [0]

ball_x_platform = [0]
ball_y_platform = [0]
train_x_platform = [0]

# Animation function
def animate(i):
    t = i * dt
    ball_x_train.append(v_ball_train * t)
    ball_y_train.append(0)
    train_x.append(v_train * t)

    ball_x_platform.append(v_ball_platform * t)
    ball_y_platform.append(0)
    train_x_platform.append(v_train * t)

    ax1.clear()
    ax1.set_xlim(0, v_train * t_max)
    ax1.set_ylim(-20, 20)
    ax1.set_xlabel('Distance (m)')
    ax1.set_ylabel('Position (m)')
    ax1.set_title('Ball Motion as Observed from Inside the Train')
    ax1.plot(ball_x_train, ball_y_train, 'ro', label='Ball')
    ax1.plot(train_x, [0] * len(train_x), 'b-', label='Observer along with the Train')
    ax1.legend()

    ax2.clear()
    ax2.set_xlim(0, v_train * t_max)
    ax2.set_ylim(-20, 20)
    ax2.set_xlabel('Distance (m)')
    ax2.set_ylabel('Position (m)')
    ax2.set_title('Ball Motion as Observed from the Platform')
    ax2.plot(ball_x_platform, ball_y_platform, 'ro', label='Ball')
    ax2.plot(train_x_platform, [0] * len(train_x_platform), 'b-', label='Train')
    ax2.legend()

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=int(t_max / dt), interval=10, repeat=False)

# Display animation
plt.show()

