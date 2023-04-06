from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#部員名簿のファイル名を入力する
print("ファイル名を入力してください")
file_name = input()
file_path = f"C:\\Users\\×××××\\Desktop\\{file_name}"

# 土曜日の最初の日にちを入力する
print("活動申請をする月を教えてください。")
month = int(input())
print("最初の土曜日の日付を入力してください。")
day = int(input())
print(f"活動申請するのは{month}月{day}日です。")

while day < 31:
  # GoogleChromeを立ち上げる
  browser = webdriver.Chrome('chromedriver.exe')

  #活動申請のサイトを立ち上げる
  browser.get("https://area31.smp.ne.jp/area/p/nbka0pitgp5lgrend3/76ijkd/login.html")

  # 活動申請するページにログインする
  browser.find_element_by_name("SMPID").send_keys("部活動のID")
  browser.find_element_by_name("SMPPASSWORD").send_keys("パスワード")
  browser.find_element_by_class_name("submit").click()

  #活動申請Aをクリックする
  elem = browser.find_element_by_xpath('//div[@class="menu"][text()="活動申請A"]')
  elem.click()

  #活動申請をする
  browser.find_element_by_name("numberID").send_keys("学籍番号")
  browser.find_element_by_name("applicationName").send_keys("名前")
  browser.find_element_by_name("emailAddress").send_keys("メールアドレス")
  browser.find_element_by_name("emailAddress:cf").send_keys("メールアドレス")
  textarea = browser.find_element_by_name('actOverview')
  textarea.send_keys('練習')

  #学外からの車両入構者
  textarea = browser.find_element_by_name('Vehicle')
  textarea.send_keys('なし')


  #活動場所
  select_box = Select(browser.find_element_by_name("reserveFac1"))
  select_box.select_by_value("21")


  textarea = browser.find_element_by_name('Adjustment')
  textarea.send_keys('なし')

  browser.find_element_by_name("hopeDate:y").send_keys("2023")
  browser.find_element_by_name("hopeDate:m").send_keys(f"{month}")
  browser.find_element_by_name("hopeDate:d").send_keys(f"{day}")

  browser.find_element_by_name("hopeTimeStart:hh").send_keys("8")
  browser.find_element_by_name("hopeTimeStart:mm").send_keys("00")

  browser.find_element_by_name("hopeTimeEnd:hh").send_keys("10")
  browser.find_element_by_name("hopeTimeEnd:mm").send_keys("00")

  browser.find_element_by_name("MenParticipants").send_keys("14")
  browser.find_element_by_name("MisParticipants").send_keys("7")

  browser.find_element_by_name("attendName").send_keys("なし")

  radio_buttons = WebDriverWait(browser, 10).until(
      EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".radio.cf input[type='radio']"))
  )
  radio_buttons[1].click()

  #ファイルアップロードの要素を取得する
  file_input = browser.find_element_by_name("f013346165")

  #ファイルをアップロードする(ファイルパスを人によって、変える必要あり)
  file_input.send_keys(file_path)

  #確認画面へ
  submit_button = browser.find_element_by_css_selector('.submit.redirection')
  submit_button.click()

  #送信ボタンをクリックする
  submit_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][name='submit']")))
  submit_button.click()

  browser.quit()
  day += 7





