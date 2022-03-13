import os
import getpass

class wifii:

    def __init__(self):                
        while (True):
            selection =input("1: display available netwroks \n2: connecting to a preconfigured network \n3: configure new network connection \nQ: close the program \nyour selection :")
            if (selection=="1"): 
                self.displayAvailableNetworks()
            elif (selection=="2"):
                self.preconfigured()
            elif (selection=="3"):
                self.configureNewNet()
            elif (selection=="q"or selection== "Q" ):
                os.system("cls")
                print("\n**************\nprogram closed\n**************\n\n") 
                break
            else:
                print("\n*************** \nwrong selection \n***************\n\n")

    def displayAvailableNetworks(self):
        command = "netsh wlan show networks interface=Wi-Fi"
        os.system(command)  
    
    def preconfigured(self):
        name_of_router = input('Enter Name/SSID of the Wifi Network you wish to connect to: ')
        os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')      
        print("If you're not yet connected, try connecting to a previously connected SSID again!")
    
    def configureNewNet(self):            
        name = input("Name of Wi-Fi: ")       
        password = getpass.getpass("Password: ")

        def createNewConnection(name, SSID, password):
            config = """<?xml version=\"1.0\"?>
            <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">   

            <name>"""+name+"""</name>

            <SSIDConfig>

                <SSID>

                    <name>"""+SSID+"""</name>

                </SSID>

            </SSIDConfig>

            <connectionType>ESS</connectionType>

            <connectionMode>auto</connectionMode>

            <MSM>

                <security>

                    <authEncryption>

                        <authentication>WPA2PSK</authentication>

                        <encryption>AES</encryption>

                        <useOneX>false</useOneX>

                    </authEncryption>

                    <sharedKey>

                        <keyType>passPhrase</keyType>

                        <protected>false</protected>

                        <keyMaterial>"""+password+"""</keyMaterial>

                    </sharedKey>

                </security>

            </MSM>
            </WLANProfile>"""

            command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
            with open(name+".xml", 'w') as file:
                file.write(config) 
            os.system(command) 

        def connect(name, SSID):
            command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
            os.system(command) 
        createNewConnection(name, name, password) 
        connect(name, name)
        print("If you aren't connected to this network, try connecting with the correct password!")
       
wifii()