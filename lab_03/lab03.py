var_string1 = input()
var_bool1 = var_string1 == "True"

var_string2 = input()
var_bool2 = var_string2 == "True"

var_string3 = input()
var_bool3 = var_string3 == "True"

var_string4 = 0

if var_bool1 and var_bool2 and var_bool3 == True:
    var_string4 = "True"
else:
    var_string4 = "False"

print ("Tosse:",var_string1,"\nFebre:",var_string2,"\nDificuldade para respirar:",var_string3,"\nProvavelmente eh COVID-19:",var_string4)
