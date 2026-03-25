# 2D Heat Equation Simulation (Finite Difference Method)

## Overview

This project implements a numerical solution of the two-dimensional transient heat equation using the Finite Difference Method (FDM) in Python. The simulation models heat diffusion in a square domain under fixed boundary conditions.

## Governing Equation

∂T/∂t = α (∂²T/∂x² + ∂²T/∂y²)

## Methodology

* Discretization: Finite Difference Method (Explicit Scheme)
* Stability condition: rₓ + rᵧ ≤ 0.5
* Grid: 50 × 50
* Time-stepping: Explicit iteration

## Features

* 2D heat diffusion simulation
* Stability analysis of numerical scheme
* Time evolution visualization (Initial, Mid, Final states)
* Automated result saving

## Results

The simulation demonstrates heat propagation from high-temperature boundaries into the domain, showing smooth diffusion under stable conditions and instability when the time step is increased.

## Tools Used

* Python
* NumPy
* Matplotlib

## How to Run

```bash
python src/heat_2d.py
```

## Output

* Heat distribution plots
* Saved image: `results/heat_evolution.png`

## Learning Outcome

This project strengthened my understanding of:

* Numerical solution of PDEs
* Stability conditions in finite difference methods
* Scientific computing using Python
