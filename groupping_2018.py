import random
from cup import Cup
from country import Country
from worldcup_exceptions import WorldCupException
import utils
import input_data


def worldcup_2018():
    country_list = []
    for data in input_data.data_2018:
        ctry = Country(data[0], data[1], data[2])
        country_list.append(ctry)
    cup_2018 = Cup('World Cup 2018')
    cup_2018.set_group_members(country_list, goupping_function_2018)
    print cup_2018.all


def goupping_function_2018(group_list, country_list, **kwargs):
    utils.reset_countries(country_list)
    country_dict = {}
    for country in country_list:
        country_dict[country.name] = country
    country_dict['Russia'].is_host()
    utils.set_pots(country_list, num_of_groups=8)

    fail_to_group = False
    try:
        for pot in range(1, 5):
            if pot == 1:
                group_list[0].add_member(country_dict['Russia'], pot)
            elif pot == 2:
                for group in group_list:
                    if 'CONMEBOL' not in group.valid_confederations:
                        group.add_member(random.choice(utils.generate_standby_list(country_list, pot, group.valid_confederations)), pot)
            elif pot == 3:
                for group in group_list:
                    if 'UEFA' not in group.valid_confederations or 'CONCACAF' not in group.valid_confederations:
                        group.add_member(random.choice(utils.generate_standby_list(country_list, pot, group.valid_confederations)), pot)
            elif pot == 4:
                groups_not_double_eu = []
                for group in group_list:
                    if 'UEFA' in group.valid_confederations:
                        groups_not_double_eu.append(group)
                country_dict['Serbia'].add_into_group(random.choice(groups_not_double_eu))

                groups_no_concacaf = []
                for group in group_list:
                    if pot not in group.members and 'CONCACAF' in group.valid_confederations:
                        groups_no_concacaf .append(group)
                country_dict['Panama'].add_into_group(random.choice(groups_no_concacaf))

                for group in group_list:
                    if pot not in group.members and 'AFC' not in group.valid_confederations:
                        group.add_member(random.choice(utils.generate_standby_list(country_list, pot, group.valid_confederations)), pot)

                for group in group_list:
                    if pot not in group.members and 'CAF' not in group.valid_confederations:
                        group.add_member(random.choice(utils.generate_standby_list(country_list, pot, group.valid_confederations)), pot)

            for group in group_list:
                if pot not in group.members:
                    group.add_member(random.choice(utils.generate_standby_list(country_list, pot, group.valid_confederations)), pot)
    except WorldCupException as e:
        fail_to_group = True
        print 'Grouping Failed! Please read the following for detais:'
        print e
    if fail_to_group:
        print '####################'
        print 'Countries not selected:'
        for country in country_list:
            if not country.selected:
                print country.all
        print '####################'

if __name__ == "__main__":
    worldcup_2018()
