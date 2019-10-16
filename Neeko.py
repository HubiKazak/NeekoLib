import requests

class LoL:
    api = "" #doesn't work lol, get a new one
    region = "eun1"
    sumid = ""

    def GetSummoner(self,type,id,): # I hope it works, needs testing
        i = ""
        if (type == "nick"):
           i = "by-name/" 
        if (type == "aid"):
            i = "by-account/"
        if (type == "puuid" ):
            i = "by-puuid/"
        summoner = requests.get(f"https://{lol.region}.api.riotgames.com/lol/summoner/v4/summoners/{i}{id}?api_key={lol.api}")
        x = summoner.json()
        #json :
        #profileIconId == id of the icon that summoner has selected
        #name == name of the summoner (duh)
        #puuid == encrypted PUUID of the summoner
        #summonerLevel == idk some number :w
        #revisionDate == time (in epoch seconds when summoner did something {details in documentation})
        #id == summoner id
        #accountId == account id (different then summoner id !!!)
        return x


    def SIDGetMasteries(self, sid):
        summoner = requests.get(f"https://{lol.region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{sid}?api_key={lol.api}") #gets mastery levels (list) form summoner ID
        x = summoner.json()
        return x #returns a list, use [] to select single champions (descending from most mastery)
    #json :
    #chestGranted == boolean about chests
    #championLevel == mastery level on that champ
    #championPoints == mastery points on that champ
    #championId == id of the champ
    #championPointsUntilNextLevel == how many points are missing until next level (0 for mastery 6 and 7)
    #lastPlayTime == duh (in Unix miliseconds)
    #tokensEarned == how many mastery tokens were earned (and not used already)
    #championPointsSinceLastLevel == how many points were earned on this mastery level 
    #summonerId == duh
    
    def SIDGetChampMastery(self, sid, chid):
        summoner = requests.get(f"https://{lol.region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{sid}/by-champion/{chid}?api_key={lol.api}") #gets mastery level (JSON) form summoner ID and champion ID
        x = summoner.json()
        return x #same json as above, but for single champ
  
    def SIDGetTotalMastery(self, sid):
        summoner = requests.get(f"https://{lol.region}.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{sid}?api_key={lol.api}") #gets total mastery level (int) form summoner ID
        x = summoner.json()
        return x #returns an intiger with total mastery score of the summoner

    def GetFreeRotation():
        summoner = requests.get(f"https://{lol.region}.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={lol.api}") #gets free champion rotaion info
        x = summoner.json()
        return x 
    #json : 
    #freeChampionIdsForNewPlayers == list of ints (champion ids) of new player free champs
    #freeChampionIds == list of ints (champion ids) of regular free rotation
    #maxNewPlayerLevel == max level at which player can access new player free rotation

    def SIDGetCurrentGameInfo(self, sid):
        summoner = requests.get(f"https://{lol.region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{sid}?api_key={lol.api}") #gets current game information for given summoner id
        x = summoner.json()
        return x #the return is long and complicated, so I won't explain it here, consult riot API documentation

    def SIDGetCurrentGameInfo():
        summoner = requests.get(f"https://{lol.region}.api.riotgames.com/lol/spectator/v4/featured-games?api_key={lol.api}") #gets list of featured games
        x = summoner.json()
        return x #the return is long and complicated, so I won't explain it here, consult riot API documentation

lol = LoL()
a = lol.NGetSummoner("hubikazak")
asdf = a['id']
print(lol.SIDGetMasteries(asdf)[0])

#https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/hubikazak?api_key=RGAPI-b6d191ef-5200-411a-9afe-d80d1eb53a00


