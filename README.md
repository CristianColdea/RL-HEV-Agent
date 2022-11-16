# RL HEV Agent
> Reinforcement Learning (RL) Agent for intelligent management of a Hybrid Electric Vehicle (HEV) Powertrain

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
* The objective of this project is to code a Reinforcement Learning Agent able to manage the complex HEV Powertrain.
* The agent will work based on a number of reward shaping systems, i.e., a system of systems in a cybernetic way.
* Precisely this is going to be a Deep Q-Network agent.
* The reward shaping systems are as following:
    * charge-discharge;
    * fuel consumption map;
    * electric motor (EM) efficiency map;
    * gear shift.
## Screenshots
![Example screenshot](agent.png)

## Technologies
* Tech 1 - Plain _Python_ and its specialized lybraries;
* Tech 2 - _Keras_;
* Tech 3 - _TensorFlow_.

## Setup
Keep the scripts, files and modules in the same folder.
Also, some additional modules must be imported, i.e., fuel consumption simulator and electric motor efficiency map generator from the corresponding repos of this developer.

## Code Examples
Show examples of usage (just an example):
* Import fuel consumption simulator as a _Python module.
```
import sfc.py as sfc
```
* Call the specific fuel consumption simulator with the appropriated args.
```
sfc = sfc(arg1, arg2,  ...)
```

## Features
List of features ready and TODOs for future development
* Project started, README partially done.

To-do list:
* ~~Get ready the README file, with project outline.~~
* Code the charge-discharge reward system.
* Code gear shift reward system.
* Code the data gathering part of the RL agent.
* Assemble all the reward shaping systems.
* Code the neural network in order to model the DQ part.
* Train the agent and collect output.
* Collect vehicle parameters for testing.
* Code the WLTP cycle in order to get the road test parameters for a certain vehicle.
* Test the vehicle according to WLTP cycle, only Internal Combustion Engine powertrain.
* Test the vehicle according to WLTP cycle, HE powertrain.
* Results and analysis.

## Status
Project is: __in progress_.

## Inspiration
1) https://www.researchgate.net/publication/308830029_Efficiency_maps_of_electrical_machines
2) Ben-Chaim, Michael and Shmerling, Efraim. A Model of Vehicle Fuel Consumption at Conditions of the EUDC. International Journal of Mechanics.
3) Ben-Chaim, Michael, Shmerling, Efraim and Kuperman, Alon. Analytic Modeling of Vehicle Fuel Consumption. mdpi.com/journal/energies, 2013.
4) Schoen, Alexander et al. A Machine Learning Model for Average Fuel Consumption in Heavy Vehicles.

## Contact
rdt333@gmail.com - feel free to contact me!
