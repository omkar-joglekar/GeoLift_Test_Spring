#To import R packages
import os
os.environ['R_HOME'] = 'C:/Users/omkar.joglekar/Anaconda3/Lib/R-4.3.1'

from rpy2.robjects.packages import importr


utils = importr('utils')

#Install remotes 
utils.install_packages("remotes", repos='http://cran.us.r-project.org')

# Load remotes package
remotes = importr('remotes')

# Install augsynth, CommutingZones and GeoLift from GitHub
remotes.install_github("ebenmichael/augsynth")
remotes.install_github("facebookincubator/GeoLift")

