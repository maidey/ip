import ipapi
import os
def sh(script):
    os.system("bash -c '%s'" % script)
#color
class colors:
        reset='\033[0m'
        bold='\033[01m'
        disable='\033[02m'
        underline='\033[04m'
        reverse='\033[07m'
        strikethrough='\033[09m'
        invisible='\033[08m'
        class fg:
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
        class bg:
            black='\033[40m'
            red='\033[41m'
            green='\033[42m'
            orange='\033[43m'
            blue='\033[44m'
            purple='\033[45m'
            cyan='\033[46m'
            lightgrey='\033[47m'
            
plus='\033[31m[\033[34m÷\033[31m]\033[0m'
def head():
    sh ("clear")
    print ("┏┓┏━┓────┏┓░░░░░░░░░░░┏┓░")
    print ("┣┫┃╋┃╔══╗┃┗┓┏┳┓┏━┓░┏━┓┃┣┓")
    print ("┃┃┃┏┛╚══╝┃┏┫┃┏┛┃╋┗┓┃━┫┃━┫",colors.fg.black,colors.bg.green,"by dai re a.k.a mogion",colors.reset)
    print ("┗┛┗┛░────┗━┛┗┛░┗━━┛┗━┛┗┻┛")
    print ("◈ ━━━━━━━━━━ ● ━━━━━━━━━ ◈")
    
head()
print (colors.fg.green,"loding data..",colors.reset)
#this fucking shit
ip_id = input("DROP IP >>")
ip= ipapi.location(ip=ip_id,output='ip')
city= ipapi.location(ip=ip_id,output='city')
region= ipapi.location(ip=ip_id,output='region')
region_code= ipapi.location(ip=ip_id,output='region_code')
country= ipapi.location(ip=ip_id,output='country')
country_code= ipapi.location(ip=ip_id,output='country_code')
country_code_iso3= ipapi.location(ip=ip_id,output='country_code_iso3')
country_capital= ipapi.location(ip=ip_id,output='country_capital')
country_tld= ipapi.location(ip=ip_id,output='country_tld')
country_name= ipapi.location(ip=ip_id,output='country_name')
continent_code= ipapi.location(ip=ip_id,output='continent_code')
in_eu= ipapi.location(ip=ip_id,output='in_eu')
postal= ipapi.location(ip=ip_id,output='postal')
latitude= ipapi.location(ip=ip_id,output='latitude')
longitude= ipapi.location(ip=ip_id,output='longitude')
timezone= ipapi.location(ip=ip_id,output='timezone')
utc_offset= ipapi.location(ip=ip_id,output='utc_offset')
country_calling_code= ipapi.location(ip=ip_id,output='country_calling_code')
currency= ipapi.location(ip=ip_id,output='currency')
currency_name= ipapi.location(ip=ip_id,output='currency_name')
languages= ipapi.location(ip=ip_id,output='languages')
country_area= ipapi.location(ip=ip_id,output='country_area')
country_population= ipapi.location(ip=ip_id,output='country_population')
latlong= ipapi.location(ip=ip_id,output='latlong')
asn= ipapi.location(ip=ip_id,output='asn')
org= ipapi.location(ip=ip_id,output='org')
head()
print (plus,colors.fg.yellow,ip)
print (plus,colors.fg.yellow,city)
print (plus,colors.fg.yellow,region)
print (plus,colors.fg.yellow,region_code)
print (plus,colors.fg.yellow,country)
print (plus,colors.fg.yellow,country_code)
print (plus,colors.fg.yellow,country_code_iso3)
print (plus,colors.fg.yellow,country_capital)
print (plus,colors.fg.yellow,country_tld)
print (plus,colors.fg.yellow,country_name)
print (plus,colors.fg.yellow,continent_code)
print (plus,colors.fg.yellow,in_eu)
print (plus,colors.fg.yellow,postal)
print (plus,colors.fg.yellow,latitude)
print (plus,colors.fg.yellow,longitude)
print (plus,colors.fg.yellow,timezone)
print (plus,colors.fg.yellow,utc_offset)
print (plus,colors.fg.yellow,country_calling_code)
print (plus,colors.fg.yellow,currency)
print (plus,colors.fg.yellow,currency_name)
print (plus,colors.fg.yellow,languages)
print (plus,colors.fg.yellow,country_area)
print (plus,colors.fg.yellow,country_population)
print (plus,colors.fg.yellow,latlong)
print (plus,colors.fg.yellow,asn)
print (plus,colors.fg.yellow,org)
print ("")
print ("")
print (colors.fg.green,"contact me:")
print (colors.fg.yellow,"[t]",colors.fg.green,"telegram",colors.fg.yellow,"[w]",colors.fg.green,"website")

def cois():
    print ("◈ ━━━━━━━━━━ ● ━━━━━━━━━ ◈")
    ipu = input("\033[0m t / w >> ")
    if ipu == "w":
        sh("xdg-open https://maidey.github.io/")
    elif ipu == "t":
        sh("xdg-open https://t.me/mogionc")
    else:
        print ("")

cois()
