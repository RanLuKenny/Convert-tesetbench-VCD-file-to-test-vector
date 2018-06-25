#python file for vcd imformation extraction
# vcd_file_name = 'test_file.vcd'
vcd_file_name = 'test_file.vcd'

input_ports = ['CLK','RESET','ENABLE','LOAD']
output_ports = ['D [3:0]', 'Q [3:0]']

ports = input_ports + output_ports

ports_adjust = []
port_and_sign = {}
muil_but_sign = {}

output_sequence = {}
output_sequence_new = {}

def handle_mul_bus(port_name, line):
    if ':' in port_name:
        if port_name in line:
            position = line.index(port_name)
            sign = line[position - 2]
            muil_but_sign[port_name] = sign
            # print(muil_but_sign)
            # muil_but_sign.setdefault(port_name, sign)
    else:
        if port_name in line:
            position = line.index(port_name)
            sign = line[position - 2]
            port_and_sign[port_name] = sign
            # print(port_and_sign)
            # port_and_sign.setdefault(port_name, sign)
pass

def array(strings, mul_ports): #convert the bus or port
    if ':' in strings:
        pos = strings.index(':')
        number = int(strings[pos - 1])
        for i in range(number+1):
            temp = strings[0: pos - 1] + str(i) + ']'
            mul_ports.append(temp)
    else:
        mul_ports.append(strings)
    #print(ports_adjust)
pass

def get_wavetime(strings): #timeslot
    if strings[0] == "#":
        print(strings[1:])
pass

def get_ports(port_name, line): # match the sign and port
    if port_name in line:
        position = line.index(port_name)
        sign = line[position-2]
        port_and_sign[port_name] = sign
        #print(port_and_sign)
        return 0
pass

def ini_sequence():
    for port in ports:
        output_sequence[port] = ''
pass

def store_lines(): #detect #
    f = open(vcd_file_name)
    file_lines = []
    line = f.readline()
    while line:
        line = f.readline()
        remove = line.strip('\t').strip('\n')
        if remove != '':
            file_lines.append(remove)
    f.close()
    return file_lines
pass

def detect_signal_value(f):
    for line in f:
        sub_line
