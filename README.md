<!-- Center the main title -->
<h1 align="center">Rapid and label-free Influenza A subtyping using surface-enhanced Raman spectroscopy with incident-wavelength analysis</h1>

<h5 align='center'>This project tests the incident wavelength of Raman spectroscopy (785 nm vs 532) to detect viruses. Additionally, we test the robustness of our previously published platform by introducing biological replicates (having separate growth cultures), variation between runs, and variation in the CNT platform. Finally, we demonstrate how this technology works in the real world by performing a data simulation.</h5>


## Table of Contents
- [Table of Contents](#table-of-contents)
- [Manuscript information](#manuscript-information)
- [Location of Files and Code](#location-of-files-and-code)

## Manuscript information

**_Rapid and label-free Influenza A subtyping using surface-enhanced Raman spectroscopy with incident-wavelength analysis_**    
RYEANNE RICKER<sup>1,2</sup>, NESTOR PEREA<sup>3</sup>,  MURRAY LOEW<sup>2</sup>, AND ELODIE GHEDIN<sup>1,*</sup>   

**Author Affiliations**: 
- <sup>1</sup>Affiliation 1
- <sup>2</sup>Affiliation 2
- <sup>2</sup>Affiliation 2

**For more information please contact**: [elodie.ghedin@nih.gov](mailto:main.author@example.com)

**Important links**:       
[Manuscript Link: Biomedical Optics Express](https://doi.org/10.1364/BOE.533457)   

**How to cite GitHub code and material**: DOI 10.5281/zenodo.11475062

---

## Location of Files and Code

- **Data**: [`data/`](https://github.com/GhedinSGS/Virus_Detection_Raman_Wavelength_Comparison/tree/main/data) - Collected at 100X magnification for 5 seconds with 400 spectra collected per biological replicate. 40 files in total, each with 400 spectra.
    - [`data/532nm`](https://github.com/GhedinSGS/Virus_Detection_Raman_Wavelength_Comparison/tree/main/data/532nm) - 20 files
        - Raw H1N1 samples - 10 files/10 biological replicates, each one containing 400 spectra
        - Raw H3N2 samples - 10 files/10 biological replicates, each one containing 400 spectra
    - [`data/785nm`](https://github.com/GhedinSGS/Virus_Detection_Raman_Wavelength_Comparison/tree/main/data/785nm) - 20 files
        - Raw H1N1 samples - 10 files/10 biological replicates, each one containing 400 spectra
        - Raw H3N2 samples - 10 files/10 biological replicates

- **Code**: [`codes/`](https://github.com/GhedinSGS/Virus_Detection_Raman_Wavelength_Comparison/tree/main/codes) - run in the following order: 
    1. `codes/preprocess.py` - preprocess the data
    2. `codes/cnn_h1n1_vs_h3n2_cv_plus_test.py` - CNN model that optimizes the hyperparameters and performs cross validation + testing
    3. `codes/rf_flu_subtype.py` - Random Forest model that is optimized, performs CV, and extracts feature importance
    4. `codes/random_sampling_experiment.py` - real world simulation
    5. `codes/visualizations_and_calculations.py` - visualizations and calculations/statistics

- **Results**: [`results/`](https://github.com/GhedinSGS/Virus_Detection_Raman_Wavelength_Comparison/tree/main/results) 
    - `results/AUC and accuracies` 
    - `results/t-tests` 
    - `results/Training Losses` 
    - `results/Simulation Results` 
    - `results/Feature Importance`
    - `results/Class Probabilities of Predictions on the Testing Samples`
    
---
