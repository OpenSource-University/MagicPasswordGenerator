sudo apt update && sudo apt install -y wipe cdrskin coreutils

sudo mkdir -p /var/pdtslsw/
sudo cp config.json /var/pdtslsw/config.json

sudo python3 readncut_stream.py MAKE-YES-SURE

sudo mkdir -p build/release/

sudo cp pdtslsw build/release/pdtslsw
sudo chmod a+x build/release/pdtslsw
sudo cp build/release/pdtslsw /usr/bin/pdtslsw

sudo cp pdtslsw-rules.py build/release/pdtslsw-rules
sudo chmod a+x build/release/pdtslsw-rules
sudo cp build/release/pdtslsw-rules /usr/bin/pdtslsw-rules

sudo cp verify_sector_by_sector_files_checksum.py build/release/verify_sector_by_sector_files_checksum
sudo chmod a+x build/release/verify_sector_by_sector_files_checksum
sudo cp build/release/verify_sector_by_sector_files_checksum /usr/bin/verify_sector_by_sector_files_checksum
 
sudo rm -rf build/