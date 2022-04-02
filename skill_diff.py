import csv

current_skills = {}
improved_skills = {}
skill_diff = {}

with open('base.txt') as base:
    reader = csv.reader(base)

    for row in base:
        skill = row[:-2]
        skill_value = int(row.strip()[-1])

        if skill_value == 0:
            continue

        current_skills[skill] = skill_value

with open('improved.txt') as improved:
    reader = csv.reader(improved)

    for row in improved:
        skill = row[:-2]
        skill_value = int(row.strip()[-1])

        if skill_value == 0:
            continue

        improved_skills[skill] = skill_value


for skill, skill_value in improved_skills.items():

    if current_skills.get(skill, 0) != skill_value:
        skill_diff[skill] = skill_value

for skill, skill_value in skill_diff.items():
    print(f'Current skill {skill} {current_skills.get(skill, 0)} skill upto {skill_value}')
