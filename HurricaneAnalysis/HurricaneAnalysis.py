from collections import Counter, defaultdict

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(damages):
    #changes Billion and Million-values from String to floats
    updated_list = []
    for values in damages:
        if 'Damages not recorded' in values:
            updated_list.append('Damages not recorded')
        if 'M' in values:
            values = values.replace('M', '')
            updated_list.append(float(values) * 1000000)
        if 'B' in values:
            values = values.replace('B', '')
            updated_list.append(float(values) * 1000000000)
    return updated_list


# write your construct hurricane dictionary function here:
def convert_to_dict(name, month, year, max_wind, areas_affected, damage, death):
    hurricane_dict = {}
    for i in range(len(name)):
        hurricane_dict.update({name[i]:{ "Month": month[i], "Year": year[i], "Max Sustained Wind": max_wind[i], "Areas Affected": areas_affected[i], "Damage": damage[i], "Death": death[i]}})
    return hurricane_dict
hurricane_dict = (convert_to_dict(names, months, years, max_sustained_winds, areas_affected, update_damages(damages), deaths))
#print(hurricane_dict)



# write your construct hurricane by year dictionary function here:
def hurricanes_by_year(hurricanes):
    year_dict = {}
    for keys, values in hurricanes.items():
        for i in range(len(hurricanes)):
            year_dict.update({values['Year']: {keys: values}})
    return year_dict
year_dict = (hurricanes_by_year(hurricane_dict))
#print(year_dict)



# write your count affected areas function here:
def count_areas(hurricanes):
    areas = []
    areas_dict = {}
    for area in hurricanes.values():
        areas.append(area["Areas Affected"])
    for i in range(len(areas)):
        for x in range(len(areas[i])):
            if areas[i][x] not in areas_dict:
                areas_dict[areas[i][x]] = 1
            else:
                areas_dict[areas[i][x]] += 1
    return areas_dict
count_areas(hurricane_dict)




# write your find most affected area function here:
def most_affected(areas):
    area = []
    amount = []
    worst_area = {}
    for keys, values in areas.items():
        area.append(keys)
        amount.append(values)
    highest_amount = max(amount)
    worst_area[area[amount.index(highest_amount)]] = highest_amount
    return worst_area
red_area_dict = (most_affected(count_areas(hurricane_dict)))
#print("The most affected area is "+ str(red_area_dict))





# write your greatest number of deaths function here:
def greatest_number_of_deaths(hurricanes):
    deaths = []
    hurricane_names = []
    worst_hurricane = {}
    for keys, values in hurricanes.items():
        deaths.append(values['Death'])
        hurricane_names.append(keys)
    highest_death = max(deaths)
    worst_hurricane[hurricane_names[deaths.index(highest_death)]] = highest_death
    return worst_hurricane
#print(greatest_number_of_deaths(hurricane_dict))






# write your catgeorize by mortality function here:
def categorize_by_mortality(hurricanes):
    deaths = []
    hurricane_names = []
    mortality_scale = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for keys, values in hurricanes.items():
        hurricane_names.append(keys)
        deaths.append(values['Death'])
    tmp = dict(zip(hurricane_names, deaths))
    for keys, values in tmp.items():
        if values == 0:
            mortality_scale[0].append(keys)
            mortality_scale[0].append(values)
        elif values > 0 and values <= 100:
            mortality_scale[1].append(keys)
            mortality_scale[1].append(values)
        elif values > 100 and values <= 500:
            mortality_scale[2].append(keys)
            mortality_scale[2].append(values)
        elif values > 500 and values <= 1000:
            mortality_scale[3].append(keys)
            mortality_scale[3].append(values)
        elif values > 1000 and values <= 10000:
            mortality_scale[4].append(keys)
            mortality_scale[4].append(values)
        else:
            mortality_scale[5].append(keys)
            mortality_scale[5].append(values)
    return mortality_scale

#print(categorize_by_mortality(hurricane_dict))





# write your greatest damage function here:
def greatest_damage(hurricanes):
    damages = []
    names = []
    worst_damage = {}
    count = 0
    for key, value in hurricanes.items():
        names.append(key)
        if value['Damage'] == 'Damages not recorded':
            count += 1
            continue
        else:
            damages.append((int(value['Damage'])))
    number = float(max(damages))
    worst_damage[names[damages.index(number) + count]] = number
    return worst_damage
#print(greatest_damage(hurricane_dict))




# write your catgeorize by damage function here:
def categorize_by_damage(hurricane):
    damages = []
    hurricane_names = []
    damage_scale = {'NaN': [], 0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for keys, values in hurricane.items():
        hurricane_names.append(keys)
        damages.append(values['Damage'])
    tmp = dict(zip(hurricane_names, damages))
    for keys, values in tmp.items():
        if values == 'Damages not recorded':
            damage_scale['NaN'].append(keys)
            damage_scale['NaN'].append(values)
        elif values == 0:
            damage_scale[0].append(keys)
            damage_scale[0].append(values)
        elif values > 0 and values <= 100000000:
            damage_scale[1].append(keys)
            damage_scale[1].append(values)
        elif values > 100000000 and values <= 1000000000:
            damage_scale[2].append(keys)
            damage_scale[2].append(values)
        elif values > 1000000000 and values <= 10000000000:
            damage_scale[3].append(keys)
            damage_scale[3].append(values)
        elif values > 10000000000 and values <= 50000000000:
            damage_scale[4].append(keys)
            damage_scale[4].append(values)
        else:
            damage_scale[5].append(keys)
            damage_scale[5].append(values)
    return damage_scale
print(categorize_by_damage(hurricane_dict))