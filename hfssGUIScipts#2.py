# encoding: utf-8
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.SetActiveEditor("3D Modeler")
oDefinitionManager = oProject.GetDefinitionManager()
oModule = oDesign.GetModule("BoundarySetup")

import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

# import numpy as np

from System.Drawing import Color, Point
from System.Windows.Forms import (Application, BorderStyle, Button,
                                  Form, FormBorderStyle, Label, AnchorStyles, Panel, Screen, TextBox,
                                  RadioButton, MessageBox, CheckBox, ListBox, ComboBox)

# num_port = 13
refresh_count = 0
refresh_count2 = 0


def AssignPort(PortName, GndName):
    PortNum = len(PortName)
    for i in range(0, PortNum):
        oModule.AutoIdentifyTerminals(
            [
                "NAME:ReferenceConductors",
                GndName
            ], PortName[i], False)

    for i in range(0, PortNum):
        oDesign.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:HfssTab",
                    [
                        "NAME:PropServers",
                        "BoundarySetup:" + str(PortName[i])
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Deembed",
                            "Value:="		, True
                        ]
                    ]
                ]
            ])
    # oProject.Save()


def CreatePort(PortID, PortName, GndName):
    IDNum = len(PortID)
    for i in range(0, IDNum):
        oModule.AutoIdentifyPorts(
            [
                "NAME:Faces",
                PortID[i]
            ], False,
            [
                "NAME:ReferenceConductors",
                GndName
            ], PortName[i], False)
    for i in range(0, IDNum):
        oDesign.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:HfssTab",
                    [
                        "NAME:PropServers",
                        "BoundarySetup:" + str(PortName[i])
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Deembed",
                            "Value:="		, True
                        ]
                    ]
                ]
            ])
    oProject.Save()


