# default unit is "um"
unit="um"

def SetModelUnits(unit,rescale=False):
    oEditor.SetModelUnits(
        [
            "NAME:Units Parameter",
            "Units:="       , unit,
            "Rescale:="     , rescale
        ])