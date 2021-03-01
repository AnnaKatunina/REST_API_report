from datetime import datetime, timedelta
import operator
import os

start_file = 'start.log'
end_file = 'end.log'
abbreviations_file = 'abbreviations.txt'


def string_to_time(string):
    return datetime.strptime(string.rstrip()[14:], '%H:%M:%S.%f')


def build_report(path):
    result_dict = {}
    with open(os.path.join(path, start_file)) as start:
        for line in start:
            result_dict[line[:3]] = string_to_time(line)
    with open(os.path.join(path, end_file), 'r') as end:
        for line in end:
            delta = string_to_time(line) - result_dict[line[:3]]
            if delta > timedelta(seconds=0):
                result_dict[line[:3]] = delta
            else:
                result_dict[line[:3]] = result_dict[line[:3]] - string_to_time(line)
    sorted_result_dict = sorted(result_dict.items(), key=operator.itemgetter(1))
    return sorted_result_dict, result_dict


def drivers_abbreviations(path):
    drivers_dict = {}
    sorted_result_dict, result_dict = build_report(path)
    with open(os.path.join(path, abbreviations_file), encoding='utf-8') as abbreviations:
        for line in abbreviations:
            line = line.rstrip().split('_')
            drivers_dict[line[0]] = [line[1], line[2], result_dict[line[0]]]
    sorted_drivers = sorted(drivers_dict.items(), key=operator.itemgetter(1))
    return drivers_dict, sorted_drivers


def print_report(path, driver=None, order='asc'):
    sorted_result_dict, result_dict = build_report(path)
    drivers_dict, sorted_driver_dict_name = drivers_abbreviations(path)
    report_list = []
    if driver is not None:
        driver = f'{drivers_dict[driver][0]} | {drivers_dict[driver][1]} | {str(drivers_dict[driver][2])[3:11]}'
        report_list.append(driver)
    else:
        if order == 'desc':
            sorted_result_dict = sorted_result_dict[::-1]
        number = 0
        for key in sorted_result_dict:
            number += 1
            driver_result = f'{str(number)} | {drivers_dict[key[0]][0]} | {drivers_dict[key[0]][1]} | ' \
                            f'{str(key[1])[3:11]}'
            report_list.append(driver_result)
            if number == 15:
                report_list.append(65 * '-')
    return report_list
