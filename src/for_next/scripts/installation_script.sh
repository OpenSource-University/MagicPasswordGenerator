echo "installation d'outils de paranoiaques..."
sudo apt update && sudo apt upgrade -y && sudo apt install -y nmap ufw coreutils
sudo ufw deny 22 && sudo ufw deny 27017 && sudo ufw deny 80 && sudo ufw deny 443
sudo ufw enable && sudo ufw status
