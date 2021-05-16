from SaveModel import SaveModel
from DiceModel import diceRoller
from UserReq import UserReq
from Menu import Menu
from SimComp import SimComp
import random

#python 3.5.2
#{'1':[1, 1], '1d2':[1, 2], '1d3':[1, 3], '1d4':[1, 4], '1d6':[1, 6], '1d8':[1, 8], '1d10':[1, 10], '2d6':[2, 6], '2d8':[2, 8], '3d6':[3, 6], '3d8':[3, 8], '4d6':[4, 6], '4d8':[4, 8], '6d6':[6, 6], '6d8':[6, 8], '8d6':[8, 6], '8d8':[8, 8], '12d6':[12, 6], '12d8':[12, 8], '16d6':[16, 6]}


def MyFunc(e):
    return (e['Initiative']) #Used to sort SimInstance[{'Initiative': Initiative,'ListPointer':Number,'Wounds':0}] by Initiative
       
def main():

    outText = {
    'base':['  c: Combatents\n  w: Weapons\n  s: Simulation\n  e: Exit\n:'],
    'Weapin':['Current Loaded Weapons\n','  a: Weapon Add\n  c: Weapons Clear\n  i: Weapons Information\n  s: Weapons Save\n  e: Exit\n:'],
    'Combatent':['Current Loaded Combatants\n','  a: Combatant Add\n  c: Combatant Clear\n  i: Combatants Information\n  s: Combatants Save\n  e: Exit\n:'],
    'Simulation':['  a: Add\n  c: Clear\n  i: Information\n  r: Run\n  e: Exit\n:']
    } #Can be moved to a json file.  
    SetGroups = [
    'PC',
    'NPC'
    ]
    WeaponFile = 'Weapon.txt'
    CombatantFile = 'Combatent.txt'

    SaveData = SaveModel(WeaponFile, CombatantFile) #Instance of a class
    print(SaveData.StartUp())

    while True:
        UserAction = Menu().Base()
        
        if UserAction == 'Exit':
            break

        if UserAction == 'Weapon':
            while True:
                UserAction = Menu().Modify(SaveData.ListWeapon(), outText['Weapin'])
                if UserAction == 'Exit':
                    break
                if UserAction == 'Add':
                    name = input('\nName of weapon:')
                    SaveData.AddWeapon(name, UserReq().AddWeapon())

                if UserAction == 'Clear':
                    SaveData.ClearWeapons()

                if UserAction == 'Information':
                    SaveData.InfoWeapons()

                if UserAction == 'Save':
                    SaveData.DumpWeapons()

        if UserAction == 'Combatent':
            while True:
                UserAction = Menu().Modify(SaveData.ListCombatant(), outText['Combatent'])
                if UserAction == 'Exit':
                    break
                if UserAction == 'Add':
                    name = input('\nName of Combatent:')
                    SaveData.AddCombatant(name, UserReq().AddChar())

                if UserAction == 'Clear':
                    SaveData.ClearCombatant()

                if UserAction == 'Information':
                    SaveData.InfoCombatant()

                if UserAction == 'Save':
                    SaveData.DumpCombatant()
                

        if UserAction == 'Simulation':   
            SimList = []#(Name, Weapon, Group).  
            while True:
                UserAction = Menu().Simulation(outText['Simulation'])
                if UserAction == 'Exit':
                    break
                if UserAction == 'Add':
                    Name = UserReq().PickItem(SaveData.ListCombatant(), 'add text')
                    Weapon = UserReq().PickItem(SaveData.ListWeapon(), 'add text')
                    Group = UserReq().PickItem(SetGroups, 'add text')
                    Number = UserReq().InputNumber('Number of\n: ')
                    print(SimComp().AppendList(Name, Weapon, Group, Number, SimList))
                if UserAction == 'Clear':
                    SimList = []
                if UserAction == 'Information':
                    print(SimList)
                if UserAction == 'RunSim':
                    tCheck = {} #Using a Dict to cant the number of groups
                    PartyCheck = False
                    for i in range(len(SimList)):
                        tCheck[SimList[i][2]] = 'True' 
                    if len(tCheck) > 1:
                        print('good to go')
                        PartyCheck = True
                    
                    if PartyCheck == True:
                        NumberOfSims = UserReq().InputNumber('Number of Simulation\n: ')
                        DeathLog = {SetGroups[0]:0,SetGroups[1]:0}
                        for i in range(NumberOfSims):
                            print('Simulation', i+1)#Python counts from 0
                            SimInstance = []
                            SimGroups = {SetGroups[0]:{'Remaining':0, 'Focus':0},SetGroups[1]:{'Remaining':0, 'Focus':0}}#Could be put in to a for loop to allow for expansion 
                            #SimList = [[],[]], SimInstance = [{},{}], SimGroups{{},{}} ~ A RDBMS would of been lot less work! 
                            
                            for x in range(len(SimList)):#Sets both SimInstance and the 'Remaining' of SimGroups. But does not set the 'Focus'
                                SimComp().SetSim(x, random.randint(1,20) + SaveData.GetInactive(SimList[x][0]), SimList[x][2], SimInstance, SimGroups)#Number, Initiative, Group

                            SimInstance.sort(key=MyFunc, reverse=True)#Sort need to happen before the Focus is set

                            SimComp().GetFocus(SetGroups[0], SetGroups[1], SimInstance, SimGroups, SimList)
                            SimComp().GetFocus(SetGroups[1], SetGroups[0], SimInstance, SimGroups, SimList)
                            print(SimGroups, 'check group\n')
                            #The discrepancy between Remaining and Focuse is due to counting from 0.
                            
                                                        
                            count = 0
                            #print(SimList[SimComp().TargetPointer(count, SimList, SimInstance, SimGroups)][0])#what are they hitting
                            #print(SimList[SimInstance[count]['ListPointer']][0])#what they are
                            kiri = 0
                            while True:
                                
                                #print(SimList[SimInstance[count]['ListPointer']][0])
                                #print(SimList[SimInstance[count]['ListPointer']][1])
                                #print(count, 'check count\n')
                                #print(count, SimList, SimInstance, SimGroups)
                                #print(SimComp().TargetPointer(count, SimList, SimInstance, SimGroups), '\n')
                                HitResult = diceRoller().HitRoll(
                                    SaveData.GetCritRange(SimList[SimInstance[count]['ListPointer']][1]),
                                    SaveData.GetHitBonus(SimList[SimInstance[count]['ListPointer']][0], SimList[SimInstance[count]['ListPointer']][1]),
                                    SaveData.GetDefence(SimList[SimComp().TargetPointer(count, SimList, SimInstance, SimGroups)][0], 'AC'),
                                    True) #Alway True.  Crit Range, Hit Bonus, Defence, Crit Enabled. Return Miss, Hit or Critical
                                
                                if HitResult == 'Miss':
                                    print('Missed')
                                else:
                                    Message = ''
                                    if HitResult == 'Hit': 
                                        Multi = 1
                                        Message = 'Hit For '  
                                    elif HitResult == 'Critical':
                                        Multi = SaveData.GetCritMulti(SimList[SimInstance[count]['ListPointer']][1])
                                        Message = 'Critical Hit For '
                                    else:
                                        print('Error.  Attack did not hit, miss or crit')
                                    #kiri kiri kiri
                                    KiriKiri = diceRoller().DamageRoll(
                                        SaveData.GetDiceType(SimList[SimInstance[count]['ListPointer']][1]),
                                        SaveData.GetDamgeBonus(SimList[SimInstance[count]['ListPointer']][0], SimList[SimInstance[count]['ListPointer']][1]),
                                        Multi,
                                        SaveData.SizeMod(SimList[SimInstance[count]['ListPointer']][0])
                                        )#DiceType, BonusDamage, Multi, Size

                                    print(Message, KiriKiri)#KiriKiri is from an old horror film
                                    SimInstance[SimComp().FocusPointer(count, SimList, SimInstance, SimGroups)]['Wounds'] += KiriKiri

                                    if SimInstance[SimComp().FocusPointer(count, SimList, SimInstance, SimGroups)]['Wounds'] > SaveData.GetHealth(SimList[SimComp().TargetPointer(count, SimList, SimInstance, SimGroups)][0]):
                                        
                                        DefGroup = SimList[SimComp().TargetPointer(count, SimList, SimInstance, SimGroups)][2]
                                        AttGroup = SimList[SimInstance[count]['ListPointer']][2]
                                        print('dead', DefGroup)
                                        if SimGroups[DefGroup]['Remaining'] == 0:
                                            DeathLog[DefGroup] += 1
                                            print('n\End Block\n')
                                            break
                                        else:
                                            SimComp().FocusDead(count, SimList, SimInstance, SimGroups,)
                                            if count > SimGroups[AttGroup]['Focus']:
                                                count += -1
                                                
                                            SimComp().GetFocus(DefGroup, AttGroup,
                                                         SimInstance, SimGroups, SimList)#def,attack
                                            


                                        
                                if count == len(SimInstance) - 1:
                                    count = 0
                                else:
                                    count += 1

                                
                                  
                            
                            #print(SimInstance)
                            #print(SimGroups)
                            #print(SimList)
                        print(DeathLog)
                            
                    else:
                        print('You have less then two groups')

    print('This Is The End')
   
    
    

    
    

    
        
    

if __name__=='__main__':
    main()

#   for x in range(NumberBandit):
#       Bandit = Bandit + [[CharModle(),'']]
#       Bandit[x][0].LoadStats(iStats)
#       Bandit[x][1] = rDice.D20Roll() + Bandit[x][0].iInit
#       print(Bandit[x][1])
    
