# RL HEV Agent
> Reinforcement Learning (RL) Agent for intelligent management of a Hybrid Electric (HEV) Powertrain

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
* The objective of this project is to have a Reinforcement Learning Agent able to manage the complex HEV Powertrain.
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
* Tech 1 - Plain _Python_ and specialized lybraries;
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
* Awesome feature 1
* Awesome feature 2
* Awesome feature 3

To-do list:
* Wow improvement to be done 1
* Wow improvement to be done 2

## Status
Project is: __in progress_.

## Inspiration
Add here credits. Project inspired by..., based on...

## Contact
Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!
