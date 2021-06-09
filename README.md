# Arduino "streamdeck"

This is the V1.3 of my streamdeck, it will be improved. This V1.3 allows you to lower/higher your computer's volume, pause/play music on spotify, and play next/previous song.
For the wiring, se _connectivity.png_

## Requirements
(only for _Linux_ systems)
- first, you'll need to install python, arduino IDE (VS code with extensions works well) amixer, pytify (``sudo pip install pytify``) and pyserial (``sudo pip install pyserial``)
- you'll need Spotify installed in your computer. When the program is running, Spotify have to be opened

## Installation
- upload _main.ino_ into you arduino
- change your serial port in _main.py_ (line 15, port = "your_serial_port")
- run the _main.py_ file, you can put it in your startup applications.