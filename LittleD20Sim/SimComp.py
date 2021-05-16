import random

class SimComp:
      
    def AppendList(self, Name, Weapon, Group, Number, SimList):
        for x in range(Number):
            SimList.append([Name, Weapon, Group])#This originally hold bonus.  But never got added
        return 'Added ' + str(Number) + ' ' + Name + ' To List In Group ' + Group

    def SetSim(self, Number, Initiative, Group, SimInstance, SimGroups):
        SimGroups[Group]['Remaining'] += 1
        SimInstance.append({'Initiative': Initiative,'ListPointer':Number,'Wounds':0})
        
    def GetFocus(self, DefGroup, AttfGroup, SimInstance, SimGroups, SimList):
        Count = 0
        #print(SimGroups[DefGroup])
        SimGroups[DefGroup]['Remaining'] += -1
        RNumber = random.randint(0,SimGroups[DefGroup]['Remaining'])
        for i in range(len(SimInstance)):
            if (SimList[SimInstance[i]['ListPointer']][2]) == DefGroup:
                if Count == RNumber:
                    #print(DefGroup, AttfGroup , i)
                    SimGroups[AttfGroup]['Focus'] = i #need to switch
                    break
                Count += 1
        #The discrepancy between Remaining and Focuse is due to counting from 0.  
        #eg. 'PC': {'Remaining': 0, 'Focus': 2}, 'NPC': {'Remaining': 1, 'Focus': 1}
        #by added one: 'PC': {'Remaining': 1, 'Focus': 3}, 'NPC': {'Remaining': 2, 'Focus': 2}
        #Combined list, so 'Focus' are added together

    def FocusDead(self, count, SimList, SimInstance, SimGroups,):
        Group = SimList[SimInstance[count]['ListPointer']][2]
        SimInstance.pop(self.FocusPointer(count, SimList, SimInstance, SimGroups))
        for iKey in SimGroups.keys():
            if iKey != Group:
                if SimGroups[iKey]['Focus'] > SimGroups[Group]['Focus']:
                    SimGroups[iKey]['Focus'] += -1
        
    def TakeWounds(self, Damage, Focus, SimInstance):
        SimInstance[Focus]['Wounds'] += Damage

    def TargetPointer(self, count, SimList, SimInstance, SimGroups):#return int that point to SimList. Targets [name, weapon, group]
        #print('\n:', count, SimInstance[count], SimList[SimInstance[count]['ListPointer']],SimGroups[SimList[SimInstance[count]['ListPointer']][2]], SimInstance[SimGroups[SimList[SimInstance[count]['ListPointer']][2]]['Focus']])
        return SimInstance[SimGroups[SimList[SimInstance[count]['ListPointer']][2]]['Focus']]['ListPointer']
    
    def FocusPointer(self, count, SimList, SimInstance, SimGroups):#return int that point to SimInstance [Initiative, Wounds, ListPointer]
        #print('\n:', count, SimInstance[count], SimList[SimInstance[count]['ListPointer']], SimGroups[SimList[SimInstance[count]['ListPointer']][2]])
        return SimGroups[SimList[SimInstance[count]['ListPointer']][2]]['Focus']

    def TurnPointer(self, count):
        return count
        
        
                        
    def bingo(self, number):
        xNumber = []
        for i in range(number):
            xNumber.append(i)
        return xNumber

    def CallTarget(self, Group, SimGroups):
        i = random.randint(0,len(SimGroups[Group])-1)
        rItem = SimGroups[Group][i]
        SimGroups[Group].pop(i)
        return rItem
                        

def MyFunc(e):
    return (e['Initiative']) 


