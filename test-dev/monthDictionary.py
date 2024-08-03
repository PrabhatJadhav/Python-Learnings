monthConversions={
    "Jan":"January",
    "Feb":"Febuary",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}

print(monthConversions["Feb"])
print(monthConversions.get('Dec1',"Invalid Key"))
print(monthConversions.values())
print(monthConversions.keys())