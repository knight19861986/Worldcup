from utils import confederations
from worldcup_exceptions import NonePotException, HasBeenSelectedException, IllegalConfederationException


class Country(object):
    def __init__(self, name, confederation=None, rank=None, pot=None):
        self.name = name
        self.set_confederation(confederation)
        self.rank = rank
        self.pot = pot
        self.selected = False
        self.host = False

    def __str__(self):
        return self.name

    def set_confederation(self, confederation):
        if confederation and confederation not in confederations:
            raise IllegalConfederationException('ERROR: Illegal confederation!')
        self.confederation = confederation

    def set_rank(self, rank):
        self.rank = rank

    def set_pot(self, pot):
        self.pot = pot

    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False

    def is_host(self):
        self.host = True

    def is_not_host(self):
        self.host = False

    def add_into_group(self, group):
        if not self.selected:
            if self.pot:
                group.add_member(self, self.pot)
            else:
                raise NonePotException('ERROR: Pot number of country must be set before added into a group!')
        else:
            raise HasBeenSelectedException('ERROR: Country that has been selected cannot be added into a group!')

    def __getattr__(self, key):
        if key == 'name':
            return self.name
        if key == 'confederation':
            return self.confederation
        if key == 'rank':
            return self.pot
        if key == 'pot':
            return self.pot
        if key == 'selected':
            return self.selected
        if key == 'host':
            return self.host

        if key == 'all':
            return {
                'name': self.name,
                'confederation': self.confederation,
                'rank': self.rank,
                'pot': self.pot,
                'host': self.host,
                'selected': self.selected
            }
