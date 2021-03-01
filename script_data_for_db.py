from models import Driver
from report_functions import build_report, drivers_abbreviations

sorted_list_report, dict_report = build_report('docs')
driver_dict, sorted_list_drivers = drivers_abbreviations('docs')

for driver in sorted_list_report:
    one_driver = Driver.create(
        name=driver_dict[driver[0]][0],
        driver_id=driver[0],
        team=driver_dict[driver[0]][1],
        result=driver[1],
    )
