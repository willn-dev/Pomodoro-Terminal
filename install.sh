#!/bin/sh

#this script installs the necessary dependencies in a venv, creates the executable, and puts it in path

cd "$(dirname "$0")" # makes sure you are in the right directory to start with.


mkdir -p ~/.local/lib/ # makes the directory local/lib if for some really weird reason you dont have it.


if [ ! -d ~/.local/lib/pomo-term ]; then
    python3 -m venv ~/.local/lib/pomo-term/venv #creates a venv if you dont already have one from installing this before
                                                # a venv is pythons isolated environment so packages here dont affect your main system.
fi

. ~/.local/lib/pomo-term/venv/bin/activate #activates the venv

python3 -m pip install -r requirements.txt #installs the packages the script needs to run in the virtual environment

cp -r .  ~/.local/lib/pomo-term/ #copies everything in the folder to the right place


cat > ~/.local/bin/pomo-term << 'EOF' #this creates a small script that tells your system where to find the timer app.
#!/bin/sh
~/.local/lib/pomo-term/venv/bin/python ~/.local/lib/pomo-term/pomodoro.py
EOF

chmod +x ~/.local/bin/pomo-term

rm ~/.local/lib/pomo-term/install.sh #you dont need the install script anymore so it gets removed. 





