def fetchData():
    while True:
        try:
            with open(input("Enter filename: ")) as fil:
                kek=[]
                a=[]
                for line in fil:
                    a=line.strip('\n').split(";")
                    kek.append({"rank":int(a[0]),"name":a[1].strip().split(', '),"place":a[2].strip(),"elo":int(a[3]),"Birth Year":int(a[4])})
                return kek
        except FileNotFoundError:
            print("error")
        except TypeError:
            print("something wrong with the DATA")

def segrigate(Data,key):
    groups=dict()#{key:[values,values,values...]}
    for player in Data:
        if(player[key] not in groups):
            groups[player[key]]=[player]
        else:
            groups[player[key]].append(player)
    return groups

def satistics(group):#returns avredge statistics of elo
    elo=0
    for player in group:
        elo+=player['elo']
    return elo/len(group)


def writeNashonalList(groups):
    sortedGroups=sorted(groups.items())
    print("Players by birth year:\n-------------------")
    for place in sortedGroups:
        print('{} ({}) ({:.1f}):'.format(place[0], len(place[1]), satistics(place[1])))
        for player in place[1]:
            print('{:>40}{:>10d}'.format(player['name'][-1] + ' ' + player['name'][0], player['elo']))

def main():
    Data=fetchData()
    groups=segrigate(Data,'place')
    writeNashonalList(groups)
    groups=segrigate(Data,'Birth Year')
    writeNashonalList(groups)

main()
#gogn/assignments/development/chess-top-100.csv