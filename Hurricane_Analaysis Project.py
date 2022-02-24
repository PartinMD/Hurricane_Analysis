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

# Update Recorded Damages
def damage_convert(damages):
  updated_list = []
  for i in damages:
    if i[-1] == "M":
      i = i.replace("M", "")
      i = float(i) * 1000000
      updated_list.append(i)
    elif i[-1] == "B":
      i = i.replace("B", "")
      i = float(i) * 1000000000
      updated_list.append(i)
    else:
      updated_list.append(i)
  return updated_list

updated_damages = damage_convert(damages)
#print(updated_damages)

# Create and view the hurricanes dictionary
def dictionary_constructor(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  zipped_lists = list(zip(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths))
  hurricane_data = {}
  for i in zipped_lists:
    hurricane_data[i[0]] = {"Name": i[0], "Months": i[1], "Years": i[2], "Max Sustained Winds": i[3], "Areas Affected": i[4], 'Damages': i[5], "Deaths": i[6]}
  return hurricane_data

hurricane_dictionary = dictionary_constructor(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricane_dictionary)

# Organizing by Year
def by_year_constructor(dictionary):
  hurricane_years = {}
  for i in dictionary:
    current_year = dictionary[i]['Years']
    if current_year not in hurricane_years:
      hurricane_years[current_year] = []
    hurricane_years[current_year].append(dictionary[i])
  return hurricane_years

hurricanes_by_year = by_year_constructor(hurricane_dictionary)
#print(hurricanes_by_year[1932])

# Counting Damaged Areas
def affected_constructor():
  affected_dictionary = {};
  for i in range(len(areas_affected)):
    areas = areas_affected[i]
    for area in areas:
      if(area not in affected_dictionary):
        affected_dictionary[area] = 1
      else:
        affected_dictionary[area] += 1
  return affected_dictionary
areas_affected_dict = affected_constructor()
#print(areas_affected_dict)

# Calculating Maximum Hurricane Count
def most_affected_function():
  most_affected_area = ""
  most_affected_count = 0
  for (area, count) in areas_affected_dict.items():
    if (count > most_affected_count):
      most_affected_count = count
      most_affected_area = area
  return (most_affected_area, most_affected_count)
#print(most_affected_function())

# Calculating the Deadliest Hurricane
death_data = zip(names, deaths)

def most_deadly_function():
  most_deadly_hurricane = ""
  highest_death_count = 0
  for (names, deaths) in death_data:
    if (deaths > highest_death_count):
      highest_death_count = deaths
      most_deadly_hurricane = names
  return (most_deadly_hurricane, highest_death_count)
#print(most_deadly_function())

# Rating Hurricanes by Mortality
# mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}

def mortality_rating_function(hurricane_dictionary):
  mortality_rating = {0: [], 1: [], 2:[], 3:[], 4:[], 5:[]}
  for i in hurricane_dictionary.values():
    if i["Deaths"] == 0:
      mortality_rating[0].append(i)
    elif i["Deaths"] > 0 and i["Deaths"] <= 100:
      mortality_rating[1].append(i)
    elif i["Deaths"] > 100 and i["Deaths"] <= 500:
      mortality_rating[2].append(i)
    elif i["Deaths"] > 500 and i["Deaths"] <= 1000:
      mortality_rating[3].append(i)
    elif i["Deaths"] > 1000 and i["Deaths"] <= 10000:
      mortality_rating[4].append(i)
    elif i["Deaths"] > 10000:
      mortality_rating[5].append(i)
  return mortality_rating

mortality_rating_dictionary = mortality_rating_function(hurricane_dictionary)
#print(mortality_rating_dictionary)

# Calculating Hurricane Maximum Damage
def max_damage_function(hurricane_dictionary):
  variable = [i["Damages"] for i in hurricane_dictionary.values() if type(i["Damages"]) == float]
  for i in hurricane_dictionary.values():
    if i["Damages"] == max(variable):
      return (i["Name"], i["Damages"])
#print(max_damage_function(hurricane_dictionary))

# Rating Hurricanes by Damage
#'''damage_scale = {0: 0,
#                1: 100000000,
#                2: 1000000000,
#               3: 10000000000,
#                4: 50000000000}

def damage_scale_function(hurricane_dictionary):
  damage_scale = {0: [], 1: [], 2:[], 3:[], 4:[], 5:[]}
  for i in hurricane_dictionary.values():
   if type(i["Damages"]) == float:
    if i["Damages"] == 0:
      damage_scale[0].append(i)
    elif i["Damages"] > 0 and i["Damages"] <= 100000000:
      damage_scale[1].append(i)
    elif i["Damages"] > 100000000 and i["Damages"] <= 1000000000:
      damage_scale[2].append(i)
    elif i["Damages"] > 1000000000 and i["Damages"] <= 10000000000:
      damage_scale[3].append(i)
    elif i["Damages"] > 10000000000 and i["Damages"] <= 50000000000:
      damage_scale[4].append(i)
    elif i["Damages"] > 50000000000:
      damage_scale[5].append(i)
  return damage_scale

damage_scale_dictionary = damage_scale_function(hurricane_dictionary)
#print(damage_scale_dictionary)