from pypresence import Presence
import time

CLIENT_ID = "1349418433170903090"  
rpc = Presence(CLIENT_ID)
print("RPC is ready to use")
rpc.connect()

start_time = time.time()  # Фиксируем время старта один раз

while True:
    rpc.update(
        state="Love U <3",
        details="404 (Page not found)",
        large_image="nya",
        start=start_time  # Используем одно и то же время
    )
    time.sleep(15)
