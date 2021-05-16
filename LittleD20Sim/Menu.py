class Menu:
    UserAction = ''
    
    def Base(self):
        print('Menu')
        while True:
            UserAction = input('  c: Combatents\n  w: Weapons\n  s: Simulation\n  e: Exit\n:').lower()
            if UserAction == 'e':
                UserAction = 'Exit'
            elif UserAction == 'w':
                UserAction = 'Weapon'
            elif UserAction == 'c':
                UserAction = 'Combatent'
            elif UserAction == 's':
                UserAction = 'Simulation'
            else:
                continue
            break
        return(UserAction)

    def Modify(self, List, inText):
        print(inText[0],'\n', List, '\n')
        while True:
            UserAction = input(inText[1]).lower()
            if UserAction == 'e':
                UserAction = 'Exit'
            elif UserAction == 'a':
                UserAction = 'Add'
            elif UserAction == 'c':
                UserAction = 'Clear'
            elif UserAction == 'i':
                UserAction = 'Information'
            elif UserAction == 's':
                UserAction = 'Save'
            else:
                continue
            break
        return(UserAction)

    def Simulation(self, inText):
        while True:
            UserAction = input(inText[0]).lower()
            if UserAction == 'e':
                UserAction = 'Exit'
            elif UserAction == 'a':
                UserAction = 'Add'
            elif UserAction == 'c':
                UserAction = 'Clear'
            elif UserAction == 'i':
                UserAction = 'Information'
            elif UserAction == 'r':
                UserAction = 'RunSim'
            else:
                continue
            break
        return(UserAction)


def main():
    print(Menu().Base())

if __name__=='__main__':
    main()
