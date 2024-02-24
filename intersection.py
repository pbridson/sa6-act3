eat_fish = ["dolphin", "gannet", "grizzly bear", "osprey", "shark"]
can_fly = ["gannet", "hummingbird", "osprey", "robin", "vampire bat"]

eat_fish_and_fly = list(filter(lambda x: x in can_fly, eat_fish))
print(eat_fish_and_fly)