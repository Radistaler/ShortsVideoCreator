import undetected_chromedriver as uc
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, requests

WPM = 150
WPS = 2.5
voiceoverDir = "Narrations"


"""
    Scrapes mp3 from listnr.tech
    
    Note:
        -needs gmail and password since the site stores the audio at google cloud
    
"""


def Narrate(fileName, text):
    filePath = f"{voiceoverDir}/{fileName}.mp3"
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    chrome_options.add_argument("--log-level=3")

    driver = uc.Chrome(options=chrome_options)

    driver.get("https://www.listnr.tech/text-to-speech/united-states-english")
    time.sleep(1)
    # Locate and interact with the dropdown menu
    dropdown = driver.find_element(
        By.XPATH, "//span[contains(@role, 'button') and contains(@tabindex, '0')]"
    )
    dropdown.click()
    wait = WebDriverWait(driver, 10)
    item_to_click = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//a[contains(@role, 'button') and contains(@tabindex, '0') and p[text()='Christopher'] and span[contains(@aria-label,'star')]]",
            )
        )
    )
    driver.execute_script("arguments[0].scrollIntoView();", item_to_click)
    time.sleep(2)
    item_to_click.click()
    time.sleep(1)
    content_div = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "ql-editor"))
    )
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    content_div.send_keys(text)
    time.sleep(1)
    convert = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[text()='Convert']/parent::button",
            )
        )
    )
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    convert.click()
    time.sleep(5)
    console_logs = driver.get_log("browser")
    voice_url = [
        str(i["message"])[: str(i["message"]).find(".mp3") + 4]
        for i in console_logs
        if str(i["message"]).find(".mp3") != -1
        and str(i["message"]).find("en-US") == -1
    ]
    if len(voice_url) > 1:
        return False
    else:
        voice_url = str(voice_url)
    voice_url = voice_url[voice_url.find("https://storage") : len(voice_url) - 2]

    driver.get(voice_url)
    driver.implicitly_wait(5)

    loginBox = driver.find_element(By.XPATH, '//*[@id ="identifierId"]')
    loginBox.send_keys("email")

    nextButton = driver.find_element(By.XPATH, '//*[@id ="identifierNext"]')
    nextButton.click()
    driver.implicitly_wait(5)

    passWordBox = driver.find_element(
        By.XPATH, '//*[@id ="password"]/div[1]/div / div[1]/input'
    )
    passWordBox.send_keys("password")

    nextButton = driver.find_element(By.XPATH, '//*[@id ="passwordNext"]')
    nextButton.click()

    audio_url = wait.until(
        EC.presence_of_element_located(
            (
                By.TAG_NAME,
                "source",
            )
        )
    )
    audio_url = audio_url.get_attribute("src")
    response = requests.get(audio_url)

    if response.status_code == 200:
        with open(filePath, "wb") as file:
            file.write(response.content)

    driver.quit()


Narrate(
    "myAudio",
    "There is a person standing by a big red button that will make all human life disappear including their own. You have one minute to convince them not to. What do you say?",
)
