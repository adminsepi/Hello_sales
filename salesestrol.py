from colorama import init, Fore, Back, Style
import requests
import json
import webbrowser
import os
import platform
from ipaddress import ip_address
import time

# Initialize colorama
init()

# Define neon colors for Anonymous aesthetic
GREEN_NEON = '\033[38;5;46m'   # Neon green
GREEN_DARK = '\033[38;5;22m'   # Dark green
WHITE_NEON = '\033[38;5;255m'  # Neon white
CYAN_NEON = '\033[38;5;51m'    # Neon cyan for accents
PINK_NEON = '\033[38;5;201m'   # Neon pink
PINK_LIGHT = '\033[38;5;207m'  # Light pink
PINK_DARK = '\033[38;5;161m'   # Dark pink

# Enhanced ASCII Art for Anonymous with Guy Fawkes mask
BANNER = f"""
{PINK_NEON}╔══════════════════════════════════════════════════════════════════════╗
{PINK_NEON}║                                                                      ║
{WHITE_NEON}║           _____                                                      ║
{WHITE_NEON}║          /     \\                                                    ║
{PINK_NEON}║         /_______\\                                                   ║
{WHITE_NEON}║         |  ***  |         We are  @salesestrol                        ║
{WHITE_NEON}║         |  ***  |         Coder: #salesestrol   
            ID= @One_of_the_Anonimous_Group                             ║
{PINK_NEON}║         |_______|         We do not forgive                         ║
{WHITE_NEON}║                           We do not forget                          ║
{PINK_NEON}║                           Expect Us                                 ║
{PINK_NEON}╚══════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
{CYAN_NEON}                @salesestrol - United as One, Divided by Zero{Style.RESET_ALL}
"""

# Print the banner
print(BANNER)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def open_telegram():
    telegram_url = "https://t.me/salesestrol"
    telegram_app_url = "tg://resolve?domain=salesestrol"
    print(f"\n{PINK_LIGHT}[*] Opening Telegram channel...{Style.RESET_ALL}")
    try:
        if platform.system() == "Linux" and "android" in platform.platform().lower():
            result = os.system(f"am start -a android.intent.action.VIEW -d {telegram_app_url}")
            if result != 0:
                print(f"{PINK_DARK}[!] Failed to open Telegram app, trying browser...{Style.RESET_ALL}")
                webbrowser.open(telegram_url)
        else:
            webbrowser.open(telegram_url)
    except Exception as e:
        print(f"{PINK_DARK}[!] Failed to open Telegram: {e}{Style.RESET_ALL}")
        print(f"{PINK_LIGHT}[*] Falling back to browser...{Style.RESET_ALL}")
        try:
            webbrowser.open(telegram_url)
        except Exception as e2:
            print(f"{PINK_DARK}[!] Failed to open in browser: {e2}{Style.RESET_ALL}")

def animate_loading(message="Loading", duration=2):
    chars = "⣾⣷⣯⣟⡿⢿⣻⣽"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in chars:
            print(f"\r{PINK_NEON}{char} {message}...{Style.RESET_ALL}", end="", flush=True)
            time.sleep(0.1)
    print(f"\r{PINK_LIGHT}✓ {message} complete!{Style.RESET_ALL}")

def validate_ip(ip):
    try:
        ip_obj = ip_address(ip)
        if ip_obj.is_private:
            print(f"{PINK_DARK}[!] Warning: This is a private IP address{Style.RESET_ALL}")
        elif ip_obj.is_loopback:
            print(f"{PINK_DARK}[!] Warning: This is a loopback address{Style.RESET_ALL}")
        elif ip_obj.is_multicast:
            print(f"{PINK_DARK}[!] Warning: This is a multicast address{Style.RESET_ALL}")
        return True
    except ValueError:
        return False

