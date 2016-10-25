# Security-IP-camera

**In this project we will make a security-IP camera based on a Raspberry Pi 3 model B.**

We will use two Arduinos UNO with one motion sensor and one RF transceiver on each of them. The Raspberry will also have one motion sensor and one RF transceiver to communicate with the Arduinos.
Whenever one of the Arduinos detects movement inside the house it will commounicate with Raspberry and the Respberry will move the servo and start the camera to record the event. 





Hardware components needed:
- 1 Raspberry Pi 3 model B
- 1 Raspberry pi camera
- 3 PIR (motion) sensor [HC-SR501]
- 2 Arduinos UNO
- 3 RF transceivers
- 1 Servo
- 1 Breadboard (maybe)




If the system detects movement or sound inside the house the Raspberry Pi camera will start recording!!
The video will be saved into the Rasberry's SDcard, simultaneously the system will stream the recording video 
