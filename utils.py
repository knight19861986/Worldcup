from worldcup_exceptions import WorldCupException
confederations = ['AFC', 'CAF', 'CONCACAF', 'CONMEBOL', 'OFC', 'UEFA']


def reset_countries(country_list):
    for country in country_list:
        country.unselect()


def set_pots(country_list, num_of_groups=8):
    country_list.sort(key=lambda x: (-x.host, x.rank))
    i = 1
    pot = 1
    for country in country_list:
        if i > num_of_groups:
            pot += 1
            i = 1
        country.pot = pot
        i += 1


def generate_standby_list(country_list, pot=None, confederations=None):
    res = []
    ok = False
    for country in country_list:
        if not country.selected:
            ok = True
        if pot and country.pot != pot:
            ok = False
        if confederations and country.confederation not in confederations:
            ok = False
        if ok:
            res.append(country)
            ok = False

    if res:
        return res
    else:
        raise WorldCupException('ERROR: Failed to generate standby list!')


def num_of_countries_in_group(group, country_name_list):
    res = 0
    for country in group.members.values():
        if country.name in country_name_list:
            res += 1
    return res
