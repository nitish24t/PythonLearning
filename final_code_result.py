import requests
import numpy as np

"""
Desc : Reads the https and returns json response after selecting the string
params: 
path : Http path
key_string : key for the json input
"""
def read_http_path(path,key_string):
  try:
    response_json = requests.get(path).json().get(key_string)
    return response_json
  except Exception as e:
    print("Exception while reading the json https {0}. \n Exception : {1}\n".format(path, e))

"""
Desc : Reads the input sources and creates datafreames of them
params: 
"""
def read_sources():
  print("reading the sources")
  json_people_res = read_http_path("https://api.nobelprize.org/v1/laureate.json", "laureates")
  json_location_res = read_http_path("https://api.nobelprize.org/v1/country.json","countries")
  return json_people_res,json_location_res

"""
Desc: Handles null values in Dictionary
"""
def check_null_field(dict, key):
  if key not in dict:
    return ""
  else:
    return dict.get(key)

def main():
  try:
    json_people_res,json_location_res = read_sources()
    location_dict = {}
    for elem in json_location_res:
      if elem.get('code') not in location_dict:
        location_dict[elem.get('code')] = elem.get('name')
 
    people_list = []
    print("traversing the json data")
    for elem in json_people_res:
#       id = elem.get('id')
      id = check_null_field(elem,'id')
      name = check_null_field(elem,'firstname')
      surname = check_null_field(elem,'surname')
      if name == "":
        name = check_null_field(elem,'surname')
      if name is not None and surname is not None:
        name = name + surname
      dob = check_null_field(elem,'born')
      gender = check_null_field(elem,'gender')
      prizes = check_null_field(elem,'prizes')
      prize_years = ""
      prize_categories = ""
      unique_prize_years = []
      unique_prize_categories = []
      for prize in prizes:
        prize_years = check_null_field(prize,'year')
        prize_category = check_null_field(prize,'category')
        unique_prize_years.append(prize_years)
        unique_prize_categories.append(prize_category)
      unique_prize_years = ';'.join(set(unique_prize_years))
      unique_prize_categories = ';'.join(set(unique_prize_categories))
      bornCountryCode = check_null_field(elem,'bornCountryCode')
      # lookup for country name from Dictionary
      bornCountryName = location_dict.get(bornCountryCode)
      people_list.append([name,dob,gender,unique_prize_years,unique_prize_categories,bornCountryName])
    np.savetxt("noble_prize_output.csv", rows, delimiter =", ", fmt ='% s') 
  except Exception as e:
    print("exeption raised : "+str(e))
    
    

"""
The main method
"""
main()