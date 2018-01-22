#!/usr/bin/python
import time
from time import sleep
from mcstatus import MinecraftServer


def main():

    # retry until started
    while 1:
        try:
            # If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
            server = MinecraftServer("127.0.0.1", 25565)

            while 1:
                # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
                status = server.status()
                print("[{2}] The server has {0} players and replied in {1} ms".format(
                    status.players.online,
                    status.latency,
                    time.strftime("%d.%m.%Y %H:%M:%S")))
                sleep(5)
        except:
            print("Failed to connect to server. Retrying")
            sleep(1)


main()
