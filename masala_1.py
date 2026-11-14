matritsa = [
    [1, 2, 3],
    [4, 5, 6]
]
yigindi = 0

for son in matritsa:
    for sonlar in son:
        yigindi += sonlar
        
print(f"Yigindi: {yigindi}")