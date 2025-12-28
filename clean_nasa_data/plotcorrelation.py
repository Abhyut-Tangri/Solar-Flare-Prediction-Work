import sys
import os
import matplotlib.pyplot as plt
import pandas as pd   
import seaborn as sns
import numpy as np




# Print the current working directory
print(os.getcwd())


fpath = r'c:\Users\abhyu\projectsolarsci\CleanData_and_Code'


# Read the data file
data = pd.read_csv(fpath+r'\clean_data.csv')
print(data.keys())

#drop unnescary data including positive correlation of 1 and negative correlations of -1
#data['column1'].corr(data['column2'])
v='   Kp         '
# for name in data.keys():
#     for name1 in data.keys():

#         if name!=name1:
#             c=data[name1].corr(data[name])
#             if np.abs(c)>.95:
#                 print(f'{name1} and {name} :{c}')
#         #print(f'correlation of {name} and {v} is {c}')
        


plt.figure(figsize=(20,20))

corr = data.corr()
sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)
plt.tight_layout()
plt.savefig('corr.png')



# Index(['Unnamed: 0.1', 'Unnamed: 0', '    Year                               ',
#        '    Decimal Day                        ',
#        '    Hour                               ', '   Bartels rotation number',
#        '    ID for IMF spacecraft              ',
#        '    ID for SW plasma spacecraft        ',
#        '   # of points in the IMF averages     ',
#        '   # of points in the plasma averages  ',
#        '   Field Magnitude Average |B|         ',
#        '   Magnitude of Average Field Vector   ',
#        '   Lat.Angle of Aver. Field Vector  ',
#        '   Long.Angle of Aver.Field Vector  ', '   Bx GSE, GSM   ',
#        '   By GSE        ', '   Bz GSE        ', '   By GSM        ',
#        '   Bz GSM        ', '   sigma|B|      ', '   sigma B       ',
#        '   sigma Bx      ', '   sigma By      ', '   sigma Bz      ',
#        '  Proton temperature       ', '   Proton Density           ',
#        '   Plasma (Flow) speed      ', '   Plasma Flow Long. Angle  ',
#        '   Plasma  Flow Lat. Angle  ', '   Na/Np               ',
#        '   Flow Pressure       ', '  sigma T             ',
#        '   sigma N             ', '   sigma V             ',
#        '   sigma phi V         ', '   sigma theta V       ',
#        '   sigma-Na/Np         ', '   Electric field      ',
#        '   Plasma beta         ', '   Alfven mach number  ', '   Kp         ', 
#        '    R                     ', '   DST Index              ',
#        '   AE-index               ', 'Proton flux0            ',
#        ' Proton flux1            ', ' Proton flux2            ',
#        ' Proton flux3            ', ' Proton flux4            ',
#        ' Proton flux5            ', ' Flag(***)              ',
#        '  ap-index              ', '  f10.7_index           ',
#        '   PC(N) index          ', '    AL-index            ',
#        '  AU-index,             ', '  Magnetosonic mach number',
#        '   Solar Lyman Alpha Irradiance ', ' Proton QI'],
#       dtype='object')

#correlated numbers have to get rid of later
# Magnitude of Average Field Vector    and    Field Magnitude Average |B|          :0.9629536232526952
#    Field Magnitude Average |B|          and    Magnitude of Average Field Vector    :0.9629536232526952
#    By GSM         and    By GSE         :0.9709407744970328
#    By GSE         and    By GSM         :0.9709407744970328
#    Electric field       and    Bz GSM         :-0.9701785041962901
#    Bz GSM         and    Electric field       :-0.9701785041962901
#     AL-index             and    AE-index                :-0.9678172397761449
#  Proton flux1             and Proton flux0             :0.9529470215270623
# Proton flux0             and  Proton flux1             :0.9529470215270622
#    AE-index                and     AL-index             :-0.9678172397761449
#df.drop

to_drop=['   Magnitude of Average Field Vector   ','   By GSE        ',
         '   Bz GSM        ','   AE-index               ',' Proton flux1            ']


for drops in to_drop:
    data.drop(drops, inplace=True,axis=1)
    
print(data.keys())

corr = data.corr()

# Getting the Upper Triangle of the co-relation matrix
matrix = np.triu(corr)

# using the upper triangle matrix as mask 

plt.figure(figsize=(20,20))

sns.heatmap(corr,mask=matrix, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)
plt.tight_layout()
plt.savefig('final_corr.png')

