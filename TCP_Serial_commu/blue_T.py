# import asyncio
# from bleak import BleakClient
#
# # BLE 장치와 연결
# async def run(address, loop):
#     async with BleakClient(address, loop=loop) as client:
#         # 서비스 검색
#         services = await client.get_services()
#         for service in services:
#             print(service)
#
#         # 특정 서비스의 특성 검색
#         characteristics = await client.get_characteristics(service_uuid="SERVICE_UUID")
#         for characteristic in characteristics:
#             print(characteristic)
#
#         # 특정 특성에 데이터 쓰기
#         await client.write_gatt_char("CHARACTERISTIC_UUID", b"Hello, BLE!")
#
#         # 특정 특성에서 데이터 읽기
#         data = await client.read_gatt_char("CHARACTERISTIC_UUID")
#         print("Received:", data)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(run("DEVICE_ADDRESS", loop))
#
# import asyncio
# from bleak import BleakClient
#
# # BLE 장치와 연결
# while True:
#     async def run(address, loop):
#         async with BleakClient(address, loop=loop) as client:
#             # 서비스 검색
#             services = await client.get_services()
#             for service in services:
#                 print(service)
#
#             # 특정 서비스의 특성 검색
#             characteristics = await service.get_characteristics("89d3502b-0f36-433a-8ef4-c502ad55f8dc")
#             for characteristic in characteristics:
#                 print(characteristic)
#
#             # 특정 특성에 데이터 쓰기
#             await client.write_gatt_char("c6b2f38c-23ab-46d8-a6ab-a3a870bbd5d7", b"Hello, BLE!")
#
#             # 특정 특성에서 데이터 읽기
#             data = await client.read_gatt_char("c6b2f38c-23ab-46d8-a6ab-a3a870bbd5d7")
#             print("Received:", data)
#
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(run("70:B3:06:1F:D3:58", loop))


import bluetooth

# 블루투스 디바이스 검색
nearby_devices = bluetooth.discover_devices(duration=30)

# 검색된 디바이스 출력
for device in nearby_devices:
    print(device)

# 특정 디바이스에 연결
# target_name = "HeeJun Pro"
# target_address = "70:B3:06:1F:D3:58"
target_address = "80:86:D9:9B:97:D4"

# 검색된 디바이스들 중에서 이름이 'DEVICE_NAME'인 디바이스의 MAC 주소를 찾음
# for address in nearby_devices:
#     if target_name == bluetooth.lookup_name(address):
#         target_address = address
#         break

if target_address is "80:86:D9:9B:97:D4":
    print("Found target device with address:", target_address)
    # 디바이스와 연결
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((target_address, 1))
    # 연결된 디바이스와 데이터 송수신
    sock.send("Hello, Bluetooth!")
    data = sock.recv(1024)
    print("Received:", data)
    # 연결 종료
    sock.close()
else:
    print("Could not find target device")