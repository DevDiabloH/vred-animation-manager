'''
<< vrCustomAnimation.py >>
paste C:\Program Files\Autodesk\{사용중인 VRED 버전}}\lib\python

<< VSET Example >>
VariantSet Script탭에 아래 예제를 추가합니다.

#1. Automotive_Genesis Door Example
import VrCustomAnimation as vca
key = 'Door'
animList = ['Doors All Open', 'Doors All Close']
animDuration = 1
isSequential = True
vca.VrPlayAnimation(key, animList, animDuration, isSequential)


#2. Automotive_Genesis Wheel Example
import VrCustomAnimation as vca
key = 'Wheel'
animList = ['Wheel Position Left', 'Wheel Position Right', 'Wheel Position Normal']
animDuration = 0.6
isSequential = True
vca.VrPlayAnimation(key, animList, animDuration, isSequential)
'''

import vrAnimWidgets
from threading import Timer


AnimDic = dict()

def VrPlayAnimation(key, animList, animDuration, sequential):
    isModified = False
    try:
        if AnimDic[key] == None:
            isModified = True
        elif(AnimDic[key].isModified(animList, animDuration, sequential)):
            isModified = True
    except:
        isModified = True

    if isModified:
        AnimDic[key] = VrCustomAnimation(animList, animDuration, sequential)

    AnimDic[key].play()

class VrCustomAnimation:
    def __init__(self, animList, animDuration, sequential):
        self.isPlay = False
        self.anims = animList
        self.animDuration = animDuration
        self.isSequential = sequential
        self.idx = 0

    def isModified(self, otherAnims, otherAnimDuration, otherIsSequential):
        if (self.anims != otherAnims) or (self.animDuration != otherAnimDuration) or (self.isSequential != otherIsSequential):
            return True
        else:
            return False

    def play(self):
        if self.isPlay:
            print('this animation already playing...')
            return

        print('animation start')
        self.isPlay = True
        if self.isSequential:
            vrAnimWidgets.playCAnimation(self.anims[self.idx])
            self.next()
        else:
            for i in self.anims: 
                vrAnimWidgets.playCAnimation(i)

        Timer(self.animDuration, self.end).start()

    def next(self):
        self.idx += 1
        if self.idx == len(self.anims):
            self.idx = 0
    
    def end(self):
        print('animation end')
        self.isPlay = False