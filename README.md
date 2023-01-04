# Software+Electronics = SoftElectron.
### Step by step implementations
Tutorial:
 By the below steps you can implement the project by own.
 
https://pjreddie.com/darknet/yolo/ ( Main link for reference )

YOLOv3 is extremely fast and accurate. In mAP measured at .5 IOU YOLOv3 is on par with Focal Loss but about 4x faster. Moreover, you can easily tradeoff between speed and accuracy simply by changing the size of the model, no retraining required! You only look once (YOLO) is a state-of-the-art, real-time object detection system. On a Pascal Titan X it processes images at 30 FPS and has a mAP of 57.9% on COCO test-dev.

Stepwise Implementation
( Note: Below commands are entered in Raspberry-pi Terminal)

Step 1:

Download the repository by copying whole line and paste then enter in Terminal
git clone https://github.com/GuruprasadaShridharHegde/SoftElectron.git
The above link contains GitHub repository and that contains required files and documents which are associated with the program. No need to search it everywhere like google or any other internet sources. The above repository is made to public so that anyone can access.

Step 2:

Install OpenCV and its dependencies
Drag SoftElectron folder to desktop. Next, we'll install OpenCV and all the dependencies needed for the package. Because Open-CV alone will not going to be work, it needs some of its dependencies. So you can install it by one line command in terminal as shown below.
In terminal
--> cd Desktop
--> cd SoftElectron --> bash get_pi_requirements.sh

Step 3:

Download weights file from the below google drive link and paste that file in Softlectron folder
https://drive.google.com/drive/folders/1IEqGFtI1grkLpe5PzKFoGRWORgdUCCp?usp=sharing
Weights file is about 45Mb so, in GitHub large sized files will not be uploaded, So made one google drive link to access that and it has public access.
Step 4: Program Execution:
•	Weights file, configuration file, python file, labels and all audio frequency files should be there in one folder.
•	In the programming part allocate all file location as an absolute path. Install required libraries if not installed as shows in terminal. 
•	Allocate gpio pins where it connected with Raspberry pi and its peripherals.
•	Update the mobile number if required.

Step 4: 

To enable messaging on GSM module
•	Set the wiring between the RPi and Sim800C Module as

•	RPi 5V ←→ SIM800L VCC_IN

•	RPi GND ←→ SIM800L GND

•	RPi GPIO14 (TXD) ←→ SIM800C RXD

•	RPi GPIO15 (RXD) ←→ SIM800C TXD

•	On the RPi you will need to disable the login shell over serial and enable serial through GPIO.

•	On Rasbian OS, open a terminal prompt,

•	# sudo raspi-config

•	Select Option 'Interfacing Options'

•	Select Option 'Serial Port'

•	For Question 'Would you like a login shell to be accessible over serial?' answer 'No'

•	For Question 'Would you like the serial port hardware to be enabled?' answer 'Yes'

•	'Finish' raspi-config and reboot the Pi for changes to take effect.

•	# sudo reboot now

•	Log back into the RPi, and install minicom

•	# sudo apt install minicom

•	Now to open minicom and connect. 

•	Depending on your version of RPi, (video is 3) I connect to ttyAMA0. 

•	On RPi4 I could connect using ttyS0 instead, so if ttyAMA0 freezes minicom, then try ttyS0

•	# sudo minicom -D /dev/ttyAMA0 -b 115200 

or

•	# sudo minicom -D /dev/ttyS0 -b 115200 (Working)

•	type AT and then press [ctrl-m] for the carriage return.

•	Camera cap set to 0, it means raspberry pi camera, if you are using USB camera then make it to 1.

Step 5: 

Execution

•	Open the folder and run test.py to see the results. Initially in terminal shows Farmland is secure. If any breach in between laser or fire detection then different alarm tone will be played and certain message will be sent to the user or farmer. In case of fire detection one sms for user and one sms for the Fire department will be sent.

•	If any animal intrusion happens, based on type of animal certain irritation frequency tone will be played along with one sms alert to the farmer.

•	Press ‘Q’ to break the execution in between running. 
