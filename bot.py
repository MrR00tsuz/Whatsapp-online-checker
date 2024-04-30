import os
import time
import psutil
from datetime import datetime

def check_online_status():
    numara = "Numarayı buraya yazın" 
    online_start_time = None

    dosya_dizini = os.path.join(os.getcwd(), "kayit.txt")

    while True:
        if any("WhatsApp.exe" in process.name() for process in psutil.process_iter()):
            process = Popen(f"WhatsApp.exe {numara}", stdout=PIPE)
            output, _ = process.communicate()
            output_str = output.decode("utf-8")
            
            if "Çevrimiçi" in output_str:
                if online_start_time is None:
                    online_start_time = datetime.now()
            else:
                if online_start_time is not None:
                    online_end_time = datetime.now()
                    online_duration = online_end_time - online_start_time
                    with open(dosya_dizini, 'a') as file:
                        file.write(f"Çevrimiçi kaldığı süre: {online_duration}\n")
                    online_start_time = None
        else:
            online_start_time = None

        time.sleep(2)
check_online_status()
