import time
import requests
import re
# is a Python library that is used to parse information out of HTML or XML files.
# It parses its input into an object on which you can run a variety of searches.
from urllib.parse import urljoin
from pprint import pprint


def scan_sql_injection(url):
    try:

        urlt = url.split("=")
        urlt = urlt[0] + '='
        payload1 = "'"
        urlq = urlt + payload1
        reqqq = requests.get(urlq).text
        if ('mysql_fetch_array()' or 'You have an error in your SQL syntax' or 'error in your SQL syntax' \
            or 'mysql_numrows()' or 'Input String was not in a correct format' or 'mysql_fetch' \
            or 'num_rows' or 'Error Executing Database Query' or 'Unclosed quotation mark' \
            or 'Error Occured While Processing Request' or 'Server Error' or 'Microsoft OLE DB Provider for ODBC Drivers Error' \
            or 'Invalid Querystring' or 'VBScript Runtime' or 'Syntax Error'or "SQL syntax.*?MySQL" or "MySQLSyntaxErrorException"
            or 'GetArray()' or 'FetchRows()'or "Warning.*?\Wmysqli?_") in reqqq:
            print("\n[*] SQL Error found!")
            print("[!] Payload:", payload1)
            print("[!] POC:", urlq)
            records_URL(url)
        else:
            print("[-] SQL injection vulnerablity not found.")

    except Exception as e:
        print("[-] SQL injection vulnerablity not found.")



def sql_Time(url):

    try:
        print("\n[!] Testing SQLi")
        urlt = url.split("=")
        urlt = urlt[0] + '='
        urlb = urlt + '1-SLEEP(2)'

        time1 = time.time()
        req = requests.get(urlb)
        time2 = time.time()
        timet = time2 - time1
        timet = str(timet)
        timet = timet.split(".")
        timet = timet[0]

        if int(timet) >= 2:
            print("[*] Blind SQL injection time based found!")
            print("[!] Payload:",'1-SLEEP(2)')
            print("[!] POC:",urlb)

        else:
            print("[-] SQL time based failed - SQL injection vulnerablity not found. ")

    except Exception:
        pass


# to record the error:

flag=False
def records_URL(url):

    try:

        FSQL = open("SQL-Injection.txt", 'r+')
        lines = [line.rstrip() for line in FSQL]
        for y in lines:
            if url == y:
                print("[+] It is already in the SQL Injection vulnerable sites list")
                return

        flag = True
        print("                                                       ")
        if (flag):
            FSQL.write(url)
            FSQL.write("\n")

    except Exception:
        print("Unexpected Error ")
        FSQL.close()


def printi_list():
    try:
        FSQL = print("-->  SQL injection vulnerable websites:\n")
        FSQL = open("SQL-Injection.txt", "r")
        for l in FSQL.readlines():
            print("[*] ", l)


    except Exception:
        print("Unexpected Error ")
        FSQL.close()


def crawl(url):
    href_link = extract_link(url)

    for link in href_link:
        link = urljoin(url, link)
        print('\n',link)
        scan_sql_injection(link)

def request (url):
    try:
            get_response = requests.get(url)
            return get_response

    except requests.exceptions.ConnectionError:
       pass
    except requests.exceptions.InvalidURL:
        print("Invalid url")
    except requests.exceptions:
        pass

# to find all links in page
def extract_link (url):
    response = requests.get(url)
    # to parse the content of the response and take only the urls
    return re.findall('(?:href=")(.*?)"',response.content.decode('utf-8'))


def thank_you():
    print("""

 _____ _   _   ___   _   _  _   __ __   _______ _   _ _ 
|_   _| | | | / _ \ | \ | || | / / \ \ / /  _  | | | | |
  | | | |_| |/ /_\ \|  \| || |/ /   \ V /| | | | | | | |
  | | |  _  ||  _  || . ` ||    \    \ / | | | | | | | |
  | | | | | || | | || |\  || |\  \   | | \ \_/ / |_| |_|
  \_/ \_| |_/\_| |_/\_| \_/\_| \_/   \_/  \___/ \___/(_)
                                                        
                                                        

    """)