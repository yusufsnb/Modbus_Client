import easymodbus.modbusClient

modbus_client = easymodbus.modbusClient.ModbusClient('192.168.1.1', 700)

modbus_client.connect()
if(modbus_client.is_connected):
    print("Connection established")
    input_registers = modbus_client.read_holdingregisters(0, 1)
    print(input_registers)
    modbus_client.write_single_register(0, 30)
else:
    print("Connection Error")
modbus_client.close()