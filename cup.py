import random
import utils
from group import Group
from worldcup_exceptions import WorldCupException


class Cup(object):
    def __init__(self, name, num_of_groups=8, group_size=4):
        self.name = name
        self.num_of_groups = num_of_groups
        self.group_size = group_size
        self.set_groups()

    def __str__(self):
        return self.name

    def set_groups(self):
        self.groups = []
        for i in range(0, self.num_of_groups):
            self.groups.append(Group(' '.join(['Group', chr(ord('A') + i)]), self.group_size))

    def set_group_members(self, country_list, groupping_function=None, **kwargs):
        self.clear_groups()
        if groupping_function:
            groupping_function(self.groups, country_list, **kwargs)
        else:
            fail_to_group = False
            try:
                for j in range(1, self.group_size + 1):
                    for group in self.groups:
                        group.add_member(random.choice(utils.generate_standby_list(country_list)), j)
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

    def clear_groups(self):
        for group in self.groups:
            group.clear_members()

    def teams_in_same_group(self, country_name_list):
        res = False
        if len(country_name_list) > 1 and len(country_name_list) <= self.group_size:
            for group in self.groups:
                num = utils.num_of_countries_in_group(group, country_name_list)
                if num > 0 and num < len(country_name_list):
                    break
                elif num == len(country_name_list):
                    res = True
                    break
        return res

    def __getattr__(self, key):
        if key == 'name':
            return self.name
        if key == 'num_of_groups':
            return self.num_of_groups
        if key == 'groups':
            return self.groups
        if key == 'all':
            ret = []
            ret.append('####################')
            ret.append('Groups of ' + self.name + ':')
            ret.append('####################')
            for group in self.groups:
                ret.append(group.all)
            return '\n'.join(ret)
        if key == 'all_detailed':
            ret = []
            ret.append('####################')
            ret.append('Groups of ' + self.name + ':')
            ret.append('####################')
            for group in self.groups:
                ret.append(group.all_detailed)
            return '\n'.join(ret)
