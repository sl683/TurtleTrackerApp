#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Abby Liu (sl683@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

# Create a variable point to the data file
file_name = 'data/raw/sara.txt'

# Create a file object from the filename
file_object = open(file=file_name, mode ='r') 

# Read contents of each line
lineString = file_object.readline()

# Extract one data line into a variable
while lineString:
    
    # Check to see if the lineString is a data line 
    if lineString[0] in ('#', 'u'):
        lineString = file_object.readline()
        continue

    # Split lineString into a list of items
    lineData = lineString.split()
    
    # Assign variables to items in the lineData list
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    # Print information to the user
    print(f'Record {record_id} indicates Sara was seen at {obs_lat}N, {obs_lon}W on {obs_date}.')
    
    # Move to the next line in the file
    lineString = file_object.readline()
    
# Close the file object
file_object.close()