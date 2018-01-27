from utils import confederations
from worldcup_exceptions import IllegalPotException


class Group(object):
    def __init__(self, name, size=4):
        self.name = name
        self.size = size
        self.members = {}
        self.valid_confederations = confederations[:]

    def __str__(self):
        return self.name

    def add_member(self, country, pot):
        if pot and pot in range(1, self.size + 1):
            if pot in self.members:
                self.rm_member(pot)
            self.members.update({pot: country})
            self.update_valid_confederations()
            country.select()
        else:
            raise IllegalPotException('ERROR: Illegal pot number!')

    def rm_member(self, pot):
        if pot and pot in range(1, self.size + 1):
            if pot in self.members:
                self.members[pot].unselect()
                self.members.pop(pot)
                self.update_valid_confederations()
        else:
            raise IllegalPotException('ERROR: Illegal pot number!')

    def clear_members(self):
        for pot in range(1, self.size + 1):
                if pot in self.members:
                    self.members[pot].unselect()
        self.members.clear()
        self.update_valid_confederations()

    def update_valid_confederations(self):
        self.valid_confederations = confederations[:]
        num_of_uefa = 0
        for k, v in self.members.iteritems():
            if v.confederation != 'UEFA':
                if v.confederation in self.valid_confederations:
                    self.valid_confederations.remove(v.confederation)
            else:
                num_of_uefa = num_of_uefa + 1
        if num_of_uefa > 1:
            if 'UEFA' in self.valid_confederations:
                self.valid_confederations.remove('UEFA')

    def __getattr__(self, key):
        if key == 'name':
            return self.name
        if key == 'size':
            return self.size
        if key == 'members':
            return self.members
        if key == 'valid_confederations':
            self.valid_confederations
        if key == 'all':
            ret = []
            ret.append(self.name + ':')
            for pot in range(1, self.size + 1):
                if pot in self.members:
                    member = self.members[pot]
                    ret.append(member.name)
            ret.append('####################')
            return '\n'.join(ret)
        if key == 'all_detailed':
            ret = []
            ret.append(self.name + ':')
            for pot in range(1, self.size + 1):
                if pot in self.members:
                    member = self.members[pot]
                    ret.append(str(member.all))
            ret.append('####################')
            return '\n'.join(ret)
