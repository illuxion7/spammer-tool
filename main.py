import pyautogui
import time


print('''


\t\t\t\t   ______                 __ 
\t\t\t\t  / ____/______  ______  / /_
\t\t\t\t/ /   / ___/ / / / __ \/ __/
\t\t\t\t/ /___/ /  / /_/ / /_/ / /_  
\t\t\t\t\____/_/   \__, / .___/\__/  Spammer v1.0
\t\t\t\t          /____/_/           

''')

spam_msg = input('> Enter the spam message : ')
delay = input('> Enter spam delay : ')
times = input('> How many times do you want to execute the spam :  ')

print('> Executing the spam in 7 seconds...')
time.sleep(7)

for i in range (int(times)):
    pyautogui.write(spam_msg)
    pyautogui.press('enter')
    time.sleep(int(delay))
    print(f'> ({i}) [SUCCESS] message sent')


print('Spam executed successfully \n CryptSpammer ; Dev - github.com/illuxion7 ; discord - illuxion7#0777 , ')
