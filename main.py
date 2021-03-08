import os
from dotenv import load_dotenv
from time import strftime, gmtime
from bs4 import BeautifulSoup
import requests

def log(input):
    print(input)
    fileName = "Log_" + datestamp
    logfile = open(fileName + ".txt", "a")

    #logfile.write(MyCampusLoginRequest.text)

    logfile.write("test")
    logfile.close()

def getCredentials():
    global login_userID, login_password
    load_dotenv()
    login_userID = os.getenv('MY_OTU_STUDENT_ID')
    login_password = os.getenv('MY_OTU_MYCAMPUS_PASSWORD')

def clearTargetCourses():
    global targetCoursesList, firstAddedTargetCourse
    targetCoursesList = [""]
    firstAddedTargetCourse = False

def checkNBreakCourseCode(inputtedCourse):
    global targetCoursesList, firstAddedTargetCourse
    log("Checking and breaking inputted course code into smaller strings " + inputtedCourse)
    log("BYPASSING ..")
    log("")

def attemptLogin():
    global MyCampusLoginRequest, MyCampusLoginRequestYield
    log("Attempting to login to MyCampus..!")
    log("")
    setPage(frontPageURL)
    loginRequestPayload = {'pass': login_password, 'user': login_userID, 'uuid': '0xACA021'}
    MyCampusLoginRequest = requests.post(loginPageURL, data=loginRequestPayload)

    #savePage(frontPageURL)

    log("Login complete! " + MyCampusLoginRequestYield)
    log("")

def addTargetCourse(targetCourse):
    global targetCoursesList, firstAddedTargetCourse

    checkNBreakCourseCode(targetCourse)

    if firstAddedTargetCourse == False:
        firstAddedTargetCourse = True
        targetCoursesList = [targetCourse]
    else:
        targetCoursesList.append(targetCourse)
    targetCoursesListAsString = ' '.join([str(elem) for elem in targetCoursesList])
    log(targetCourse + ", has been added to targetCoursesList " + targetCoursesListAsString)
    log("")

def setupPageAddresses():
    global loginPageURL, loginPageNextURL, frontPageURL, lookupClassesURL, adminPageURL
    loginPageURL = "https://portal.mycampus.ca/cp/home/login"
    loginPageNextURL = "https://portal.mycampus.ca/cp/home/next"
    frontPageURL = "https://ontariotechu.ca/mycampus/"
    lookupClassesURL = "https://ssbp.mycampus.ca/prod_uoit/bwskfcls.p_sel_crse_search"
    adminPageURL = "http://portal.mycampus.ca/cp/render.UserLayoutRootNode.uP?uP_tparam=utf&utf=/cp/school/sctmain"
    # https://ontariotechu.ca/mycampus/
    # administration self service > Student Information - OT > Registration > Add/Drop Classes
    # http://portal.mycampus.ca/cp/render.UserLayoutRootNode.uP?uP_tparam=utf&utf=/cp/school/sctmain
    # lookup classes
    # https://ssbp.mycampus.ca/prod_uoit/bwskfcls.p_sel_crse_search

def setPage(page):
    global URL, source, PageNickName, PageFileName, soup, pSoup
    URL = page
    source = requests.get(URL).text
    soup = BeautifulSoup(source, 'lxml')
    pSoup = soup.prettify()
    if URL == loginPageURL:
        PageNickName = "Login Page"
        PageFileName = "Login_Page_"
    elif URL == frontPageURL:
        PageNickName = "Front Page"
        PageFileName = "Front_Page_"
    elif URL == lookupClassesURL:
        PageNickName = "Lookup Classes Page"
        PageFileName = "Lookup_Classes_"
    elif URL == adminPageURL:
        PageNickName = "Admin Page"
        PageFileName = "Admin_Page_"
    else:
        PageNickName = ""
        PageFileName = ""
    log("Page set to: " + page)
    log("")

def savePage(page):
    global URL, source, PageNickName, PageFileName, soup, pSoup
    datestamp = strftime("%Y_%m_%d_%H_%M_%S", gmtime())
    fileName = PageFileName + "_" + datestamp
    pagefile = open(fileName + ".html", "a")
    pagefile.write(fileName.text)
    pagefile.close()


def printPSoup():

    # old code needs to be reworked

    datestamp = PageFileName + strftime("%Y_%m_%d_%H_%M_%S", gmtime())

    savePage(page)

    pagefile = open(datestamp + ".html", "a")
    pagefile.write(pSoup)
    pagefile.close()
    # print(pSoup)
    log("")
    log("Finished!")

def setupClassAdder():
    global MyCampusLoginRequestYield, datestamp
    datestamp = strftime("%Y_%m_%d_%H_%M_%S", gmtime())
    MyCampusLoginRequestYield = "Not Yet Attempted"
    getCredentials()
    clearTargetCourses()
    setupPageAddresses()

# COURSES/SETUP
setupClassAdder()

#addTargetCourse("MATH1010U")
#addTargetCourse("ENGR1025U")

# START CONNECTION
attemptLogin()


# WORKING UP UNTIL HERE - LOGIN SUCCESSFUL THEN GETS AN ERROR
#MyCampusLoginRequest = requests.get("https://portal.mycampus.ca/cp/home/next")

log(MyCampusLoginRequest)

source = requests.get(URL).text
soup = BeautifulSoup(source, 'lxml')
pSoup = soup.prettify()
log(pSoup)

log("")
log("Finished!")