def main():
    
    TestComb = {
    'Clu': {'Inactive': 1, 'RangeH': 3, 'MeleeD': -1, 'RangeD': -1, 'MeleeH': 1, 'AC': 15, 'Touch': 12, 'Flat': 14, 'Health': 11},
    'Yori': {'Inactive': 1, 'RangeH': 3, 'MeleeD': -1, 'RangeD': -1, 'MeleeH': 1, 'AC': 15, 'Touch': 12, 'Flat': 14, 'Health': 11},
    'Sark': {'Inactive': 1, 'RangeH': 3, 'MeleeD': -1, 'RangeD': -1, 'MeleeH': 1, 'AC': 15, 'Touch': 12, 'Flat': 14, 'Health': 9},
    'Gibbs': {'Inactive': 2, 'RangeH': 3, 'MeleeD': -1, 'RangeD': -1, 'MeleeH': 1, 'AC': 15, 'Touch': 12, 'Flat': 14, 'Health': 9},
    'Guards': {'Inactive': 1, 'RangeH': 3, 'MeleeD': -1, 'RangeD': -1, 'MeleeH': 1, 'AC': 15, 'Touch': 12, 'Flat': 14, 'Health': 9}
    }

    TestWep = {
    'Sling': {'Diec': 4, 'Range': 50, 'Multi': 2, 'Type': 'Simple Ranged', 'Crit': 20},
    'sword': {'Diec': 5, 'Crit': 19, 'Multi': 2, 'Range': 0, 'Type': 'Martial One-Handed Melee'}
    }

    SimList = []
    SimInstance = []
    SimGroups = {'Trash':{'Remaining':0, 'Focus':0},'Player':{'Remaining':0, 'Focus':0}}    

    f = SimComp()

    print(f.AppendList('Guards', 'sword', 'Trash', 2, SimList))
    print(f.AppendList('Clu', 'sword', 'Player', 1, SimList))
    print(f.AppendList('Gibbs', 'sword', 'Trash', 1, SimList))
    print(f.AppendList('Sark', 'sword', 'Trash', 1, SimList))
    print(f.AppendList('Yori', 'sword', 'Player', 1, SimList))
    
    print('\n')
    print(SimList)

    for x in range(len(SimList)):
        f.SetSim(x, random.randint(1,20) + TestComb[SimList[x][0]]['Inactive'], SimList[x][2], SimInstance, SimGroups)

    SimInstance.sort(key=MyFunc, reverse=True)

    f.GetFocus('Trash', 'Player', SimInstance, SimGroups, SimList)
    f.GetFocus('Player', 'Trash', SimInstance, SimGroups, SimList)

    print(SimGroups)
    print('\n\n')
    print(SimInstance)

    count = 0

    #print(SimList[f.FocusPointer(count, SimList, SimInstance, SimGroups,)][2])
    #print(SimInstance[f.TargetPointer(count, SimList, SimInstance, SimGroups)])
    
    print('##')
    print(SimList[f.TargetPointer(count, SimList, SimInstance, SimGroups)][2])
    print(SimList[SimInstance[count]['ListPointer']][2])
    print('##')
    DefGroup = SimList[f.TargetPointer(count, SimList, SimInstance, SimGroups)][2]
    print(DefGroup, 'hell')

    f.FocusDead(count, SimList, SimInstance, SimGroups,)
    
    #f.GetFocus(SimList[f.TargetPointer(count, SimList, SimInstance, SimGroups)][2],
    #           SimList[SimInstance[count]['ListPointer']][2],
    #           SimInstance, SimGroups, SimList)
    #Good to know I'm not the only thing getting confused 
    
    f.GetFocus(DefGroup, SimList[SimInstance[count]['ListPointer']][2],
               SimInstance, SimGroups, SimList)#def,attack


    print(SimInstance)
    print(SimGroups)
    print('\n')

    print('##')
    print(SimList[f.TargetPointer(count, SimList, SimInstance, SimGroups)][2])
    print(SimList[SimInstance[count]['ListPointer']][2])
    print('##')
    DefGroup = SimList[f.TargetPointer(count, SimList, SimInstance, SimGroups)][2]
    if SimGroups[DefGroup]['Remaining'] == 0:
        print('gg')
    else:
        f.FocusDead(count, SimList, SimInstance, SimGroups,)
        f.GetFocus(DefGroup, SimList[SimInstance[count]['ListPointer']][2],
                     SimInstance, SimGroups, SimList)#def,attack

    print(SimInstance, 'o')
    print(SimGroups)

    

if __name__=='__main__':
    main()
