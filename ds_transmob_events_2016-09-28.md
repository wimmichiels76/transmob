# DATASET

- **Project:**    TRANSMOB (Belgium)
- **Type:**       Ticketing events 
- **Source:**     `events`, `persons` tables 
- **Date:**       Sep 28, 2016
- **Author:**     Angel J. Lopez @ UGent

## FIELD DESCRIPTION

- "trip_userid":    User identifier to match the trip data
- "id":				Event identifier 
- "person_id":		User identifier 
- "cause":			Event cause (START/END)
- "transport_mode": Event type 
- "latitude"		Latitude (degrees) 
- "longitude"		Longitude (degrees)
- "timestamp"		Event time

### Event type (transport_mode)

- SHARED_BIKE
- TRAIN
- BUS/TRAM/METRO
- PARKING_STREET
- PARKING_GARAGE
