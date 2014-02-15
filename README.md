RPi_DJ
======
This is a web-based song request system that runs standalone on a Raspberry Pi.

Here are some steps to set this up. Enjoy.

Step 1. Install Raspbian on the Raspberry Pi.

	- Go to http://www.raspberrypi.org/downloads and download the NOOBS (network install).
	- Format the SD card.
	- Unzip the NOOBS file and extract the contents onto the SD card (drag and drop).
	- Put the SD card into the Raspberry Pi and boot it (plug it in).
	- Choose Raspbian and click install (or hit “i” on a keyboard).
	- The defaults are user: pi    password: raspberry

Step 2. Install SSH.

	- sudo apt-get install ssh
	- sudo update-rc.d ssh defaults
	- sudo reboot

Step 3. Network Configuration

	- sudo nano /etc/network/interfaces
		- iface eth0 inet static
		- address 192.168.1.215 (your choice here)
		- netmask 255.255.255.0
		- gateway 192.168.1.1
	- Ctrl+X to save and exit
	- sudo reboot

Step 4. Update the pre-installed software on the system.

	- sudo dpkg-reconfigure tzdata
	- sudo apt-get update
	- sudo apt-get upgrade

Step 5. Install Apache (web server)

	- sudo apt-get install apache2 php5 libapache2-mod-php5
	- sudo service apache2 restart
	- Now test by entering its IP into your web browser

Step 6. Install MySQL (database)
	
	- sudo apt-get install mysql-server mysql-client php5-mysql
	- sudo reboot

Step 7. Install FTP (so you can code on your computer and transfer files to the RPi)

	- sudo chown -R pi /var/www
	- sudo apt-get install vsftpd
	- sudo nano /etc/vsftpd.conf
		- change anonymous_enable=YES to NO
		- uncomment local_enable=YES and write_enable=YES
		- add to bottom of file: force_dot_files=YES
	- sudo service vsftpd restart

	- sudo passwd root
	- log out of SSH session (cmd = logout)
	- log into SSH as root
	- nano /etc/passwd
		- uncomment out the line that says pi:x:1000….
	- usermod -d /var/www pi
	- exit SSH and log back in with pi
	- sudo usermod -L root
	- now log off
	- you can use an FTP client to easily read and write files to /var/www (use port 21)



How to Make Your Raspberry Pi a Modern-Day Jukebox!

Step 8. Install Python MySQL library

	- sudo apt-get install python-mysqldb

Step 9. Download id3reader for Python (this reads the tags on the mp3 files)

	- This is the link: http://nedbatchelder.com/code/modules/id3reader.html
	- follow the instructions there

Step 10. Auto-mount an external hard drive.
	
	- ls -l /dev/disk/by-uuid/
	- get the UUID number (it follows after the date) on the ../../sda1 line 7E0D-1907
	- sudo mkdir /media/JUKEBOX (or what ever you would like)
	- sudo chmod 777 /media/JUKEBOX 
	- sudo mount -t vfat -o uid=pi,gid=pi /dev/sda1 /media/JUKEBOX
	- sudo cp /etc/fstab /etc/fstab.backup
	- sudo nano /etc/fstab 
	- add this line: UUID=<your uuid #> /media/JUKEBOX vfat umask=000 0 0
	- sudo reboot

Step 11. Set up the raspberry pi to rip music off of YouTube.
	
	- Install youtube-dl (this downloads videos from youtube given the web link)
		- sudo curl https://yt-dl.org/downloads/2014.01.28.1/youtube-dl -o /usr/local/bin/youtube-dl
		- sudo chmod a+x /usr/local/bin/youtube-dl
		- sudo wget https://yt-dl.org/downloads/2014.01.28.1/youtube-dl.sig -O youtube-dl.sig
		- gpg --verify youtube-dl.sig /usr/local/bin/youtube-dl
		- rm youtube-dl.sig
		- if you have problems check this website for updated instructions if available: http://rg3.github.io/youtube-dl/download.html
		- I’ve also found that the instructions involving the sig file are not needed (so feel free to skipping them if they don’t work ;) )

	- Install ffmpeg (to get wav file from video)
		- sudo apt-get install ffmpeg
	
	- Install lame (to convert wav to mp3)
		- sudo apt-get lame


	**Usage**: This process is as simple as 4 commands in the terminal.
		- $ youtube-dl http://www.youtube.com/watch?v=6E2hYDIFDIU
		- $ youtube-dl --get-title http://www.youtube.com/watch?v=6E2hYDIFDIU
		- $ ffmpeg -i 6E2hYDIFDIU.flv 6E2hYDIFDIU.wav
		- $ lame 6E2hYDIFDIU.wav 6E2hYDIFDIU.mp3



So now you are ready to start coding. Here are a couple of very good resources:

	- PHP and MySQL: http://dev.mysql.com/tech-resources/articles/ddws/
	- Python and SQL: http://www.tutorialspoint.com/python/python_database_access.htm


Now get coding.
