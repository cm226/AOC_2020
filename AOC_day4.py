import re

def validHeight(size, unit):
    if unit == 'in':
        return size.isnumeric() and int(size) >=59 and int(size) <=76
    elif unit == 'cm':
        return size.isnumeric() and int(size) >=150 and int(size) <=193
    else:
        return False

def Validate(attr, v):
    if attr == 'byr':
        return v.isnumeric() and len(v) == 4 and int(v) >= 1920 and int(v) <= 2002
    if attr == 'iyr':
        return v.isnumeric() and len(v) == 4 and int(v) >= 2010 and int(v) <= 2020
    if attr == 'eyr':
        return v.isnumeric() and len(v) == 4 and int(v) >= 2020 and int(v) <= 2030
    if attr == 'hgt':
        return validHeight(v[0:-2], v[-2:])
    if attr == 'hcl':
        match = re.search('#[0-9,a-z]{6}$',v)
        return match != None
    if attr == 'ecl':
        if v == 'amb':
            return True
        if v == 'blu':
            return True
        if v == 'brn':
            return True
        if v == 'gry':
            return True
        if v == 'grn':
            return True
        if v == 'hzl' :
            return True
        if v == 'oth':
            return True
        
        return False

    if attr == 'pid':
        return len(v) == 9 and v.isnumeric()

valid_attr = {
'byr' : False,
'iyr' : False,
'eyr' : False,
'hgt' : False,
'hcl' : False,
'ecl' : False,
'pid' : False
}

f = open("input_day4.txt")

passports =[]
tmppassport =''
for line in f:
    if line == '\n':
        passports.append(tmppassport.strip())
        tmppassport = ''
    else:
        tmppassport += line.replace('\n', ' ')

if tmppassport != '':
    passports.append(tmppassport.strip())

valid_count = 0;
for p in passports:
    attr_markers = valid_attr.copy()
    for attrs in p.split(' '):
        attr, v = attrs.split(':')
        attr_markers[attr] = Validate(attr,v)

    valid_passport =True
    if len(attr_markers) == 0:
        valid_passport = False

    for attr in attr_markers.values():
        if attr==False:
            valid_passport=False

    if valid_passport:
        print(p)
        print(attr_markers)
        print()
        valid_count +=1

print(valid_count)


