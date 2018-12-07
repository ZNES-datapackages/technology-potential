import pandas as pd
from datapackage import Package
# data from:
# https://gitlab.com/hotmaps/potential/potential_municipal_solid_waste
# https://gitlab.com/hotmaps/potential/potential_biomass

# waste ------------------------------------------------------------------------
waste = pd.read_csv('archive/potential_municipal_solid_waste/data/solid_waste.csv')
waste['country'] = waste['code'].apply(lambda x: x[0:2])
# waste was 0.9 % of total electricity demand of 530 TWh -> 4.7 TWhel
# assuming conversion efficiency of 0.3 for waste to electricity
# this leadas to 8.27 TWh
# waste.groupby(['country']).sum().at['DE', 'value'] / 3.6 * 0.3

waste = waste.groupby(['country']).sum() / 3.6 # PJ to TWh
waste = waste.drop(['Unnamed: 0', 'code_label', 'nuts_level'], axis=1)
waste['carrier'] = 'waste'
waste['source'] = 'hotmaps'
waste.to_csv('data/carrier.csv')

agr = pd.read_csv('archive/potential_biomass/data/agricultural_residues.csv')
agr['country'] = agr['code'].apply(lambda x: x[0:2])

forest = pd.read_csv('archive/potential_biomass/data/forest_residues.csv')
forest['country'] = forest['code'].apply(lambda x: x[0:2])

# biomass ----------------------------------------------------------------------
# Germany has 143,7 TWh_th heat demand based on biomass 2017
# https://www.umweltbundesamt.de/themen/klima-energie/erneuerbare-energien/erneuerbare-energien-in-zahlen#statusquo
# Therefore the total sustainable potential in germany is already used by
# the existing heat demand (or above assuming 0.8 eff, -> 120.13 TWh heat
# potential if all is used for heat
# pd.concat([agr, forest]).groupby(['country']).sum().at['DE','value'] / 3.6 * 0.8

biomass = pd.concat([agr, forest]).groupby(['country']).sum() / 3.6
biomass = biomass.drop(['Unnamed: 0', 'code_label', 'nuts_level'], axis=1)
biomass['carrier'] = 'biomass'
biomass['source'] = 'hotmaps'
biomass.to_csv('data/carrier.csv', mode='a', header=False)
biomass['source'] = 'hotmaps'
