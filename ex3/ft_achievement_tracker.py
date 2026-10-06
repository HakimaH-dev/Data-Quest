import random

base_list = {
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Sharp Mind",
    "TreasureHunter"
}

def gen_player_achievements():
    nombre = random.randint(1, 11)
    succes = random.sample(list(base_list), nombre )
    return set(succes)


def ft_achievement_tracker():
    player1 = "Hakima"
    player2 = "Wassim"
    player3 = "Mamoune"
    player4 = "Papou"
    Hakima = gen_player_achievements()
    Wassim = gen_player_achievements()
    Mamoune = gen_player_achievements()
    Papou= gen_player_achievements()

    all_achivement = set.union(Hakima,Wassim,Mamoune,Papou)
    commun = set.intersection(Hakima,Wassim,Mamoune,Papou)
    
    unique1 = set.union(Hakima) - set.union(Wassim,Mamoune,Papou)
    unique2 = set.union(Wassim) - set.union(Hakima,Mamoune,Papou)
    unique3 = set.union(Mamoune)- set.union(Hakima,Wassim,Papou)
    unique4 = set.union(Papou)-set.union(Hakima,Wassim,Mamoune)

    missing1 = all_achivement - set.union(Hakima)
    missing2 = all_achivement - set.union(Wassim)
    missing3 = all_achivement - set.union(Mamoune)
    missing4 = all_achivement - set.union(Papou)

    print("=== Achievement Tracker System ===")

    print(f"Player {player1}: {Hakima}")
    print(f"Player {player2}: {Wassim}")
    print(f"Player {player3}: {Mamoune}")
    print(f"Player {player4}: {Papou}\n")

    print(f"All distinct achievements:{all_achivement}\n")

    print(f"Commun achievements:{commun}\n")
    print(f"Only {player1} has:{unique1}")
    print(f"Only {player2} has: {unique2}")
    print(f"Only {player3} has: {unique3}")
    print(f"Only {player4} has: {unique4}\n")
    #print(f"Only {player4} has: {unique4}")

    print(f"{player1} is missing: {missing1}")
    print(f"{player2} is missing: {missing2}")
    print(f"{player3} is missing: {missing3}")
    print(f"{player4} is missing: {missing4}")

   

if __name__ == "__main__":
    ft_achievement_tracker()
