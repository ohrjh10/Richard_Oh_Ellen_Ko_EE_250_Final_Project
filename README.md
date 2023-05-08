Team members: Richard Oh, Ellen Ko
---------------------------------------------------------------------------
Instructions:
The weather_rpi_code.py file must be loaded onto the rpi, and the first variable on the client.connect line must be set to the ip address of the rpi. From there, run the weather_vm_code.py on the vm before running the file on the rpi. Each value being sent to the vm will also print in the terminal. Once the values have stopped printing in the terminal, that means the csv file has been populated. Put the csv file in the same location that the train.ipynb file is located, and open that folder using jupyter notebook. Then, the code in the train.ipynb file can be run and the classification graph shown. 
---------------------------------------------------------------------------
External Libraries used:
*taken from lab manuals 3 and 4*
flask (pip install flask)
requests (pip install requests)
paho-mqtt (sudo apt install python3-pip then run pip3 install paho-mqtt)
mosquitto-clients (sudo apt install mosquitto-clients)
Mosquitto rpi instructions: 
install mosquitto on rpi as well (sudo apt install -y mosquitto mosquitto-clients)
enable it to run on rpi at start up (sudo systemctl enable mosquitto.service)
configure mosquitto broker (sudo nano /etc/mosquitto/mosquitto.conf)
  -add lines: listener 1883
              allow_anonymous true
restart for changes (sudo systemctl restart mosquitto)
---------------------------------------------------------------------------
Demo Video Link:
https://drive.google.com/drive/folders/1KPIF6Lh7YHzD2Fkh0Ux1tNskojxPwmd6
