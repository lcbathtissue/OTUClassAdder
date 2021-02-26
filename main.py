import os
from dotenv import load_dotenv
from time import strftime, gmtime
from bs4 import BeautifulSoup
import requests

login_userID = os.getenv('MY_OTU_STUDENT_ID')
login_password = os.getenv('MY_OTU_MYCAMPUS_PASSWORD')

# https://ontariotechu.ca/mycampus/
# administration self service > Student Information - OT > Registration > Add/Drop Classes
# http://portal.mycampus.ca/cp/render.UserLayoutRootNode.uP?uP_tparam=utf&utf=/cp/school/sctmain
# lookup classes
# https://ssbp.mycampus.ca/prod_uoit/bwskfcls.p_sel_crse_search

def setPage(input):
    global URL, source, PageNickName, PageFileName, soup, pSoup
    URL = input
    source = requests.get(URL).text
    soup = BeautifulSoup(source, 'lxml')
    pSoup = soup.prettify()
    if URL == frontPageURL:
        PageNickName = "Front_Page_"
        PageFileName = "Front_Page_"
    else:
        PageNickName = ""
        PageFileName = ""


def printPSoup():

    # old code needs to be reworked

    datestamp = strftime("%Y_%m_%d_%H_%M_%S", gmtime())
    logfile = open(datestamp + ".txt", "a")
    logfile.write(pSoup)
    logfile.close()
    # print(pSoup)
    print("")
    print("Finished!")


frontPageURL = "https://ontariotechu.ca/mycampus/"
lookupClassesURL = "https://ssbp.mycampus.ca/prod_uoit/bwskfcls.p_sel_crse_search"
adminPageURL = "http://portal.mycampus.ca/cp/render.UserLayoutRootNode.uP?uP_tparam=utf&utf=/cp/school/sctmain"

payload = {'pass': login_password, 'user': login_userID, 'uuid': '0xACA021'}

r = requests.post("https://portal.mycampus.ca/cp/home/login", data=payload)

# WORKING UP UNTIL HERE - LOGIN SUCCESSFUL THEN GETS AN ERROR

r = requests.get("https://portal.mycampus.ca/cp/home/next")
print(r.text)

datestamp = strftime("%Y_%m_%d_%H_%M_%S", gmtime())
logfile = open(datestamp + ".txt", "a")
logfile.write(r.text)
logfile.close()
# print(pSoup)
print("")
print("Finished!")