#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import hades


# In[2]:


form_class = uic.loadUiType("hades.ui")[0]
class WindowClass(QMainWindow, form_class) :
    def __init__(self,data) :
        super().__init__()
        self.setupUi(self)
        self.hds = data
        self.unSelected = [self.label_9, self.label_10, self.label_11, self.label_12, self.label_13, self.label_14, self.label_15, self.label_16, self.label_17, self.label_18, self.label_19, self.label_20, self.label_21, self.label_22, self.label_23, self.label_24, self.label_25, self.label_26,self.label_27, self.label_28, self.label_29, self.label_30, self.label_31, self.label_32, self.label_33, self.label_34, self.label_35, self.label_36]
        self.Selected = [self.label_58, self.label_56, self.label_59, self.label_60, self.label_55, self.label_62, self.label_49, self.label_48, self.label_50, self.label_39, self.label_40, self.label_38, self.label_41, self.label_37, self.label_45, self.label_43, self.label_46, self.label_47, self.label_44,self.label_42, self.label_57, self.label_63, self.label_61, self.label_52, self.label_51, self.label_54, self.label_53, self.label_64]
        self.duoIndex = {'바다 폭풍' : 0,'벼락 방진' : 1,'그을린 공기' : 2,'피뢰침' : 3,'복수심에 불타는 기분' : 4,'반짝이는 축제' : 5,'요지부동 기개' : 6,'달콤한 넥타르' : 7,'신기루 사격' : 8,'악사의 저주' : 9,'특권' : 10,'저온융합' : 11,'눈보라탄환' : 12,'갈라진 사격' : 13,'치명적인 반격' : 14,'자비로운 최후' : 15,'계산된 위험' : 16,'끈질긴 생명력' : 17,'비통함' : 18,'갈망의 저주' : 19,'낮은 내성' : 20,'차가운 포옹' : 21,'사냥하는 칼날' : 22,'쪼개지는 두통' : 23,'수정같은 선명함' : 24,'메스꺼움의 저주' : 25,'결빙 소용돌이' : 26,'얼음 포도주' : 27}
        self.refresh()
        self.Attack.activated[str].connect(self.onActivatedAttackButton)
        self.SpecialAttack.activated[str].connect(self.onActivatedSpecialAttackButton)
        self.Dash.activated[str].connect(self.onActivatedRushButton)
        self.Support.activated[str].connect(self.onActivatedSupportButton)
        self.Magic.activated[str].connect(self.onActivatedMagicButton)
        self.SpecialMagic.activated[str].connect(self.onActivatedSpecialMagicButton)
        #self.ResetButton.clicked.connect(self.onResetButton)
        self.ResetButton.clicked.connect(self.onResetButton)
    def unColor(self,widgets):
        for widget in widgets:
            widget.setStyleSheet("background-color: rgba(255, 255, 255, 10)")
    def resetData(self):
        self.hds = hades.resetHades()
    def setUnSelectedActive(self, number):
        self.unSelected[number].setStyleSheet("background-color: lightgreen")
    def setSelectedActive(self, number):
        self.Selected[number].setStyleSheet("background-color: lightgreen")
    def refresh(self):
        self.unColor(self.unSelected)
        self.unColor(self.Selected)
        unSelectedLists = hades.getUnSelected(self.hds)
        for item in unSelectedLists:
            self.setUnSelectedActive(self.duoIndex[item])
        SelectedLists = hades.getSelected(self.hds)
        for item in SelectedLists:
            self.setSelectedActive(self.duoIndex[item])
        for idx, item in enumerate(self.unSelected):
            desc = ""
            gods = list(self.hds[idx]['owner'].keys())
            for i in range(2):
                desc += gods[i]
                abil = ""
                for cd in self.hds[idx]['condition'][0]:
                    abil += ' ' + cd
                desc += abil + '\n'
            item.setToolTip(self.hds[idx]['description'] + '\n' + desc)
        for idx, item in enumerate(self.Selected):
            item.setToolTip(self.hds[idx]['description'])
    def onActivatedAttackButton(self, text):
        hades.selectItem(self.hds,text,'공격')
        self.refresh()
    def onActivatedSpecialAttackButton(self, text):
        hades.selectItem(self.hds,text,'특공')
        self.refresh()
    def onActivatedMagicButton(self, text):
        hades.selectItem(self.hds,text,'마법')
        self.refresh()
    def onActivatedSpecialMagicButton(self, text):
        if (text == '전기마법' or text == '천둥마법' or text == '피해강화'):
            owner = '제우스'
        elif(text == '탄환마법'):
            owner = '아테나'
        elif (text == '마법광선'):
            owner = '데메테르'
        else:
            owner = ''
        hades.selectItem(self.hds,owner,text)
        self.refresh()
    def onActivatedRushButton(self, text):
        hades.selectItem(self.hds,text,'돌진')
        self.refresh()
    def onActivatedSupportButton(self, text):
        hades.selectItem(self.hds,text,'지원')
        self.refresh()
    def resetComboBox(self):
        self.Attack.setCurrentIndex(0)
        self.SpecialAttack.setCurrentIndex(0)
        self.Dash.setCurrentIndex(0)
        self.Support.setCurrentIndex(0)
        self.Magic.setCurrentIndex(0)
        self.SpecialMagic.setCurrentIndex(0)
    def onResetButton(self, text):  
        self.hds = hades.resetHades()
        self.refresh()
        self.resetComboBox()
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    data =  hades.openJson()
    myWindow = WindowClass(data) 
    myWindow.show()
    app.exec_()


# In[ ]:




