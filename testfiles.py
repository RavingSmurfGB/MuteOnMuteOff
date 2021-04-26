import pathlib, os

username = os.getlogin()

maindir = "C:\\Users\\"+ username + "\\Documents\\Py_Ormolu"
projectname = "\\MuteOnMuteOff"
target_dir = maindir + projectname

if pathlib.Path(maindir).is_dir() == False:
    pathlib.Path(maindir).mkdir()
    
