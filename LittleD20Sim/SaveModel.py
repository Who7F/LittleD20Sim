import json
import os.path
#Damage Dice Progression Chart
#1, 1d2, 1d3, 1d4, 1d6, 1d8, 1d10, 2d6, 2d8, 3d6, 3d8, 4d6, 4d8, 6d6, 6d8, 8d6, 8d8, 12d6, 12d8, 16d6

class SaveModel:
    def __init__(self, WeaponFile, CombatantFile):
        self.WeaponSave = WeaponFile
        self.CombatantSave = CombatantFile
        self.comWeap={}
        self.comComb={}
    
    def FileCheck(self, FileName):
        if not os.path.isfile(FileName):
            print('New File')
            with open(FileName, 'w') as outfile:json.dump({}, outfile)
        
    def Loader(self, FileName):
        self.FileCheck(FileName)
        with open(FileName) as json_file:
            return json.load(json_file)

    def StartUp(self):
        self.comWeap = self.Loader(self.WeaponSave)
        self.comComb = self.Loader(self.CombatantSave)
        return('Start up...\n')

        
    def AddWeapon(self, name, data):
        self.comWeap[name] = data

    def ClearWeapons(self):
        self.comWeap = {}

    def ListWeapon(self):
        return sorted(self.comWeap.keys())

    def InfoWeapons(self):
        for key, value in self.comWeap.items():
            print(key, value)
        
    def DumpWeapons(self):
        with open(self.WeaponSave, 'w') as outfile:json.dump(self.comWeap, outfile)
        print('saved')
        

        
    def AddCombatant(self,name,data):
        self.comComb[name] = data

    def ClearCombatant(self):
        self.comComb = {}
    
    def ListCombatant(self):
        return sorted(self.comComb.keys())

    def InfoCombatant(self):
        for key, value in self.comComb.items():
            print(key, value)

    def DumpCombatant(self):
        with open(self.CombatantSave, 'w') as outfile:json.dump(self.comComb, outfile)
        print('saved')
        

    def GetInactive(self, Combatant):
        return(self.comComb[Combatant]['Inactive'])

    def GetHitBonus(self, Combatant, Weapon):
        AttackType = self.AttackType(Weapon)
        if AttackType == 'Range':
            return(self.comComb[Combatant]['RangeH'])
        return(self.comComb[Combatant]['MeleeH'])

    def GetDamgeBonus(self, Combatant, Weapon):
        AttackType = self.AttackType(Weapon)
        if AttackType == 'Range':
            return(self.comComb[Combatant]['RangeD'])
        return(self.comComb[Combatant]['MeleeD'])

    def AttackType(self, Weapon):
        if self.comWeap[Weapon]['Type'] == 'Simple Ranged' or self.comWeap[Weapon]['Type'] == 'Martial Ranged' or self.comWeap[Weapon]['Type'] == 'Exotic Ranged':
            return 'Range'
        return 'Melee'

    def GetCritRange(self, Weapon):
        return self.comWeap[Weapon]['Crit']

    def GetCritMulti(self, Weapon):
        return self.comWeap[Weapon]['Multi']

    def GetDiceType(self, Weapon):
        return self.comWeap[Weapon]['Diec']

    def SizeMod(self, Combatant):
        return 0 #Not working

    def GetDefence(self, Combatant, Type):
        return self.comComb[Combatant][Type]

    def GetHealth(self, Combatant):
        return self.comComb[Combatant]['Health']

def main():
    Action = 'y'
    f = SaveModel('Weapon.txt','Combatent.txt')
    f.StartUp()
    print(f.GetInactive('Clu'))
    print(f.GetHitBonus('Kobold', 'Longbow'))
    print(f.GetDamgeBonus('Kobold', 'Sword'))
    print(f.AttackType('Hand Crossbow'))
    print(f.GetCritRange('Sword'))
    print(f.GetCritMulti('Sword'))
    print(f.GetDiceType('Sword'))
    print(f.GetDefence('Kobold', 'AC'))
    
      

if __name__=='__main__':
    main()
