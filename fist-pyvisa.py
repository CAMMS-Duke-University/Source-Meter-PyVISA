import pyvisa
rm = pyvisa.ResourceManager('@py')
print(rm.list_resources()) # rm.list_resources() is a tuple


print("-----")
list_of_resources = rm.list_resources()
print("-----")
print(list_of_resources[-1])
my_instrument = rm.open_resource(list_of_resources[-1])

my_instrument.baud_rate = 115200
my_instrument.read_termination = '\n'
my_instrument.write_termination = '\n'

while True:
    my_instrument.write_raw('55555'.encode('utf-8'))
    print(my_instrument.read_bytes(10))

# print(dir(my_instrument))
