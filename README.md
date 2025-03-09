# Municipal farming area RAMP challenge

AVAKIAN Alexia, DEROUX Alexandre, ERRAJI Kenza, GUILLAUME Constantin, MARIN-BERTIN Guillaume, TOZZA Jean

## Introduction

The [dataset](https://www.data.gouv.fr/fr/datasets/historique-detaille-des-surfaces-cheptels-et-nombre-doperateurs-par-commune) originates from the agricultural agency [Agence Bio](https://www.agencebio.org) and aims to track farming activities across French municipalities from 2008 to 2023. It includes detailed information on the location of the farming parcels (region, department, etc.) and the usage of these parcels (surface, type of production, etc.).

This data covers metropolitan France and the DROMs. This is anonymized data, i.e. the information concerning the natural or legal person who cultivates these plots is absent.

The challenge is to design an algorithm able to predict the activity type (`code_activites`) based on the other characteristics of the farming parcels.

During recent years, a push for a more sustainable agriculture and farming practices has been made, with significant implications regarding environmental and health concerns.

Understanding farming activity patterns can help policy makers plan more appropriate initiatives in order to support farming organizations and farmers, encourage the transition to organic production, and improve the sustainability of practices. Previous policies can also be evaluated thanks to this.

## Getting started

### Install

To run a submission and the notebook you will need the dependencies listed
in `requirements.txt`. You can install install the dependencies with the
following command-line:

```bash
pip install -U -r requirements.txt
```

If you are using `conda`, we provide an `environment.yml` file for similar
usage.

### Create data

You need to create data.

In the "Data-Camp-Project" folder, run the following script:

```bash
python create_data.py
```

### Download data

You need to have this file in the data folder: data_municipal_farming_areas_2008_2023_agencybio.csv.

In the "Data-Camp-Project" folder, run the following script:

```bash
python download_data.py
```

### Challenge description

Let us analyze the dataset in more details.

It includes different types of information, among which we can find:

#### Year information
- `annee`: year of the record (from 2008 to 2023)

#### Geographic information
- `code_region`: numeric identifier for the region
- `region`: name of the region in France
- `code_departement`: numeric identifier for the department
- `departement`: name of the department
- `code_epci`: numeric identifier for the Public Inter-municipal Cooperation Establishments (Etablissements Publics de Coopération Intercommunale)
- `epci`: name of the EPCI
- `code_insee_commune`: numeric identifier assigned to the municipality by the National Institute of Statistics and Economic Studies, INSEE (Institut National de la Statistique et des Etudes Economiques)
- `code_postal_commune`: postal code of the municipality
- `commune`: name of the municipality

#### Farming activity
- `production_principale`: main type of production done in the municipality
- `activites`: type of farming activity 
- `code_activites`: categorical identifier for the activities

#### Surface usage indicators
- `nombre_operateurs`: number of operators involved in the famring activity
- `code_groupe_surface`: categorical identifier for the surface
- `nombre_exploitations_surface`: number of farms in the surface
- `surface_terme_conversion`: surface area that is converted for organic farming 
- `surface_conversion_annee_1`: surface area converted for organic farming in year 1
- `surface_conversion_annee_2`: surface area converted for organic farming in year 2
- `surface_conversion_annee_3`: surface area converted for organic farming in year 3
- `surface_totale_conversion`: total surface area converted for organic farming
- `surface_totale_bio`: total surface area currently certified for organic farming

#### Livestock presence indicators
- `code_groupe_cheptel`: categorical identifier defining the size and type of the livestock 
- `nombre_exploitations_cheptel`: number of farms that have livestock
- `cheptel_terme_conversion`: number of livestock currently being converted to organic
- `cheptel_conversion_simultanee`: number of livestock converted to organic at the same time as the land
- `cheptel_conversion_non_simulatanee`: number of livestock converted to organic at a different time as the land
- `cheptel_total_bio`: total number of organic livestock

The challenge is to predict farming activity categories based on these characteristics.

### Test a submission

The submissions need to be located in the `submissions` folder. For instance
for `my_submission`, it should be located in `submissions/my_submission`.

To run a specific submission, you can use the `ramp-test` command line:

```bash
ramp-test --submission my_submission
```

You can get more information regarding this command line:

```bash
ramp-test --help
```

### To go further

You can find more information regarding `ramp-workflow` in the
[dedicated documentation](https://paris-saclay-cds.github.io/ramp-docs/ramp-workflow/stable/using_kits.html).