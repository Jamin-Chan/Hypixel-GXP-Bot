import requests
import os

API_KEY = str(os.environ['uwutech'])


def get_guildInfo(guildName):
  try:
      mojang_data = requests.get(f'https://api.hypixel.net/guild?name={guildName}&key={API_KEY}').json()
  except:
      return "The name you provided is not valid. Are you sure this is the correct name? `{user}`"
  
  return mojang_data
  
def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count


def name_to_memberList(name):
    try:
      mojang_data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{name}?').json()
    except:
      return "The name you provided is not valid. Are you sure this is the correct name? `{user}`"

    else:
      data = requests.get(f"https://api.hypixel.net/player?key={API_KEY}&uuid={mojang_data['id']}").json()

    guildUuid = data["player"]["uuid"]

    findGuild = f"https://api.hypixel.net/findGuild?key={API_KEY}&byUuid={guildUuid}"
    res = requests.get(findGuild)
    data = res.json()
    guildId = data["guild"]
    guildUrl = f"https://api.hypixel.net/guild?key={API_KEY}&id={guildId}"
    res = requests.get(guildUrl)
    data = res.json()

    return data
    try:
      memberList = data["guild"]["members"]
      print(memberList)

      return memberList
    except:
      return "no guild"
