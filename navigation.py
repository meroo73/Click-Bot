import pyautogui as py
import time
import random

class SomeClass:
        # Expanded version of go_to_text('die letzten 6 Monaten ungewollt mehr als 5 kg')
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(0.3)
        py.write('Durchblutungsstörungen der Beine („Schaufensterkrankheit“, pAVK)')
        time.sleep(0.3)
        py.press("enter")
        time.sleep(0.5)
        py.press("esc")
        py.press("tab")
        py.press("right")
        #folgenden Aussagen    Welche der folgenden Aussagen bzgl. Ihrer Mobilität ist am besten zutreffend?*
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.2) 
        time.sleep(0.1)

        for choice in random.sample(range(8), random.randint(1, 9)):
            for _ in range(choice):
                 py.press('tab')
                 time.sleep(0.1)
            py.press("space")
            for _ in range(choice):
                # Instead of shift_tab()
                py.keyDown('shiftleft')
                py.press('tab')
                py.keyUp('shiftleft')
        time.sleep(0.8)
        py.hotkey('ctrl', 'f')
        time.sleep(0.3)
        #Magen-/Darmerkrankungen 
        py.write('Magen-/Darmerkrankungen ')
        time.sleep(0.3)
        py.press("enter")
        time.sleep(0.5)
        py.press("esc")
        py.press("tab")
        py.press("right")
        for choice in random.sample(range(12), random.randint(1, 13)):
            for _ in range(choice):
                 py.press('tab')
                 time.sleep(0.1)
            py.press("space")
            for _ in range(choice):
                # Instead of shift_tab()
                py.keyDown('shiftleft')
                py.press('tab')
                py.keyUp('shiftleft')



# To run the code
some_instance = SomeClass()
some_instance.some_method()






# time.sleep(1)
# py.scroll(-500)
# py.click(x=747, y=330)
# py.press('tab')
# py.press('right')

# for _ in range(5):
#     py.hotkey('ctrl', '-')
# time.sleep(0.3)
# time.sleep(0.5)

# py.scroll(+800)



# py.click(x=675, y=426)
# py.press('tab')
# py.press('right')
# py.press('right')
# time.sleep(0.5)
# py.press('tab')
# py.press('right')


# py.hotkey('ctrl', 'f')
# time.sleep(1)
# search_word = "Wie würden Sie Ihren Gesundheitszustand"
# py.write(search_word)
# time.sleep(1)
# py.press("esc")
# py.press('tab')

# # Generiere eine zufällige Zahl zwischen 1 und 5
# num_down_presses = random.randint(1, 5)

# # Drücke die 'down'-Taste die zufällige Anzahl von Malen
# for _ in range(num_down_presses):
#     py.press('down') 
#     time.sleep(0.4)

# py.press('tab')

# # Generiere eine zufällige Zahl zwischen 1 und 5
# num_down_presses = random.randint(1, 5)

# # Drücke die 'down'-Taste die zufällige Anzahl von Malen
# for _ in range(num_down_presses):
#     py.press('down') 
#     time.sleep(0.4)
# pass




# py.press('tab')
# py.press('right') 
# py.scroll(-500)
# py.scroll(+200)
# # time.sleep(1.2)
# # py.scroll(+828)
# # py.click(x=432, y=557)
# # time.sleep(1)
# # py.click(x=491, y=810)
# # py.press('tab')
# # py.press('right') 
# # py.press('right')




# time.sleep(1)

# py.moveTo(x=459,y=882)




# Wait for the website to load
# time.sleep(5)


# # Press Ctrl + F to open the browser's search box
# py.hotkey('ctrl', 'f')

# # Wait for the find box to appear
# time.sleep(1)

# # Type the word you're searching for
# search_word = " schon mal eine Thrombose"
# py.write(search_word)
# time.sleep(1)
# py.press("esc")
# py.press("tab")
# py.press("right")


# Press Enter to initiate the search
# time.sleep(1.2)
# py.scroll(+828)

# py.scroll(-828)
# py.click(x=472, y=438)
# time.sleep(1)
# py.click(x=470, y=557)
# py.press('tab')
# py.press('right') 
# py.press('right')

