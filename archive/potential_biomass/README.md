# Biomass energy potential

## Repository structure
```
Agricultural residues      -- Folder with energy potential from agricultural reisudes
Livestock effluents        -- Folder with energy potential from Livestock effluents 
Forestry residues          -- Folder with energy potential from Forestry residues
readme_files               -- Folder with .png for readme.md file
```

Each folder contains the following data:

```
datapackage.json           -- Datapackage JSON file with themain meta-data
output_potential.csv       -- CSV data with the NUTS3 data set
forest_potential.png       -- PNG with example of nuts3 map for the README.md
```

## Documentation
The nuts3 data-set covers the following biomass sources:

### Agricultural residues
Original data at NUTS0 level from the Intelligent Energy Europe [1]  for energy potentials in PJ of straws, prunings and residues from agro-industrial processes (olive pits) have been spatialized on the base of Lucas dataset [2].


### Livestock effluents 
Original data from the Intelligent Energy Europe [1] on production of solid and liquid residues from breeding of the following livestock:

- pig
- cattle
- poultry
 
The whole energy potential in PJ has been spatialized on the base of the EURASTAT dataset **Holdings with manure storage facilities**.

### Forestry residues
Original data at country level from the Intelligent Energy Europe [1]. 

Results in terms of PJ of energy potential have been spatialized by using the Corine Land Cover.

## Description of the task

The present task provides data with following characteristics:

<table>
  <tr>
    <td> </td>
    <td>Spatial resolution</td>
    <td>Temporal resolution</td>
  </tr>
  <tr>
    <td>Biomass availability</td>
    <td>NUTS0</td>
    <td>yearly</td>
  </tr>
</table>

**Table 1.** Characteristics of data provided within Task 2.6 Renewable energy sources data collection and potential review.

In this task, we collected and re-elaborated data on energy potential of renewable sources at national level, in order to build datasets for all EU28 countries at NUTS3 level. We considered the following renewable sources: biomass, waste and wastewater, shallow geothermal, wind, and solar energy. These data will be used in the toolbox to map the sources of renewable thermal energy across the EU28 and support energy planning and policy.

### Biomass

Data on availability and potential of agricultural and forest biomass were retrieved from a 2014 report by Intelligent Energy Europe for the Biomass Policies project, "Outlook of spatial biomass value chains in EU28" [143]. The report presents data on the energetic potential of biomass expressed in PJ at NUTS0 level, without accounting for energy conversion or giving any indication of the technology employed to extract such potential.

The agricultural residues considered for energy generation have been selected from those included in the report, according to sustainability criteria. Residues from agricultural production and processes and effluents from livestock breeding have been included, while crops cultivated purposely for biofuel production have been excluded due to the prospective environmental impacts in terms of land use change, biodiversity losses and water resources depletion.

Agricultural residues are summarized in Table 2.

<table>
  <tr>
    <td>Crop</td>
    <td>Production Process</td>
    <td>Biomass</td>
  </tr>
  <tr>
    <td>Cereals (excluding maize and rice) </td>
    <td>Cereal production for food and fodder </td>
    <td>Straw  </td>
  </tr>
  <tr>
    <td>Maize  </td>
    <td>Maize production for food and fodder </td>
    <td>Stover </td>
  </tr>
  <tr>
    <td>Oilseed rape and sunflower </td>
    <td>Oil production </td>
    <td>Stubble  </td>
  </tr>
  <tr>
    <td>Sugar beet </td>
    <td>Sugar production </td>
    <td>Leaves and tops </td>
  </tr>
  <tr>
    <td>Rice  </td>
    <td>Rice production </td>
    <td>Straw  </td>
  </tr>
  <tr>
    <td>Olives  </td>
    <td>Oil production </td>
    <td>Pits  </td>
  </tr>
  <tr>
    <td>Olives  </td>
    <td>Olive and oil production </td>
    <td>Residues from pruning </td>
  </tr>
  <tr>
    <td>Citrus  </td>
    <td>Citrus production </td>
    <td>Residues from pruning </td>
  </tr>
  <tr>
    <td>Grape  </td>
    <td>Wine production </td>
    <td>Residues from pruning </td>
  </tr>
</table>

**Table 2.** Agricultural residues included in the calculation of energy potential from agricultural biomass.

The livestock effluents considered for energy generation were solid and liquid manure from breeding of cattle, pigs and poultry.  

Forest biomass includes two categories of residues originated from forest management, and in particular from wood harvest and processing residues (from industrial production and non): 

* Fuelwood and roundwood;
* Fuelwood and roundwood residues.

Tables on energy potential in PJ for each biomass at NUTS0 level have been extracted from the report, elaborated in R and unified in three (agriculture, forest, and livestock residues) output datasets containing the energy potential of biomass in PJ at national level.

#### Methodology

###### **_Agricultural biomass_**

To spatialize the data on energy potential of agricultural biomass at NUTS3 level, we used the LUCAS [144] framework, a survey that provides statistics on land use and land cover in the EU28 territory. LUCAS data are organized as a grid of georeferenced points, each characterized by a land use/cover class.

