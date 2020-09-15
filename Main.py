import os
import sys
import json 
import subprocess
from enum import Enum

class PythoneVrsion(Enum):
    Python3 = 1
    Python2 = 2 

def FindPackageInJson(PackageName,ListPackage):
    for Package in json.loads(ListPackage):
        if(Package["name"]==PackageName):
            return True
    return False    

def CheakInstallPackage(PackageName,pythoneVrsion) :
    if(pythoneVrsion==PythoneVrsion.Python3):
        # pip3 list --format=json
        result = subprocess.run(['pip3','list','--format=json'], stdout=subprocess.PIPE)   
        return FindPackageInJson(PackageName,result.stdout)
    else:
        # pip list --format=json
        result = subprocess.run(['pip','list','--format=json'], stdout=subprocess.PIPE)   
        return FindPackageInJson(PackageName,result.stdout)


if(CheakInstallPackage("virtualenv",PythoneVrsion.Python3)):
    print("yes")
else:
    print("no")    
