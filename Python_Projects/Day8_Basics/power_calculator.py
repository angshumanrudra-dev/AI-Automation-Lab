def get_input():
    v=int(input("Tell me the voltage in Volt:"))
    i= int(input("Tell me the current in Amp:"))
    pf = int(input("Tell me the power factor"))
    return v,i,pf 

def caculate_power (v,i,pf):
    power = (v*i*pf)/1000
    return power
def show_result(power):
    return print("power", power)

def show_energy (power):
    time = int(input("how much time in Hrs?: "))
    energy = power * time
    return energy

while True:
    powr_consmp = input("Do you want to know power consumption (yes/no)? ").lower()
    if powr_consmp == "yes":
        v,i,pf = get_input()
        power=caculate_power(v,i,pf)
        show_result(power)
        print("Energy: ", show_energy(power))
    elif powr_consmp == "no":
        break

# get_input()
# caculate_power()