In order to identify the points of the LUCAS grid with land cover classes relevant to our research, i.e. those relative to the selected biomasses, the LUCAS database has been elaborated in R and the following land cover classes were extracted based on the residues: 

* Cereal straw: B11 – common wheat, B12 – durum wheat, B13 – barley,  B14 – rye, B15 – oats, B19 – other cereals
* Grain maize stover: B16 – maize 
* Rice straw: B17 – rice 
* Sugar beet leaves: B22 – sugar beet 
* Rape and sunflower stubble: B31 – sunflower, B32 – rape and turnip rape
* Citrus pruning: B76 – oranges, B77 – other citrus fruit 
* Olive pruning and pits: B81 – olive groves 
* Vineyard pruning: B82 – vineyards 

The LUCAS grid, including only the points belonging to the above listed classes, was then imported in Grass GIS, where it was possible to cross it with a vector file of the EU28 area at NUTS0 and NUTS3 level. The LUCAS points were counted at NUTS0 and NUTS3 level and again in R it was possible to establish the percentage of land cover points at NUTS3 level based on the total of each NUTS0 area. These percentages were finally multiplied by the energy potential of each type of biomass at national level, resulting in an estimate of the potential of each biomass at NUTS3 level. The results are stored in a .csv table in the repository but they can also be visualized as a color-coded map created in QGIS.

###### **_Forest biomass_**

For the spatialization of data on energy potentials of forest biomass at NUTS3 level we used Corine Land Cover [1]. In Grass GIS it was possible to extract the land cover classes related to forest:  

* 3.1.1. Broad-leaved forest 
* 3.1.2. Coniferous forest 
* 3.1.3. Mixed forest 
* 3.2.1. Natural grassland 
* 3.2.2. Moors and heathland 
* 3.2.3. Sclerophyllous vegetation 
* 3.2.4. Transitional woodland shrub 

The raster file with the extracted classes was then used as a proxy to spatialize the data on forest potential at national level, at NUTS3 level. The results are stored in a .csv table in the repository but they can also be visualized as a color-coded map created in QGIS.

##### **_Livestock effluents_**

In order to spatialize the data on the energy potential of livestock effluents we used the EUROSTAT database statistics [145] on livestock head counts at NUTS2 and NUTS0 level for cattle, pigs and poultry.

In R it was possible to establish the percentage of cattle, pigs and poultry at NUTS2 level, based on the total of each NUTS0 area. These percentages were multiplied by the energy potential of each effluent at national level, resulting in an estimate of the potential of each biomass type at NUTS2 level. The data were first imported in Grass GIS for the creation of the vector at NUTS2 level and finally the visualization of results was performed in QGIS. An estimate at NUTS3 level was also possible, without considering the type of animal, from which the effluents come from and using as proxy for the number of manure storage facilities at NUTS3 level. The results are stored in a .csv table in the repository but they can also be visualized as a color-coded map created in QGIS.

### Limitations of data

The data here calculated are estimations of the energy potential from renewable energy sources. The hypotheses we made when deciding what data to consider, when re-elaborating the data at more aggregated territorial levels and finally when deciding how to convey the results, can influence the results.

In some cases, we underestimated the actual potential (biomass), by downscaling the available resource for sustainability reasons, in others, we overestimated the potential (wind, solar) due to our assumption of using all available areas, according only to some GIS sustainable criteria, where energy generation is feasible without considering economic profitability.

The potentials here reported **do not account for any type of energy conversion**: when estimating the actual potential, the user will need to choose the technology through which the potential can be exploited (for example COP for the wastewater treatment plant or the efficiency for solar thermal, photovoltaic and wind).

For these reasons, the data must be considered **as indicators, rather than absolute figures** representing the actual energy potential of renewable sources in a territory.

## References
[1] [Outlook of Spatial Biomass Value Chains in EU28](http://www.biomasspolicies.eu/wp-content/uploads/2014/12/Outlook-of-spatial-biomass-value-chains-in-EU28.pdf), Deliverable 2.3 of the Biomass Policies project, Intelligent Energy Europe, September 204
[2] [Land Use and Cover Area frame Survey](http://ec.europa.eu/eurostat/web/lucas/data/primary-data/2015), Eurostat, 2015

## How to cite

## Authors
Chiara Scaramuzzino <sup>*</sup>
Giulia Garegnani<sup>*</sup>,

<sup>*</sup> [Eurac Research](www.eurac.edu)
Institute for Renewable Energy
VoltaStraße/Via Via A. Volta 13/A
39100 Bozen/Bolzano

## License

Copyright © 2016-2018: Giulia Garegnani <giulia.garegnani@eurac.edu>,  Pietro Zambelli <pietro.zambelli@eurac.edu>
 
Creative Commons Attribution 4.0 International License
This work is licensed under a Creative Commons CC BY 4.0 International License.

SPDX-License-Identifier: CC-BY-4.0
License-Text: https://spdx.org/licenses/CC-BY-4.0.html


## Acknowledgement
We would like to convey our deepest appreciation to the Horizon 2020 [Hotmaps Project](http://www.hotmaps-project.eu/) (Grant Agreement number 723677), which provided the funding to carry out the present investigation.