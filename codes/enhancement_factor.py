#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 09:09:35 2023

Author: RyeAnne Ricker

Title: Gold Nanoparticles Enhancement Factor



"""

#%%
# libraries
import pandas as pd # v 1.3.5
#import numpy as np # v 1.21.2
import matplotlib.pyplot as plt # v 3.1.0
#import scipy as sp # v 1.7.3
import os
import seaborn as sns
# python version 3.7.11


#%%
# Load the data
folder = '/Users/rickerr2/Library/CloudStorage/OneDrive-NationalInstitutesofHealth/Documents/LAB_STUFF/PEOPLE/rye/Publications/Optica Biomedical Optics Express (Submitted) - Raman Wavelength Comparison/data/enhancement_factor/glycine_no_cnts' # path
files = os.listdir(folder) # list of files at the path location
data_files = [] # list to store all ibv file dataframes in
names = [] # list to store the sample number - this is in the same order as the ibvfiles
counter = 0 # start counter at 0

for file in sorted(files): # go through each file and
    if file.endswith('.txt'): # only process .txt files
        df = pd.DataFrame(pd.read_csv(os.path.join(folder,file),
                        sep="\s+", skiprows=19, # the first set of lines are not part of the data
                        index_col=None, header=None, 
                        encoding= 'unicode_escape')) # loads data and skips the rows with run info
        data_files.append(df.iloc[:,:]) # add the file into the list of sample files 
        names.append(file[:-4]) # add the name to list of names, without the .txt part
        print(file) # print file name so we can see all the files we used
        print(df.shape)
        counter = counter + 1 # gives tally of files added
print('') 
print('The number of samples in list is:', counter)


#%%

# check a sample
data_files[0].head()


#%%

# find the mean spectra of each sample and view it

for i in range(len(data_files)):
    data_files[i]['mean'] = data_files[i].iloc[:,1:].mean(axis=1)
    

# plot spectra
plt.figure(figsize=(15,8))
counter = 0
counter2 = 0
for i in range(len(data_files)):
    plt.plot(data_files[i].iloc[:,0], data_files[i].loc[:,'mean']+counter2, label = names[counter])
    counter = counter + 1
    counter2 = counter + 5
plt.xlabel('Wavenumber')
plt.ylabel('Intensity')
plt.title('Raw Spectra')
plt.legend()
plt.show() 


#%%

# remove the 'mean' column from the data
final_files = []
for file in data_files:
    file = file.iloc[:,:-1]
    final_files.append(file)
data_files = final_files


#%%
# Truncate the data from 600 cm-1 to 1800 cm-1

i_wn = 20  # initial wavenumber
o_wn = 1800.5 # outer edge wavenumber
trimmed_files = []
for file in data_files: # go through each file
    df = []
    for i in range(file.shape[0]): # go through the rows
        if file.iloc[i,0] > i_wn and file.iloc[i,0] < o_wn: # trim to lengths
            df.append(file.iloc[i,:]) # add to list
    dff = pd.DataFrame(df)
    trimmed_files.append(dff)
    

#%%

# find the mean spectra of each sample and view it

for i in range(len(data_files)):
    trimmed_files[i]['mean'] = trimmed_files[i].iloc[:,1:].mean(axis=1)
names[0] = "glycine solution, 10 mg/mL\nno gold particles (RS)"    
names[1] = "glycine solution, 10 x 10^-5 mg/mL\n+ gold nanoparticles (SERS)"
# plot spectra
plt.figure(figsize=(4,3))
counter = 0
counter2 = 0
color_list = ['teal', 'palevioletred']
for i in range(len(trimmed_files)):
    plt.plot(trimmed_files[i].iloc[:,0], trimmed_files[i].loc[:,'mean']+counter2, label = names[counter], color = color_list[counter])
    counter = counter + 1
    counter2 = counter + 5
plt.xlabel('Wavenumber ($cm^{-1}$)', fontsize=10, fontname="Arial")
plt.ylabel('Intensity (arbitrary units)', fontsize=10, fontname="Arial")
plt.tick_params(left = True, right = False , labelleft = True, 
                labelbottom = True, bottom = True) 
plt.xticks(fontname= "Arial", fontsize=8)
plt.yticks(fontname= "Arial", fontsize=8)
sns.despine()
plt.legend(fontsize=8,frameon=False)

    
#plt.savefig('/Users/rickerr2/Library/CloudStorage/OneDrive-NationalInstitutesofHealth/Documents/LAB_STUFF/PEOPLE/rye/Publications/Optica Biomedical Optics Express (Submitted) - Raman Wavelength Comparison/figures/EF_Glycine.png', dpi=1000, bbox_inches = "tight") 
#plt.savefig('/Users/rickerr2/Library/CloudStorage/OneDrive-NationalInstitutesofHealth/Documents/LAB_STUFF/PEOPLE/rye/Publications/Optica Biomedical Optics Express (Submitted) - Raman Wavelength Comparison/figures/EF_Glycine.pdf', dpi=1000, bbox_inches = "tight") 

plt.show()


#%%

trimmed_files[0].index = trimmed_files[0].iloc[:,0]
glycine_max = trimmed_files[0].iloc[:,1].nlargest(n=35).index

glycine_max

#Out[212]: 
#Float64Index([ 114.85, 117.552, 112.147, 524.906, 5.79165, 109.443, 120.252,
#              8.54176, 106.737, 79.6177, 85.0512,  527.43, 896.484, 82.3351,
#              76.8991, 894.116, 522.381, 87.7662, 95.9039, 165.981, 74.1794,
#              122.952, 60.5624,   90.48, 171.339, 174.015, 898.851, 104.031,
#              93.1925, 101.323, 3.04031, 176.691, 1326.99, 891.748, 1331.37],
#             dtype='float64', name=0)
    
# thus, the associated peaks are at 114.85, 896.48, and 1326.99 - the othes all cluster around these are these are consistent with the literature (see supplemental paper for reference)
# Round to 115, 896, and 1327
# 524.9 is the SI
#%%
#%%

# get the max peak of the SERS solution:

EF1 = trimmed_files[1].iloc[:,1].max()/trimmed_files[0].iloc[:,1].max()


#%%

# get EF 2

#look between wavenumbers 600 and 1000 as this is where the second promiment peak of glycine is found

i_wn = 600  # initial wavenumber
o_wn = 1000 # outer edge wavenumber
ef2_files = []
for file in trimmed_files: # go through each file
    df = []
    for i in range(file.shape[0]): # go through the rows
        if file.iloc[i,0] > i_wn and file.iloc[i,0] < o_wn: # trim to lengths
            df.append(file.iloc[i,:]) # add to list
    dff = pd.DataFrame(df)
    ef2_files.append(dff)
 
EF2 = ef2_files[1].iloc[:,1].max()/ef2_files[0].iloc[:,1].max()


#%%

# get EF 3

#look between wavenumbers 1000 and 1500 as this is where the second promiment peak of glycine is found

i_wn = 1000 # initial wavenumber
o_wn = 1500 # outer edge wavenumber
ef3_files = []
for file in trimmed_files: # go through each file
    df = []
    for i in range(file.shape[0]): # go through the rows
        if file.iloc[i,0] > i_wn and file.iloc[i,0] < o_wn: # trim to lengths
            df.append(file.iloc[i,:]) # add to list
    dff = pd.DataFrame(df)
    ef3_files.append(dff)
 
EF3 = ef3_files[1].iloc[:,1].max()/ef3_files[0].iloc[:,1].max()

#%%

EF = (EF1+EF2+EF3)/3
EF
