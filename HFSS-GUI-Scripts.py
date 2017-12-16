# encoding: utf-8
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.SetActiveEditor("3D Modeler")
oDefinitionManager = oProject.GetDefinitionManager()

import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Drawing import Color, Point
from System.Windows.Forms import (Application, BorderStyle, Button,
    Form, FormBorderStyle, Label, Panel, Screen, TextBox, 
    RadioButton, MessageBox, CheckBox)

units = "um"

# metal_material_name:add metal material name you want to add, change the string below
# or you can add more checkbox and add more material name string
metal_material_name = ("M1", "M2", "M3", "M4", "M5", "M6", "M7")
# metal_material_cond:add metal material conductive you want to add, change the num below
metal_material_cond = (1, 1, 1, 1, 1, 1, 1)

def SetModelUnits(unit,rescale=False):
    oEditor.SetModelUnits(
        [
            "NAME:Units Parameter",
            "Units:="       , unit,
            "Rescale:="     , rescale
        ])
    # units = unit

def CreateBox(name,un,c1,c2,c3,trans,material,Xpos,Ypos,Zpos,Xsize,Ysize,Zsize):
    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XPosition:="       , str(Xpos)+un,
            "YPosition:="       , str(Ypos)+un,
            "ZPosition:="       , str(Zpos)+un,
            "XSize:="       , str(Xsize)+un,
            "YSize:="       , str(Ysize)+un,
            "ZSize:="       , str(Zsize)+un
        ], 
        [
            "NAME:Attributes",
            "Name:="        , name,
            "Flags:="       , "",
            "Color:="       , "("+c1+" "+c2+" "+c3+")",
            "Transparency:="    , trans,
            "PartCoordinateSystem:=", "Global",
            "UDMId:="       , "",
            "MaterialValue:="   , "\""+material+"\"",
            "SolveInside:="     , True,
            "IsMaterialEditable:="  , True
        ])

def AddMaterial(name,per=1,cond=0):
    oDefinitionManager.AddMaterial(
        [
            "NAME:"+name,
            "CoordinateSystemType:=", "Cartesian",
            "BulkOrSurfaceType:="   , 1,
            [
                "NAME:PhysicsTypes",
                "set:="         , ["Electromagnetic"]
            ],
            "permittivity:="    , per,
            "conductivity:="    , cond
        ])

