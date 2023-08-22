import toml
import numpy

par_dict = toml.load("flash.toml")["Parfile"]

print(f"rho = {par_dict['mph_rhoGas']}")
print(f"mu = {par_dict['mph_muGas']}")
print(f"Cp = {par_dict['mph_CpGas']}")
print(f"k = {par_dict['mph_thcoGas']}")
print(f"a = {par_dict['mph_thcoGas']/(par_dict['mph_CpGas']*par_dict['mph_rhoGas'])}")
print(f"Re = {1/par_dict['ins_invReynolds']}")
print(f"Pr = {par_dict['ht_Prandtl']}")
print(f"St = {par_dict['mph_Stefan']}")
print(f"Fr = {numpy.sqrt(1/abs(par_dict['ins_gravY']))}")
print(f"We = {1/par_dict['mph_invWeber']}")
