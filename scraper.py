from gml_scraper import scrape


stations_url = "http://maps.runnymede.gov.uk/arcgis/services/runnymedeinspire/MapServer/WFSServer?service=WFS&version=1.3.0&request=GetFeature&typeNames=runnymedeinspire%3APolling_Stations"
stations_fields = {
    '{http:///runnymedeinspire/MapServer/WFSServer}OBJECTID': 'OBJECTID',
    '{http:///runnymedeinspire/MapServer/WFSServer}Ward': 'Ward',
    '{http:///runnymedeinspire/MapServer/WFSServer}Polling_District': 'Polling_District',
    '{http:///runnymedeinspire/MapServer/WFSServer}Station_Number': 'Station_Number',
    '{http:///runnymedeinspire/MapServer/WFSServer}Premises': 'Premises',
    '{http:///runnymedeinspire/MapServer/WFSServer}Number_of_Electorates': 'Number_of_Electorates',
}

districts_url = "http://maps.runnymede.gov.uk/arcgis/services/runnymedeinspire/MapServer/WFSServer?service=WFS&version=1.3.0&request=GetFeature&typeNames=runnymedeinspire%3APolling_Districts"
districts_fields = {
    '{http:///runnymedeinspire/MapServer/WFSServer}OBJECTID': 'OBJECTID',
    '{http:///runnymedeinspire/MapServer/WFSServer}ID': 'ID',
    '{http:///runnymedeinspire/MapServer/WFSServer}Ward': 'Ward',
    '{http:///runnymedeinspire/MapServer/WFSServer}Number_of_Electorates': 'Number_of_Electorates',
    '{http:///runnymedeinspire/MapServer/WFSServer}Station_Number': 'Station_Number',
    '{http:///runnymedeinspire/MapServer/WFSServer}Premises': 'Premises',
    '{http:///runnymedeinspire/MapServer/WFSServer}Poling_Districts': 'Poling_Districts',
    '{http:///runnymedeinspire/MapServer/WFSServer}District': 'District',
    '{http:///runnymedeinspire/MapServer/WFSServer}SHAPE.area': 'SHAPE.area',
    '{http:///runnymedeinspire/MapServer/WFSServer}SHAPE.len': 'SHAPE.len',
}

council_id = 'E07000212'


scrape(stations_url, council_id, 'stations', stations_fields, 'OBJECTID')
scrape(districts_url, council_id, 'districts', districts_fields, 'OBJECTID')
