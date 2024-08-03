football_players=["Cristiano","Messi","Neymar","Quaresma","Nani"]
jsersey_numbers=[7,10,11,17,6]

football_players.append("Pogba")
football_players.insert(-1,"Gerrard")
football_players.remove("Gerrard")
print(football_players)

football_players.pop()
print(football_players)

print(football_players.index("Neymar"))
# print(football_players.index("Scholes"))
print(football_players.extend("Neymar"))
print(football_players.extend("Neymar"))
print(football_players)
print(football_players.count("Neymar"))

print(football_players.sort())

football_players.clear()
print(football_players)