class HFSS(Form):
    def __init__(self):
        self.Text = "HFSS Scripts -- By Phower_CBL"

        screenSize = Screen.GetWorkingArea(self)
        self.Width = 430
        self.Height = 400
        self.FormBorderStyle = FormBorderStyle.Fixed3D
        self.MaximizeBox = False

        self.setupPanel1()
        self.setupPanel2()
        self.setupPanel3()

        self.Controls.Add(self.panel1)
        self.Controls.Add(self.panel2)
        self.Controls.Add(self.panel3)

    def setupPanel1(self):  #介质层BOX Panel
        self.panel1 = Panel()
        self.panel1.Text = "Media_Box Panel"
        self.panel1.Width = self.Width
        self.panel1.Height = 120
        self.panel1.Location = Point(0, 50)
        self.panel1.BorderStyle = BorderStyle.FixedSingle

        self.label1 = Label()
        self.label1.Text = "介质层宽度(X轴):"
        self.label1.Location = Point(25, 25)
        self.label1.Height = 25
        self.label1.Width = 150

        self.label2 = Label()
        self.label2.Text = "介质层长度(Y轴):"
        self.label2.Location = Point(25, 50)
        self.label2.Height = 25
        self.label2.Width = 150

        self.textbox1 = TextBox()
        self.textbox1.Text = "0"
        self.textbox1.Location = Point(200, 22)
        self.textbox1.Width = 80

        self.textbox2 = TextBox()
        self.textbox2.Text = "0"
        self.textbox2.Location = Point(200, 47)
        self.textbox2.Width = 80

        self.button1 = Button()
        self.button1.Text = 'Create'
        self.button1.Location = Point(25, 75)
        self.button1.Width = 100
        self.button1.Click += self.update

        self.button2 = Button()
        self.button2.Text = 'Reset'
        self.button2.Location = Point(180, 75)
        self.button2.Width = 100
        self.button2.Click += self.reset

        self.AcceptButton = self.button1
        self.CancelButton = self.button2

        self.radio1 = RadioButton()
        self.radio1.Text = "mm"
        self.radio1.Location = Point(300, 50)
        self.radio1.Width = 35
        self.radio1.CheckedChanged += self.checkedChanged

        self.radio2 = RadioButton()
        self.radio2.Text = "um"
        self.radio2.Location = Point(300, 25)
        self.radio2.Width = 35
        self.radio2.Checked = True
        self.radio2.CheckedChanged += self.checkedChanged

        self.panel1.Controls.Add(self.label1)
        self.panel1.Controls.Add(self.label2)
        self.panel1.Controls.Add(self.textbox1)
        self.panel1.Controls.Add(self.textbox2)
        self.panel1.Controls.Add(self.button1)
        self.panel1.Controls.Add(self.button2)
        self.panel1.Controls.Add(self.radio1)
        self.panel1.Controls.Add(self.radio2)

    def setupPanel2(self):
        self.panel2 = Panel()
        self.panel2.Text = "Change_unit Panel"
        self.panel2.Width = self.Width
        self.panel2.Height = 50
        self.panel2.Location = Point(0, 0)
        self.panel2.BorderStyle = BorderStyle.FixedSingle

        self.label3 = Label()
        self.label3.Text = "设置视图单位:"
        self.label3.Location = Point(25, 15)
        self.label3.Height = 15
        self.label3.Width = 100

        self.textbox3 = TextBox()
        self.textbox3.Text = "um"
        self.textbox3.Location = Point(125, 12)
        self.textbox3.Width = 60

        self.button3 = Button()
        self.button3.Text = 'ok'
        self.button3.Location = Point(200, 10)
        self.button3.Width = 40
        self.button3.Click += self.c_unit

        self.panel2.Controls.Add(self.label3)
        self.panel2.Controls.Add(self.textbox3)
        self.panel2.Controls.Add(self.button3)
    
    def setupPanel3(self):
        self.panel3 = Panel()
        self.panel3.Width = self.Width
        self.panel3.Height = 125
        self.panel3.Location = Point(0, 170)
        self.panel3.BorderStyle = BorderStyle.FixedSingle

        self.checkLabel1 = Label()
        self.checkLabel1.Text = "选择以下金属层材料进行创建:"
        self.checkLabel1.Location = Point(25, 25)
        self.checkLabel1.AutoSize = True

        self.P3button1 = Button()
        self.P3button1.Text = 'ok'
        self.P3button1.Location = Point(200, 20)
        self.P3button1.Width = 40
        self.P3button1.Click += self.P3_update1

        self.check1 = CheckBox()
        self.check1.Text = "M1"
        self.check1.Location = Point(25,50)
        self.check1.Width = 90

        self.check2 = CheckBox()
        self.check2.Text = "M2-8"
        self.check2.Location = Point(115,50)
        self.check2.Width = 90

        self.check3 = CheckBox()
        self.check3.Text = "M9"
        self.check3.Location = Point(205,50)
        self.check3.Width = 90

        self.check4 = CheckBox()
        self.check4.Text = "M10(UTM)"
        self.check4.Location = Point(295,50)
        self.check4.Width = 90

        self.check5 = CheckBox()
        self.check5.Text = "Via1-7"
        self.check5.Location = Point(25,75)
        self.check5.Width = 90

        self.check6 = CheckBox()
        self.check6.Text = "Via8"
        self.check6.Location = Point(115,75)
        self.check6.Width = 90

        self.check7 = CheckBox()
        self.check7.Text = "Via9"
        self.check7.Location = Point(205,75)
        self.check7.Width = 90

        self.check8 = CheckBox()
        self.check8.Text = "全选"
        self.check8.Location = Point(295,75)
        self.check8.Width = 90
        self.check8.CheckedChanged += self.P3C8_update

        self.panel3.Controls.Add(self.checkLabel1)
        self.panel3.Controls.Add(self.P3button1)
        self.panel3.Controls.Add(self.check1)
        self.panel3.Controls.Add(self.check2)
        self.panel3.Controls.Add(self.check3)
        self.panel3.Controls.Add(self.check4)
        self.panel3.Controls.Add(self.check5)
        self.panel3.Controls.Add(self.check6)
        self.panel3.Controls.Add(self.check7)
        self.panel3.Controls.Add(self.check8)

    def update(self, sender, event):
        temp1 = self.textbox1.Text
        temp2 = self.textbox2.Text
        if (float(temp1) > 0) and (float(temp2) > 0):
            MessageBox.Show("根据工艺添加介质层参数")
        else:
            MessageBox.Show("错误参数！！")

    def reset(self, sender, event):
        self.textbox1.Text = "0"
        self.textbox2.Text = "0"

    def c_unit(self, sender, event):
        temp = self.textbox3.Text
        SetModelUnits(temp)

    def checkedChanged(self, sender, args):
    	global units
        if not sender.Checked:
            return
        if sender.Text == "mm":
            units = "mm"
        else:
            units = "um"
    
    def P3_update1(self, sender, args):
        temp = False

        check_1 = self.check1.Checked
        check_2 = self.check2.Checked
        check_3 = self.check3.Checked
        check_4 = self.check4.Checked
        check_5 = self.check5.Checked
        check_6 = self.check6.Checked
        check_7 = self.check7.Checked

        for x in range(1,8):
            if locals()['check_'+str(x)] == True:
                AddMaterial(metal_material_name[x-1],1,metal_material_cond[x-1])
                temp = True

        if temp == True:
            MessageBox.Show("创建完成")
            self.check1.CheckState = self.check1.CheckState.Unchecked
            self.check2.CheckState = self.check2.CheckState.Unchecked
            self.check3.CheckState = self.check3.CheckState.Unchecked
            self.check4.CheckState = self.check4.CheckState.Unchecked
            self.check5.CheckState = self.check5.CheckState.Unchecked
            self.check6.CheckState = self.check6.CheckState.Unchecked
            self.check7.CheckState = self.check7.CheckState.Unchecked
            self.check8.CheckState = self.check8.CheckState.Unchecked
            self.check8.Text = "全选"
        else:
            MessageBox.Show("请选择材料！！")
            
    def P3C8_update(self, sender,args):
        # MessageBox.Show("selected"+"\n"+self.check8.CheckState.ToString())
        if self.check8.Checked == True:
            self.check1.CheckState = self.check1.CheckState.Checked
            self.check2.CheckState = self.check2.CheckState.Checked
            self.check3.CheckState = self.check3.CheckState.Checked
            self.check4.CheckState = self.check4.CheckState.Checked
            self.check5.CheckState = self.check5.CheckState.Checked
            self.check6.CheckState = self.check6.CheckState.Checked
            self.check7.CheckState = self.check7.CheckState.Checked
            self.check8.Text = "反选"
        else:
            self.check1.CheckState = self.check1.CheckState.Unchecked
            self.check2.CheckState = self.check2.CheckState.Unchecked
            self.check3.CheckState = self.check3.CheckState.Unchecked
            self.check4.CheckState = self.check4.CheckState.Unchecked
            self.check5.CheckState = self.check5.CheckState.Unchecked
            self.check6.CheckState = self.check6.CheckState.Unchecked
            self.check7.CheckState = self.check7.CheckState.Unchecked
            self.check8.Text = "全选"   

SetModelUnits('um')
form = HFSS()
Application.Run(form)
