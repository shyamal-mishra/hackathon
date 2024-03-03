* Settings *
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections
Library    String

* Variables *
${URL}           https://boards.greenhouse.io/whatnot/jobs/4983690004
${BROWSER}       Chrome
${file_path}     C:/Users/12676/Downloads/HW3 - HBS Case Study (1)

* Test Cases *
Open And Fill Application Form
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    2s  # It's good to specify the unit (seconds in this case)
    Wait Until Page Contains Element    //*[@id="apply_button"]  30s
    Scroll Element Into View    //*[@id="main_fields"]
    Wait Until Page Contains Element    //*[@id="main_fields"]  30s
    ${inputEle}=    Get WebElements     //*[@id="main_fields"]//input
    Input Text    ${inputEle}[0]    Geeta 
    Input Text    ${inputEle}[1]    Kukreja
    Input Text    ${inputEle}[2]    gk457@drexel.edu
    Input Text    ${inputEle}[3]    9257918535
    Choose File    xpath=//*[@id="resume_fieldset"]/div/div[3]/button[1]  ${file_path}
    Scroll Element Into View    //*[@id="custom_fields"]
    Wait Until Page Contains Element    //*[@id="custom_fields"]  30s

    Sleep    10s