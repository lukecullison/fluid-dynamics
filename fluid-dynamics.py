from fipy import CellVariable, Grid1D, DiffusionTerm
import matplotlib.pyplot as plt
import numpy as np

# Parameters
length = 10.0  # Length of the pipe (meters)
num_cells = 3  # Number of grid cells
#num_cells = 100  # Number of grid cells
mu = 1.0  # Dynamic viscosity (Pa.s)
pressure_gradient = -1.0  # Pressure gradient (Pa/m)

# Create a 1D mesh
mesh = Grid1D(dx=length / num_cells, nx=num_cells)

# Define the velocity field variable
velocity = CellVariable(mesh=mesh, name="Velocity", value=0.0)

# Equation: d(mu * dU/dx)/dx = -dP/dx
equation = DiffusionTerm(coeff=mu) == pressure_gradient

# Boundary conditions: no-slip at both ends
velocity.constrain(0.0, mesh.facesLeft)  # Inlet
velocity.constrain(0.0, mesh.facesRight)  # Outlet

# Solve the equation
equation.solve(var=velocity)

# Visualization using Matplotlib
x = np.linspace(0, length, num_cells)  # Create x-coordinates

# Configure Matplotlib to use an interactive backend
plt.plot(x, velocity.value, label="Velocity Profile", color="blue")
plt.title("1D Velocity Distribution in a Pipe", fontsize=16)
plt.xlabel("Position along the pipe (m)", fontsize=14)
plt.ylabel("Velocity (m/s)", fontsize=14)
plt.grid(True)
plt.legend(fontsize=12)
plt.show(block=True)  # Ensure the plot stays open