def get_enhanced_ip_info(ip, full_info=False):
    try:
        if not validate_ip(ip):
            print(f"{PINK_DARK}[!] Error: Invalid IP address format{Style.RESET_ALL}")
            return
        
        animate_loading("Gathering IP data")
        
        fields = "status,message,query,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,mobile,proxy,hosting"
        if full_info:
            fields = "status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
        
        response = requests.get(f"http://ip-api.com/json/{ip}?fields={fields}", timeout=10)
        data = response.json()
        
        if data['status'] == 'success':
            print(f"\n{PINK_NEON}╔══════════════════════════════════════════════════════════════════════╗")
            print(f"║{PINK_LIGHT}                 IP TRACKING DATA FOR {ip}                     {PINK_NEON}║")
            print(f"╚══════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
            
            print(f"\n{PINK_LIGHT}┌─────────────────────{CYAN_NEON} LOCATION INFO {PINK_LIGHT}─────────────────────┐")
            print(f"{PINK_LIGHT}│{CYAN_NEON} Country      : {PINK_NEON}{data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})")
            print(f"{PINK_LIGHT}│{CYAN_NEON} Region       : {PINK_NEON}{data.get('regionName', 'N/A')} ({data.get('region', 'N/A')})")
            print(f"{PINK_LIGHT}│{CYAN_NEON} City         : {PINK_NEON}{data.get('city', 'N/A')}")
            print(f"{PINK_LIGHT}│{CYAN_NEON} ZIP Code     : {PINK_NEON}{data.get('zip', 'N/A')}")
            print(f"{PINK_LIGHT}│{CYAN_NEON} Coordinates  : {PINK_NEON}{data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")
            print(f"{PINK_LIGHT}│{CYAN_NEON} Timezone     : {PINK_NEON}{data.get('timezone', 'N/A')}")
            
            if full_info:
                print(f"{PINK_LIGHT}│{CYAN_NEON} Continent    : {PINK_NEON}{data.get('continent', 'N/A')} ({data.get('continentCode', 'N/A')})")
                print(f"{PINK_LIGHT}│{CYAN_NEON} District     : {PINK_NEON}{data.get('district', 'N/A')}")
                print(f"{PINK_LIGHT}│{CYAN_NEON} Currency     : {PINK_NEON}{data.get('currency', 'N/A')}")
                print(f"{PINK_LIGHT}│{CYAN_NEON} UTC Offset   : {PINK_NEON}{data.get('offset', 'N/A')}")
            
            print(f"{PINK_LIGHT}└──────────────────────────────────────────────────────────────────────┘")
            
            print(f"\n{PINK_DARK}┌─────────────────────{CYAN_NEON} NETWORK INFO {PINK_DARK}─────────────────────┐")
            print(f"{PINK_DARK}│{CYAN_NEON} ISP          : {PINK_NEON}{data.get('isp', 'N/A')}")
            print(f"{PINK_DARK}│{CYAN_NEON} Organization : {PINK_NEON}{data.get('org', 'N/A')}")
            print(f"{PINK_DARK}│{CYAN_NEON} AS Number    : {PINK_NEON}{data.get('as', 'N/A')}")
            
            if full_info:
                print(f"{PINK_DARK}│{CYAN_NEON} AS Name      : {PINK_NEON}{data.get('asname', 'N/A')}")
                print(f"{PINK_DARK}│{CYAN_NEON} Reverse DNS  : {PINK_NEON}{data.get('reverse', 'N/A')}")
            
            print(f"{PINK_DARK}└──────────────────────────────────────────────────────────────────────┘")
            
            print(f"\n{PINK_LIGHT}┌─────────────────────{CYAN_NEON} SECURITY ANALYSIS {PINK_LIGHT}─────────────────────┐")
            mobile_status = "Yes" if data.get('mobile', False) else "No"
            proxy_status = "Yes" if data.get('proxy', False) else "No"
            hosting_status = "Yes" if data.get('hosting', False) else "No"
            
            print(f"{PINK_LIGHT}│{CYAN_NEON} Mobile       : {PINK_NEON}{mobile_status}")
            print(f"{PINK_LIGHT}│{CYAN_NEON} Proxy/VPN    : {PINK_NEON}{proxy_status}")
            print(f"{PINK_LIGHT}│{CYAN_NEON} Hosting      : {PINK_NEON}{hosting_status}")
            print(f"{PINK_LIGHT}└──────────────────────────────────────────────────────────────────────┘")
            
            lat = data.get('lat')
            lon = data.get('lon')
            if lat and lon:
                maps_url = f"https://www.google.com/maps/place/{lat},{lon}"
                print(f"\n{PINK_DARK}[+] Google Maps: {CYAN_NEON}{maps_url}{Style.RESET_ALL}")
                
                open_map = input(f"\n{PINK_LIGHT}[?] Open location in Google Maps? (y/n): {Style.RESET_ALL}").lower()
                if open_map == 'y':
                    webbrowser.open(maps_url)
            
            print(f"\n{PINK_NEON}║{PINK_LIGHT}                 TRACKING COMPLETED SUCCESSFULLY                  {PINK_NEON}║")
            print(f"╚══════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
            
        else:
            print(f"{PINK_DARK}[!] Error: {data.get('message', 'Unknown error')}{Style.RESET_ALL}")
            
    except ValueError:
        print(f"{PINK_DARK}[!] Error: Invalid IP address format{Style.RESET_ALL}")
    except requests.RequestException as e:
        print(f"{PINK_DARK}[!] Error: Failed to connect to IP API - {str(e)}{Style.RESET_ALL}")
    except json.JSONDecodeError:
        print(f"{PINK_DARK}[!] Error: Invalid response from server{Style.RESET_ALL}")
    except Exception as e:
        print(f"{PINK_DARK}[!] Unexpected error: {str(e)}{Style.RESET_ALL}")

def get_my_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=10)
        data = response.json()
        return data.get('ip', None)
    except:
        try:
            response = requests.get("https://httpbin.org/ip", timeout=10)
            data = response.json()
            return data.get('origin', None)
        except:
            return None

def show_menu():
    print(f"\n{PINK_NEON}┌─────────────────────────{CYAN_NEON} IP TRACKER MENU {PINK_NEON}─────────────────────────┐")
    print(f"{PINK_NEON}│{PINK_LIGHT} [0] {CYAN_NEON}- Gᴇᴛ Mʏ IP Aᴅᴅʀᴇꜱꜱ & Iɴꜰᴏʀᴍᴀᴛɪᴏɴ")
    print(f"{PINK_NEON}│{PINK_LIGHT} [1] {CYAN_NEON}- Tʀᴀᴄᴋ IP Aᴅᴅʀᴇꜱꜱ (Bᴀꜱɪᴄ Iɴꜰᴏ)")
    print(f"{PINK_NEON}│{PINK_LIGHT} [2] {CYAN_NEON}- Tʀᴀᴄᴋ IP Aᴅᴅʀᴇꜱꜱ (Fᴜʟʟ Iɴꜰᴏ)")
    print(f"{PINK_NEON}│{PINK_LIGHT} [3] {CYAN_NEON}- Oᴘᴇɴ Tᴇʟᴇɢʀᴀᴍ Cʜᴀɴɴᴇʟ")
    print(f"{PINK_NEON}│{PINK_LIGHT} [4] {CYAN_NEON}- E x ɪ ᴛ")
    print(f"{PINK_NEON}└──────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}")

def main():
    while True:
        clear_screen()
        print(BANNER)
        print(f"{PINK_LIGHT}                    {CYAN_NEON}A ᴅ ᴠ ᴀ ɴ ᴄ ᴇ ᴅ  IP T ʀ ᴀ ᴄ ᴋ ᴇ ʀ{Style.RESET_ALL}")
        print(f"{PINK_LIGHT}                    {PINK_NEON}C ᴏ ᴅ ᴇ ʀ : #salesestrol{Style.RESET_ALL}")
        print(f"{PINK_LIGHT}                    {PINK_DARK}T ᴇ ʟ ᴇ ɢ ʀ ᴀ ᴍ : @salesestrol{Style.RESET_ALL}")
        
        show_menu()
        
        choice = input(f"\n{PINK_LIGHT}[?] Sᴇʟᴇᴄᴛ ᴀɴ ᴏᴘᴛɪᴏɴ: {Style.RESET_ALL}").strip()
        
        if choice == "0":
            print(f"\n{PINK_LIGHT}[*] Gᴇᴛᴛɪɴɢ ʏᴏᴜʀ IP ᴀᴅᴅʀᴇꜱꜱ...{Style.RESET_ALL}")
            my_ip = get_my_ip()
            if my_ip:
                print(f"\n{PINK_NEON}[+] Yᴏᴜʀ IP Aᴅᴅʀᴇꜱꜱ: {CYAN_NEON}{my_ip}{Style.RESET_ALL}")
                get_enhanced_ip_info(my_ip, full_info=True)
            else:
                print(f"{PINK_DARK}[!] Cᴏᴜʟᴅ ɴᴏᴛ ᴅᴇᴛᴇʀᴍɪɴᴇ ʏᴏᴜʀ IP ᴀᴅᴅʀᴇꜱꜱ{Style.RESET_ALL}")
        
        elif choice == "1":
            ip = input(f"\n{PINK_LIGHT}[?] Eɴᴛᴇʀ IP ᴀᴅᴅʀᴇꜱꜱ ᴛᴏ ᴛʀᴀᴄᴋ: {Style.RESET_ALL}").strip()
            if ip:
                get_enhanced_ip_info(ip, full_info=False)
            else:
                print(f"{PINK_DARK}[!] Pʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴀ ᴠᴀʟɪᴅ IP ᴀᴅᴅʀᴇꜱꜱ{Style.RESET_ALL}")
        
        elif choice == "2":
            ip = input(f"\n{PINK_LIGHT}[?] Eɴᴛᴇʀ IP ᴀᴅᴅʀᴇꜱꜱ ꜰᴏʀ ꜰᴜʟʟ ᴛʀᴀᴄᴋɪɴɢ: {Style.RESET_ALL}").strip()
            if ip:
                get_enhanced_ip_info(ip, full_info=True)
            else:
                print(f"{PINK_DARK}[!] Pʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴀ ᴠᴀʟɪᴅ IP ᴀᴅᴅʀᴇꜱꜱ{Style.RESET_ALL}")
        
        elif choice == "3":
            open_telegram()
        
        elif choice.lower() in ["4", "exit", "quit"]:
            print(f"\n{PINK_LIGHT}Tʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱɪɴɢ IP-Tʀᴀᴄᴋᴇʀ Sᴀʟᴇꜱ Eꜱᴛʀᴏʟ!{Style.RESET_ALL}")
            print(f"{PINK_NEON}Jᴏɪɴ ᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ: {CYAN_NEON}@salesestrol{Style.RESET_ALL}")
            break
        
        else:
            print(f"{PINK_DARK}[!] Iɴᴠᴀʟɪᴅ ᴏᴘᴛɪᴏɴ. Pʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ.{Style.RESET_ALL}")
        
        input(f"\n{PINK_LIGHT}Pʀᴇꜱꜱ Eɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{PINK_DARK}[!] Pʀᴏɢʀᴀᴍ ɪɴᴛᴇʀʀᴜᴘᴛᴇᴅ ʙʏ ᴜꜱᴇʀ{Style.RESET_ALL}")
        print(f"{PINK_LIGHT}Tʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱɪɴɢ IP-Tʀᴀᴄᴋᴇʀ Sᴀʟᴇꜱ Eꜱᴛʀᴏʟ!{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{PINK_DARK}[!] Aɴ ᴜɴᴇxᴘᴇᴄᴛᴇᴅ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ: {str(e)}{Style.RESET_ALL}")