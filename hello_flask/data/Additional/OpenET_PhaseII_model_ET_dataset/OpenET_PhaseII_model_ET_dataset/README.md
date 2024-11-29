# OpenET model data for assessing the accuracy of OpenET satellite-based evapotranspiration data to support water resource and land management applications

This dataset includes daily and monthly evapotranspiration (ET) data from the remote sensing models that comprise the [OpenET](https://openetdata.org/) ensemble as described in Melton et al., 2022 (https://doi.org/10.1111/1752-1688.12956); these data were extracted at specific locations within the contiguous United States that coincide with *in situ* measurement stations, including eddy covaraiance, Bowen-ratio, and lysimeter stations. Model ET data where extracted at each site in this dataset using flux footprints as described in Volk et al., (2023) (https://doi.org/10.1016/j.agrformet.2023.109307). These model data alongside the corresponding *in situ* ET data (https://doi.org/10.1016/j.dib.2023.109274) were subsequently used in the manuscript for the OpenET Phase II Intercomparison and Accuracy Assessment (https://doi.org/10.1038/s44221-023-00181-7). 


## Description of the data and file structure

The dataset is in a compressed (zipped) archive titled "OpenET_PhaseII_model_ET_dataset", so first it needs to be downloaded and extracted. The dataset is comprised of just three files. The first file is a Microsoft Excel file "Station_metadata.xlsx" that contains information about the *in situ* ET measurement stations where the OpenET model data was extracted. This file contains information such as site ID's, coordinates, land cover information, and site principal investigator (PI) contact information. Again, the corresponding *in situ* ET data are not included in this dataset. The other two files are tab-delimited text files containing timeseries the OpenET model data themselves, namely the daily ET [mm/day] and monthly ET [mm/month] as extracted for each model and the ensemble value as used in the OpenET Phase II Intercomparison and Accuracy Assessment. 


## Access information and code/software

OpenET data that was used here was produced using operational methods that are implemented on the Google Earth Engine platform. Monthly OpenET model data can be retrieved through Google Earth Data Catalog (e.g., https://developers.google.com/earth-engine/datasets/catalog/OpenET_ENSEMBLE_CONUS_GRIDMET_MONTHLY_v2_0) or through the [online data explorer](https://openetdata.org/) or using the [OpenET API](https://openetdata.org/api-info/).


## Citation

Volk, J. M., Huntington, J.L., Melton, F.S., Allen, R., Anderson, M., Fisher, J. B., Kilic, A., Ruhoff, A., Senay, G. B., Minor, B., Morton, C., Ott, T., Johnson, L., Andrade, B. C. D., Carrara, W., Doherty, C. T., Dunkerly, C., Friedrichs, M., Guzman, A., Hain, C., Halverson, G., Kang, Y., Knipper, K., Laipelt, L., Ortega-Salazar, S., Pearson, C., Parrish, G. E. L., Purdy, A., ReVelle, P., Wang, T., and Yang, Y.. Assessing the accuracy of OpenET satellite-based evapotranspiration data to support water resource and land management applications. Nature Water (2023). DOI: 10.1038/s44221-023-00181-7 
