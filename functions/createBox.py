# c1,c2,c3 is for RGB color
# un is shorted of units
# trans is shorted of Transparency

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