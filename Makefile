libpostal_datadir_prefix = /var/local


full-build:
	sudo apt-get install python3 curl autoconf automake libtool python-dev pkg-config git python3-pip
	git submodule update --init
	cd libpostal
	sudo mkdir -p $(libpostal_datadir_prefix)
	./bootstrap.sh
	./configure --datadir=$(libpostal_datadir_prefix)
	make
	sudo make install
	sudo ldconfig
	libpostal_data download all $(libpostal_datadir_prefix)/libpostal
	cd ..
	pip3 install -r requirements.txt

quick-build:
	sudo apt-get install python3 curl autoconf automake libtool python-dev pkg-config git python3-pip
	git submodule update --init
	cd libpostal
	sudo make install
	sudo ldconfig
	libpostal_data download all $(libpostal_datadir_prefix)/libpostal
	cd ..
	pip3 install -r requirements.txt
