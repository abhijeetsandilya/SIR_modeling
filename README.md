# SIR_modeling
The SIR model (Susceptible-Infected-Removed) is a fundamental, simple mathematical model used in epidemiology to predict the theoretical spread and dynamics of a contagious disease within a fixed, closed population over time.

This project simulates how an infectious disease spreads through a population using the SIR model.
It’s a simple mathematical model but surprisingly powerful for understanding outbreaks, peaks, and how long an infection sticks around.

## 1. What the SIR Model Actually Is

The model splits a population into three groups:

### S – Susceptible
People who can catch the disease.

### I – Infected
People who currently have the disease and can spread it.

### R – Recovered
People who had the infection and are now immune (or removed).

The idea is that people “flow” from S → I → R over time.
The flow is controlled by two things:

### β (beta) – How easily the disease spreads.
Higher β → infections explode quickly.

### γ (gamma) – How fast infected people recover.
Higher γ → infections die out sooner.

The model uses differential equations:

dS/dt = – (β * S * I) / N

dI/dt = (β * S * I) / N – γI

dR/dt = γI

more infected people means more spread; more recovery means fewer infected.

## 2. What the Code Is Doing

The code basically does four things:

Sets the population and parameters

Uses the SIR differential equations to calculate how S, I, and R change over time

Uses the RK4 numerical method (a standard ODE solver) to simulate day-by-day movement

Plots the results and saves a CSV with the numbers

The core math is in sir_model.py.
run_sir.py just calls that math, plots the output, and prints some useful numbers like:

when infections peak

how big the peak is

what percentage of people end up recovering

basic reproduction number R₀ (= β / γ)

## 3. The Parameters Used in This Simulation

These are the values chosen by default:

Total population (N): 1,000,000

Initial infected: 10

Initial recovered: 0

Initial susceptible: everything else

β (beta): 0.3

γ (gamma): 0.1

This gives:

R₀ = β / γ = 3.0
Meaning each infected person infects an average of 3 others in a fully susceptible population.

This is high enough to create a noticeable outbreak curve.

Simulation time: 160 days

Time resolution: 1600 steps
(0.1 day per step)

The RK4 solver handles the math so you don’t have to solve any equations manually.

## 4. What You Get After Running It

A plot showing how S, I, and R change over time

A CSV file (sir_output.csv) with every value for each time step

Printed stats like:

peak infection proportion

the day peak occurs

final recovered percentage

You can edit the parameters in run_sir.py to model anything from a mild seasonal infection to a massive epidemic
