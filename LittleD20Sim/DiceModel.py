import random
#1, 1d2, 1d3, 1d4, 1d6, 1d8, 1d10, 2d6, 2d8, 3d6, 3d8, 4d6, 4d8, 6d6, 6d8, 8d6, 8d8, 12d6, 12d8, 16d6
class diceRoller:
 
    DiceType = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 6],
                [1, 8], [1, 10], [2, 6], [2, 8], [3, 6],
                [3, 8], [4, 6], [4, 8], [6, 6], [6, 8],
                [8, 6], [8, 8], [12, 6], [12, 8], [16, 6]]
    
    def D20Roll(self):
        return random.randint(1, 20)

    def HitRoll(self, Crit, HitBonus, TargetNumber, CritEnabled):
        ThisRoll = self.D20Roll()
        if ThisRoll + HitBonus >= TargetNumber and ThisRoll != 1 or ThisRoll == 20 and ThisRoll != 1:
            if ThisRoll >= Crit:
                ThisRoll = self.D20Roll()
                if ThisRoll + HitBonus >= TargetNumber and CritEnabled == True:
                    return 'Critical'
            return 'Hit'
        return 'Miss'

    def DamageRoll(self, GetDiceType, BonusDamage, Multi, Size):
        ToldDamage = 0
        DiceType = GetDiceType + Size #Should of just saved and int
        if DiceType < 0:
            DiceType = 0
        elif DiceType > 19:
            DiceType = 19 
        for i in range(Multi * self.DiceType[DiceType][0]):
            RolledDamage = random.randint(1, self.DiceType[DiceType][1]) + BonusDamage
            ToldDamage += RolledDamage   
        return ToldDamage

                    
def main():
    f = diceRoller()

    
    HitResult = 'Hit'
    if HitResult == 'Hit':
        print('j')
    print(f.DiceType[0])
    print(f.DamageRoll(5,0 ,1, 22), '!')
    print(f.DamageRoll(5,0 ,1, 0), '!')

    for i in range(20):
        print(f.HitRoll(18,-20,13, True))
    

    


if __name__=='__main__':
    main()
