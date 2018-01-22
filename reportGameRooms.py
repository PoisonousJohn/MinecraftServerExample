#!/usr/bin/python
import time
import json
import os
import urllib2
import socket
from time import sleep
from mcstatus import MinecraftServer


def main():

    hostname = socket.gethostname()
    report_url = os.environ['REPORT_ROOMS_URL']
    if not report_url:
        raise Exception('REPORT_ROOMS_URL env var should be set')

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
                req = urllib2.request(report_url)
                data = {
                    'nodes' : [
                        {
                            'nodeId': hostname,
                            'rooms': status.players.online
                        }
                    ]
                }
                req.add_header('Content-Type', 'application/json')
                response = urllib2.urlopen(req, json.dumps(data))
                print('Reported server rooms: {0}'.format(response.info()))
                sleep(5)
        except:
            print("Failed to connect to server. Retrying")
            sleep(1)


main()
