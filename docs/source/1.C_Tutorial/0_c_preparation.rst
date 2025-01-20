C Language Preparation
===================================

Requirements
-----------------------------------

* Windows - Win 10 and newer, 64 bits
* Linux - 64 bits
* Mac OS X - Version 10.14: “Mojave” or newer, 64 bits

1.Download the Arduino IDE 2.x.x
-------------------------------

#. Visit `Download Arduino IDE <https://www.arduino.cc/en/software>`_ page.

#. Download the IDE for your OS version.

   .. image:: /preparation/img/C_preparation/Install_Arduino_IDE_1.png

.. note:: Uploading code to the Arduino UNO R4 requires Arduino IDE version 2.2 
   or higher. If your version is older, please upgrade to the latest version.

Installation
--------------

Windows
^^^^^^^^

#. Double click the ``arduino-ide_xxxx.exe`` file to run the downloaded file.

#. Read the License Agreement and agree it.

   .. image:: /preparation/img/C_preparation/Install_Arduino_IDE_2.png

#. Choose installation options.

   .. image:: /preparation/img/C_preparation/Install_Arduino_IDE_3.png

#. Choose install location. It is recommended that the software be installed on a drive other than the system drive.

   .. image:: /preparation/img/C_preparation/Install_Arduino_IDE_4.png

#. Then Finish. 

   .. image:: /preparation/img/C_preparation/Install_Arduino_IDE_5.png

MacOS
^^^^^^^^

Double click on the downloaded ``arduino_ide_xxxx.dmg`` file and follow the 
instructions to copy the **Arduino IDE.app** to the **Applications** folder, you will see the Arduino IDE installed successfully after a few seconds.

.. image:: /preparation/img/C_preparation/Install_Arduino_IDE_6.png
    :width: 800

Linux
"""""""

For the tutorial on installing the Arduino IDE 2.0 on a Linux system, please 
refer `Linux-Install Arduino IDE <https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing#linux>`_

Open the IDE
^^^^^^^^^^^^^

#. When you first open Arduino IDE 2.0, it automatically installs the Arduino AVR Boards, built-in libraries, and other required files.

   .. image:: /preparation/img/C_preparation/Install_Arduino_IDE_7.png

#. In addition, your firewall or security center may pop up a few times asking you if you want to install some device driver. Please install all of them.

   .. image:: /preparation/img/C_preparation/Install_Arduino_IDE_8.png

#. Now your Arduino IDE is ready!

.. note::
   In the event that some installations didn't work due to network issues or other 
   reasons, you can reopen the Arduino IDE and it will finish the rest of the 
   installation. The Output window will not automatically open after all installations 
   are complete unless you click Verify or Upload.


设置你的树莓派PICO
-----------------------------------
1.安装UF2固件
^^^^^^^^^^^^
When you initially connect the Raspberry Pi Pico W or hold down the BOOTSEL button while inserting it, you’ll see the device showing up as a drive without being assigned a COM port. This makes it impossible to upload code.

To fix this, you need to install UF2 firmware. This firmware supports MicroPython and is also compatible with the Arduino IDE.

* 从下面的链接下载固件(或者在项目的LAFVIN_Super_Starter_Kit_For_Pico/Arduino/3.firmware中也可以找到)

* 使用Micro-USB数据线链接Pico和计算机，并复制固件到Pico的根目录。

.. image:: /preparation/img/C_preparation/pico_1.png

* Drag and drop the downloaded UF2 firmware into the RPI-RP2 drive.

.. image:: /preparation/img/C_preparation/pico_1.png

* After this, the RPI-RP2 drive will disappear, and you can proceed with the following steps.

2.Installing the Board Package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To program the Raspberry Pi Pico W, you’ll need to install the corresponding package in the Arduino IDE. Here’s a step-by-step guide:

* In the Boards Manager window, search for pico. Click the Install button to commence the installation. This will install the Arduino Mbed OS RP2040 Boards package, which includes support for the Raspberry Pi Pico W.

.. image:: 

* During the process, a few pop-up prompts will appear for the installation of specific device drivers. Select “Install”.

.. image:: arg1

* Afterwards, there will be a notification indicating that the installation is complete.

3.Selecting the Board and Port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* To select the appropriate board, navigate to Tools -> Board -> Arduino Mbed OS RP2040 Boards -> Raspberry Pi Pico.

.. image:: arg1

* If your Raspberry Pi Pico W is connected to the computer, set the right port by navigating to Tools -> Port.

.. image:: arg1

* Arduino 2.0 offers a new quick-select feature. For the Raspberry Pi Pico W, which is typically not auto-recognized, click Select other board and port.

.. image:: 

* Type Raspberry Pi Pico into the search bar, select it when it shows up, choose the appropriate port, and click OK.

.. image:: arg1

* You can easily reselect it later through this quick access window.

.. image::

* Either of these methods will enable you to set the correct board and port. You’re now all set to upload code to the Raspberry Pi Pico W.

4.上传代码
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Open any .ino file or use the empty sketch currently displayed. Then, click the Upload button.

.. image:: arg1

* Wait for the uploading message to appear, as shown below.

.. image:: arg1

* Hold down the BOOTSEL button, quickly unplug your Raspberry Pi Pico W, and plug it back in.

.. image:: arg1
















