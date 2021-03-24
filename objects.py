class DTO(object):
    """Base mixin class for synthesizing JSON responses from the API."""
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

    def __str__(self):
        return str(self.json)

    def __repr__(self):
        return str(self.json)

    def set_attributes(self, attrs, sub=False):
        for attr, value in attrs.items():
            if sub and isinstance(value, dict):
                self.__setattr__(attr, DTO(value))
            else:
                self.__setattr__(attr, value)


class ActDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.tagLine = None
        self.gameName = None
        self.set_attributes(obj)

    def __getattribute__(self, name):
        return super(ActDTO, self).__getattribute__(name)


class AccountDTO(DTO):
    def __getattribute__(self, name):
        return super(AccountDTO, self).__getattribute__(name)


class ContentItemDTO(DTO):
    def __getattribute__(self, name):
        return super(ContentItemDTO, self).__getattribute__(name)


class PlatformDataDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj, sub=True)

    def __getattribute__(self, name):
        return super(PlatformDataDTO, self).__getattribute__(name)


class PlayerDTO(DTO):
    def __getattribute__(self, name):
        return super(PlayerDTO, self).__getattribute__(name)


class LeaderboardDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

        plys = [PlayerDTO(p) for p in obj["players"]]
        self.players = ContentList(plys)

    def __getattribute__(self, name):
        return super(LeaderboardDTO, self).__getattribute__(name)

class MatchlistEntryDTO(DTO):
    def __getattribute__(self, name):
        return super(MatchlistEntryDTO, self).__getattribute__(name)


class MatchlistDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

        hstry = [MatchlistEntryDTO(h) for h in obj["history"]]
        self.history = ContentList(hstry)

    def __getattribute__(self, name):
        return super(MatchlistDTO, self).__getattribute__(name)

# playerroundstats
class FinishingDamageDTO(DTO):
   def __getattribute__(self, name):
        return super(FinishingDamageDTO, self).__getattribute__(name) 

class KillsDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

        vctmLctn = [LocationDTO(l) for l in obj["victimLocation"]]
        plyrLctn = [PlayerLocationsDTO(p) for p in obj["playerLocations"]]
        fnshngDmg = [FinishingDamageDTO(f) for f in obj["finishingDamage"]]
        self.victimLocation = ContentList(vctmLctn)
        self.playerLocations = ContentList(plyrLctn)
        self.finishingDamage = ContentList(fnshngDmg)
    def __getattribute__(self, name):
        return super(KillsDTO, self).__getattribute__(name)

class DamageDTO(DTO):
    def __getattribute__(self, name):
        return super(DamagelDTO, self).__getattribute__(name)

class EconomyDTO(DTO):
    def __getattribute__(self, name):
        return super(EconomyDTO, self).__getattribute__(name)

class AbilityDTO(DTO):
    def __getattribute__(self, name):
        return super(AbilityDTO, self).__getattribute__(name)

class PlayerRoundStatsDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

        klls = [KillsDTO(k) for k in obj["kills"]]
        dmg = [DamageDTO(d) for d in obj["damage"]]
        ecnmy = [EconomyDTO(e) for e in obj["economy"]]
        ablty = [AbilityDTO(a) for a in obj["ability"]]
        self.kills = ContentList(klls)
        self.damage = ContentList(dmg)
        self.economy = ContentList(ecnmy)
        self.ability = ContentList(ablty)

    def __getattribute__(self, name):
        return super(PlayerRoundStatsDTO, self).__getattribute__(name)


# match
class MatchInfoDTO(DTO):
    def __getattribute__(self, name):
        return super(MatchInfoDTO, self).__getattribute__(name)

class AbilityCastsDTO(DTO):
   def __getattribute__(self, name):
        return super(AbilityCastsDTO, self).__getattribute__(name)

class PlayerStatsDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

        abltyCsts = [AbilityCastsDTO(a) for a in obj["abilityCasts"]]
        self.abilityCasts = ContentList(abltyCsts)
    def __getattribute__(self, name):
        return super(PlayerStatsDTO, self).__getattribute__(name)

class MatchPlayerDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

        plyrstts = [PlayerStatsDTO(s) for s in obj["stats"]]
        self.playerStats = ContentList(plyrstts)
    def __getattribute__(self, name):
        return super(MatchPlayerDTO, self).__getattribute__(name)

class TeamDTO(DTO):
    def __getattribute__(self, name):
        return super(TeamDTO, self).__getattribute__(name)

class LocationDTO(DTO):
    def __getattribute__(self, name):
        return super(LocationDTO, self).__getattribute__(name)

class PlayerLocationsDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

        lctn = [LocationDTO(l) for l in obj["location"]]
        self.location = lctn
    def __getattribute__(self, name):
        return super(PlayerLocationsDTO, self).__getattribute__(name)


class RoundResultDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

        plntPlyrLctns = [PlayerLocationsDTO(p) for p in obj["plantPlayerLocations"]]
        plntLctn = [LocationDTO(p) for p in obj["plantLocation"]]
        dfsPlyrLctns = [PlayerLocationsDTO(d) for d in obj["defusePlayerLocations"]]
        dfsLctn = [LocationDTO(d) for d in obj["defuseLocation"]]
        plyrStts = [PlayerRoundStatsDTO(p) for p in obj["playerStats"]]
        self.plantPlayerLocations = ContentList(plntPlyrLctns)
        self.plantLocation = ContentList(plntLctn)
        self.defusePlayerLocations = ContentList(dfsPlyrLctns)
        self.defuseLocation = ContentList(dfsLctn)
        self.playerStats = ContentList(plyrStts)

    def __getattribute__(self, name):
        return super(RoundResultDTO, self).__getattribute__(name)


class MatchDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

        mtchInf = [MatchInfoDTO(m) for m in obj["matchInfo"]]
        plyr = [MatchPlayerDTO(p) for p in obj["player"]]
        tms = [TeamDTO(t) for t in obj["teams"]]
        mtchInf = [RoundResultDTO(r) for r in obj["roundResult"]]
        self.matchInfo = ContentList(mtchInf)
        self.players = ContentList(plyr)
        self.teams = ContentList(tms)
        self.matchInfo = ContentList(mtchInf)

    def __getattribute__(self, name):
        return super(matchDTO, self).__getattribute__(name)

class ContentList(list, object):
    def get(self, name: str, default=None):
        """Safe method for getting items in the ContentList by name atter."""
        for item in self.copy():
            try:
                if item.name == name:
                    return item
                else: continue
            except AttributeError:
                continue

        return default

    def find(self, value: str, attr: str, default=None):
        """Find an item in the ContentList by it's given attribute value."""
        for item in self.copy():
            try:
                if getattr(item, attr) == value:
                    return item
                else: continue
            except AttributeError:
                continue
        
        return default





