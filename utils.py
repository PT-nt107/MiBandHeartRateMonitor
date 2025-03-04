import asyncio
from bleak import BleakScanner
import time

TIMEOUT=4
async def scan_for_mi_band():
    devices = await BleakScanner.discover(return_adv=True,timeout=TIMEOUT)
    for device, adv in devices.values():
        if adv.manufacturer_data and 0x0157 in adv.manufacturer_data:
            company_id = 0x0157
            manufacturer_data = adv.manufacturer_data[company_id]
            heart_rate = manufacturer_data[3] if len(manufacturer_data) > 3 else None
            if heart_rate != None:
                now=time.strftime("%H:%M:%S")
                print(f"from device:{device.name}(rssi={adv.rssi}), get heartrate:\n{heart_rate}@{now}")
            else:
                print('have not recived data.')
            return heart_rate
    return None

def get_heart_rate():
    # 为每个线程创建独立的事件循环
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    # 检查事件循环是否关闭
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(scan_for_mi_band())
    finally:
        # 关闭临时创建的事件循环
        if not loop.is_closed():
            loop.close()
