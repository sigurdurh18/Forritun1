def openFile(filename):#pukes out the contents of the file in a 2 dementional list
    try:
        with open(filename) as fil:
            return [q.strip('\n').split(',') for q in fil]
    except Exception as e:
        print("Cannot find file",filename)
        return []

DOI=['Heart Disease Death Rate','Motor Vehicle Death Rate','Teen Birth Rate','Adult Smoking','Adult Obesity']#Diseasees Of Interest
def check(value):
    for i in DOI:
        if i in value:
            return True
    return False
def Filter(kek):
    return [[i for i in kek[0] if check(i)]]+[[line[0]]+[float(line[index].strip('%')) for index in range(1,len(kek[0])) if check(kek[0][index])] for line in kek[1:]]#mjög læsilegur og hreinn kóði

def satistics(kek):
    kik=[]#lines[disease[name,min[city name, stat], max[city name, stat]]]
    for i in range(len(kek[0])):
        kik.append([kek[0][i],[kek[1][0],kek[1][i+1]],[kek[1][0],kek[1][i+1]]])#set the default to the first colum
        for q in range(2, len(kek)):#we can skip the first city (because of the set default)
            if(kek[q][i+1]<kik[i][1][1]):
                kik[i][1][1]=kek[q][i+1]
                kik[i][1][0] = kek[q][0]
            if (kek[q][i+1] > kik[i][2][1]):
                kik[i][2][1] = kek[q][i+1]
                kik[i][2][0] = kek[q][0]
    return kik

def write(kek):
    print('{:<33}{:<27}{:6}{:<21}'.format('Indicator', 'Min', '', 'Max'))
    print('-' * 87)
    for i in kek:
        print('{:<33}{:<21}{:>6,.1f}{:6}{:<15}{:>6,.1f}'.format(i[0] + ':', i[1][0], i[1][1], '', i[2][0], i[2][1]))

fetch=openFile("riskFactors.csv")
if fetch:
    write(satistics(Filter(fetch)))
else:
    write([])