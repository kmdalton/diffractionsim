from matplotlib import pyplot as plt
import matplotlib as mpl
from crystal import crystal


#This must be a CNS format reflection record 
#See dataset_description.txt for how to make this
inFN = "1ubq.pdb.hkl"

#Directory to save images in
outDir = 'images/'



x = crystal(inFN)
x.orientrandom()
reflection_scale = 50. #Relative size of spots for matplotlib

phistep = 1. #Phi angle step between images in degrees
nsteps  = 90 #Number of phi steps to execute



def plotframe(outFN, dataframe):
    plt.figure(figsize=(8,8))
    sizes = reflection_scale*dataframe['F']**2 / ((dataframe['F']**2).max())
    plt.scatter(dataframe['X'], dataframe['Y'], s=sizes, c=sizes)
    plt.xlim(-60., 60.)
    plt.ylim(-60., 60.)
    plt.title(r"$\phi = {}\deg$".format(i))
    plt.xlabel(r"X-position (mm)")
    plt.ylabel(r"Y-position (mm)")
    plt.savefig(outFN)
    plt.close()

F = x.phiseries(phistep, nsteps)
for i,dataframe in iter(F.groupby('PHINUMBER')):
    outFN = outDir + '{:03}.png'.format(i)
    plotframe(outFN, dataframe)


