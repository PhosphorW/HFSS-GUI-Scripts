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