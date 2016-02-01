__author__ = 'rpdcorbion'

from merger import merger

###feed_infos=[]
networks=[('network_id', 0),('network_name', 0),('network_url', 0),('network_timezone', 0),('network_lang', 0),('network_phone', 0),('network_sort_order', 0)]
calendar=[('service_id', 1),('monday', 0),('tuesday', 0),('wednesday', 0),('thursday', 0),('friday', 0),('saturday', 0),('sunday', 0),('start_date', 0),('end_date', 0)]
calendar_dates=[('service_id', 1),('date', 0),('exception_type', 0)]
comments=[('comment_id', 1),('comment_type', 0),('comment_name', 0),('comment_url', 0)]
comment_links=[('object_id', 0),('object_type', 0),('comment_id', 1)]
commercial_modes=[('commercial_mode_id', 0),('commercial_mode_name', 0)]
companies=[('company_id', 1),('company_name', 0),('company_address_name', 0),('company_address_number', 0),('company_address_type', 0),('company_url', 0),('company_mail', 0),('company_phone', 0),('company_fax', 0)]
contributors=[('contributor_id', 0),('contributor_name', 0)]
frequencies=[('trip_id', 0),('start_time', 0),('end_time', 0),('headway_secs', 0)]
lines=[('line_id', 0),('line_code', 0),('line_name', 0),('forward_line_name', 0),('forward_direction', 0),('backward_line_name', 0),('backward_direction', 0),('line_color', 0),('line_text_color', 0),('line_sort_order', 0),('network_id', 0),('commercial_mode_id', 0),('contributor_id', 0),('geometry_id', 1),('line_opening_time', 0),('line_closing_time', 0)]
routes=[('route_id', 0),('route_name', 0),('is_forward', 0),('line_id', 0),('contributor_id', 0),('geometry_id', 1),('destination_id', 0)]
physical_modes=[('physical_mode_id', 0),('physical_mode_name', 0),('co2_emission', 0)]
equipments=[('equipment_id', 1),('wheelchair_boarding', 0),('sheltered', 0),('elevator', 0),('escalator', 0),('bike_accepted', 0),('bike_depot', 0),('visual_announcement', 0),('audible_announcement', 0),('appropriate_escort', 0),('appropriate_signage', 0)]
stops=[('stop_id', 0),('visible', 0),('stop_name', 0),('city_code', 0),('stop_lat', 0),('stop_lon', 0),('fare_zone_id', 0),('location_type', 0),('geometry_id', 1),('parent_station', 0),('stop_timezone', 0),('equipment_id', 1),('contributor_id', 0)]
stop_times=[('stop_time_id', 0),('trip_id', 0),('arrival_time', 0),('departure_time', 0),('stop_id', 0),('stop_sequence', 0),('stop_headsign', 0),('pickup_type', 0),('drop_off_type', 0),('local_zone_id', 0),('date_time_estimated', 0)]
transfers=[('from_stop_id', 0),('to_stop_id', 0),('min_transfer_time', 0),('real_min_transfer_time', 0),('equipment_id', 1)]
trip_properties=[('trip_property_id', 0),('wheelchair_accessible', 0),('bike_accepted', 0),('air_conditioned', 0),('visual_announcement', 0),('audible_announcement', 0),('appropriate_escort', 0),('appropriate_signage', 0),('school_vehicle_type', 0)]
trips=[('route_id', 0),('service_id', 1),('trip_id', 0),('trip_headsign', 0),('block_id', 0),('company_id', 1),('physical_mode_id', 0),('trip_property_id', 0),('contributor_id', 0),('geometry_id', 1)]
geometries=[('geometry_id', 1),('geometry_wkt', 0)]
object_properties=[('object_type', 0),('object_id', 0),('object_property_name', 0),('object_property_value', 0)]
object_codes=[('object_type', 0),('object_id', 0),('object_system', 0),('object_code', 0)]
admin_stations=[('admin_id', 0),('admin_name', 0),('stop_id', 0),('stop_name', 0)]
line_groups=[('line_group_id', 1),('line_group_name', 0),('main_line_id', 0)]
line_group_links=[('line_group_id', 1),('line_id', 0)]
grid_calendars=[('calendar_id', 1),('name', 0),('monday', 0),('tuesday', 0),('wednesday', 0),('thursday', 0),('friday', 0),('saturday', 0),('sunday', 0)]
grid_exception_dates=[('calendar_id', 1),('date', 0),('type', 0)]
grid_periods=[('calendar_id', 1),('start_date', 0),('end_date', 0)]
grid_rel_calendar_line=[('calendar_id', 1),('line_id', 0),('line_external_code', 0)]


files=[('contributors',contributors), ('networks',networks), ('commercial_modes',commercial_modes), ('companies',companies), ('lines',lines), ('physical_modes',physical_modes), ('routes',routes), ('stop_times',stop_times), ('stops',stops), ('trips',trips), ('calendar',calendar), ('calendar_dates',calendar_dates), ('comments',comments), ('comment_links',comment_links), ('frequencies',frequencies), ('equipments',equipments), ('transfers',transfers), ('trip_properties',trip_properties), ('geometries',geometries), ('object_properties',object_properties), ('object_codes',object_codes), ('admin_stations',admin_stations), ('line_groups',line_groups), ('line_group_links',line_group_links), ('grid_calendars',grid_calendars), ('grid_exception_dates',grid_exception_dates), ('grid_periods',grid_periods), ('grid_rel_calendar_line',grid_rel_calendar_line)]
####///////////////////////////////////////////////////////////////

#env_to_merge=['NTFS_fr-ne','NTFS_fr-nw','NTFS_fr-se','NTFS_fr-sw','NTFS_fr-idf']
#dossier_work='E:\\DATA\\temp\\merger\\'

#merger(files,env_to_merge, dossier_work)

