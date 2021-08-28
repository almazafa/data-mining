# split columnes with Python:
# importing pandas module 
import csv
import pandas as pd 
# reading csv from file to data frame
data = pd.read_csv(r'C:\Users\Shir Ams\Desktop\pro_splt.csv') 
# dropping null value columns to avoid errors 
data.dropna(inplace = True) 
# new data frame with split value columns 
new = data["listed_in"].str.split(", ", n = 1, expand = True) 
# making separate column from new data frame 
data["Janner1"]= new[0] 
# making separate column from new data frame 
data["extras"]= new[1]
# new data frame with split value columns
new = data["extras"].str.split(", ", n = 1, expand = True) 
# making separate column from new data frame 
data["Janner2"]= new[0] 
# making separate column from new data frame 
data["extras"]= new[1] 
# new data frame with split value columns
new = data["extras"].str.split(", ", n = 1, expand = True) 
# making separate column from new data frame 
data["Janner3"]= new[0] 
# making separate column from new data frame 
data["extras"]= new[1]
# Dropping columns 
data.drop(columns =["extras"], inplace = True) 
#insert to csv file:
data.to_csv(r'C:\Users\Shir Ams\Desktop\pro_splt.csv', index = False)



# split columnes with Python:
# importing pandas module 
import csv
import pandas as pd 
# reading csv file from 
data = pd.read_csv(r'C:\Users\Shir Ams\Desktop\pro_splt.csv') 
# new data frame with split value columns 
new = data["date_added"].str.split(", ", n = 1, expand = True) 
# making separate column from new data frame 
data["Releas_date"]= new[0] 
# making separate column from new data frame 
data["erase"]= new[1]
# Dropping columns 
data.drop(columns =["date_added"], inplace = True)
data.drop(columns =["erase"], inplace = True)
#insert to csv file:
data.to_csv(r'C:\Users\Shir Ams\Desktop\pro_splt.csv', index = False)




# split columnes with Python:
# importing pandas module 
import csv
import pandas as pd 
# reading csv file from 
data = pd.read_csv(r'C:\Users\Shir Ams\Desktop\pro_splt.csv') 
# new data frame with split value columns 
new = data["country"].str.split(", ", n = 1, expand = True) 
# making separate column from new data frame 
data["Country1"]= new[0] 
# making separate column from new data frame 
data["countries"]= new[1]
# new data frame with split value columns 
new = data["countries"].str.split(", ", n = 1, expand = True) 
# making separate column from new data frame 
data["Country2"]= new[0] 
# making separate column from new data frame 
data["countries2"]= new[1]
# new data frame with split value columns 
new = data["countries2"].str.split(", ", n = 1, expand = True) 
# making separate column from new data frame 
data["Country3"]= new[0] 
# making separate column from new data frame 
data["countries3"]= new[1]
# Dropping columns 
data.drop(columns =["country"], inplace = True)
data.drop(columns =["countries"], inplace = True)
data.drop(columns =["countries2"], inplace = True)
data.drop(columns =["countries3"], inplace = True)
#insert to csv file:
data.to_csv(r'C:\Users\Shir Ams\Desktop\pro_splt.csv', index = False)



# split columnes with Python:
# importing pandas module 
import csv
import pandas as pd 
# reading csv file from 
data = pd.read_csv(r'C:\Users\Shir Ams\Desktop\pro_splt.csv') 
# new data frame with split value columns 
new = data["cast"].str.split(", ", n = 1, expand = True) 
# making separate column from new data frame 
data["Main_Acter"]= new[0] 
# making separate column from new data frame 
data["droping"]= new[1]
# Dropping columns 
data.drop(columns =["cast"], inplace = True)
data.drop(columns =["droping"], inplace = True)
#insert to csv file:
data.to_csv(r'C:\Users\Shir Ams\Desktop\pro_splt.csv', index = False)


# split columnes with Python:
# importing pandas module 
import csv
import pandas as pd 
# reading csv file from 
data = pd.read_csv(r'C:\Users\Shir Ams\Desktop\pro_splt.csv') 
# new data frame with split value columns 
new = data["director"].str.split(", ", n = 1, expand = True) 
# making separate column from new data frame 
data["Director1"]= new[0] 
# making separate column from new data frame 
data["Others"]= new[1]
# new data frame with split value columns 
new = data["Others"].str.split(", ", n = 1, expand = True) 
# making separate column from new data frame 
data["Director2"]= new[0] 
# making separate column from new data frame 
data["Others2"]= new[1]
# new data frame with split value columns 
new = data["Others2"].str.split(", ", n = 1, expand = True) 
# making separate column from new data frame 
data["Director3"]= new[0] 
# making separate column from new data frame 
data["Others3"]= new[1]
# Dropping columns 
data.drop(columns =["director"], inplace = True)
data.drop(columns =["Others"], inplace = True)
data.drop(columns =["Others2"], inplace = True)
data.drop(columns =["Others3"], inplace = True)
#insert to csv file:
data.to_csv(r'C:\Users\Shir Ams\Desktop\pro_splt.csv', index = False)


# split columnes with Python:
# importing pandas module 
import csv
import pandas as pd 
# reading csv file from 
data = pd.read_csv(r'C:\Users\Shir Ams\Desktop\pro_splt.csv') 
# new data frame with split value columns 
new = data["duration"].str.split(" ", n = 1, expand = True) 
# making separate column from new data frame 
data["duration[Seasons/Min]"]= new[0] 
# making separate column from new data frame 
data["erase"]= new[1]
# Dropping columns 
data.drop(columns =["duration"], inplace = True)
data.drop(columns =["erase"], inplace = True)
#insert to csv file:
data.to_csv(r'C:\Users\Shir Ams\Desktop\pro_splt.csv', index = False)
#plot Data:
data





