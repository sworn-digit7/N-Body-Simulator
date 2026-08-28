# N-Body Gravitational Simulator

A Python-based N-body simulation that models the gravitational interactions between multiple bodies using numerical integration.

The project was built from first principles to explore the intersection of **physics, numerical methods, object-oriented programming, and scientific computing**.

The simulator can model predefined systems such as the Solar System and Earth–Moon system, as well as completely custom systems supplied by the user. Simulation results are visualised using Matplotlib, while energy conservation is used to evaluate the numerical accuracy and stability of the simulation.

---
<img width="638" height="484" alt="image" src="https://github.com/user-attachments/assets/7da780fc-6c06-421f-8574-4b8211708884" />

## Features

- 🌌 N-body gravitational simulation
- ☀️ Predefined Solar System model
- 🌍 Earth–Moon simulation
- 🛠️ Custom user-defined systems
- ⚙️ User-configurable simulation duration
- ⏱️ User-configurable timestep
- 📈 Automatic orbital visualisation
- ⚡ Kinetic and gravitational potential energy calculations
- 📊 Percentage energy-conservation error
- 🧱 Object-oriented design using Python classes
- 🧪 Unit testing with `pytest`
- 📐 SI units throughout the simulation

---

## Project Overview

The gravitational N-body problem involves predicting the motion of multiple bodies interacting through gravity.

For two bodies, the equations of motion can be solved relatively easily. However, once additional bodies are introduced, every body affects every other body, making the system significantly more complex.

For a system containing \(N\) bodies, the gravitational acceleration of one body depends on the position and mass of every other body.

The simulator calculates these interactions at each timestep and updates the position and velocity of every body.

Conceptually:

```text
        Body 1
       ↙  ↓  ↘
   Body 2 → Body 3
       ↖  ↑  ↗
        Body 4