class HFSSAssignPort(Form):

    def __init__(self):
        self.Text = "HFSS_GUI_Scripts_#2"

        screenSize = Screen.GetWorkingArea(self)
        # self.Width = 350
        # self.Height = 300
        self.Width = 350
        self.Height = 300
        self.FormBorderStyle = FormBorderStyle.Fixed3D
        self.MaximizeBox = False

        self.authorName = Label()
        self.authorName.Text = "by Phower"
        self.authorName.Height = 25
        self.authorName.AutoSize = True
        self.authorName.Location = Point(265, 245)
        # self.authorName.Anchor = AnchorStyles.Left | AnchorStyles.Bottom

        self.setupPanel1()
        self.setupPanel2()

        self.Controls.Add(self.panel1)
        self.Controls.Add(self.panel2)
        self.Controls.Add(self.authorName)

    def setupPanel1(self):
        self.panel1 = Panel()
        self.panel1.Width = self.Width
        self.panel1.Height = 120
        self.panel1.Location = Point(0, 0)
        self.panel1.BorderStyle = BorderStyle.FixedSingle

        self.title1 = Label()
        self.title1.Text = "ReAssign Terminal"
        self.title1.Location = Point(25, 22)
        self.title1.Height = 25
        self.title1.AutoSize = True

        self.label2 = Label()
        self.label2.Text = "Ground Metal Name: "
        self.label2.Location = Point(25, 50)
        self.label2.Height = 25
        self.label2.Width = 150

        self.button1 = Button()
        self.button1.Text = 'Assign'
        self.button1.Location = Point(25, 75)
        self.button1.Width = 100
        self.button1.Click += self.update

        self.button2 = Button()
        self.button2.Text = 'Reset'
        self.button2.Location = Point(180, 75)
        self.button2.Width = 100
        self.button2.Click += self.reset

        self.list1 = ComboBox()
        self.list1.Text = '——Select'
        self.list1.Location = Point(180, 47)
        self.list1.Width = 100
        self.list1.Height = 35
        self.DropDownHeight = 50
        self.list1.Click += self.listUpdate

        self.AcceptButton = self.button1
        self.CancelButton = self.button2

        self.panel1.Controls.Add(self.label2)
        self.panel1.Controls.Add(self.title1)
        self.panel1.Controls.Add(self.button1)
        self.panel1.Controls.Add(self.button2)
        self.panel1.Controls.Add(self.list1)

    def setupPanel2(self):
        self.panel2 = Panel()
        # self.panel2.Text = "Panel"
        self.panel2.Width = self.Width
        self.panel2.Height = 120
        self.panel2.Location = Point(0, 120)
        self.panel2.BorderStyle = BorderStyle.FixedSingle

        self.p2title1 = Label()
        self.p2title1.Text = "Create Lumped Port"
        self.p2title1.Location = Point(25, 22)
        self.p2title1.Height = 25
        self.p2title1.AutoSize = True

        self.p2label1 = Label()
        self.p2label1.Text = "Ground Metal Name: "
        self.p2label1.Location = Point(25, 50)
        self.p2label1.Height = 25
        self.p2label1.Width = 150

        self.p2button1 = Button()
        self.p2button1.Text = 'Create'
        self.p2button1.Location = Point(25, 75)
        self.p2button1.Width = 100
        self.p2button1.Click += self.p2update

        self.p2button2 = Button()
        self.p2button2.Text = 'Reset'
        self.p2button2.Location = Point(180, 75)
        self.p2button2.Width = 100
        self.p2button2.Click += self.p2reset

        self.p2list1 = ComboBox()
        self.p2list1.Text = '——Select'
        self.p2list1.Location = Point(180, 47)
        self.p2list1.Width = 100
        self.p2list1.Height = 35
        self.DropDownHeight = 50
        self.p2list1.Click += self.p2listUpdate

        self.AcceptButton = self.p2button1
        self.CancelButton = self.p2button2

        self.panel2.Controls.Add(self.p2title1)
        self.panel2.Controls.Add(self.p2label1)
        self.panel2.Controls.Add(self.p2button1)
        self.panel2.Controls.Add(self.p2button2)
        self.panel2.Controls.Add(self.p2list1)

    def update(self, sender, event):
        temp = oModule.GetPortExcitationCounts()
        tempNum = len(temp)
        tempRecord = []
        for x in range(1, tempNum, 2):
            if temp[x] == '0':
                tempRecord.append(temp[x - 1])
        # MessageBox.Show(str(tempRecord))
        temp2 = self.list1.SelectedItem
        if tempRecord and (temp2 != None):
            AssignPort(tempRecord, str(temp2))
        elif temp2 == None:
            MessageBox.Show("请选择参考金属")
        elif len(tempRecord) == 0:
            MessageBox.Show("全部Port已完成")
        else:
            MessageBox.Show("错误参数！！")

    def reset(self, sender, event):
        global refresh_count
        if (self.list1.SelectedItem != None):
            self.list1.Items.Clear()
            self.list1.Text = '——Select'
            refresh_count = 0
            MessageBox.Show("已重置！！")
        else:
            MessageBox.Show("已重置！！")

    def listUpdate(self, sender, event):
        global refresh_count
        if (refresh_count == 0):
            refresh_count = 1
            self.list1.BeginUpdate()
            # self.list1.Items.AddRange(tuple(oEditor.GetObjectsByMaterial("m10_tsmcN40", "m2_tsmcN40")))
            # self.list1.Items.AddRange(tuple(oEditor.GetObjectsInGroup("Solids")))
            self.list1.Items.AddRange(tuple(oEditor.GetMatchedObjectName("M*")))
            self.list1.EndUpdate()

    def p2listUpdate(self, sender, event):
        global refresh_count2
        if (refresh_count2 == 0):
            refresh_count2 = 1
            self.p2list1.BeginUpdate()
            self.p2list1.Items.AddRange(tuple(oEditor.GetMatchedObjectName("M*")))
            self.p2list1.EndUpdate()

    def p2update(self, sender, event):
        temp = self.p2list1.SelectedItem
        unPort = oEditor.GetObjectsInGroup("Unassigned")
        unPortID = []
        for x in range(0, len(unPort)):
            unPortID.append(oEditor.GetFaceIDs(unPort[x])[0])
        if unPortID and (temp != None):
            CreatePort(unPortID, unPort, temp)
        elif temp == None:
            MessageBox.Show("请选择参考金属")
        elif len(unPortID) == 0:
            MessageBox.Show("全部Port已完成")
        else:
            MessageBox.Show("错误参数！！")
        # MessageBox.Show(str(unPortID))

    def p2reset(self, sender, event):
        global refresh_count2
        if (self.p2list1.SelectedItem != None):
            self.p2list1.Items.Clear()
            self.p2list1.Text = '——Select'
            refresh_count2 = 0
            MessageBox.Show("已重置！！")
        else:
            MessageBox.Show("已重置！！")

form = HFSSAssignPort()
Application.Run(form)
