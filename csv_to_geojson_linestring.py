import csv

# Read in raw data from csv
rawData = csv.reader(open('transports-waypoints_all.csv', 'rb'), dialect='excel')

# the template. where data from the csv will be formatted to geojson
# fill in the data from start of trip to penultimate point	
template = \
    ''' \
    { "type" : "Feature",
      "geometry" : {
                "type" : "LineString",
                "coordinates" : [
				["%s","%s"],

	'''
# fill in the last point
template2 = \
	''' \
				["%s","%s"]

	'''
# add the properties
template3 = \
	''' \
			},        
			"properties" : { 
			"userid" : "%s",
			"activity" : "%s",
			"transportid" : "%s",
			"mode" : "%s",
			"timestamp" : "%s"
		}
	},
    '''
# the head of the geojson file
output = \
    ''' \
{ "type" : "Feature Collection",
    {"features" : [
    '''

# loop through the csv by row skipping the first
iter = 0
transportid = ""
for row in rawData:
    iter += 1,
    if iter == 2:
			transportid = row[2],
			output += template % (row[4], row[5]),
			userid = row[0],
			activity = row[1],
			mode = row[3],
			lat = row[4],
			lon = row[5],
			timestamp = row[6]
    if iter > 2:
		if row[2] != transportid:
			transportid = row[2],
			output += template3 % (userid, activity, transportid, mode, timestamp)
        else:
			output += template2 % (row[4], row[5]),
			output += ",",
			userid = row[0],
			activity = row[1],
			mode = row[3],
			lat = row[4],
			lon = row[5],
			timestamp = row[6]
# the tail of the geojson file
output += \
    ''' \
    ]
}
    '''
# opens an geoJSON file to write the output to
outFileHandle = open("output.geojson", "w")
outFileHandle.write(output)
outFileHandle.close()