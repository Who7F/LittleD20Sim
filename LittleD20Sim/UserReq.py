class UserReq:

    
    def PickItem(self, KeyList, InText):
        text = ''
        for i in range(len(KeyList)):
            text = text + str(i+1) + ": " + str(KeyList[i]) + '\n'
        text = text + ': '
        ListI = self.LimitInputNumber(text, len(KeyList))    
        return KeyList[ListI-1]


    def InputNumber(self, message):
        userInput = ''
        while isinstance(userInput, int) == False:
            try:
                userInput = int(input(message))
            except ValueError:
                print('Error: user input is not an integer')
        return userInput
        


    def AddChar(self):
        Health = self.InputNumber('Health Point :')
        Inactive = self.InputNumber('inactive     :')
        AC = self.InputNumber('AC           :')
        Touch = self.InputNumber('Touch        :')
        Flat = self.InputNumber('Flat         :')
        RangeH = self.InputNumber('Range Hit    :')
        RangeD = self.InputNumber('Range Damage :')
        MeleeH = self.InputNumber('Melee Hit    :')
        MeleeD = self.InputNumber('Melee Damage :')
        SizeB = self.InputNumber('Size Bonuse  :')
        return {'Health':Health, 'Inactive':Inactive, 'AC':AC, 'Touch':Touch, 'Flat':Flat, 'RangeH':RangeH, 'RangeD':RangeD, 'MeleeH':MeleeH, 'MeleeD':MeleeD}


    def LimitInputNumber(self, message, limit):
        while True:
            KeyNumber = self.InputNumber(message)
            if KeyNumber >0 and KeyNumber <limit+1:
                break
        return KeyNumber

            
    
    def AddWeapon(self):
        WepRang = self.InputNumber('Weapon Range          :')
        WepCrit = self.InputNumber('Weapon Crit Range     :')
        WepCritx = self.InputNumber('Weapon Crit Mutplayer :')
        WepDice = (self.LimitInputNumber('Damage Dice 1:1, 2:1d2, 3:1d3, 4:1d4, 5:1d6, 6:1d8, 7:1d10, 8:2d6, 9:2d8:', 9)-1)
        
        sTypeNum = self.LimitInputNumber('1:Simple, 2:Martial  3:Exotic:', 3)
                    
        if sTypeNum == 1:
            sWepType ='Simple '
            TypeNum = self.LimitInputNumber('1:Simple Light Melee, 2:Simple One-Handed Melee, 3:SimpleTwo-Handed Melee Weapons, 4:Simple Ranged, 5:Simple Unarmed:', 5)                
        elif sTypeNum == 2:
            sWepType ='Martial '
            TypeNum = self.LimitInputNumber('1:Martial Light Melee, 2:Martial One-Handed Melee, 3:Martial Two-Handed Melee, 4:Martial Ranged Weapons:', 4)
        elif sTypeNum == 3:
            sWepType ='Exotic '
            TypeNum = self.LimitInputNumber('1:Exotic Light Melee, 2:Exotic One-Handed Melee, 3:Exotic Two-Handed Melee, 4:Exotic Ranged Weapons:', 4)

        if TypeNum == 1:
            WepType = 'Light Melee'
        elif TypeNum == 2:
            WepType = 'One-Handed Melee'
        elif TypeNum == 3:
            WepType = 'Two-Handed Melee'
        elif TypeNum == 4:
            WepType = 'Ranged'
        elif TypeNum == 5:
            WepType = 'Unarmed'   
        
        return {'Range': WepRang, 'Crit':WepCrit, 'Multi':WepCritx, 'Diec':WepDice, 'Type':sWepType+WepType}


def MyFunc(e):
    print(e)
    return (e['year'], e['car'])

        
def main():
    print('hello')
    dog = ''   
    for i in range(5):
        dog = dog + str(5) + ": " + str(6) + '\n'
    print(dog)
    

    data = {}
    
    data[input('Name:')] = UserReq().AddChar()
    print(data)
    print(data['sword']['Range'])
    
    

    
    


if __name__=='__main__':
    main()
