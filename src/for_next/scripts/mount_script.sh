echo "MOUNT FILE..."
sudo mkdir {}.dir__.mount_point
sudo mount {} {}.dir__.mount_point
sudo chown $USER {}.dir__.mount_point
echo "paranoia..."
sudo chmod o-w {}.dir__.mount_point
sudo chmod o-r {}.dir__.mount_point
sudo chmod o-x {}.dir__.mount_point
sudo chmod u+w {}.dir__.mount_point
sudo chmod u+r {}.dir__.mount_point
sudo chmod u+x {}.dir__.mount_point