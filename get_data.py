import requests
import json
from get_config import get_config
import configparser

settings = configparser.ConfigParser()
settings.read('config.ini')

s = requests.Session()
config = get_config()

r = s.post('https://signin.lds.org/login.html', {'username': settings['auth']['username'],
                                                 'password': settings['auth']['password']})

print('Getting your unit number...')
r = s.get(config['current-user-unit'])
my_unit = r.json()['message']

print('Getting unit membership (membership.json)...')
unit_membership_url = config['unit-membership'].replace('%@', my_unit)
r = s.get(unit_membership_url)
membership = r.json()
with open('data/membership.json', 'w+') as membership_file:
    json.dump(membership, membership_file)

print("Getting unit membership with callings (membership_callings.json)...")
unit_membership_with_callings_url = config['unit-members-and-callings-v2'].replace('%@', my_unit)
r = s.get(unit_membership_with_callings_url)
membership_with_callings = r.json()
with open('data/membership_callings.json', 'w+') as membership_file:
    json.dump(membership_with_callings, membership_file)

print("Getting Unit Statistics (unit-statistics.json)...")
r = s.get(config['unit-statistics'].replace('%@', my_unit))
statistics = r.json()
with open('data/unit-statistics.json', 'w+') as statistics_file:
     json.dump(statistics, statistics_file)

print("Getting Ministering Families (htvt.json)...")
r = s.get('https://www.lds.org/htvt/services/v1/%s/members' % my_unit)
htvt = r.json()
with open('data/htvt.json', 'w+') as htvt_file:
     json.dump(htvt, htvt_file)

print("Finding unique districts...")
ht_districts = []
for family in htvt['families']:
    id_ = family['responsibleHTAuxiliaryId']
    if id_ not in ht_districts:
        ht_districts.append(id_)
print("Found %d districts: %s" % (len(ht_districts), ht_districts))

districts = []
for district in ht_districts:
    print("Getting Companionships and Assignments for %s" % district)
    r = s.get('https://www.lds.org/htvt/services/v1/%s/districts/%s' % (my_unit, district))
    districts += r.json()

with open('data/districts.json', 'w+') as districts_file:
    json.dump(districts, districts_file)

