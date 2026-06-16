# Daniel V. Grib
# 06/2026
# grib6206@stthomas.edu
# University of St. Thomas

'''
Demonstrate the delay generator within instrbuilder
'''

from instrbuilder.instrument_opening import open_by_name

dg = open_by_name(name='dg645')

#print("ID:", dg.get('id'))

#dg.set("reset")

print("A before:", dg.get("delay", configs={"channel": 2}))
dg.set("delay", 20e-6, configs={"channel": 2, "reference": 0})
print("A after:", dg.get("delay", configs={"channel": 2}))

# Last error gives the last error in the buffer. Error lookup table is in the DG645 Manual
#print("Last error:", dg.get("last_error"))

dg.set("trigger_source", 1) # Changes the type of trigger
dg.set("trigger_rate", 1000.0) # Changes rate at which the triggers occur (Hz)

# Changing amplitude of outputs
dg.set("amplitude", 2.5, configs={"output": 0}) # T0
dg.set("amplitude", 2.5, configs={"output": 1}) # AB

dg.set("local")

dg.comm_handle.close()