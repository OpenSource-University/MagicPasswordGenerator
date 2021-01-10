sudo apt update && sudo apt install -y wipe cdrskin coreutils python3-pip python3

sudo apt upgrade -y

sudo apt autoremove -y

sudo python3 -m pip install termcolor getch

sudo mkdir -p /var/nobrain/
sudo cp config.json /var/nobrain/config.json

sudo python3 readncut_stream.py MAKE-YES-SURE

sudo mkdir -p build/release/

sudo cp nobrain build/release/nobrain
sudo chmod a+x build/release/nobrain
sudo cp build/release/nobrain /usr/bin/nobrain

sudo cp magicpsswd.py build/release/magicpsswd
sudo chmod a+x build/release/magicpsswd
sudo cp build/release/magicpsswd /usr/bin/magicpsswd

sudo cp verify_sector_by_sector_files_checksum.py build/release/verify_sector_by_sector_files_checksum
sudo chmod a+x build/release/verify_sector_by_sector_files_checksum
sudo cp build/release/verify_sector_by_sector_files_checksum /usr/bin/verify_sector_by_sector_files_checksum
 
sudo rm -rf build/
