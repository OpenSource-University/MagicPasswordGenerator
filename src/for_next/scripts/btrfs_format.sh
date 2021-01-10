echo "formatage du disque virtuel en BTRFS..."
sudo mkfs.btrfs {}
echo "vous devenez unique proprietaire..."
sudo chown $USER {}
echo "paranoia..."
sudo chmod o-w {}
sudo chmod o-r {}
sudo chmod o-x {}
sudo chmod u+w {}
sudo chmod u+r {}
sudo chmod u+x {}
sudo chmod g-r {}
sudo chmod g-x {}
echo "Voila pour les droits..."