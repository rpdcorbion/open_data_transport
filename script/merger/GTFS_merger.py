__author__ = 'rpdcorbion'

from merger import merger

agency=[("agency_id", 0),("agency_name", 0),("agency_url", 0),("agency_timezone", 0),("agency_lang", 0),("agency_phone", 0),("agency_fare_url", 0)]
calendar=[("service_id", 1),("monday", 0),("tuesday", 0),("wednesday", 0),("thursday", 0),("friday", 0),("saturday", 0),("sunday", 0),("start_date", 0),("end_date", 0)]
calendar_dates=[("service_id", 1),("date", 0),("exception_type", 0)]
stops=[("stop_id", 0),("stop_code", 0),("stop_name", 0),("stop_desc", 0),("stop_lat", 0),("stop_lon", 0),("zone_id", 2),("stop_url", 0),("location_type", 0),("parent_station", 0),("stop_timezone", 0),("wheelchair_boarding", 0)]
routes=[("route_id", 0),("agency_id", 0),("route_short_name", 0),("route_long_name", 0),("route_desc", 0),("route_type", 0),("route_url", 0),("route_color", 0),("route_text_color", 0)]
trips = [("route_id", 0),("service_id", 1),("trip_id", 0),("trip_headsign", 0),("trip_short_name", 0),("direction_id", 0),("block_id", 1),("shape_id", 1),("wheelchair_accessible", 0),("bikes_allowed", 0),("trip_desc", 0)]
stop_times = [("trip_id", 0),("arrival_time", 0),("departure_time", 0),("stop_id", 0),("stop_sequence", 0),("stop_headsign", 0),("pickup_type", 0),("drop_off_type", 0),("shape_dist_traveled", 0),("stop_time_desc", 0),("date_time_estimated", 0),("stop_itl",0)]
fare_attributes = [("fare_id", 1),("price", 0),("currency_type", 0),("payment_method", 0),("transfers", 0),("transfer_duration", 0)]
fare_rules = [("fare_id", 1),("route_id", 0),("origin_id", 2),("destination_id", 2),("contains_id",2)]
shapes = [("shape_id", 1),("shape_pt_lat", 0),("shape_pt_lon", 0),("shape_pt_sequence", 0),("shape_dist_traveled", 0)]
frequencies = [("trip_id", 0),("start_time", 0),("end_time", 0),("headway_secs", 0),("exact_times", 0)]
transfers = [("from_stop_id", 0),("to_stop_id", 0),("transfer_type", 0),("min_transfer_time", 0)]
feed_info = [("feed_publisher_name", 0),("feed_publisher_url", 0),("feed_lang", 0),("feed_start_date", 0),("feed_end_date", 0),("feed_version", 0)]

files=[('agency',agency),('calendar',calendar),('calendar_dates',calendar_dates),('routes',routes),('stops',stops),('stop_times',stop_times),('trips',trips),('transfers',transfers)]
####///////////////////////////////////////////////////////////////

##env_to_merge=['fr-ne','fr-nw','fr-se','fr-sw','fr-idf']
##dossier_work='E:\\DATA\\temp\\merger\\'


##merger(files,env_to_merge, dossier_work)


