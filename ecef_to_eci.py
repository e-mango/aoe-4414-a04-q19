# ecef_to_eci.py 
#
# Usage: python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km.
#  Converts ECEF frame to ECI
# Parameters:
#  year: year of the time instant
#  month: month of the time instant
#  day: day of the time instant
#  hour: hour of the time instant
#  minute: minute of the time instant
#  second: second of the time instant
#  ecef_x_km: x component of ECEF frame in km
#  ecef_y_km: y component of ECEF frame in km
#  ecef_z_km: z component of ECEF frame in km
# Output:
#  Prints the x, y, and z components of the ECI frame
#
# Written by Evan Schlein
# Other contributors: None

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.137
E_E    = 0.081819221456
w = 7.292115e-5

# initialize script arguments
year = float('nan')     # year of the time instant
month = float('nan')    # month of the time instant
day = float('nan')      # day of the time instant
hour = float('nan')     # hour of the time instant
minute = float('nan')   # minute of the time instant
second = float('nan')   # second of the time instant
ecef_x_km = float('nan') # x component of ECEF frame in km
ecef_y_km = float('nan') # y component of ECEF frame in km
ecef_z_km = float('nan') # z component of ECEF frame in km


# parse script arguments
if len(sys.argv) == 10:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
    ecef_x_km = float(sys.argv[7])
    ecef_y_km = float(sys.argv[8])
    ecef_z_km = float(sys.argv[9])
else:
    print(
        'Usage: '
        'python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km'
    )
    exit()

# write script below this line

#Calculate the Frac. Julian Date
JD = (day - 32075 + int(1461 * (year + 4800 + int((month - 14) / 12)) / 4)+ int(367 * (month - 2 - int((month - 14) / 12) * 12) / 12) - int(3 * int((year + 4900 + int((month - 14) / 12)) / 100) / 4))
JD_midnight = JD - 0.5
D_frac = (second + 60 * (minute + 60 * hour)) / 86400
jd_frac = JD_midnight + D_frac

#Calculate the GMST Angle
T_ut1 = (jd_frac - 2451545.0)/36525
Theta_GMST_sec = 67310.54841 + (876600*60*60 + 8640184.812866)*T_ut1 + 0.093104*(T_ut1**2) + (-6.2e-6 * (T_ut1**3))
GMST_rad = (Theta_GMST_sec % 86400) * w 

# Rotate ECI to ECEF
ECI_vec = [ecef_x_km * math.cos(GMST_rad) - ecef_y_km * math.sin(GMST_rad), ecef_y_km * math.cos(GMST_rad) + ecef_x_km * math.sin(GMST_rad), ecef_z_km]

eci_x_km = ECI_vec[0]
eci_y_km = ECI_vec[1]
eci_z_km = ECI_vec[2]

print(eci_x_km)
print(eci_y_km)
print(eci_z_km)
