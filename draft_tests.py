# import random
from country import Country
# from group import Group
# from cup import Cup
# from groupping_2018 import goupping_function_2018
# from worldcup_exceptions import WorldCupException
# import utils
import input_data

# num_of_groups = 8

country_list = []
for data in input_data.data_2018:
    ctry = Country(data[0], data[1], data[2])
    country_list.append(ctry)

# utils.set_pots(country_list, num_of_groups)

# country_dict = {}
# for country in country_list:
#     country_dict[country.name] = country

# group_list = []
# for i in range(0, num_of_groups):
#     group_list.append(Group(' '.join(['Group', chr(ord('A') + i)])))

# group_test = Group('Group Test')
# ctry = Country('China', 'UEFA')
# group_test.add_member(ctry, 1)
# group_test.add_member(ctry, 2)
# print group_test.all
# print group_test.valid_confederations
# group_test.rm_member(1)
# print group_test.all
# print group_test.valid_confederations
# group_test.rm_member(2)
# print group_test.all
# print group_test.valid_confederations

# try:
#     ctry = Country('China')
#     print ctry.all
#     ctry.set_confederation('CHI')
# except WorldCupException as e:
#     print e
# print ctry.all

# print '####'
# for country in country_list:
#     print country.all
# i = 0
# for k, v in country_dict.iteritems():
#     i = i + 1
#     print i, k, v.all
# print '####'

# print '$$$$'
# j = 0
# for country in country_list:
#     j += 1
#     print ' '.join([str(j), str(country.all)])
# print '$$$$'

# print '%%%%'
# standby_list = utils.generate_standby_list(country_list)
# j = 0
# for country in standby_list:
#     j += 1
#     print ' '.join([str(j), str(country.pot), str(country.all)])
# print '%%%%'

# groupA = Group('Group A')
# for i in range(1, 5):
#     groupA.add_member(random.choice(utils.generate_standby_list(country_list, i, groupA.valid_confederations)), i)
# print groupA.all
# members_temp = groupA.members.values()
# groupA.rm_member(1)
# print groupA.all
# for v in members_temp:
#     print v.all
# groupA.clear_members()
# print groupA.all
# for v in members_temp:
#     print v.all

# groupA = Group('Group A')
# for i in range(1, 5):
#     groupA.add_member(random.choice(utils.generate_standby_list(country_list, i, groupA.valid_confederations)), i)
# print groupA.all
# members_temp = groupA.members.values()
# print country_dict['Serbia'].all
# country_dict['Serbia'].add_into_group(groupA)
# print groupA.all
# print country_dict['Serbia'].all
# for v in members_temp:
#     print v.all

# group_test = Group('Group Test')
# for i in range(1, 5):
#     group_test.add_member(random.choice(utils.generate_standby_list(country_list, i, group_test.valid_confederations)), i)
# print group_test.all
# members_temp = group_test.members.values()
# print utils.num_of_coutries_in_group(group_test, ['Japan', 'Sweden', 'Spain', 'Brazil'])


# def goupping_function_2018(group_list, country_list, **kwargs):
#     utils.reset_countries(country_list)
#     country_dict = {}
#     for country in country_list:
#         country_dict[country.name] = country
#     country_dict['Russia'].is_host()
#     utils.set_pots(country_list, num_of_groups=8)

#     fail_to_group = False
#     try:
#         for j in range(1, 5):
#             for group in group_list:
#                 if group_list.index(group) == 0 and j == 1:
#                     group.add_member(country_dict['Russia'], j)
#                 else:
#                     group.add_member(random.choice(utils.generate_standby_list(country_list, j, group.valid_confederations)), j)
#     except WorldCupException as e:
#         fail_to_group = True
#         print 'Grouping Failed! Please read the following for detais:'
#         print e
#     if fail_to_group:
#         print '####################'
#         print 'Countries not selected:'
#         for country in country_list:
#             if not country.selected:
#                 print country.all
#         print '####################'

# world_cup_2018 = Cup('World Cup 2018')
# world_cup_2018.set_group_members(country_list, goupping_function_2018)
# print world_cup_2018.all_detailed
# print world_cup_2018.teams_in_same_group('England', 'Argentina')

# world_cup_2018.clear_groups()
# print world_cup_2018.all_detailed
