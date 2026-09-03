
import dbus

#3.9.2026

bus=dbus.SystemBus()


device_path = "org/freedesktop/UPower/devices/headset_dev_68_59_32_D0_F1_46"
bluez_path = "/org/bluez/hci0/dev_68_59_32_D0_F1_46"

device=bus.get_object("org.bluez", bluez_path)
interface=dbus.Interface(device, "org.freedesktop.DBus.Properties")

try:

    percentage = int(interface.Get("org.bluez.Battery1", "Percentage"))

except Exception:
    percentage = None
    
print(f"JBL Battery: %{percentage}")


