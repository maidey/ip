reset='\033[0m'
bold='\033[01m'
disable='\033[02m'
underline='\033[04m'
reverse='\033[07m'
strikethrough='\033[09m'
invisible='\033[08m'
black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'
bblack='\033[40m'
bred='\033[41m'
bgreen='\033[42m'
borange='\033[43m'
bblue='\033[44m'
bpurple='\033[45m'
bcyan='\033[46m'
blightgrey='\033[47m'

head(){
    clear
    echo "┏┓┏━┓────┏┓░░░░░░░░░░░┏┓░"
    echo "┣┫┃╋┃╔══╗┃┗┓┏┳┓┏━┓░┏━┓┃┣┓"
    echo "┃┃┃┏┛╚══╝┃┏┫┃┏┛┃╋┗┓┃━┫┃━┫"$black$bgreen"by dai re a.k.a mogion"$reset
    echo "┗┛┗┛░────┗━┛┗┛░┗━━┛┗━┛┗┻┛"
    echo "◈ ━━━━━━━━━━ ● ━━━━━━━━━ ◈"
    }
    
head
echo "instaling python ..."
pkg i python python2 python3 -y
pip install --upgrade ipapi
echo "instaling ip api..."
git clone https://github.com/ipapi-co/ipapi-python
cd ipapi-python && python3 setup.py install
python3 ip.py
