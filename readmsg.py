from sim800l import SIM800L

sim800l=SIM800L('/dev/serial0')
# sim800l.read_sms(id)

print(sim800l.read_sms(1))
