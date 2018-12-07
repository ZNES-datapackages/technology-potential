# Municipal solid waste energy potential

## Repository structure

```
datapackage.json           -- Datapackage JSON file with themain meta-data
output_potential.csv       -- CSV data with the NUTS3 data set
```

## Description
Data show the total energy potential of municipal solid waste from household and economic activities - NACE - in the EU28 at NUTS3 level. Data at national level have been spatialized on the number of people (for household waste) and on the GDP (for NACE waste).

### Municipal solid waste

For calculating the energy potential of waste we decided to consider only one type of waste: municipal solid waste (MSW). Again, this decision was motivated by sustainability criteria: all recyclable waste should not be considered as energy source, hence the exclusion of paper and cardboard and wood waste. Food, vegetal waste and used frying oil (UFO) should not be included in the estimation of the potential since they should be employed in compost production. The method for generating thermal energy from MSW is not specified here: it could either be combustion or anaerobic digestion. Thus, the numbers stated for the potential of municipal solid waste are given in terms of its calorific value.

#### Methodology

The data on municipal solid waste generation from households and economic activities (NACE) in the EU28 in tons were collected from the Eurostat Database for the year 2014. By using the parameters presented in Table 3 [147], it was possible to quantify the energy potential of waste from household and NACE activities in PJ.

<table>
  <tr>
    <td>Parameter</td>
    <td>Value</td>
    <td>Unit</td>
  </tr>
  <tr>
    <td>Waste low heating value (c)</td>
    <td>13.81644</td>
    <td>MJ/Kg</td>
  </tr>
  <tr>
    <td>Equivalence ratio (ER)</td>
    <td>0.340656</td>
    <td>-</td>
  </tr>
</table>

**Table 3.** Parameters for calculating energy potential of municipal solid waste. Source: [147]

In R, we obtained the value for waste potential in PJ at national level, according to the following equation (7), where Pwaste is the potential of waste and Qwaste the quantity of available waste [147].

```
P(waste) = Q(waste) * c * ER     (7)
```

##### **_Household waste_**

Once we had the potential of MSW at national level we used the population statistics from the Eurostat Database for the year 2011 as proxy to spatialize the potential of household waste at NUTS3 level. R elaborations allowed us to calculate the percentages of population in each province with respect to the total national populations and to multiply the results by the energy potentially generated from this waste.

##### **_Economic activities waste (NACE)_**

The potential of MSW from different NACE activities at NUTS3 level was obtained by using the GDP statistics at NUTS3 level from the Eurostat Database for the year 2014 as a proxy. The procedure adopted was then the same of the one used for household MSW.

## Limitations of data

The data here calculated are estimations of the energy potential from renewable energy sources. The hypotheses we made when deciding what data to consider, when re-elaborating the data at more aggregated territorial levels and finally when deciding how to convey the results, can influence the results.

In some cases, we underestimated the actual potential (biomass), by downscaling the available resource for sustainability reasons, in others, we overestimated the potential (wind, solar) due to our assumption of using all available areas, according only to some GIS sustainable criteria, where energy generation is feasible without considering economic profitability.

The potentials here reported **do not account for any type of energy conversion**: when estimating the actual potential, the user will need to choose the technology through which the potential can be exploited (for example COP for the wastewater treatment plant or the efficiency for solar thermal, photovoltaic and wind).

For these reasons, the data must be considered **as indicators, rather than absolute figures** representing the actual energy potential of renewable sources in a territory.

## How to cite

## Authors
Chiara Scaramuzzino <sup>*</sup>,
Giulia Garegnani<sup>*</sup>

<sup>*</sup> [Eurac Research](www.eurac.edu)
Institute for Renewable Energy
VoltaStrae/Via Via A. Volta 13/A
39100 Bozen/Bolzano

## License

Copyright © 2016-2018: Giulia Garegnani <giulia.garegnani@eurac.edu>,  Pietro Zambelli <pietro.zambelli@eurac.edu>
 
Creative Commons Attribution 4.0 International License
This work is licensed under a Creative Commons CC BY 4.0 International License.

SPDX-License-Identifier: CC-BY-4.0
License-Text: https://spdx.org/licenses/CC-BY-4.0.html


## Acknowledgement
We would like to convey our deepest appreciation to the Horizon 2020 [Hotmaps Project](http://www.hotmaps-project.eu/) (Grant Agreement number 723677), which provided the funding to carry out the present investigation.