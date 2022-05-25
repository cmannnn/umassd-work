# this program will compute wind chill
# Author: Chris Murphy
# date: 02/22/2022

# t = air temp (in Fahrenheit)
# v = wind speed (mph)
t = 10

wind_speeds = range(5, 65, 5)

for wind_speed in wind_speeds:
	wind_chill = 35.74 + (0.6215 * t) - (35.75 * (wind_speed ** .16)) + 0.4275 * (t * (wind_speed ** .16))
	print('T = %.0f, wind = %.0f, wind chill = %.0f' % (t, wind_speed, round(wind_chill)))