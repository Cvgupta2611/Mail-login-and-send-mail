from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep

# setting options
opts = Options()
# setting headless false explicitly that is the defualt behaviour of selenium
opts.headless = False

# loading the chrome driver
driver = Chrome(options=opts, executable_path='/Users/demon/Downloads/chromedriver')

try:
    # opening the login url
    driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    # prompting the user for email
    driver.execute_script("var a = prompt('Enter your mail id', 'abc@gmail.com');document.body.setAttribute('user-manual-input', a)")
    # giving user 20 seconds so that he can easily insert the email
    sleep(20)
    # capturing the email id entered by the end user
    email_id = driver.find_element_by_tag_name('body').get_attribute('user-manual-input')  
    #  capturing the input field for email on the page using xpath of the same
    email_box = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    # entring the user input email in the email field
    email_box.send_keys(email_id)
    # capturing the next button using it's xpath
    email_box = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span/span")
    # clicking the next button
    email_box.click()
    # giving a span of 30 seconds such that if a re-captcha is there user have enough time to fill that
    sleep(30)
    
    
    # till this time email is entered and password page is prompted
    # showing a prompt to user for entering the password of the corresponding email
    driver.execute_script("var a = prompt('Enter your Password', 'password');document.body.setAttribute('user-password-input', a)")
    # capturing the password entered by end user
    email_password = driver.find_element_by_tag_name('body').get_attribute('user-password-input')  
    # capturing the user password input field using xpath
    email_box = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    # entring the password given by end user into password field
    email_box.send_keys(email_password)
    # capturing the next button using xpath
    email_box = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span/span")
    # clicking the next button
    email_box.click()
    # giving 10 seconds to load next page
    sleep(10)



    # till this time login is done
    
    # prompting the user for to, subject and mail body
    driver.execute_script("var a = prompt('Enter mail id you want to send E-mail', 'to@gmail.com');document.body.setAttribute('mail-to-input', a);var b = prompt('Enter your mail subject', 'sample subject');document.body.setAttribute('mail-subject-input', b);var c = prompt('Enter your mail body', 'sample body');document.body.setAttribute('mail-body-input', c)")
    # giving user 40 seconds so that he can easily insert the asked data
    sleep(40)

    # capturing the email_to entered by the end user
    email_to = driver.find_element_by_tag_name('body').get_attribute('mail-to-input')  
    # capturing the email_subject entered by the end user
    email_subject = driver.find_element_by_tag_name('body').get_attribute('mail-subject-input')  
    # capturing the email_body entered by the end user
    email_body = driver.find_element_by_tag_name('body').get_attribute('mail-body-input')    
    # capturing compose mail button
    send_button = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div")
    # clicking compose mail button
    send_button.click()
    #  capturing the email to field on the page using xpath of the same
    email_to_input = driver.find_element_by_xpath("/html/body/div[17]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[2]")
    # clicking the email to field to make it editable
    email_to_input.click()
    # entring the email to
    email_to_input.send_keys(email_to)
    #  capturing the input field for email subject on the page using xpath of the same
    email_subject_input = driver.find_element_by_xpath("/html/body/div[17]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/div/input")
    # entring the email subject
    email_subject_input.send_keys(email_subject)
    #  capturing the email body field for email on the page using xpath of the same
    email_body_input = driver.find_element_by_xpath("/html/body/div[17]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div")
    # clicking the div to make it editable
    email_body_input.click()
    # entring the user mail body
    email_body_input.send_keys(email_body)
    # capturing the send button using it's xpath
    send_button = driver.find_element_by_xpath("/html/body/div[17]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]")
    # clicking the send button
    send_button.click()
    # giving a span of 30 seconds such that mail is succesfully sent
    sleep(30)
    
    


finally:
    # close the chrome window once the mail is sent
    driver.quit()