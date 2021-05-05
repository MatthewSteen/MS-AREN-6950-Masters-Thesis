
from __future__ import division
import os

'''
Opens hourly output files and creates annual summary file.  
Hourly output is averaged or summed depending on the type of data.
'''

# Hourly output file directory
hour_dir = "C:\\Users\\msteen\\Documents\\BEopt_devel\\1 HOUROUTPUT"

# Annual summary directory and file for writing
year_dir = "C:\\Users\\msteen\\Documents\\BEopt_devel\\2 YEAROUTPUT"
year_fname = 'Sum.csv'
if not os.path.exists(year_dir):
	os.mkdir(year_dir)
if os.path.exists(year_dir):
	year_file = os.path.join(year_dir, year_fname)
fout = open(year_file, 'w')

# Write column headers
fname_headers = '% Conditioned, \
State, \
Azimuth, \
Wall R-value, \
Roof R-value, \
Window U-factor, \
Window SHGC, \
Infiltration, \
Zones,'
output_headers = 
'''
'Outdoor Drybulb, \
Outdoor Humidity Ratio, \
'''
'EMS Cooling Electricty, \
CC Elec Power, \
CC Sensible Rate, \
CC Latent Rate, \
CC RTF, \
CC Fan RTF, \
HC Sensible Rate, \
HC RTF, \
HC Fan Power, \
HC Fan RTF, \
Living 55-2004 Summer, \
Garage 55-2004 Summer, \
Living 55-2004 Winter, \
Garage 55-2004 Winter, \
Living Htg Setpoint Not Met, \
Garage Htg Setpoint Not Met, \
Living Clg Setpoint Not Met, \
Garage Clg Setpoint Not Met, \
Living Interzone Transfer Rate, \
Garage Interzone Transfer Rate,'
'''
Living Zone Mean Air Temperature, \
Garage Zone Mean Air Temperature, \
Living Zone Mean Air Humidity Ratio, \
Garage Zone Mean Air Humidity Ratio, \
'''
fout.write(fname_headers + output_headers)

# Loop through hourly output files and create annual summary file

filenames = os.listdir(hour_dir)

