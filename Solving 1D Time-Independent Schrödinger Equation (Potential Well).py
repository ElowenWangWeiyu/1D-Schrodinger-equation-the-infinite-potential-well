import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# Constants
L = 10.0  # Length of the well
N = 100  # Number of grid points
dx = L / (N-1)
x = np.linspace(0, L, N)  # Position grid

# Note: ħ²/2m is set to 1 for simplicity, so the Hamiltonian uses a unitless form.
# Energies are normalised and must be scaled by (ħ²/2m) for physical units.

# Define the potential (Infinite well)
V = np.zeros(N)
V[0] = V[-1] = 1e10  # Infinite potential at the boundaries

# Set up the Hamiltonian matrix (discretised)
H = -0.5 * (np.diag(np.ones(N-1), -1) - 2 * np.diag(np.ones(N), 0) + np.diag(np.ones(N-1), 1)) / (dx**2)
H += np.diag(V)

# Convert to a QuTiP Qobj (quantum object)
H_qobj = Qobj(H)

# Solve for the eigenvalues (energies) and eigenstates (wavefunctions)
energies, wavefunctions = H_qobj.eigenstates()

# Normalise the wavefunctions
wavefunctions = [wf.full() / np.linalg.norm(wf.full()) for wf in wavefunctions]

# Plot the first few wavefunctions
plt.figure(figsize=(10, 6))
for i in range(5):
    plt.plot(x, wavefunctions[i], label=f"Energy = {energies[i]:.2f}")
plt.title("First Few Eigenfunctions of the 1D Quantum Well")
plt.xlabel("Position x")
plt.ylabel("Wavefunction ψ(x)")
plt.legend()
plt.grid(True)
plt.show()

# Print the first few energy levels
print("First few energy levels:")
for i in range(3):
    print(f"Energy {i+1} = {energies[i]:.2f}")
