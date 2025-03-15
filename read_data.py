import os
import numpy as np

#directory where data files are saved
DIR=
#importing filenames 
for i in os.walk(DIR):
    FILENAMES=i[2]

#selecting only .dat files    
for i in FILENAMES:
    if i[-4:]!='.dat':
        FILENAMES.remove(i)

    
fileID=np.array([i[:-4] for i in FILENAMES]) #experiment name array

#specifying wanted columns of data from data file (USINE format)
COLUMNS = ['Energy','Intensity','Err_stat-','Err_stat+','Err_syst-','Err_syst+','Flux']
column_ind = [3,6,7,8,9,10,11] 



#extracting relevant data from all files and storing in one big array

DATA = []

for expt in FILENAMES:
    
    rowlabel = np.genfromtxt(DIR+'\\'+expt,usecols=0,dtype='|S5') #get row names
    electron_rows = np.where(rowlabel==b'e-+e+')[0] #select rows with electron+positron data
    
    arr = np.genfromtxt(DIR+'\\'+expt,usecols=column_ind)[electron_rows,:]  #extract data from selected rows and columns
    arr = np.c_[arr[:,0],arr[:,1:6]*1e-4]  #converting intensity values to the correct units (from m2 in the data to cm2 used in the simulations)
    DATA.append(arr)
    
DATA = np.array(DATA)

np.savez_compressed(DIR+'\\ALL_DATA_ARRAY_nocalet',DATA=DATA, EXPERIMENTS=fileID,COLUMNS=COLUMNS)