for filename in filenames:
    
	# Read hourly output file
	fin = open(os.path.join(hour_dir, filename), 'r')
	hourlycsv_lines = fin.readlines()
	fin.close()

	# Write file name to annual summary file
	fout.write("\n")
	fout.write(filename + ',')
	
	# Store 1st header line - column names - NEED?
	header = hourlycsv_lines.pop(0).strip().split(",")
	header2 = header[2] #first two columns are Tout and Wout
	header3 = header[3]
	header4 = header[4]
	header5 = header[5]
	header6 = header[6]
	header7 = header[7]
	header8 = header[8]
	header9 = header[9]
	header10 = header[10]
	header11 = header[11]
	header12 = header[12]
	header13 = header[13]
	header14 = header[14]
	header15 = header[15]
	header16 = header[16]
	header17 = header[17]
	header18 = header[18]
	header19 = header[19]
	header20 = header[20]
	header21 = header[21]
	header22 = header[22]
	header23 = header[23]
	header24 = header[24]
	header25 = header[25]
	
	# Remove 2nd header line - units
	units = hourlycsv_lines.pop(0).strip().split(",")

	# Create lists to store annual data ?
	hourdata = []
	OutdoorDrybulb = []
	OutdoorHumidity = []    
	EmsCoolingElectricity = []
	CcElecPower = []
	CcSensibleRate = []
	CcLatentRate = []
	CcRtf = []
	CcFanRtf = []
	HcSensibleRate = []
	HcRtf = []
	HcFanPower = []
	HcFanRtf = []
	LivingStd55Summer = []
	GarageStd55Summer = []
	LivingStd55Winter = []
	GarageStd55Winter = []
	LivingHtgSetpointNotMet = []
	GarageHtgSetpointNotMet = []
	LivingClgSetpointNotMet = []
	GarageClgSetpointNotMet = []
	LivingMeanAirTemp = []
	GarageMeanAirTemp = []
	LivingMeanAirHumidity = []
	GarageMeanAirHumidity = []
	LivingTransferRate = []
	GarageTransferRate = []    

	# Loop through data 
	for hournum, hourlycsv_line in enumerate(hourlycsv_lines):
		
		# Strip whitespace and split line at comma        
		data = hourlycsv_line.strip().split(",")
		# create dictionary of lists for each column
		hourdict = {}
		# start after OutdoorTemperature [0] and OutdoorHumidity [1] 
		'''
		hourdict['OutdoorDrybulb'] = float(data[0]) #units?
		hourdict['OutdoorHumidity'] = float(data[1]) 
		'''
		hourdict['EmsCoolingElectricity'] = float(data[2])
		hourdict['CcElecPower'] = float(data[5])		#moved up
		hourdict['CcSensibleRate'] = float(data[3])
		hourdict['CcLatentRate'] = float(data[4])
		hourdict['CcRtf'] = float(data[6])
		hourdict['CcFanRtf'] = float(data[7])
		hourdict['HcSensibleRate'] = float(data[8])
		hourdict['HcRtf'] = float(data[9])
		hourdict['HcFanPower'] = float(data[10])
		hourdict['HcFanRtf'] = float(data[11])
		hourdict['LivingStd55Summer'] = float(data[12])
		hourdict['GarageStd55Summer'] = float(data[13])
		hourdict['LivingStd55Winter'] = float(data[14])
		hourdict['GarageStd55Winter'] = float(data[15])
		hourdict['LivingHtgSetpointNotMet'] = float(data[16])
		hourdict['GarageHtgSetpointNotMet'] = float(data[17])
		hourdict['LivingClgSetpointNotMet'] = float(data[18])
		hourdict['GarageClgSetpointNotMet'] = float(data[19])
		'''
		hourdict['LivingMeanAirTemp'] = float(data[20])
		hourdict['GarageMeanAirTemp'] = float(data[21])
		hourdict['LivingMeanAirHumidity'] = float(data[22])
		hourdict['GarageMeanAirHumidity'] = float(data[23])
		'''
		hourdict['LivingTransferRate'] = float(data[24])
		hourdict['GarageTransferRate'] = float(data[25])
		# Add to annual data list
		hourdata.append(hourdict)    

	# Summarize hourly output - not sure what this does exactly
	annualdata = []
	'''
	annualdata.append(sum([x['OutdoorDrybulb'] for x in hourdata][:])/8760)
	annualdata.append(sum([x['OutdoorHumidity'] for x in hourdata][:])/8760)
	'''
	annualdata.append(sum([x['EmsCoolingElectricity'] for x in hourdata][:]))
	annualdata.append(sum([x['CcElecPower'] for x in hourdata][:]))
	annualdata.append(sum([x['CcSensibleRate'] for x in hourdata][:]))
	annualdata.append(sum([x['CcLatentRate'] for x in hourdata][:]))
	annualdata.append(sum([x['CcRtf'] for x in hourdata][:]))
	annualdata.append(sum([x['CcFanRtf'] for x in hourdata][:]))
	annualdata.append(sum([x['HcSensibleRate'] for x in hourdata][:]))
	annualdata.append(sum([x['HcRtf'] for x in hourdata][:]))
	annualdata.append(sum([x['HcFanPower'] for x in hourdata][:]))
	annualdata.append(sum([x['HcFanRtf'] for x in hourdata][:]))
	annualdata.append(sum([x['LivingStd55Summer'] for x in hourdata][:]))
	annualdata.append(sum([x['GarageStd55Summer'] for x in hourdata][:]))
	annualdata.append(sum([x['LivingStd55Winter'] for x in hourdata][:]))
	annualdata.append(sum([x['GarageStd55Winter'] for x in hourdata][:]))
	annualdata.append(sum([x['LivingHtgSetpointNotMet'] for x in hourdata][:]))
	annualdata.append(sum([x['GarageHtgSetpointNotMet'] for x in hourdata][:]))
	annualdata.append(sum([x['LivingClgSetpointNotMet'] for x in hourdata][:]))
	annualdata.append(sum([x['GarageClgSetpointNotMet'] for x in hourdata][:]))
	'''
	annualdata.append(sum([x['LivingMeanAirTemp'] for x in hourdata][:])/8760)
	annualdata.append(sum([x['GarageMeanAirTemp'] for x in hourdata][:])/8760)
	annualdata.append(sum([x['LivingMeanAirHumidity'] for x in hourdata][:])/8760)
	annualdata.append(sum([x['GarageMeanAirHumidity'] for x in hourdata][:])/8760)
	'''
	annualdata.append(sum([x['LivingTransferRate'] for x in hourdata][:]))
	annualdata.append(sum([x['GarageTransferRate'] for x in hourdata][:]))

	# Write summary data and close file  
	fout.write(str(annualdata))

#fout.close()
