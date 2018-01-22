#!/bin/sh
sudo apt-get update && sudo apt-get -y install python-pip
python -m pip install mcstatus
java -Xmx512M -Xms512M -jar minecraft_server.1.12.2.jar nogui&
/usr/bin/python reportGameRooms.py& >> report.log
wait
echo "Server shutting down..."
