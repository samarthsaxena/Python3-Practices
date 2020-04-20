# demo the usage of OrderedDict object


# One of the downsides of ordinary dictionary is; it does NOT keep the track of order of items in which they're
# inserted.The concept of OrderedDict has been externalized that can cope with such bottleneck

from collections import OrderedDict as od

from Practices.Colour import Colour



def main():
    # List of of sport teams with wins and losses
    sportTeams = [
        ("Royal", (18, 12)), ("Rockets", (24, 6)), ("Cardinals", (20, 10)), ("Dragons", (22, 8)), ("Kings", (15, 15)),
        ("Chargers", (20, 10)), ("Jets", (16, 14)), ("Warriors", (25, 5))
    ]

    # Sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)
    print(f'Sorted teams key=wins {sortedTeams}')

    # TODO: Create an ordered dictionary of the teams
    teams = od(sortedTeams)
    print(teams)
    # Any item inserted in this OrderedDict object; will be added at the very end.
    # OrderedDict object would never sort the items , that would be done explicitly

    # TODO : use popitems to remove the top item
    tm_key, wl_value = teams.popitem(last=False)  # last = False i.e. 1st item from the beginning.
    print(f'Top item: {tm_key} with {wl_value[0]} / {wl_value[1]}')

    # TODO:  what are next the top 3 teams?
    for index, team in enumerate(teams, start=1):
        print(f'{index} {team}')
        if index == 4:
            break

    # TODO : Test for equality
    a = od({"a": 1, "b": 2, "c": 3})
    b = od({"a": 1, "b": 2, "c": 3})
    c = od({"a": 1, "c": 3, "b": 2})
    d = {"b": 2, "a": 1, "c": 3}

    print(f'(Same content and order )           {a} and {b} are equal : {a == b}')
    print(f'(Same content different order)      {a} and {c} are equal : {a == c}')
    print(f' Now if you compare an OrderedDict with a default dict()')
    print(f'(Same content different order)      {a} and {d} are equal : {a == d}')
    print(f'\n{Colour.YELLOW}{Colour.BOLD}When 2 OrderedDict are compared CONTENT & ORDER matters.')
    print(f'When an OrderedDict is compared with default dict() type ONLY THE CONTENT matters.{Colour.END}')


if __name__ == '__main__':
    main()
