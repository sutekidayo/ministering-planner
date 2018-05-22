import json


htvt = {}
with open('data/htvt.json', 'r') as htvt_file:
    htvt = json.load(htvt_file)

districts = {}
with open('data/districts.json', 'r') as districts_file:
    districts = json.load(districts_file)


members = {}
with open('data/membership.json', 'r') as membership_file:
    members = json.load(membership_file)

households = {}
individuals = {}

for family in htvt['families']:
    households[family['headOfHouse']['individualId']] = family

for family in members:
    if family['spouse']:
        individuals[family['spouse']['individualId']] = family['spouse']
        individuals[family['spouse']['individualId']]['household'] = family
    if family['children']:
        for child in family['children']:
            individuals[child['individualId']] = child
            individuals[child['individualId']]['household'] = family
    individuals[family['headOfHouse']['individualId']] = family['headOfHouse']
    individuals[family['headOfHouse']['individualId']]['household'] = family

assignments = {}
companionships = {}

for district in districts:
    for companionship in district["companionships"]:
        for assignment in companionship['assignments']:
            assignments[assignment['individualId']] = companionship['id']
        teachers = []
        for teacher in companionship['teachers']:
            teachers.append(teacher['individualId'])
        companionships[companionship['id']] = teachers

for family in htvt['families']:
    teacher_names = ''
    if family['headOfHouse']['individualId'] in assignments:
        assignmentId = assignments[family['headOfHouse']['individualId']]
        teachers = companionships[assignmentId]
        for teacher in teachers:
            teacher_names += individuals[teacher]['formattedName'] + " & "
        teacher_names = teacher_names[:-3]
    print('%s: %s' % (family['formattedCoupleName'], teacher_names))
