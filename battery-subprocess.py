import subprocess
import time


#1.9.2026

def get_battery_percentage():
    device_path = "/org/freedesktop/UPower/devices/headset_dev_68_59_32_D0_F1_46"

    try:
        
        result = subprocess.run(
        ["upower", "-i", device_path],
        capture_output=True,
        text=True,
        check=True
        )
        
        for line in result.stdout.splitlines():
            if "percentage:" in line:
                percentage_str = line.split(":")[1].strip().replace("%","")
                return int(percentage_str)

    except subprocess.CalledProcessError as e:
        print(f"System command did not run: {e}")
    except Exception as e:
        print(f"Error: {e}")
        
    return None


if __name__ == "__main__":
    
    while True:
        percentage = get_battery_percentage()
    
        if percentage is None:
            print("You are not connected. Waiting for connection...")
            while get_battery_percentage() is None:
                time.sleep(5)  # Idle and wait for reconnection
            print("Reconnected!")
            continue  # Go back to the start of the main loop

        print(f"JBL Percentage: {percentage}")
        time.sleep(10)





