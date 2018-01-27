import sys
from cup import Cup
from country import Country
from groupping_2018 import goupping_function_2018
import input_data


def main():
    num_of_samp = 10000
    for name in sys.argv[1:]:
        if not country_name_valid(name):
            print 'Invalid country name: ' + name
            return False
    if len(sys.argv[1:]) < 2:
        print 'Input country names must be more than one!'
        return False

    country_list = []
    for data in input_data.data_2018:
        ctry = Country(data[0], data[1], data[2])
        country_list.append(ctry)

    cup_2018 = Cup('World Cup 2018')
    valid = 0
    for i in range(0, num_of_samp):
        cup_2018.set_group_members(country_list, goupping_function_2018)
        if cup_2018.teams_in_same_group(sys.argv[1:]):
            valid += 1

    result = round(float(valid) / float(num_of_samp) * 100, 2)
    msg = []
    msg.append('The possibility of')
    msg.append(', '.join(sys.argv[1:]))
    msg.append('in the same group is')
    msg.append(str(result) + '%')
    print ' '.join(msg)


def country_name_valid(name):
    for data_list in input_data.data_2018:
        if name == data_list[0]:
            return True
    return False


if __name__ == "__main__":
    main()
