# Power flows and their associated efficiency and reward chains

## Table of contents
* [Power flows at HEV Powertrain level](#power-flows)
* [Subsystem chains](#subsystem-chains)
* [Efficiency chains](#efficiency-chain)
* [Reward chains](#reward-chains)

## Power flows at HEV Powertrain level
* Elementary flows
    * ICE -> main transmission -> wheels
    * battery -> EM -> EM transmission -> wheels
    * ICE -> EG transmission -> EG -> battery

* Combined flows
    * (ICE -> main transmission -> wheels &&
          battery -> EM -> EM transmission -> wheels)
    * (ICE -> main transmission -> wheels &&
          ICE -> EG transmission -> EG -> battery)
    * (ICE -> main transmission -> wheels &&
          battery -> EM -> EM transmission -> wheels &&
          ICE -> EG transmission -> EG -> battery)

## Subsystem chains
* ICE -> main transmission -> wheels
* battery -> inverter -> EM -> EM transmission -> wheels
* ICE -> EG transmission -> EG -> rectifier-transformer -> battery

## Efficiency chains
* eta_ICE -> eta_main_trans
* eta_dch -> eta_inv -> eta_EM_trans -> eta_EM
* eta_EG_trans -> eta_EG -> eta_rectif -> eta_ch

## Reward chains
* specific fuel consumption
* ch-dch -> EM
* EG -> ch-dch

### Short abbreviations list and some clarifications
* Internal Combustion Engine = ICE
* Electric Motor = EM
* Electric Generator = EG
* Main transmission = involves gearbox, main gear ratio and differential
* EM transmission = involves EM reduction gear
* EG transmission = involves EG gear
* ch = battery charging process
* dch = battery discharging process
* eta_ICE = ICE efficiency
* eta_dch = battery discharging efficiency
* eta_ch = battery charging efficiency
* eta_inv = inverter efficiency
* eta_rectif = rectifier-transformer efficiency
* eta_main_trans = overall transmission efficiency
* eta_EM_trans = EM reduction gear efficiency
* eta_EG_trans = EG gear efficiency
