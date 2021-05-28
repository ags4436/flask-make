#Code By AGS
#Youtube - https://youtube.com/programmingforfun
#instagram - @buff3r0verflow

#------------------------------------------------------#
#  Bored Creating all the files from scratch?          #
#  Use this automated tool which creates them for you! #
#------------------------------------------------------#

import os 
import requests
from os import path
import sys, getopt

argumentList = sys.argv[1:]
options = "hpd:"
long_options = ["help", "path", "dir"]

print("--------------------------------------------------------------------")
print('''                                                                                
                                                                                
                       &@&                                                      
                       @@@@@                                                    
                      .@@@@% %@@@                                               
                    @@@@@@ @%     #@@                                           
                   @@     @@@ @                                                 
                    @@@@ @        .                                             
                    @,@@  /.#     @                                             
                     @(@@# %,@  @ @                                             
                      @@@@ @       /                                            
                        @@@@ @ @                                                
                        @#/@% #@(    @                                          
                          #@@@@@@#%    @                                        
                             ,@@@*@@@@   @*                                     
                              #@@@@@ @@&     @@      @@                         
                                  @  .@@@@@@@/@@@.@@@#,@@@@&@@                  
                                           ,@@@@@@@&.                           
                                                                                ''')
print("--------------------------------------------------------------------")
print("Code By AGS")
print("Youtube - https://youtube.com/programmingforfun")
print("instagram - @buff3r0verflow")
print("--------------------------------------------------------------------")

if(len(sys.argv)==1):
    print ("Usage: python flask_make.py -d <dir_name> -p <path>")
    print ("Example: python flask_make.py -d project -p C:\\users\\name\\Desktop")
    print ("Availabe Flags: --Help --dir --path")
    exit()

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--help"):
            print ("usage: python flask_make.py -d <dir_name> -p <path>")
            exit()
             
        elif currentArgument in ("-d", "--dir"):
            dirname=sys.argv[2]

             
        elif currentArgument in ("-p", "--path"):
            parent_dir=sys.argv[4]

             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

try: 
    from flask import Flask, render_template
except:
    print("Flask Package Not Found ")
    ch=input("Install Flask Package using pip (Y/n):")
    if(ch=="y" or ch=="Y"):
        os.system("pip install Flask")
        pass
    else:
        print("Install Flask before you work with fask :) ")
        exit()



while True:
    if not path.exists(parent_dir):
        parent_dir=input("Enter the path: ")
        print("Enter a Vaild Path!")
        parent_dir=input("Enter the path: ")
    else:
        break

flag = 0

if chr(92) in parent_dir:
    flag=1
    if parent_dir[-1]!=chr(92) :
        parent_dir+=chr(92)

if "/" in parent_dir:
    if parent_dir[-1]!="/":
        parent_dir+="/"        


path=os.path.join(parent_dir,dirname)

while True:
    try:
        os.mkdir(path)
        break
    except IOError:
        print("Directory Name already Exists!!!")
        dirname=input("Enter a different dir name: ")
        path=os.path.join(parent_dir,dirname)
        continue 


try:
    os.chdir(path)

    if flag:
        os.mkdir(path+ chr(92) +"templates")
        os.mkdir(path+ chr(92) +"static")
    else: 
        os.mkdir(path+ "/templates")
        os.mkdir(path+ "/static")

    main_file = 'https://raw.githubusercontent.com/ags4436/modules-flask/master/main.py'
    r = requests.get(main_file, allow_redirects=True)
    open('main.py', 'wb').write(r.content)

    if flag:
        os.chdir(path+ chr(92) +"templates")
    else:
        os.chdir(path+ "/templates")
    home='https://raw.githubusercontent.com/ags4436/modules-flask/master/home.html'
    r = requests.get(home, allow_redirects=True)
    open('home.html', 'wb').write(r.content)
    
    layout="https://raw.githubusercontent.com/ags4436/modules-flask/master/layout.html"
    r = requests.get(layout, allow_redirects=True)
    open('layout.html', 'wb').write(r.content)

    print("Successfully initiated flask Project")

except:
    print("Some Error Occured Try Again Later")