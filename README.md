# HFSS-GUI-Scripts
Just for intergrated circuit design project aligned with HFSS software. With GUI based on IronPython, you can save a lot of time to repeat the same operation.

本脚本用于HFSS联合Cadence、ADS等软件进行芯片级电磁仿真，可以省去大量重复工作，提高效率。

## Ahead of all
This script is based on Ironpython(Python 2.0+) and .Net Framework 2.0+, so you should confirm your computer is along with these enverionment above. And you should confirm that the version of HFSS is 16(2015)or higher version.

As for the confidential processing parameters, some data has been removed from the backstage. You'd better add these parameters according to your design. Or you can refer to the script GUI frame and wrapped functions, and deliver your own scripts.

脚本基于Ironpython(Python2.0+)和.Net Framework 2.0+，使用前先确保电脑已配备上述环境。同时HFSS软件版本高于HFSS16(2015)。

由于部分工艺参数保密，所以后台已经移除工艺数据，使用前最好按照自己所使用的工艺进行参数补充。或者可以参考本脚本的图形界面框架以及部分已经封装过的函数，开发自己的脚本来使用。

## Usage
- New/Opne Project -> New/Open HFSS Design -> Menu-Tools -> Run scripts -> Choose xxx.py

![Ver1.2.0](https://github.com/PhosphorW/HFSS-GUI-Scripts/raw/master/images/Scripts_Ver1.2.0.JPG)

#### Panels from top to end:
1. Panel1: `Scale_Unit Panel` Set unit scale in HFSS view, 'um' or 'mm'.
2. Panel2: `Create_Media_Box Panel` Create media lawyers in IC chip.
3. Panel3: `Create_Metal_Material Panel` Generate metal material

#### Exist Functions:
- SetModelUnits()
- CreateBox()
- AddMaterial()

## ChangeLog
### [Ver 1.2.1] - 2017-12-12
#### Fixed:
- Fix the bug that cannot generate 2 or more metal materials together.

#### Refactored:
- Automatically adjust the view after using Panel1 to create box.

### [Ver 1.2.0] - 2017-11-24
#### Added:
- Panel: Create_Metal_Material

### [Ver 1.1.2] - 2017-11-24
#### Added:
- Function: AddMaterial()
- Create_Media_Box Panel: Generate material
- Create_Media_Box Panel: Error message window

#### Refactored:
- Refactor the maximized window and its dragging problem.

### [Ver 1.1.1] - 2017-11-20
#### Refactored:
- Optimize interface.

#### Fixed:
- Fix some stutters in scripts.

### [Ver 1.1.0] - 2017-11-20
#### Added：
- Function: SetModelUnits()
- Panel: Scale_Unit

#### Changed:
- Create_Media_Box unit can be choose.

### [Ver 1.0.0] - 2017-11-20
#### Added：
- Function: CreateBox()
- Panel: Create_Media_Box