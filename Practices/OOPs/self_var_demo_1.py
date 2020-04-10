#!/usr/bin/env python3

# class Rest:
#     resting = False
#
#     def __init__(self,name):
#         self._name = name
#
#     def getRestingStatus(self):
#         if resting:
#             print(f'{self._name} is taking rest.')
#         else:
#             print(f'{self._name} is up.')
#
#
# Rest('Samarth').getRestingStatus()
# print(Rest().resting)


class Rest:
    currentlyResting = None

    def setCurrentStatus(self, status):
        Rest.currentlyResting = status

    def getStatus(self):
        if Rest.currentlyResting:
            return 'Resting...'
        else:
            return 'Not Resting...'

def main():
    restObj = Rest()
    restObj.setCurrentStatus(False)
    print(restObj.getStatus())

if __name__ == '__main__':
    main()