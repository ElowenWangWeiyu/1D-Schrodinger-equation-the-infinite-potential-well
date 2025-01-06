# 1D infinite quantum well simulation
This project is a Python-based simulation of a 1D infinite quantum well. It calculates and visualizes the first few eigenfunctions (wavefunctions) and eigenvalues (energies) of the system using the time-independent Schrödinger equation. The simulation uses the QuTiP library for quantum mechanics calculations and provides insights into fundamental quantum mechanics concepts.

## Features

- Solve the Schrödinger equation for a particle in a 1D infinite potential well.
- Visualize the first few energy eigenstates and their corresponding wavefunctions.
- Print the first five energy levels.

## How it works

1. The system models a particle in a box (infinite potential well):
- The boundaries of the well have infinite potential.
- The potential inside the well is zero.
2. The Schrödinger equation is solved numerically using matrix diagonalization:
- The term ℏ^2/2𝑚 is set to 1 for simplicity (normalized units).
- The results are dimensionless and need scaling for physical units.
3. The eigenvalues correspond to the energy levels, and the eigenvectors represent the wavefunctions.

## How to Use

- Clone the repository to your local machine.
- Install the required dependencies: pip install numpy matplotlib qutip
- Run the script: Solving 1D Time-Independent Schrödinger Equation (Potential Well).py

## Customisation
You can modify the simulation parameters in Solving 1D Time-Independent Schrödinger Equation (Potential Well).py:
- Length of the well (L): The physical size of the well.
- Number of grid points (N): Determines the resolution of the simulation.
- Boundary conditions: Adjust the infinite potential values if needed.
- the order of energy eigenstates and their corresponding wavefunctions visualised.

## Example Output

Here is the expected output with the parameters in the script. The output will be different with customised simulation parameters of your choice.

## Dependencies
- Python 3.x
- `matplotlib`
- `numpy`
- `qutip`

## License
This project is licensed under the
