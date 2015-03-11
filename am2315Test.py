# am2315Test.py by ThreeSixes (https://github.com/ThreeSixes/py-am2315)
# This was originally part of the OpenWeatherStn project (https://github.com/ThreeSixes/OpenWeatherStn)

###########
# Imports #
###########

from am2315 import am2315
import pprint

#######################
# Main execution body #
#######################

thSens = am2315()

thDat = thSens.getTempHumid()

print("Temperature: " + str(thDat[0]) + "C")
print("Humidity:    " + str(thDat[1]) + "%")