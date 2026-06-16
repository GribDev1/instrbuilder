# Daniel V. Grib
# 06/2026
# grib6206@stthomas.edu
# University of St. Thomas

'''
Demonstrate the delay generator within instrbuilder
An example of common commands used.
'''

from instrbuilder.instrument_opening import open_by_name

dg = open_by_name(name='dg645')

#print("ID:", dg.get('id'))

dg.set("reset")

print("A before:", dg.get("delay", configs={"channel": 2}))
dg.set("delay", 6e-9, configs={"channel": 2, "reference": 0})
print("A after:", dg.get("delay", configs={"channel": 2}))

# Last error gives the last error in the buffer. Error lookup table is in the DG645 Manual
print("Last error:", dg.get("last_error"))

dg.set("trigger_source", 0) # Changes the type of trigger (0-6)
dg.set("trigger_rate", 10000000.0) # Changes rate at which the triggers occur (Hz)

# Changing amplitude of outputs
dg.set("amplitude", 2.5, configs={"output": 0}) # T0
dg.set("amplitude", 2.5, configs={"output": 1}) # AB

dg.set("delay", 100e-9, configs={"channel": 3, "reference": 2}) # Use to modify delay band width (AB, CD, EF, GH)


# Use to clear the error buffer
while True:
    err = dg.get("last_error")

    if err not in ("0", 0, "NO ERROR"):
        print("Error:", err)
    else:
        break

# Closing port and giving control back to local/manual operation
dg.set("local")
dg.comm_handle.close()