import pyautogui as py 
import time
import random
from string import punctuation
set(punctuation)
import logging


class FormAutomation:
    def __init__(self, index): #index für wiederholung
        self.name = f"Testnachname{index}"
        self.vorname = "TESTMANN"
        self.geburtsdatum = "16011990"
        self.email = "test@test.de"
        self.strasse = f"teststrasse{random.randint(1, 44)}"
        self.postleitzahl = self.generate_random_postleitzahl()
        self.wohnort = "TestStadt"
        self.telefon = "01794152504"
        self.gewicht = self.generate_random_gewicht()
        self.grosse = self.generate_random_grosse()
        self.Beruf = "Tester/-innen"
        self.geschlecht = random.choice(['weiblich', 'divers', 'männlich']) 
        self.index = index
        #Versichertendaten
        self.hausarzt ="TestMeinHausArzt"
        self.hausartzt_anchrift="HausartztStrasse"
        # self.Thrombose=self.generate_random_

    def start_automation(self):
        print(f"Start Variant num {self.index}")
        time.sleep(4)
        py.moveTo(x=619, y=600)
        py.click()

    def typewrite_with_delay(self, text, min_delay=0.05, max_delay=0.1):
        delay = random.uniform(min_delay, max_delay)
        py.typewrite(text, interval=delay)

    def generate_random_postleitzahl(self):
        postleitzahl = random.randint(38678, 77344)
        return str(postleitzahl).zfill(5)

    def generate_random_gewicht(self):
        gewicht = random.randint(30, 230)
        return str(gewicht)

    def generate_random_grosse(self):
        grosse = random.randint(120, 230)
        return str(grosse)



    def run(self):
        self.start_automation()
        self.fill_personal_daten()
        self.select_geschlecht()
        self.gender_specific_methods()


    def fill_personal_daten(self):
        py.write(self.name)
        py.press('tab')
        py.write(self.vorname)
        py.press('tab')
        py.write(self.geburtsdatum)
        py.press('tab')

        py.press('tab')
        time.sleep(2.2)
         # Tippe den Vornamen erneut ein und fülle das E-Mail-Feld aus
        self.typewrite_with_delay(self.vorname)
        py.hotkey('altright', 'q') # Benutze Alt+Q, um die Domain auszufüllen
        self.typewrite_with_delay('zotzklimas.de')
        py.press('tab')
         # Fülle die E-Mail-Adresse zweite mal
        self.typewrite_with_delay(self.vorname)
        py.hotkey('altright', 'q') # Benutze Alt+Q, um die Domain auszufüllen
        self.typewrite_with_delay('zotzklimas.de')

    def select_geschlecht(self):
        py.press('tab')
        time.sleep(1)
        print(f"Selected Geschlecht: {self.geschlecht}")

        if self.geschlecht == 'weiblich':
            time.sleep(0.5)
            py.press('right')
        elif self.geschlecht == 'divers':
            time.sleep(0.5)
            py.press('right')
            time.sleep(0.5)
            py.press('right')
        elif self.geschlecht == 'männlich':
            time.sleep(0.5)
            py.press('right')
            time.sleep(0.5)
            py.press('right')
            time.sleep(0.5)
            py.press('right')

        time.sleep(1)
        py.press('tab')
        py.press('enter')

    def gender_specific_methods(self):
        if self.geschlecht == 'weiblich':
            weiblich = Weiblich(self)
            weiblich.handle_all()
        elif self.geschlecht == 'divers':
            divers = Divers(self)
            divers.handle_all()
        elif self.geschlecht == 'männlich':
            männlich = Männlich(self)
            männlich.handle_all()
    
    time.sleep(0.5) 
    #BLUTGRUPPE 
    def select_blutgruppe(self, index):
        
        # BLUTGRUPPE MIT index 
        blood_type_position = index % 5

        if blood_type_position == 1:
            py.press('right')  # Select B
            logging.info("Blutgruppe: B")
        elif blood_type_position == 2:
            py.press('right')  # 2x für AB
            time.sleep(0.2)
            py.press('right')
            logging.info("Blutgruppe: AB")
        elif blood_type_position == 3:
            py.press('right')  # 3x Right Für O
            time.sleep(0.2)
            py.press('right')
            time.sleep(0.2)
            py.press('right')
            logging.info("Blutgruppe: O")
        elif blood_type_position == 4:
            py.press('right')  # 4x für Unklar
            time.sleep(0.2)
            py.press('right')
            time.sleep(0.2)
            py.press('right')
            time.sleep(0.2)
            py.press('right')
            logging.info("Blutgruppe: Unklar")
        elif blood_type_position == 0:
            py.press('right')  # 5x für A
            time.sleep(0.2)
            py.press('right')
            time.sleep(0.2)
            py.press('right')
            time.sleep(0.2)
            py.press('right')
            time.sleep(0.2)
            py.press('right')
            logging.info("Blutgruppe: A")

        time.sleep(0.4)  # 
    
        


class Männlich:
    
    def __init__(self, form_automation):
        self.form_automation = form_automation
        self.thrombose_monat = self.generate_random_monat_thrombose()  
        self.thrombose_jahr = self.generate_random_jahr_thrombose()
        self.dose= self.generate_random_dose()

    def fill_form(self):
        print("Formular für 'männlich' ausfüllen")

    def handle_all(self):
        self.fill_personal_daten()
        self.Versichertendaten()
        self.vorstellungsgrund()
        self.thrombose_lungenembolie()
        self.thrombose_lungenembolie_2()
        self.thrombose_lungenembolie_3()
        self.thrombose_lungenembolie_4()
        self.thrombose_lungenembolie_5()
        self.thrombose_lungenembolie_6()
        self.blutungsneigung()
        self.wundheilung()
        self.familienanamnese()
        self.familienanamnese_2()
        self.test()
        self.familienanamnese_3()
        self.familienanamnese_4()
        self.operationen()
        self.medikamente()
        self.allergien()
        self.allgemeiner_gesundheitszustand()
        self.akute_infekte()
        self.infektneigung()
        self.infektionskrankheiten()
        self.chronische_krankheiten()
        self.chronische_krankheiten_2()
        self.chronische_krankheiten_3()
        self.chronische_krankheiten_4()
        self.tumor_krebserkrankung()
        self.gewichtsverlust_migraene()
        self.rauchverhalten()
        self.alkoholkonsum()
        

    def typewrite_with_delay(self, text, min_delay=0.05, max_delay=0.1):
        delay = random.uniform(min_delay, max_delay)
        py.typewrite(text, interval=delay)

    def generate_random_monat_thrombose(self):
        thrombose_monat = random.randint(1, 12)
        return str(thrombose_monat)

    def generate_random_jahr_thrombose(self):
        thrombose_jahr = random.randint(1999, 2023)
        return str(thrombose_jahr)
    
    def generate_random_dose(self):
        dose = random.randint(50, 1000)
        return str(dose)
    
    def fill_personal_daten(self):
        for _ in range(5):
            py.press('tab')
        time.sleep(0.3)
        py.write(self.form_automation.strasse)
        py.press('tab')
        time.sleep(0.3)

        py.write(self.form_automation.postleitzahl)
        time.sleep(0.3)
        py.press('tab')
        py.write(self.form_automation.wohnort)
        py.press('tab')
        py.write(self.form_automation.telefon)

        for _ in range(2):
            py.press('tab')

        py.write(self.form_automation.gewicht)
        py.press('tab')
        self.typewrite_with_delay(self.form_automation.grosse)
        py.press('tab')

        self.form_automation.select_blutgruppe(self.form_automation.index)
        py.press('tab')
        # Beruf
        py.write(self.form_automation.Beruf)
        py.press('tab')


    def Versichertendaten(self):
        py.press('right')
        py.press('right')
        py.moveTo(x=400, y=750)
        py.click()
        for _ in range(5):
            py.press('tab')

    def vorstellungsgrund(self):
        """
        Randomly selects between the 'Vorstellungsgrund' options and interacts with the corresponding sub-options.
        """
        # Define the main 'Vorstellungsgrund' options with their coordinates
        vorstellungsgrund_warum_options = [
            ('Auffälligkeiten/Ereignisse in der Familie', (455, 567)),
            ('Auffälligkeiten Vorgeschichte', (497, 621))
            # ('letzte option', (432, 677)) #sonsitige
        ]

        # Randomly choose one of the options
        selected_option = random.choice(vorstellungsgrund_warum_options)
        option_name, (x, y) = selected_option

        # Click the selected option
        print(f"Selected Vorstellungsgrund Warum option: {option_name}")
        py.moveTo(x, y)
        py.click()
        time.sleep(0.5)

        # Handle sub-options based on the selected option
        if option_name == 'Auffälligkeiten/Ereignisse in der Familie':
            self.handle_sub_options_auffaelligkeiten_familie()

        elif option_name == 'Auffälligkeiten Vorgeschichte':
            self.handle_sub_options_auffaelligkeiten_vorgeschichte()
        
        # elif option_name == 'letzte option':
        #     self.handle_main_sonstiges()

    # def handle_main_sonstiges(self):
    #     """
    #     Handles the main 'Sonstiges' option. After selecting it, it will enter the text "Main hi sonstiges".
    #     """
    #     # Scroll to ensure visibility
    #     py.scroll(-400)

    #     # Click on the main 'Sonstiges' option
    #     py.moveTo(432, 677)  # Coordinates for main 'Sonstiges'
    #     py.click()
    #     time.sleep(0.8)

        # # Press 'tab' and write the text "Main hi sonstiges"
        # py.press('tab')
        # time.sleep(1)
        # py.write("Main hi sonstiges")
        # time.sleep(1)    # You can add logic for 'Sonstiges' if necessary

    def handle_sub_options_auffaelligkeiten_familie(self):
        """
        Handles sub-options under 'Auffälligkeiten in der Familie'.
        """
        # Scroll to reveal the sub-options
        py.scroll(-400)

        # Define sub-options with coordinates
        auffaelligkeiten_familie_sub_options = [
            ('Thromboseneigung in der Familie', (525, 542)),
            ('Herzinfarkte/Schlaganfälle in der Familie', (487, 601)),
            ('Gefäßverschlüsse in der Familie', (488, 658)),
            ('Faktor-V-Leiden in der Familie', (481, 717)),
            ('Blutungsneigung in der Familie', (482, 774))
            # ('Sonstiges in der Familie', (482, 829))
        ]

        # Randomly select and click a sub-option
        selected_sub_option = random.choice(auffaelligkeiten_familie_sub_options)
        sub_option_name, (x, y) = selected_sub_option

        print(f"Selected sub-option: {sub_option_name}")
        py.moveTo(x, y)
        py.click()
        time.sleep(0.5)

    
    def handle_sub_options_auffaelligkeiten_vorgeschichte(self):
        """
        Handles sub-options under 'Auffälligkeiten in der Vorgeschichte'.
        """
        # Scroll to reveal the sub-options
        py.scroll(-850)
        # Define sub-options with coordinates
        auffaelligkeiten_vorgeschichte_sub_options = [
            ('Thrombosen', (457, 167)),
            ('Schlaganfall/Hirninsult/Herzinfarkt', (457, 223)),
            ('Dauer der Blutverdünnung', (457, 286)),
            ('unklare aPTT-Verlängerung', (457, 341)),
            ('unklare Quickverminderung', (457, 399)),
            ('Blutungsneigung', (457, 452)),
            ('von-Willebrand-Syndrom', (457, 508)),
            ('Plättchenfunktionsstörung', (457, 567)),
            ('zu wenige Blutplättchen', (457, 629)),
            ('zu viel Blutplättchen', (457, 685))
            # ('zu viele rote Blutkörperchen', (457, 742)),
            # ('zu viele weiße Blutkörperchen', (457, 802)),
            # ('Infektneigung/Immundefekt', (457, 860)),
            # ('last option', (457, 918))
        ]

        # Randomly select and click a sub-option
        selected_sub_option = random.choice(auffaelligkeiten_vorgeschichte_sub_options)
        sub_option_name, (x, y) = selected_sub_option

        print(f"Selected sub-option: {sub_option_name}")
        py.moveTo(x, y)
        py.click()
        time.sleep(0.5)

    # def handle_sub_options_vieleRote(self):
    #     pass
    # def handle_sub_options_vieleWeise(self):
    #     pass
        # if sub_option_name == 'last option':
        #     self.handle_sub_options_sonstiges()

    # def handle_sub_options_sonstiges(self):
    #     """
    #     Handles the 'Sonstiges' sub-option. After selecting it, it will enter the text "hi sonstiges".
    #     """
    #     time.sleep(1)
    #     py.press('tab')
    #     py.write("hi sonstiges")
    #     time.sleep(1)


    #Haben Sie schon mal eine Thrombose, Lungenembolie
    def thrombose_lungenembolie(self):

        py.scroll(+10000)
        time.sleep(1)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = " schon mal eine Thrombose"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press("right")
        py.press('tab')
        py.write(self.thrombose_monat)
        py.press('tab')
        py.write(self.thrombose_jahr)
        py.press('tab')
        py.scroll(-822)

        # Define Group A options (with sub-options)
        group_a_options = [
            ('Oberflächlich', (459, 124)),
            ('Tiefe Beinvenenthrombose', (459, 186)),
            ('Lungenarterienembolie', (459, 243)),
            ('Muskelvenenthrombose', (459, 300)),
            ('Schlüsselbeinvenenthrombose', (459, 358)),
            ('Halsgefäß-/Jugularisthrombose', (459, 418)),
            ('Armvenenthrombose', (459, 475)),
            ('ZVK-/Katheterthrombose', (459, 533)),
            ('Sinusvenenthrombose/Hirnvene', (459, 593)),
            ('Ereignis am Auge', (459, 939)),
        ]

        # Define Group B options (no sub-options, multiple selections allowed)
        group_b_options = [
            ('Mesenterialvenenthrombose', (459, 675)),
            ('Pfortader', (459, 710)),
            ('Lebervenenverschluss', (459, 767)),
            ('Milzin', (459, 821)),
            ('Arterieler', (459, 884))
        ]

        # Define Group C ('Weiß ich nicht', exclusive option)
        group_c_option = ('Weiß ich nicht', (459, 999))

        # Track selected main options
        selected_main_options = []
        sub_option_candidates = []  # Only Group A options will be added here

        # Adjust the probability so that 'Weiß ich nicht' is less likely to be chosen
        option_pool = ['A'] * 4 + ['C']  # 4x chance of selecting from Group A, 1x chance of selecting 'Weiß ich nicht'
        selected_group = random.choice(option_pool)

        if selected_group == 'C':
            # If 'Weiß ich nicht' is selected, only select this option and return
            print(f"Selected Group C option: {group_c_option[0]}")
            py.moveTo(group_c_option[1])
            py.click()
            return  # Skip any other selections and sub-options

        # If Group A is selected
        selected_a_option = random.choice(group_a_options)
        a_option_name, (a_x, a_y) = selected_a_option

        # Click the selected Group A option
        print(f"Selected Group A option: {a_option_name}")
        py.moveTo(a_x, a_y)
        py.click()
        time.sleep(0.5)

        # Add Group A option to sub-option candidates
        sub_option_candidates.append(a_option_name)
        selected_main_options.append(a_option_name)

        # Select multiple Group B options (randomly)
        selected_b_options = random.sample(group_b_options, random.randint(1, len(group_b_options)))
        for b_option_name, (b_x, b_y) in selected_b_options:
            print(f"Selected Group B option: {b_option_name}")
            py.moveTo(b_x, b_y)
            py.click()
            time.sleep(0.5)
            selected_main_options.append(b_option_name)

        # Now handle sub-options after main option selection
        self.handle_selected_sub_options(sub_option_candidates)

    def handle_selected_sub_options(self, sub_option_candidates):
        """
        Handles sub-options for selected Group A options after main options are selected.
        """
        for option in sub_option_candidates:
            if option == 'Oberflächlich':
                self.handle_sub_options_oberflächlich()
            elif option == 'Tiefe Beinvenenthrombose':
                self.handle_sub_options_tiefe_beinvenenthrombose()
            elif option == 'Lungenarterienembolie':
                self.handle_sub_options_lungenarterienembolie()
            elif option == 'Muskelvenenthrombose':
                self.handle_sub_options_muskelvenenthrombose()
            elif option == 'Schlüsselbeinvenenthrombose':
                self.handle_sub_options_schlüsselbeinvenenthrombose()
            elif option == 'Halsgefäß-/Jugularisthrombose':
                self.handle_sub_options_halsgefaess_jugularisthrombose()
            elif option == 'Armvenenthrombose':
                self.handle_sub_options_armvenenthrombose()
            elif option == 'ZVK-/Katheterthrombose':
                self.handle_sub_options_zvk_katheterthrombose()
            elif option == 'Sinusvenenthrombose/Hirnvene':
                self.handle_sub_options_sinusvenenthrombose()
            elif option == 'Ereignis am Auge':
                self.handle_sub_options_ereignis_am_auge()

    # Example sub-option handlers for Group A
    def handle_sub_options_oberflächlich(self):
        print("Handling sub-options for 'Oberflächlich'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=472, y=438)
        time.sleep(1)
        py.click(x=588, y=713)
        py.press('tab')
        py.press('right') 

    def handle_sub_options_tiefe_beinvenenthrombose(self):
        print("Handling sub-options for 'Tiefe Beinvenenthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=472, y=438)
        time.sleep(1)
        py.click(x=491, y=810)
        py.press('tab')
        py.press('right') 

    def handle_sub_options_lungenarterienembolie(self):
        print("Handling sub-options for 'Lungenarterienembolie'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')   
        


    def handle_sub_options_muskelvenenthrombose(self):
        print("Handling sub-options for 'Muskelvenenthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')   
        py.press('right')  
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

    def handle_sub_options_schlüsselbeinvenenthrombose(self):
        print("Handling sub-options for 'Schlüsselbeinvenenthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

    def handle_sub_options_halsgefaess_jugularisthrombose(self):
        print("Handling sub-options for 'Halsgefäß-/Jugularisthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

    def handle_sub_options_armvenenthrombose(self):
        print("Handling sub-options for 'Armvenenthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

    def handle_sub_options_zvk_katheterthrombose(self):
        print("Handling sub-options for 'ZVK-/Katheterthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

    def handle_sub_options_sinusvenenthrombose(self):
        print("Handling sub-options for 'Sinusvenenthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

    def handle_sub_options_ereignis_am_auge(self):
        print("Handling sub-options for 'Ereignis am Auge'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=462, y=734)
        time.sleep(1)


    #Wie wurde am Ende behandelt?*
    def thrombose_lungenembolie_2(self):
        py.scroll(+10000)
        time.sleep(1.3)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = " wurde am Ende"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.scroll(-300)

        #behandlung Options
        behandlung_options = [
            ('Heparinspritzen/Clexane/Innohep usw.', (424, 364)),
            ('Marcumar/Phenprogramm/Coumadin/Sinthrom', (422, 423)),
            ('Xarelto', (417, 479)),
            ('Eliquis', (415, 537)),
            ('Lixiana', (412, 594)),
            ('Pradaxa', (410, 651)),
        ]

        # Define the exclusive options with their coordinates
        exclusive_options = [
            ('Ich habe weder Tabletten', (442, 715)),
            ('weiß ich nicht', (436, 770))
        ]

        # Decide whether to select an exclusive option (20% chance) or non-exclusive options (80% chance)
        if random.randint(1, 5) == 1:
            # 20% chance to select an exclusive option
            selected_option = random.choice(exclusive_options)
            selected_options = [selected_option]
            print(f"Exclusive selection: {selected_option[0]}")
        else:
            # 80% chance to select one or more non-exclusive options
            num_options = random.randint(1, len(behandlung_options))  # At least 1 option
            selected_options = random.sample(behandlung_options, num_options)
            print(f"Selecting options: {[opt[0] for opt in selected_options]}")

        # Click on the selected options
        for option_name, (x, y) in selected_options:
            print(f"Selecting option: {option_name}")
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)  # Slight delay between clicks if multiple options

        time.sleep(1)
        # py.click(x=477, y=971)
        py.scroll(-400)
        py.click(x=463, y=524)
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 7)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        time.sleep(0.2)


         
         
    
       

    #RESET BILDSHRIM
    def reset_view_to_normal(self):
        """
        Resets the view by scrolling up and zooming the screen back to its normal size.
        """
        # Scroll up to bring the view back
        py.scroll(-850) # You can adjust this scroll amount based on your specific need
        
        # Zoom back to normal size
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)

        time.sleep(0.5)  # Small delay to ensure the changes are registered
    #Gab es maximal 3 Monate vor dem Ereignis Risikofaktoren
    def thrombose_lungenembolie_3(self):

        # Adjust the view
        py.scroll(-900)
        py.hotkey('ctrl', '-')
        time.sleep(0.3)
        py.hotkey('ctrl', '-')
        time.sleep(0.3)
        py.hotkey('ctrl', '-')
        time.sleep(0.3)
        py.hotkey('ctrl', '-')
        time.sleep(0.3)
        py.hotkey('ctrl', '-')

        # Define Option 1 (Single selection)
        option_1 = [
            ('Kein Auslöser bekannt', (712, 292)),
            ('Krankheitsaktivität', (690, 734)),
            ('Chronische Polyarthitis', (687, 762)),
            ('Nephrotisches Syndrom', (686, 791)),
            ('Sichelzellanämie', (684, 819)),
            ('Intravenöser', (684, 848)),
            ('Herzinfarkt', (685, 935))
        ]

        # Define Option 2 (Single selection with follow-up action)
        option_2 = [
            ('Krankenhausaufenthalt vor dem Ereignis', (681, 323)),
            # ('Gelenkinjektionen/Cortisonspritzen', (680, 440)),
            ('Chemotherapie', (688, 499)),
            ('Antibabypille mit Östrogen', (689, 558)),
            ('Medikamente wie Gerinnungsfaktoren', (689, 616))
        ]

        # Define Option 3 (Single selection with sub-options)
        option_3 = [
            ('Operationen', (678, 379)),
            # ('Unfall/Verletzung', (679, 411)),
            # ('Schwangerschaft', (686, 676)),
            # ('Wochenbett', (688, 702)),
            ('Immobilisation', (682, 879)),
            ('Infektion', (688, 905)),
            ('Reise', (681, 965)),
            ('Ungewohnte', (678, 994))
        ]

        # Randomly choose one of the three option groups
        selected_group = random.choice([1, 2, 3])
        selected_option = None

        if selected_group == 1:
            # Select one option from Option 1
            selected_option = random.choice(option_1)
            option_name, (x, y) = selected_option
            print(f"Selected Option 1: {option_name}")
            py.moveTo(x, y)
            py.click()
            self.reset_view_to_normal()

        elif selected_group == 2:
            # Select one option from Option 2 and perform follow-up actions
            selected_option = random.choice(option_2)
            option_name, (x, y) = selected_option
            print(f"Selected Option 2: {option_name}")
            py.moveTo(x, y)
            py.click()

            # Follow-up action
            py.press('tab')
            py.write("hi test")
            self.reset_view_to_normal()

        elif selected_group == 3:
            # Select one option from Option 3 and handle sub-options
            selected_option = random.choice(option_3)
            option_name, (x, y) = selected_option
            print(f"Selected Option 3: {option_name}")
            py.moveTo(x, y)
            py.click()

            # Handle sub-options for Option 3
            self.handle_sub_options(option_name)

    def handle_sub_options(self, option_name):
        """
        Handles the sub-options for Option 3.
        """
        print(f"Handling sub-options for '{option_name}'")

        if option_name == 'Operationen':
            self.handle_operationen_sub_options()
        elif option_name == 'Unfall/Verletzung':
            self.handle_unfall_sub_options()
        elif option_name == 'Schwangerschaft':
            self.handle_schwangerschaft_sub_options()
        elif option_name == 'Wochenbett':
            self.handle_wochenbett_sub_options()
        elif option_name == 'Immobilisation':
            self.handle_immobilisation_sub_options()
        elif option_name == 'Infektion':
            self.handle_infection_sub_options()
        elif option_name == 'Reise':
            self.handle_reise_sub_options()
        elif option_name == 'Ungewohnte':
            self.handle_ungewohnte_sub_options()

    # Define placeholder methods for the sub-options in Option 3

    def handle_operationen_sub_options(self):
        print("Handling sub-options for 'Operationen'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)

    
        # Definiere die Operationsoptionen mit ihren Koordinaten in aufsteigender Reihenfolge
        operation_options = [
            ('Knochenbrüche', (442, 581)),
            ('Hüft-/Kniegelenksoperation', (439, 641)),
            ('Bauchoperation', (449, 699)),
            ('Sonstiges', (431, 757))  # Sonstiges ist die letzte Option
        ]
        
        # Wähle zufällig aus, wie viele Optionen ausgewählt werden (1 bis alle)
        num_options_to_select = random.randint(1, len(operation_options))
        
        # Wähle zufällig Optionen aus (eine oder mehrere), aber in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(operation_options, num_options_to_select), key=lambda x: operation_options.index(x))
        
        # Klicke auf jede ausgewählte Option in der Reihenfolge und prüfe, ob "Sonstiges" dabei ist
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)  
            
            # Wenn "Sonstiges" ausgewählt wurde, führe eine zusätzliche Aktion aus
            if option_name == 'Sonstiges':
                py.press('tab')
                py.write('hola sonstiges')


        

    def handle_unfall_sub_options(self):
        # print("Handling sub-options for 'Unfall/Verletzung'")
        # time.sleep(1)
        # py.scroll(-850)
        # for _ in range(5):
        #     py.hotkey('ctrl', '+')
        #     time.sleep(0.3)
        # time.sleep(0.5)
        # py.click(x=443, y=584)
       pass

    # def handle_schwangerschaft_sub_options(self):
    #     print("Handling sub-options for 'Schwangerschaft'")
    #     time.sleep(1)
        
    #     for _ in range(5):
    #         py.hotkey('ctrl', '+')
    #         time.sleep(0.3)
    #     py.scroll(-1350)
    #     time.sleep(0.5)

    #         # Definiere die Schwangerschaftsoptionen mit ihren Koordinaten
    #     schwangerschaft_options = [
    #         ('in welcher Schwangerschaftswoche?', (464, 172)),
    #         ('bzw. wie viele Wochen nach der Fehlgeburt?', (457, 283)),
    #         ('Präeklampsie', (438, 398)),
    #         ('Schwangerschaftsvergiftung', (443, 454)),
    #         ('Gestose', (444, 511)),
    #         ('HELLP-Syndrom', (444, 571)),
    #         ('Geburtsgewicht <2500g', (446, 806)),  # Koordinaten für diese Option fehlen, angenommen!
    #         ('Hyperstimulationssyndrom', (456, 629)),
    #         ('Blutung', (461, 749)),
    #         ('Gewichtszunahme', (446, 806)),
    #         ('Unstillbares S', (448, 859)),
    #         ('Mehrlingsschwangerschaft', (467, 921))
    #     ]

    #     # Zufällige Anzahl von Optionen auswählen (1 bis alle)
    #     num_options_to_select = random.randint(1, len(schwangerschaft_options))
        
    #     # Wähle zufällig Optionen aus und sortiere sie in aufsteigender Reihenfolge
    #     selected_options = sorted(random.sample(schwangerschaft_options, num_options_to_select), key=lambda x: schwangerschaft_options.index(x))

    #     # Klicke jede ausgewählte Option in der Reihenfolge
    #     for option_name, (x, y) in selected_options:
    #         py.moveTo(x, y)
    #         py.click()
    #         time.sleep(0.5)

    #         # Wenn die erste oder zweite Option ausgewählt wird, eine zusätzliche Aktion ausführen
    #         if option_name == 'in welcher Schwangerschaftswoche?' or option_name == 'bzw. wie viele Wochen nach der Fehlgeburt?':
    #             py.press('tab')
    #             py.write('4')  # Beispiel für eine Ausgabe, hier '4' eingeben
    #             time.sleep(0.5)
    #         elif option_name == 'bzw. wie viele Wochen nach der Fehlgeburt?':
    #             py.press('tab')
    #             py.write('4')  # Beispielhafte Eingabe '4'
    #             time.sleep(0.5)


    def handle_wochenbett_sub_options(self):
        # print("Handling sub-options for 'Wochenbett'")
        # time.sleep(1)
        # py.scroll(-850)
        # for _ in range(5):
        #     py.hotkey('ctrl', '+')
        #     time.sleep(0.3)
        # time.sleep(0.5)
        # py.scroll(-200)
        # py.click(x=483, y=537)
        # py.press('tab')
        # for _ in range(5):
        #     py.press('right')
        # time.sleep(0.5)
        # py.press('tab')
        # py.press('right')
        # py.scroll(-200)

        # wochenbett_options = [
        #     ('Vermehrte Blutung', (495, 695)),
        #     ('Bluttransfusion', (475, 761)),
        #     ('Erneute Blutung', (475, 761)),
        #     ('Infektion', (463, 880))
        # ]
        
        # # Zufällige Anzahl von Optionen auswählen (1 bis alle)
        # num_options_to_select = random.randint(1, len(wochenbett_options))
        
        # # Optionen in aufsteigender Reihenfolge auswählen
        # selected_options = sorted(random.sample(wochenbett_options, num_options_to_select), key=lambda x: wochenbett_options.index(x))
        
        # # Klicken auf die ausgewählten Optionen
        # for option_name, (x, y) in selected_options:
        #     py.moveTo(x, y)
        #     py.click()
        #     time.sleep(0.5)
        pass

    def handle_immobilisation_sub_options(self):
        print("Handling sub-options for 'Immobilisation'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)
        py.click(x=483, y=537)
        py.press('tab')
        py.press('right')




    def handle_infection_sub_options(self):
        print("Handling sub-options for 'Infektion'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)
        py.scroll(-400)
        py.click(x=455, y=247)
        time.sleep(0.2)
        py.click(x=441, y=572)
        py.press('tab')
        py.press('right')
        py.press('tab')
        time.sleep(0.3)
        py.press('right')
        py.press('tab')
        py.write('7')

    def handle_reise_sub_options(self):
        print("Handling sub-options for 'Reise'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)
        py.click(x=756, y=566)
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 3)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)

    def handle_ungewohnte_sub_options(self):
        print("Handling sub-options for 'Ungewohnte'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)
        py.click(x=468, y=639)


    def thrombose_lungenembolie_4(self):
        py.scroll(+10000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Haben Sie eine weitere Thrombose/Embolie/Ereignis gehabt?"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press("right")
        py.press("right")
        pass

    def thrombose_lungenembolie_5(self):
        py.press('tab')
        py.press('right')
        py.scroll(-300)
        time.sleep(0.3)

        # Definiere die Venenerkrankung Optionen mit ihren Koordinaten
        venenerkrankung_options = [
            ('Besenreiser', (431, 684)),
            ('Krampfadern', (430, 741)),
            ('Venenentzündung/Phlebitis', (424, 799)),
            ('Posttrombotisches Syndrom', (434, 856)),
            ('Sonstige', (420, 914))  # Spezielle Behandlung für Sonstige
        ]

        # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        num_options_to_select = random.randint(1, len(venenerkrankung_options))

        # Wähle zufällige Optionen in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(venenerkrankung_options, num_options_to_select), key=lambda x: venenerkrankung_options.index(x))

        # Jede ausgewählte Option anklicken
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)

            # Wenn "Sonstige" ausgewählt wurde, zusätzliche Aktion ausführen
            if option_name == 'Sonstige':
                py.press('tab')
                py.write('hi sonstiges')
        

    def thrombose_lungenembolie_6(self):
        time.sleep(1)
        py.scroll(-300)
        time.sleep(0.3)
        py.click(x=586, y=862)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
                ##a
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        ##b
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        ##
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        ##
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
              ## c
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #c2
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #c3
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #c4
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

        #c5
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

    def blutungsneigung(self):
        #Nasenbluten
        py.press('tab')
        py.press('right')
        
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)

        #Blaue Flecken
        py.press('tab')
        py.press('down')
        py.press('down')
        py.press('down')
        time.sleep(0.2)
        py.press('down')
        py.press('down')
        time.sleep(0.2)

        # py.press('tab')
        # py.press('right')
        
        # py.moveTo(x=1020, y=750)
        # py.click()


        #Blutungneigung bei kleineren Verletzungen
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)

        #NBlutungen in der Mundhöhle
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        
        #Magen-Darm-Blutungen
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)          

        #Blut im Urin/Hämaturie
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)

        #Zähne ziehen/Zahnextraktion
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        

        #Chirurgische Eingriffe/Operationen
        py.press('tab')
        py.press('down')
        py.press('down')
        time.sleep(0.3)
        py.press('down')
        py.press('tab')
        py.write("hi")
        time.sleep(0.2)


        # #verstärkte Regelblutung/Hypermenorrhoe
        # py.press('tab')
        # # Generiere eine zufällige Zahl zwischen 1 und 3
        # num_down_presses = random.randint(1, 9)
        
        # # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        # for _ in range(num_down_presses):
        #     py.press('down')
        # time.sleep(0.2)

        # #Blutungen nach der Entbindung/Wochenbett
        # py.press('tab')
        # # Generiere eine zufällige Zahl zwischen 1 und 3
        # num_down_presses = random.randint(1, 5)
        
        # # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        # for _ in range(num_down_presses):
        #     py.press('down')
        # time.sleep(0.2)
        


        #Blutergüsse/Hämatome in Muskeln
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        time.sleep(0.2)

        #Blutergüsse/Hämatome in Gelenken
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 3)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        time.sleep(0.2)


        #Hirnblutungen
        py.press('tab')
        time.sleep(0.2)
        py.press('down')



        #andere Blutungsprobleme
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)


    def wundheilung(self):
        time.sleep(0.3)
        py.press('tab')
        py.press('right')
        time.sleep(0.4)
        py.press('tab')
        
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 3)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')


    def familienanamnese(self):
        time.sleep(1)
        py.scroll(+20000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Gibt es in Ihrer Familien folgende Erkrankungen?"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press("right")
        py.scroll(-300)
        #Blutarmut/Anämie/Thalassämie
        
        Blutarmut_options = [
            ('Blutarmut/Anämie ohne Ursache', (444, 550)),
            ('Blutarmut durch Eisenmangel', (434, 609)),
            ('Thalassämie', (434, 668)),
            ('Sichelzellanämie/SCD', (430, 730)),
            ('idk', (414, 785))   # Spezielle Behandlung für Sonstige
        ]

        # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        num_options_to_select = random.randint(1, len(Blutarmut_options))

        # Wähle zufällige Optionen in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(Blutarmut_options, num_options_to_select), key=lambda x: Blutarmut_options.index(x))

        # Jede ausgewählte Option anklicken
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)

            # Wenn "Sonstige" ausgewählt wurde, zusätzliche Aktion ausführen
            if option_name == 'idk':
                time.sleep(0.3)
                py.press('tab')
                py.write(' idk')

    def familienanamnese_2(self):
        time.sleep(1)
        py.scroll(-640)
        time.sleep(0.2)
        #thrombose in Familienanamese
        py.click(x=738, y=422)
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')
        py.press('right')
        #herzinfarkt/schalagenfall
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')
        py.press('right')
        py.scroll(-300)
        time.sleep(0.5)
        blutungsneigung_optionen = [
            ('von-Willebrand-Syndrom', (800, 627)),
            ('Fibrinogenmangel', (1205, 632)),
            ('Faktor-VII-Mangel', (457, 688)),
            ('Hämophilie A', (825, 690)),
            ('Hämophilie B', (1212, 690)),
            ('Faktor-X-Mangel', (435, 754)),
            ('Faktor-XI-Mangel', (821, 754)),
            ('Faktor-XII-Mangel', (1217, 754)),
            ('Plättchen', (461, 808))
        ]

        # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        num_options_to_select = random.randint(1, len(blutungsneigung_optionen))

        # Wähle zufällige Optionen in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(blutungsneigung_optionen, num_options_to_select), key=lambda x: blutungsneigung_optionen.index(x))

        # Jede ausgewählte Option anklicken
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
        #     time.sleep(0.5)


        # py.press('tab')
        # py.press('right')



    def test(self):



    #     time.sleep(0.5)
    #     # Optionen für "bei wem" mit Koordinaten
    #     bei_wem_options = [
    #         ('vater', (409, 441)),
    #         ('schwester', (412, 496)),
    #         ('mutter', (790, 443)),
    #         ('oma', (790, 557)),
    #         ('cousin', (796, 616)),
    #         ('tochter', (1190, 499))
    #     ]

    #     # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
    #     num_options_to_select = random.randint(1, len(bei_wem_options))

    #     # Wähle zufällige Optionen in aufsteigender Reihenfolge
    #     selected_options = sorted(random.sample(bei_wem_options, num_options_to_select), key=lambda x: bei_wem_options.index(x))

    #     # Jede ausgewählte Option anklicken
    #     for option_name, (x, y) in selected_options:
    #         py.moveTo(x, y)
    #         py.click()
    #         time.sleep(0.5)
         pass
        
    
    def familienanamnese_3(self):

        # py.scroll(-500)

        # thromboseereignisoptionen = [
        #     ('Beinvenenthrombose', (425, 164)),
        #     ('Lungenembolie', (429, 219)),
        #     ('Sonstiges', (429, 278))  # Spezielle Behandlung für Sonstiges
        # ]

        # # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        # num_options_to_select = random.randint(1, len(thromboseereignisoptionen))

        # # Wähle zufällige Optionen in aufsteigender Reihenfolge
        # selected_options = sorted(random.sample(thromboseereignisoptionen, num_options_to_select), key=lambda x: thromboseereignisoptionen.index(x))

        # # Jede ausgewählte Option anklicken
        # for option_name, (x, y) in selected_options:
        #     py.moveTo(x, y)
        #     py.click()
        #     time.sleep(0.5)

        #     # Wenn "Sonstiges" ausgewählt wurde, zusätzliche Aktion ausführen
        #     if option_name == 'Sonstiges':
        #         py.moveTo(695, 454)  # moveto coordinates
        #         py.click()
        #         time.sleep(0.5)
        pass

    def familienanamnese_4(self):
        # time.sleep(0.3)
        # py.click(x=675, y=426)
        # py.press('tab')
        # py.press('right')
        # py.press('tab')
        # py.press('right')
        # #herzinfarkt/schalagenfall
        # py.press('tab')
        # py.press('right')
        # py.press('right')
        # py.press('tab')
        # py.press('right')
        # time.sleep(0.4)
        # blutungsneigung_optionen = [
        #     ('von-Willebrand-Syndrom', (800, 644)),
        #     ('Fibrinogenmangel', (1205, 645)),
        #     ('Faktor-VII-Mangel', (457, 702)),
        #     ('Hämophilie A', (810, 703)),
        #     ('Hämophilie B', (1203, 703)),
        #     ('Faktor-X-Mangel', (426, 758)),
        #     ('Faktor-XI-Mangel', (821, 761)),
        #     ('Faktor-XII-Mangel', (1217, 760)),
        #     ('Plättchen', (461, 818))
        # ]

        # # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        # num_options_to_select = random.randint(1, len(blutungsneigung_optionen))

        # # Wähle zufällige Optionen in aufsteigender Reihenfolge
        # selected_options = sorted(random.sample(blutungsneigung_optionen, num_options_to_select), key=lambda x: blutungsneigung_optionen.index(x))

        # # Jede ausgewählte Option anklicken
        # for option_name, (x, y) in selected_options:
        #     py.moveTo(x, y)
        #     py.click()
        #     time.sleep(0.5)
        pass

    def operationen(self):
        time.sleep(1)
        py.scroll(+20000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Wurden Sie schonmal operiert (auch Zahnbehandlungen)"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press('right')
        py.press('right')

    def medikamente(self):
        # #Haben Sie eine Hormonspirale/Kupferspirale?
        time.sleep(0.3)
        py.press('tab')
        py.press('right')
        py.press('tab')
        py.press('right')

        #medikammente read datei
        py.press('tab')
        with open('Medikamente.txt', 'r') as file:
            medikamente = file.readlines()

        # Schritt 2: Bereinige die Medikamente (entferne Leerzeichen und Zeilenumbrüche)
        medikamente = [med.strip() for med in medikamente]

        # Schritt 3: Wähle ein zufälliges Medikament aus der Liste
        random_medikament = random.choice(medikamente)

        # Schritt 4: Verwende pyautogui, um das zufällige Medikament zu schreiben
        time.sleep(0.4)  # Optional: Verzögerung vor dem Schreiben
        py.write(random_medikament)
        py.press('tab')
        time.sleep(0.3)
        py.write(self.dose)
        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1,3)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")
        py.press('tab')
        py.write('hallo Bemerkung')
        time.sleep(0.2)
        py.press('tab')
        py.press('tab')
        py.press('tab')
        py.press('right')
        time.sleep(0.2)
        py.press('tab')
        py.press('right')
        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1,4)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")



    def allergien(self):
        time.sleep(1)
        py.scroll(+20000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Haben Sie Allergien?"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press("right")
        py.scroll(-720)

        time.sleep(0.4)
        allergie_optionen = [
            ('Heuschnupfen', (433, 539)),
            ('Allergie durch Stoffe am Arbeitsplatz', (433, 594)),
            ('Tierhaarallergie', (424, 653)),
            ('Kontaktallergie', (1021, 593)),
            ('Hausstauballergie', (427, 706)),
            ('Urtikaria/Nesselsucht/Quincke', (1021, 535)),
            ('Insektenstichallergie', (1021, 652)),
            ('Sonnenallergie', (1021, 711))
        ]

        # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        num_options_to_select = random.randint(1, len(allergie_optionen))

        # Wähle zufällige Optionen in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(allergie_optionen, num_options_to_select), key=lambda x: allergie_optionen.index(x))

        # Jede ausgewählte Option anklicken
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.3)


    def allgemeiner_gesundheitszustand(self):
        time.sleep(1)
        py.scroll(+20000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Wie würden Sie Ihren Gesundheitszustand im Allgemeinen beschreiben?"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        

    def akute_infekte(self):
        py.press("tab")
        py.press("right")
        py.press("tab")
        py.write('Test')
        time.sleep(0.5)

    def infektneigung(self):
        py.press("tab")
        time.sleep(0.3)
        py.press("right")
        py.press("tab")
        #random jahr
        time.sleep(0.3)
        py.write(self.thrombose_jahr)
        py.press("tab")
        py.press("right")
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)

        #husten
        py.press("tab")
        py.press("right")
        #shnupfen
        time.sleep(0.3)
        py.press("tab")
        py.press("right")
        #fiber
        py.press("tab")
        py.press("right")
        py.press('tab')
        time.sleep(0.3)
        #
        num_down_presses = random.randint(1, 3)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        #epidoden
        py.press('tab')
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        #Lungenentzündungen
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.press("right")
       #Mittelohrentzündung?
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.2)
        #Infektionen der Haut
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.write('test')
        #Lymphknotenschwellungen?
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.write('test2')
        #Durchfall/Diarrhö
        py.press("tab")
        py.press("right")
        py.press('tab')
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('right') 
            time.sleep(0.4)
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        #
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        #
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.scroll(-500)
        py.click(x=428, y=478)
        time.sleep(0.3)
        py.press("tab")
        py.press("tab")
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.write("Test hauter")


    def infektionskrankheiten(self):
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        pass

    def chronische_krankheiten(self):
        # py.press("tab")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        pass

    def chronische_krankheiten_2(self):
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        pass

    def chronische_krankheiten_3(self):
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        pass

    def chronische_krankheiten_4(self):
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        pass




    def tumor_krebserkrankung(self):
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.3)
        pass

    def gewichtsverlust_migraene(self):
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.3)
        # py.press("tab")
        # py.press("right")
        # py.press("tab")
        # py.write(self.thrombose_monat)
        # time.sleep(0.2)
        # py.press("tab")
        # py.write(self.thrombose_jahr)
        # time.sleep(0.2)
        pass

    def rauchverhalten(self):
        # py.press("tab")
        # py.press("right")
        # time.sleep(0.4)
        # py.press('tab') 
        # #
        # num_down_presses = random.randint(1, 4)
        
        # # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        # for _ in range(num_down_presses):
        #     py.press('right') 
        #     time.sleep(0.3)
        
        # #jahr
        # py.press('tab') 
        # py.write(self.thrombose_jahr)
        # time.sleep(0.2)
        # py.press('tab') 
        # num_down_presses = random.randint(1, 4)
        
        # # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        # for _ in range(num_down_presses):
        #     py.press('right') 
        #     time.sleep(0.3)
        # py.press('tab') 
        # py.write("2009")
        # time.sleep(0.2)
        pass


    def alkoholkonsum(self):
        # py.press('tab') 
        # time.sleep(0.2)
        # py.press('right') 
        # time.sleep(0.2)
        # num_down_presses = random.randint(1, 4)
        
        # # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        # for _ in range(num_down_presses):
        #     py.press('right') 
        #     time.sleep(0.3)
        # py.press('tab') 
        # time.sleep(0.2)
        # py.press('right') 
        # time.sleep(0.2)

        # num_down_presses = random.randint(1, 4)
        
        # # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        # for _ in range(num_down_presses):
        #     py.press('right') 
        #     time.sleep(0.3)
        # py.press("tab")
        # py.press("right")
        # #ende
        # py.press("tab")
        # time.sleep(4)
        # py.press("tab")
        # py.press("tab")
        # py.press("enter")
        # time.sleep(4)
        # py.hotkey('ctrl', 'r')
        pass
        

class Weiblich:
    def __init__(self, form_automation):
        self.form_automation = form_automation
        self.Inseminationen=self.generate_random_Inseminationen()
        self.IVF=self.generate_random_IVF()
        self.ICSI= self.generate_random_ICSI()
        self.Eizellspende= self.generate_random_Eizellspende()
        self.thrombose_monat = self.generate_random_monat_thrombose()  
        self.thrombose_jahr = self.generate_random_jahr_thrombose()
        self.Schwangerschaftswoche = self.generate_random_Schwangerschaftswoche()
        self.Schwangerschaft_monat = self.generate_random_monat_Schwangerschaft()  
        self.Schwangerschaft_jahr = self.generate_random_jahr_Schwangerschaft()
        self.dose= self.generate_random_dose()

    def fill_form(self):
        print("Formular für 'weiblich' ausfüllen")

    def handle_all(self):
        self.fill_personal_daten()
        self.Versichertendaten()
        self.vorstellungsgrund()
        self.thrombose_lungenembolie()
        self.thrombose_lungenembolie_2()
        self.thrombose_lungenembolie_3()
        self.thrombose_lungenembolie_4()
        self.thrombose_lungenembolie_5()
        self.thrombose_lungenembolie_6()
        self.blutungsneigung()
        self.wundheilung()
        self.gynaekologische_anamnese()
        self.gynaekologische_anamnese_2()
        self.gynaekologische_anamnese_3()
        self.familienanamnese()
        self.familienanamnese_2()
        self.familienanamnese_3()
        self.familienanamnese_4()
        self.operationen()
        self.medikamente()
        self.allergien()
        self.allgemeiner_gesundheitszustand()
        self.akute_infekte()
        self.infektneigung()
        self.infektionskrankheiten()
        self.chronische_krankheiten()
        self.chronische_krankheiten_2()
        self.chronische_krankheiten_3()
        self.chronische_krankheiten_4()
        self.tumor_krebserkrankung()
        self.gewichtsverlust_migraene()
        self.rauchverhalten()
        self.alkoholkonsum()


    #Alle Random Generators
    def typewrite_with_delay(self, text, min_delay=0.05, max_delay=0.1):
        delay = random.uniform(min_delay, max_delay)
        py.typewrite(text, interval=delay)

    def generate_random_Inseminationen(self):
        Inseminationen = random.randint(1, 25)
        return str(Inseminationen)
    def generate_random_IVF(self):
        IVF = random.randint(1, 25)
        return str(IVF)
    def generate_random_ICSI(self):
        ICSI = random.randint(1, 25)
        return str(ICSI)
    def generate_random_Eizellspende(self):
        Eizellspende = random.randint(1, 25)
        return str(Eizellspende)
    def generate_random_monat_thrombose(self):
        thrombose_monat = random.randint(1, 12)
        return str(thrombose_monat)

    def generate_random_jahr_thrombose(self):
        thrombose_jahr = random.randint(1999, 2023)
        return str(thrombose_jahr)
    
    def generate_random_Schwangerschaftswoche(self):
        Schwangerschaftswoche = random.randint(3, 42)
        return str(Schwangerschaftswoche)
    
    def generate_random_monat_Schwangerschaft(self):
        Schwangerschaft_monat = random.randint(1, 12)
        return str(Schwangerschaft_monat)

    def generate_random_jahr_Schwangerschaft(self):
        Schwangerschaft_jahr = random.randint(1999, 2023)
        return str(Schwangerschaft_jahr)
    
    def generate_random_dose(self):
        dose = random.randint(50, 1000)
        return str(dose)

    def fill_personal_daten(self):
        for _ in range(5):
            py.press('tab')
        time.sleep(0.3)
        py.write(self.form_automation.strasse)
        py.press('tab')
        time.sleep(0.3)

        py.write(self.form_automation.postleitzahl)
        time.sleep(0.3)
        py.press('tab')
        py.write(self.form_automation.wohnort)
        py.press('tab')
        py.write(self.form_automation.telefon)

        for _ in range(2):
            py.press('tab')

        py.write(self.form_automation.gewicht)
        py.press('tab')
        self.typewrite_with_delay(self.form_automation.grosse)
        py.press('tab')

        self.form_automation.select_blutgruppe(self.form_automation.index)
        py.press('tab')
        # Beruf
        py.write(self.form_automation.Beruf)
        py.press('tab')


    def Versichertendaten(self):
        py.press('right')
        py.press('tab')
        py.press('right')
        py.press('tab')
        py.moveTo(x=400, y=695)
        py.click()
        for _ in range(5):
            py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')

        py.press('tab')

    def vorstellungsgrund(self):
        
        # Define 'Vorstellungsgrund Warum' options with their coordinates
        vorstellungsgrund_warum_options = [
            ('Auffälligkeiten/Ereignisse in der Familie', (504, 571)),
            ('Kinderwunsch', (478, 623)),
            ('Wunsch', (478, 683)),
            ('Auffälligkeiten Vorgeschichte', (459, 736))
            # ('Sonstiges', (410, 803))
        ]

        # Randomly choose one of the options
        selected_option = random.choice(vorstellungsgrund_warum_options)
        option_name, (x, y) = selected_option

        # Click the selected option
        print(f"Selected Vorstellungsgrund Warum option: {option_name}")
        py.moveTo(x, y)
        py.click()
        time.sleep(0.5)

        # Handle sub-options based on the option selected
        if option_name == 'Auffälligkeiten/Ereignisse in der Familie':
            self.handle_sub_options_auffaelligkeiten_familie()

        elif option_name == 'Kinderwunsch':
            self.handle_sub_options_kinderwunsch()
        
        elif option_name =='Wunsch':
            self.handle_sub_options_Wunch()

        elif option_name == 'Auffälligkeiten Vorgeschichte':
            self.handle_sub_options_auffaelligkeiten_vorgeschichte()
        
        # elif option_name == 'Sonstiges':
        #     self.handle_main_sonstiges() 

    # def handle_main_sonstiges(self):
    #     """
    #     Handles the main 'Sonstiges' option. After selecting it, it will enter the text "Main hi sonstiges".
    #     """
    #     # Scroll to ensure visibility
    #     py.scroll(-400)

    #     # Click on the main 'Sonstiges' option
    #     py.moveTo(410, 803)  # Coordinates for main 'Sonstiges'
    #     py.click()
    #     time.sleep(1)

    #     # Press 'tab' and write the text "Main hi sonstiges"
    #     py.press('tab')
    #     time.sleep(0.5)
    #     py.write("Main hi sonstiges")
    #     time.sleep(1)

    def handle_sub_options_auffaelligkeiten_familie(self):
        """
        Handles the sub-options under 'Auffälligkeiten/Ereignisse in der Familie'.
        """
        # Scroll down to make sub-options visible
        py.scroll(-400)

        # Define sub-options with coordinates
        auffaelligkeiten_sub_options = [
            ('Thromboseneigung in der Familie', (440, 666)),
            ('Herzinfarkte/Schlaganfälle in der Familie', (510, 713)),
            ('Gefäßverschlüsse in der Familie', (518, 779)),
            ('Faktor-V-Leiden in der Familie', (458, 832)),
            ('Blutungsneigung in der Familie', (477, 882))
            # ('Sonstiges in der Familie', (482, 949))
        ]

        # Randomly select and click a sub-option
        selected_sub_option = random.choice(auffaelligkeiten_sub_options)
        sub_option_name, (x, y) = selected_sub_option

        print(f"Selected sub-option: {sub_option_name}")
        py.moveTo(x, y)
        py.click()
        time.sleep(0.5)

    def handle_sub_options_kinderwunsch(self):
        """
        Handles the sub-options under 'Kinderwunsch'.
        """
        # KINDERWUNSCH SUBOPTIONS
        py.scroll(-300)

        for _ in range(4):
            py.press('tab')
            time.sleep(0.2)
            
        
        # Kinderwunschbehandlung bisher erfolgt?
        py.press('right')
        py.press('tab')
        py.press('right')
        py.press('right')

        py.press('tab')
        time.sleep(0.3)
        py.write(self.Inseminationen)
        py.press('tab')
        time.sleep(0.3)
        py.write(self.IVF)
        py.press('tab')
        time.sleep(0.3)
        py.write(self.ICSI)
        py.press('tab')
        time.sleep(0.3)
        py.write(self.Eizellspende)
        time.sleep(0.3)
        # 'Weitere Kinderwunsch Behandlung' options (e.g., ja oder nein )
        py.press('tab')
        py.press('right')  # Select 'Ja' (or randomize this if needed)
        print("Selected 'ja' for 'Kinderwunsch Behandlung'")
        time.sleep(1)


    
    def handle_sub_options_Wunch(self):
        time.sleep(1)
        

    def handle_sub_options_auffaelligkeiten_vorgeschichte(self):
        """
        Handles sub-options under 'Auffälligkeiten in der Vorgeschichte'.
        """
        # Scroll to reveal the sub-options
        py.scroll(-850)
        # Define sub-options with coordinates
        auffaelligkeiten_vorgeschichte_sub_options = [
            ('Thrombosen', (457, 167)),
            ('Schlaganfall/Hirninsult/Herzinfarkt', (457, 223)),
            ('Dauer der Blutverdünnung', (457, 286)),
            ('unklare aPTT-Verlängerung', (457, 341)),
            ('unklare Quickverminderung', (457, 399)),
            ('Blutungsneigung', (457, 452)),
            ('von-Willebrand-Syndrom', (457, 508)),
            ('Plättchenfunktionsstörung', (457, 567)),
            ('zu wenige Blutplättchen', (457, 629)),
            ('zu viel Blutplättchen', (457, 685))
            # ('zu viele rote Blutkörperchen', (457, 742)),
            # ('zu viele weiße Blutkörperchen', (457, 802)),
            # ('Infektneigung/Immundefekt', (457, 860)),
            # ('Sonstiges', (457, 918))
        ]

        # Randomly select and click a sub-option
        selected_sub_option = random.choice(auffaelligkeiten_vorgeschichte_sub_options)
        sub_option_name, (x, y) = selected_sub_option

        print(f"Selected sub-option: {sub_option_name}")
        py.moveTo(x, y)
        py.click()
        time.sleep(0.5)

        if sub_option_name == 'Sonstiges in der Familie':
            self.handle_sub_options_sonstiges()

    # def handle_sub_options_sonstiges(self):
    #     time.sleep(1)
    #     py.press('tab')
    #     py.write("hi sonstiges")
    #     time.sleep(1)
        

    #Haben Sie schon mal eine Thrombose, Lungenembolie
    def thrombose_lungenembolie(self):

        py.scroll(+10000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = " schon mal eine Thrombose"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press("right")
        py.press('tab')
        py.write(self.thrombose_monat)
        py.press('tab')
        py.write(self.thrombose_jahr)
        py.press('tab')
        py.scroll(-822)

        # Define Group A options (with sub-options)
        group_a_options = [
            ('Oberflächlich', (459, 124)),
            ('Tiefe Beinvenenthrombose', (459, 186)),
            ('Lungenarterienembolie', (459, 243)),
            ('Muskelvenenthrombose', (459, 300)),
            ('Schlüsselbeinvenenthrombose', (459, 358)),
            ('Halsgefäß-/Jugularisthrombose', (459, 418)),
            ('Armvenenthrombose', (459, 475)),
            ('ZVK-/Katheterthrombose', (459, 533)),
            ('Sinusvenenthrombose/Hirnvene', (459, 593)),
            ('Ereignis am Auge', (459, 939)),
        ]

        # Define Group B options (no sub-options, multiple selections allowed)
        group_b_options = [
            ('Mesenterialvenenthrombose', (459, 675)),
            ('Pfortader', (459, 710)),
            ('Lebervenenverschluss', (459, 767)),
            ('Milzin', (459, 821)),
            ('Arterieler', (459, 884))
        ]

        # Define Group C ('Weiß ich nicht', exclusive option)
        group_c_option = ('Weiß ich nicht', (459, 999))

        # Track selected main options
        selected_main_options = []
        sub_option_candidates = []  # Only Group A options will be added here

        # Adjust the probability so that 'Weiß ich nicht' is less likely to be chosen
        option_pool = ['A'] * 4 + ['C']  # 4x chance of selecting from Group A, 1x chance of selecting 'Weiß ich nicht'
        selected_group = random.choice(option_pool)

        if selected_group == 'C':
            # If 'Weiß ich nicht' is selected, only select this option and return
            print(f"Selected Group C option: {group_c_option[0]}")
            py.moveTo(group_c_option[1])
            py.click()
            return  # Skip any other selections and sub-options

        # If Group A is selected
        selected_a_option = random.choice(group_a_options)
        a_option_name, (a_x, a_y) = selected_a_option

        # Click the selected Group A option
        print(f"Selected Group A option: {a_option_name}")
        py.moveTo(a_x, a_y)
        py.click()
        time.sleep(0.5)

        # Add Group A option to sub-option candidates
        sub_option_candidates.append(a_option_name)
        selected_main_options.append(a_option_name)

        # Select multiple Group B options (randomly)
        selected_b_options = random.sample(group_b_options, random.randint(1, len(group_b_options)))
        for b_option_name, (b_x, b_y) in selected_b_options:
            print(f"Selected Group B option: {b_option_name}")
            py.moveTo(b_x, b_y)
            py.click()
            time.sleep(0.5)
            selected_main_options.append(b_option_name)

        # Now handle sub-options after main option selection
        self.handle_selected_sub_options(sub_option_candidates)

    def handle_selected_sub_options(self, sub_option_candidates):
        """
        Handles sub-options for selected Group A options after main options are selected.
        """
        for option in sub_option_candidates:
            if option == 'Oberflächlich':
                self.handle_sub_options_oberflächlich()
            elif option == 'Tiefe Beinvenenthrombose':
                self.handle_sub_options_tiefe_beinvenenthrombose()
            elif option == 'Lungenarterienembolie':
                self.handle_sub_options_lungenarterienembolie()
            elif option == 'Muskelvenenthrombose':
                self.handle_sub_options_muskelvenenthrombose()
            elif option == 'Schlüsselbeinvenenthrombose':
                self.handle_sub_options_schlüsselbeinvenenthrombose()
            elif option == 'Halsgefäß-/Jugularisthrombose':
                self.handle_sub_options_halsgefaess_jugularisthrombose()
            elif option == 'Armvenenthrombose':
                self.handle_sub_options_armvenenthrombose()
            elif option == 'ZVK-/Katheterthrombose':
                self.handle_sub_options_zvk_katheterthrombose()
            elif option == 'Sinusvenenthrombose/Hirnvene':
                self.handle_sub_options_sinusvenenthrombose()
            elif option == 'Ereignis am Auge':
                self.handle_sub_options_ereignis_am_auge()

    # Example sub-option handlers for Group A
    def handle_sub_options_oberflächlich(self):
        print("Handling sub-options for 'Oberflächlich'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=472, y=438)
        time.sleep(1)
        py.click(x=588, y=713)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

    def handle_sub_options_tiefe_beinvenenthrombose(self):
        print("Handling sub-options for 'Tiefe Beinvenenthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=470, y=557)
        time.sleep(1)
        py.click(x=491, y=810)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        

    def handle_sub_options_lungenarterienembolie(self):
        print("Handling sub-options for 'Lungenarterienembolie'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        
    def handle_sub_options_muskelvenenthrombose(self):
        print("Handling sub-options for 'Muskelvenenthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')   
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

    def handle_sub_options_schlüsselbeinvenenthrombose(self):
        print("Handling sub-options for 'Schlüsselbeinvenenthrombose'")
        # Logic for sub-options for 'Schlüsselbeinvenenthrombose'

    def handle_sub_options_halsgefaess_jugularisthrombose(self):
        print("Handling sub-options for 'Halsgefäß-/Jugularisthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
    


    def handle_sub_options_armvenenthrombose(self):
        print("Handling sub-options for 'Armvenenthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

    def handle_sub_options_zvk_katheterthrombose(self):
        print("Handling sub-options for 'ZVK-/Katheterthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
       

    def handle_sub_options_sinusvenenthrombose(self):
        print("Handling sub-options for 'Sinusvenenthrombose/Hirnvene'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        

    def handle_sub_options_ereignis_am_auge(self):
        print("Handling sub-options for 'Ereignis am Auge'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=440, y=445)
        time.sleep(1)



    #Wie wurde am Ende behandelt?*
    def thrombose_lungenembolie_2(self):
        py.scroll(+10000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = " wurde am Ende"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.scroll(-300)

        #behandlung options
        behandlung_options = [
            ('Heparinspritzen/Clexane/Innohep usw.', (424, 364)),
            ('Marcumar/Phenprogramm/Coumadin/Sinthrom', (422, 423)),
            ('Xarelto', (417, 479)),
            ('Eliquis', (415, 537)),
            ('Lixiana', (412, 594)),
            ('Pradaxa', (410, 651)),
        ]

        # Define the exclusive options with their coordinates
        exclusive_options = [
            ('Ich habe weder Tabletten', (442, 715)),
            ('weiß ich nicht', (436, 770))
        ]

        # Decide whether to select an exclusive option (20% chance) or non-exclusive options (80% chance)
        if random.randint(1, 5) == 1:
            # 20% chance to select an exclusive option
            selected_option = random.choice(exclusive_options)
            selected_options = [selected_option]
            print(f"Exclusive selection: {selected_option[0]}")
        else:
            # 80% chance to select one or more non-exclusive options
            num_options = random.randint(1, len(behandlung_options))  # At least 1 option
            selected_options = random.sample(behandlung_options, num_options)
            print(f"Selecting options: {[opt[0] for opt in selected_options]}")

        # Click on the selected options
        for option_name, (x, y) in selected_options:
            print(f"Selecting option: {option_name}")
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)  # Slight delay between clicks if multiple options

        time.sleep(1)
        # py.click(x=477, y=971)
        py.scroll(-400)
        py.click(x=463, y=524)
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 7)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        time.sleep(0.2)

    
    
    def reset_view_to_normal(self):
        """
        Resets the view by scrolling up and zooming the screen back to its normal size.
        """
        # Scroll up to bring the view back
        py.scroll(-850) # You can adjust this scroll amount based on your specific need
        
        # Zoom back to normal size
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)

        time.sleep(0.5)

    def thrombose_lungenembolie_3(self):
        # Adjust the view
        py.scroll(-900)
        py.hotkey('ctrl', '-')
        time.sleep(0.3)
        py.hotkey('ctrl', '-')
        time.sleep(0.3)
        py.hotkey('ctrl', '-')
        time.sleep(0.3)
        py.hotkey('ctrl', '-')
        time.sleep(0.3)
        py.hotkey('ctrl', '-')

        # Define Option 1 (Single selection)
        option_1 = [
            ('Kein Auslöser bekannt', (712, 292)),
            ('Krankheitsaktivität', (690, 734)),
            ('Chronische Polyarthitis', (687, 762)),
            ('Nephrotisches Syndrom', (686, 791)),
            ('Sichelzellanämie', (684, 819)),
            ('Intravenöser', (684, 848)),
            ('Herzinfarkt', (685, 935))
        ]

        # Define Option 2 (Single selection with follow-up action)
        option_2 = [
            ('Krankenhausaufenthalt vor dem Ereignis', (681, 323)),
            ('Gelenkinjektionen/Cortisonspritzen', (680, 410)),
            ('Chemotherapie', (688, 499)),
            ('Antibabypille mit Östrogen', (689, 558)),
            ('Medikamente wie Gerinnungsfaktoren', (689, 616))
        ]

        # Define Option 3 (Single selection with sub-options)
        option_3 = [
            ('Operationen', (678, 379)),
            # ('Unfall/Verletzung', (679, 411)),
            # ('Schwangerschaft', (686, 676)),
            ('Wochenbett', (688, 702)),
            ('Immobilisation', (682, 879)),
            ('Infektion', (688, 905)),
            ('Reise', (681, 965)),
            ('Ungewohnte', (678, 994))
        ]

        # Randomly choose one of the three option groups
        selected_group = random.choice([1, 2, 3])
        selected_option = None

        if selected_group == 1:
            # Select one option from Option 1
            selected_option = random.choice(option_1)
            option_name, (x, y) = selected_option
            print(f"Selected Option 1: {option_name}")
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)  # Ensure the selection is registered
            self.reset_view_to_normal()

        elif selected_group == 2:
            # Select one option from Option 2 and perform follow-up actions
            selected_option = random.choice(option_2)
            option_name, (x, y) = selected_option
            print(f"Selected Option 2: {option_name}")
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)  # Ensure the selection is registered
            

            # Follow-up action
            py.press('tab')
            py.write("hi test")
            time.sleep(0.5)  # Ensure the follow-up action is processed
            self.reset_view_to_normal()

        elif selected_group == 3:
            # Select one option from Option 3 and handle sub-options
            selected_option = random.choice(option_3)
            option_name, (x, y) = selected_option
            print(f"Selected Option 3: {option_name}")
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)  # Ensure the selection is registered

            # Now handle sub-options for Option 3 after confirming the selection
            self.handle_sub_options(option_name)

    def handle_sub_options(self, option_name):
        """
        Handles the sub-options for Option 3.
        """
        print(f"Handling sub-options for '{option_name}'")

        if option_name == 'Operationen':
            self.handle_operationen_sub_options()
        elif option_name == 'Unfall/Verletzung':
            self.handle_unfall_sub_options()
        elif option_name == 'Schwangerschaft':
            self.handle_schwangerschaft_sub_options()
        elif option_name == 'Wochenbett':
            self.handle_wochenbett_sub_options()
        elif option_name == 'Immobilisation':
            self.handle_immobilisation_sub_options()
        elif option_name == 'Infektion':
            self.handle_infection_sub_options()
        elif option_name == 'Reise':
            self.handle_reise_sub_options()
        elif option_name == 'Ungewohnte':
            self.handle_ungewohnte_sub_options()

    # Define placeholder methods for the sub-options in Option 3

    def handle_operationen_sub_options(self):
        print("Handling sub-options for 'Operationen'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)

        operation_options = [
            ('Knochenbrüche', (442, 581)),
            ('Hüft-/Kniegelenksoperation', (439, 641)),
            ('Bauchoperation', (449, 699)),
            ('Sonstiges', (431, 757))  # Sonstiges ist die letzte Option
        ]
        
        # Wähle zufällig aus, wie viele Optionen ausgewählt werden (1 bis alle)
        num_options_to_select = random.randint(1, len(operation_options))
        
        # Wähle zufällig Optionen aus (eine oder mehrere), aber in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(operation_options, num_options_to_select), key=lambda x: operation_options.index(x))
        
        # Klicke auf jede ausgewählte Option in der Reihenfolge und prüfe, ob "Sonstiges" dabei ist
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)  
            
            # Wenn "Sonstiges" ausgewählt wurde, führe eine zusätzliche Aktion aus
            if option_name == 'Sonstiges':
                py.press('tab')
                py.write('hola sonstiges')

       

    def handle_unfall_sub_options(self):
        # print("Handling sub-options for 'Unfall/Verletzung'")
        # time.sleep(1)
        # py.scroll(-850)
        # for _ in range(5):
        #     py.hotkey('ctrl', '+')
        #     time.sleep(0.3)
        # time.sleep(0.5)
        # py.click(x=450, y=640)
        pass

    # def handle_schwangerschaft_sub_options(self):
    #     print("Handling sub-options for 'Schwangerschaft'")
    #     time.sleep(1)

    #     for _ in range(5):
    #         py.hotkey('ctrl', '+')
    #         time.sleep(0.3)
    #     py.scroll(-1350)
    #     time.sleep(0.5)
        
        
    #     schwangerschaft_options = [
    #         ('in welcher Schwangerschaftswoche?', (464, 172)),
    #         ('bzw. wie viele Wochen nach der Fehlgeburt?', (457, 283)),
    #         ('Präeklampsie', (438, 398)),
    #         ('Schwangerschaftsvergiftung', (443, 454)),
    #         ('Gestose', (444, 511)),
    #         ('HELLP-Syndrom', (444, 571)),
    #         ('Geburtsgewicht <2500g', (446, 806)),  # Koordinaten für diese Option fehlen, angenommen!
    #         ('Hyperstimulationssyndrom', (456, 629)),
    #         ('Blutung', (461, 749)),
    #         ('Gewichtszunahme', (446, 806)),
    #         ('Unstillbares S', (448, 859)),
    #         ('Mehrlingsschwangerschaft', (467, 921))
    #     ]

    #     # Zufällige Anzahl von Optionen auswählen (1 bis alle)
    #     num_options_to_select = random.randint(1, len(schwangerschaft_options))
        
    #     # Wähle zufällig Optionen aus und sortiere sie in aufsteigender Reihenfolge
    #     selected_options = sorted(random.sample(schwangerschaft_options, num_options_to_select), key=lambda x: schwangerschaft_options.index(x))

    #     # Klicke jede ausgewählte Option in der Reihenfolge
    #     for option_name, (x, y) in selected_options:
    #         py.moveTo(x, y)
    #         py.click()
    #         time.sleep(0.5)

    #         # Wenn die erste oder zweite Option ausgewählt wird, eine zusätzliche Aktion ausführen
    #         if option_name == 'in welcher Schwangerschaftswoche?' or option_name == 'bzw. wie viele Wochen nach der Fehlgeburt?':
    #             py.press('tab')
    #             py.write('4')  # Beispiel für eine Ausgabe, hier '4' eingeben
    #             time.sleep(0.5)
    #         elif option_name == 'bzw. wie viele Wochen nach der Fehlgeburt?':
    #             py.press('tab')
    #             py.write('4')  # Beispielhafte Eingabe '4'
    #             time.sleep(0.5)

    def handle_wochenbett_sub_options(self):
        print("Handling sub-options for 'Wochenbett'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)
        py.click(x=483, y=537)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

        time.sleep(0.5)
        py.press('tab')
        py.press('right')
        py.scroll(-200)

        wochenbett_options = [
            ('Vermehrte Blutung', (495, 695)),
            ('Bluttransfusion', (475, 761)),
            ('Erneute Blutung', (475, 761)),
            ('Infektion', (463, 880))
        ]
        
        # Zufällige Anzahl von Optionen auswählen (1 bis alle)
        num_options_to_select = random.randint(1, len(wochenbett_options))
        
        # Optionen in aufsteigender Reihenfolge auswählen
        selected_options = sorted(random.sample(wochenbett_options, num_options_to_select), key=lambda x: wochenbett_options.index(x))
        
        # Klicken auf die ausgewählten Optionen
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)
        


    def handle_immobilisation_sub_options(self):
        print("Handling sub-options for 'Immobilisation'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)
        py.click(x=483, y=537)
        py.press('tab')
        py.press('right')
        py.press('right')
        


    def handle_infection_sub_options(self):
        print("Handling sub-options for 'Infektion'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)
        py.scroll(-400)
        py.click(x=438, y=366)
        time.sleep(0.2)
        py.click(x=441, y=572)
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')
        time.sleep(0.3)
        py.press('right')
        py.press('tab')
        py.write('7')

    def handle_reise_sub_options(self):
        print("Handling sub-options for 'Reise'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)
        py.click(x=756, y=566)
        py.press('tab')
        py.press('down')


    def handle_ungewohnte_sub_options(self):
        print("Handling sub-options for 'Ungewohnte'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)
        py.click(x=461, y=701)


    def thrombose_lungenembolie_4(self):
        time.sleep(1)
        py.scroll(+10000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Haben Sie eine weitere Thrombose/Embolie/Ereignis gehabt?"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press("right")
        py.press("right")
        pass
        
    def thrombose_lungenembolie_5(self):
        py.press('tab')
        py.press('right')
        py.scroll(-300)
        time.sleep(0.3)

        # Definiere die Venenerkrankung Optionen mit ihren Koordinaten
        venenerkrankung_options = [
            ('Besenreiser', (431, 684)),
            ('Krampfadern', (430, 741)),
            ('Venenentzündung/Phlebitis', (424, 799)),
            ('Posttrombotisches Syndrom', (434, 856)),
            ('Sonstige', (420, 914))  # Spezielle Behandlung für Sonstige
        ]

        # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        num_options_to_select = random.randint(1, len(venenerkrankung_options))

        # Wähle zufällige Optionen in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(venenerkrankung_options, num_options_to_select), key=lambda x: venenerkrankung_options.index(x))

        # Jede ausgewählte Option anklicken
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)

            # Wenn "Sonstige" ausgewählt wurde, zusätzliche Aktion ausführen
            if option_name == 'Sonstige':
                py.press('tab')
                py.write('hi sonstiges')
        



    def thrombose_lungenembolie_6(self):
        time.sleep(1)
        py.scroll(-300)
        time.sleep(0.3)
        py.click(x=586, y=862)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
                ##a
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        ##b
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        ##
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        ##
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
              ## c
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #c2
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #c3
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #c4
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

        #c5
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

    def blutungsneigung(self):
        #Nasenbluten
        py.press('tab')
        py.press('right')
        
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)

        #Blaue Flecken
        py.press('tab')
        py.press('down')
        py.press('down')
        py.press('down')
        time.sleep(0.2)
        py.press('down')
        py.press('down')
        time.sleep(0.2)

        # py.press('tab')
        # py.press('right')
        
        # py.moveTo(x=1020, y=750)
        # py.click()


        #Blutungneigung bei kleineren Verletzungen
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)

        #NBlutungen in der Mundhöhle
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        
        #Magen-Darm-Blutungen
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)          

        #Blut im Urin/Hämaturie
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)

        #Zähne ziehen/Zahnextraktion
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        

        #Chirurgische Eingriffe/Operationen
        py.press('tab')
        py.press('down')
        py.press('down')
        time.sleep(0.3)
        py.press('down')
        py.press('tab')
        py.write("hi")
        time.sleep(0.2)


        #verstärkte Regelblutung/Hypermenorrhoe
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 9)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        time.sleep(0.2)

        #Blutungen nach der Entbindung/Wochenbett
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        time.sleep(0.2)
        


        #Blutergüsse/Hämatome in Muskeln
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        time.sleep(0.2)

        #Blutergüsse/Hämatome in Gelenken
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        time.sleep(0.2)


        #Hirnblutungen
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 3)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        time.sleep(0.2)


        #andere Blutungsprobleme
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)

    def wundheilung(self):
        time.sleep(0.3)
        py.press('tab')
        py.press('right')
        time.sleep(0.4)
        py.press('tab')
        
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 3)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        

    def gynaekologische_anamnese(self):
        time.sleep(1)
        py.scroll(+10000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Wann war Ihre erste Regelblutung?"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press('right')
        py.press('tab')
        time.sleep(0.5)
        py.write('11')
        #Haben Sie eine verstärkte Regelblutung?
        py.press('tab')
        py.press('right')
        time.sleep(0.7)
        py.press('tab')
        py.press('right')
        #Schwangerschaftseintritt
        py.press('tab')
        num_right_presses = random.randint(1, 7)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #Wie ist der errechnete Entbindungstermin?
        py.press('tab')
        py.press('right')
        py.press('tab')
        py.write("16011990")
        time.sleep(0.4)
        py.press('tab')
        #Wann war der erste Tag der letzten Periode?*
        py.press('tab')
        py.press('right')
        py.press('tab')
        py.write("16012024")
        time.sleep(0.4)
        py.press('tab')
        #In welcher Schwangerschaftswoche befinden Sie sich?
        py.press('tab')
        py.press('right')
        py.press('tab')
        py.write(self.Schwangerschaftswoche)
        time.sleep(0.5)
        py.press('tab')
        py.press('right')
        py.press('tab')
        py.write(self.Schwangerschaft_monat)
        py.press('tab')
        py.write(self.Schwangerschaft_jahr)
        #Schwangerschaftseintritt*
        py.press('tab')
        num_right_presses = random.randint(1, 8)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #Art der Schwangerschaft*
        py.press('tab')
        num_right_presses = random.randint(1,5)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        py.press('tab')
        py.write(self.Schwangerschaftswoche)
        py.press("tab")
        py.press('right')
        py.press('right')
        py.press("tab")
        py.press('right')
        py.press('right')
        # py.click(x=1369, y=355)
        # py.press("tab")
        time.sleep(1)




    def gynaekologische_anamnese_2(self):
        # pbac score
        time.sleep(1)
        py.scroll(+20000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Wie viele Binden/Tampons verwenden"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.click(x=1369, y=355)
        py.press('right')
        py.press("tab")
        py.press("tab")
        # tag1
        py.press("enter")
        num_down_presses = random.randint(1, 3)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")
        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1, 3)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")
        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1, 2)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")
        # tag2

        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1, 3)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")
        py.press('tab')    
        py.press("enter")
        num_down_presses = random.randint(1, 3)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")
        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1, 2)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        # tag3
        py.press("enter")
        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1, 3)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")
        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1, 3)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")
        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1, 2)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")




        # py.scroll(-500)
        # time.sleep(0.5)
        # # Schwangerschaftskomplikationen options with updated coordinates
        # Schwangerschaftskomplikationen_options = [
        #     ('Schwangerschaftsdiabetes', (424, 336)),
        #     ('Infektionen', (417, 393)),
        #     ('Vorzeitige Entbindung', (429, 454)),
        #     ('Totgeburt/IUFT', (423, 511)),
        #     ('Intrauterine', (425, 573)),
        #     ('Blutungen nur', (428, 628)),
        #     ('Blutungen auch', (429, 685)),
        #     ('Muttermundschwäche', (432, 743)),
        #     ('anders', (408, 860))  # Spezielle Behandlung für "anders"
        # ]

        # # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        # num_options_to_select = random.randint(1, len(Schwangerschaftskomplikationen_options))

        # # Wähle zufällige Optionen in aufsteigender Reihenfolge
        # selected_options = sorted(random.sample(Schwangerschaftskomplikationen_options, num_options_to_select), key=lambda x: Schwangerschaftskomplikationen_options.index(x))

        # # Jede ausgewählte Option anklicken
        # for option_name, (x, y) in selected_options:
        #     py.moveTo(x, y)
        #     py.click()
        #     time.sleep(0.5)

        #     # Wenn "anders" ausgewählt wurde, zusätzliche Aktion ausführen
        #     if option_name == 'anders':
        #         py.press('tab')
        #         py.write('hi sonstiges')


    def gynaekologische_anamnese_3(self):

        # py.scroll(-700)
        # time.sleep(0.5)
        pass


    def familienanamnese(self):
        time.sleep(1)
        py.scroll(+20000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Gibt es in Ihrer Familien folgende Erkrankungen?"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press("right")
        py.scroll(-300)
        #Blutarmut/Anämie/Thalassämie
        
        Blutarmut_options = [
            ('Blutarmut/Anämie ohne Ursache', (444, 550)),
            ('Blutarmut durch Eisenmangel', (434, 609)),
            ('Thalassämie', (434, 668)),
            ('Sichelzellanämie/SCD', (430, 730)),
            ('idk', (414, 785))   # Spezielle Behandlung für Sonstige
        ]

        # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        num_options_to_select = random.randint(1, len(Blutarmut_options))

        # Wähle zufällige Optionen in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(Blutarmut_options, num_options_to_select), key=lambda x: Blutarmut_options.index(x))

        # Jede ausgewählte Option anklicken
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)

            # Wenn "Sonstige" ausgewählt wurde, zusätzliche Aktion ausführen
            if option_name == 'idk':
                time.sleep(0.3)
                py.press('tab')
                py.write(' idk')

    def familienanamnese_2(self):
        time.sleep(1)
        py.scroll(-640)
        time.sleep(0.2)
        #thrombose in Familienanamese
        py.click(x=738, y=422)
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')
        py.press('right')
        #herzinfarkt/schalagenfall
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')
        py.press('right')
        py.scroll(-300)
        time.sleep(0.5)
        blutungsneigung_optionen = [
            ('von-Willebrand-Syndrom', (800, 627)),
            ('Fibrinogenmangel', (1205, 632)),
            ('Faktor-VII-Mangel', (457, 688)),
            ('Hämophilie A', (825, 690)),
            ('Hämophilie B', (1212, 690)),
            ('Faktor-X-Mangel', (435, 754)),
            ('Faktor-XI-Mangel', (821, 754)),
            ('Faktor-XII-Mangel', (1217, 754)),
            ('Plättchen', (461, 808))
        ]

        # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        num_options_to_select = random.randint(1, len(blutungsneigung_optionen))

        # Wähle zufällige Optionen in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(blutungsneigung_optionen, num_options_to_select), key=lambda x: blutungsneigung_optionen.index(x))

        # Jede ausgewählte Option anklicken
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
        #     time.sleep(0.5)


        # py.press('tab')
        # py.press('right')



    def familienanamnese_3(self):
        # py.scroll(-700)

        # thromboseereignisoptionen = [
        #     ('Beinvenenthrombose', (425, 164)),
        #     ('Lungenembolie', (429, 219)),
        #     ('Sonstiges', (429, 278))  # Spezielle Behandlung für Sonstiges
        # ]

        # # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        # num_options_to_select = random.randint(1, len(thromboseereignisoptionen))

        # # Wähle zufällige Optionen in aufsteigender Reihenfolge
        # selected_options = sorted(random.sample(thromboseereignisoptionen, num_options_to_select), key=lambda x: thromboseereignisoptionen.index(x))

        # # Jede ausgewählte Option anklicken
        # for option_name, (x, y) in selected_options:
        #     py.moveTo(x, y)
        #     py.click()
        #     time.sleep(0.5)

        #     # Wenn "Sonstiges" ausgewählt wurde, zusätzliche Aktion ausführen
        #     if option_name == 'Sonstiges':
        #         py.moveTo(695, 454)  # moveto coordinates
        #         py.click()
        #         time.sleep(0.5)
        pass

    def familienanamnese_4(self):
        # time.sleep(0.3)
        # py.click(x=675, y=426)
        # py.press('tab')
        # py.press('right')
        # py.press('tab')
        # py.press('right')
        # #herzinfarkt/schalagenfall
        # py.press('tab')
        # py.press('right')
        # py.press('right')
        # py.press('tab')
        # py.press('right')
        # time.sleep(0.4)
        # blutungsneigung_optionen = [
        #     ('von-Willebrand-Syndrom', (800, 644)),
        #     ('Fibrinogenmangel', (1205, 645)),
        #     ('Faktor-VII-Mangel', (457, 702)),
        #     ('Hämophilie A', (810, 703)),
        #     ('Hämophilie B', (1203, 703)),
        #     ('Faktor-X-Mangel', (426, 758)),
        #     ('Faktor-XI-Mangel', (821, 761)),
        #     ('Faktor-XII-Mangel', (1217, 760)),
        #     ('Plättchen', (461, 818))
        # ]

        # # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        # num_options_to_select = random.randint(1, len(blutungsneigung_optionen))

        # # Wähle zufällige Optionen in aufsteigender Reihenfolge
        # selected_options = sorted(random.sample(blutungsneigung_optionen, num_options_to_select), key=lambda x: blutungsneigung_optionen.index(x))

        # # Jede ausgewählte Option anklicken
        # for option_name, (x, y) in selected_options:
        #     py.moveTo(x, y)
        #     py.click()
        #     time.sleep(0.5)
        pass

    def operationen(self):
        time.sleep(1)
        py.scroll(+20000)
        time.sleep(1)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Wurden Sie schonmal operiert (auch Zahnbehandlungen)"
        py.write(search_word)
        time.sleep(0.8)
        py.press("esc")
        py.press("tab")
        py.press('right')
        py.press('right')

    def medikamente(self):
        #Haben Sie eine Hormonspirale/Kupferspirale?
        time.sleep(0.3)
        py.press('tab')
        py.press('right')
        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1, 23)
        for _ in range(num_down_presses):
            py.press('down')
            
        py.press("enter")
        time.sleep(0.3)
        py.press('tab')
        py.press('right')
        py.press('tab')
        py.press('right')

        #medikammente read datei
        py.press('tab')
        with open('Medikamente.txt', 'r') as file:
            medikamente = file.readlines()

        # Schritt 2: Bereinige die Medikamente (entferne Leerzeichen und Zeilenumbrüche)
        medikamente = [med.strip() for med in medikamente]

        # Schritt 3: Wähle ein zufälliges Medikament aus der Liste
        random_medikament = random.choice(medikamente)

        # Schritt 4: Verwende pyautogui, um das zufällige Medikament zu schreiben
        time.sleep(0.4)  # Optional: Verzögerung vor dem Schreiben
        py.write(random_medikament)
        py.press('tab')
        time.sleep(0.3)
        py.write(self.dose)
        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1,3)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")
        py.press('tab')
        py.write('hallo Bemerkung')
        time.sleep(0.2)
        py.press('tab')
        py.press('tab')
        py.press('tab')
        py.press('right')
        time.sleep(0.2)
        py.press('tab')
        py.press('right')
        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1,4)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")

    def allergien(self):
        time.sleep(1)
        py.scroll(+20000)
        time.sleep(1.5)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Haben Sie Allergien?"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press("right")
        py.scroll(-720)

        time.sleep(0.4)
        allergie_optionen = [
            ('Heuschnupfen', (433, 539)),
            ('Allergie durch Stoffe am Arbeitsplatz', (433, 594)),
            ('Tierhaarallergie', (424, 653)),
            ('Kontaktallergie', (1021, 593)),
            ('Hausstauballergie', (427, 706)),
            ('Urtikaria/Nesselsucht/Quincke', (1021, 535)),
            ('Insektenstichallergie', (1021, 652)),
            ('Sonnenallergie', (1021, 711))
        ]

        # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        num_options_to_select = random.randint(1, len(allergie_optionen))

        # Wähle zufällige Optionen in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(allergie_optionen, num_options_to_select), key=lambda x: allergie_optionen.index(x))

        # Jede ausgewählte Option anklicken
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.3)


    def allgemeiner_gesundheitszustand(self):
        time.sleep(1)
        py.scroll(+20000)
        time.sleep(1.5)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Wie würden Sie Ihren Gesundheitszustand im Allgemeinen beschreiben?"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        


    def akute_infekte(self):
        py.press("tab")
        py.press("right")
        py.press("tab")
        py.write('Test')
        time.sleep(0.5)

    def infektneigung(self):
        py.press("tab")
        time.sleep(0.3)
        py.press("right")
        py.press("tab")
        #random jahr
        time.sleep(0.3)
        py.write(self.thrombose_jahr)
        py.press("tab")
        py.press("right")
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)

        #husten
        py.press("tab")
        py.press("right")
        #shnupfen
        time.sleep(0.3)
        py.press("tab")
        py.press("right")
        #fiber
        py.press("tab")
        py.press("right")
        py.press('tab')
        num_down_presses = random.randint(1, 3)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        #epidoden
        py.press('tab')
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        #Lungenentzündungen
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.press("right")
       #Mittelohrentzündung?
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.2)
        #Infektionen der Haut
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.write('test')
        #Lymphknotenschwellungen?
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.write('test2')
        #Durchfall/Diarrhö
        py.press("tab")
        py.press("right")
        py.press('tab') 
        #
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('right') 
            time.sleep(0.4)
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        #
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        #
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.scroll(-500)
        py.click (x=462, y=660)
        time.sleep(0.3)
        py.press("tab")
        py.write("Test impf")
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.write("Test hauter")


    def infektionskrankheiten(self):
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.4)

    
    def chronische_krankheiten(self):
        # py.press("tab")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        pass

    def chronische_krankheiten_2(self):
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        pass

    def chronische_krankheiten_3(self):
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        pass
    def chronische_krankheiten_4(self):
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        pass

    def tumor_krebserkrankung(self):
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.4)
        pass
    def gewichtsverlust_migraene(self):
        # py.press("tab")
        # py.press("right")
        # py.press("right")
        # time.sleep(0.3)
        # py.press("tab")
        # py.press("right")
        # py.press("tab")
        # py.write(self.thrombose_monat)
        # time.sleep(0.2)
        # py.press("tab")
        # py.write(self.thrombose_jahr)
        # time.sleep(0.2)
        pass

    def rauchverhalten(self):
        py.press("tab")
        py.press("right")
        time.sleep(0.4)
        py.press('tab') 
        #
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('right') 
            time.sleep(0.3)
        
        #jahr
        py.press('tab') 
        py.write(self.thrombose_jahr)
        time.sleep(0.2)
        py.press('tab') 
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('right') 
            time.sleep(0.3)
        py.press('tab') 
        py.write("2009")
        time.sleep(0.2)


    def alkoholkonsum(self):
        py.press('tab') 
        time.sleep(0.2)
        py.press('right') 
        time.sleep(0.2)
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('right') 
            time.sleep(0.3)
        py.press('tab') 
        time.sleep(0.2)
        py.press('right') 
        time.sleep(0.2)
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('right') 
            time.sleep(0.3)
        py.press("tab")
        py.press("right")


        #ende
        py.press("tab")
        time.sleep(4)
        py.press("tab")
        py.press("tab")
        py.press("enter")
        time.sleep(4)
        py.hotkey('ctrl', 'r')

#GESCHLECHT DIVERS CLASS
class Divers:
    
    def __init__(self, form_automation):
        self.form_automation = form_automation
        self.thrombose_monat = self.generate_random_monat_thrombose()  
        self.thrombose_jahr = self.generate_random_jahr_thrombose()
        self.dose= self.generate_random_dose()

    def fill_form(self):
        print("Formular für 'divers' ausfüllen")

    def handle_all(self):
        self.fill_personal_daten()
        self.Versichertendaten()
        self.thrombose_lungenembolie()
        self.thrombose_lungenembolie_2()
        self.thrombose_lungenembolie_3()
        self.thrombose_lungenembolie_4()
        self.thrombose_lungenembolie_5()
        self.thrombose_lungenembolie_6()
        self.blutungsneigung()
        self.wundheilung()
        self.familienanamnese()
        self.familienanamnese_2()
        self.familienanamnese_3()
        self.familienanamnese_4()
        self.operationen()
        self.medikamente()
        self.allergien()
        self.allgemeiner_gesundheitszustand()
        self.akute_infekte()
        self.infektneigung()
        self.infektionskrankheiten()
        self.chronische_krankheiten()
        self.chronische_krankheiten_2()
        self.chronische_krankheiten_3()
        self.chronische_krankheiten_4()
        self.tumor_krebserkrankung()
        self.gewichtsverlust_migraene()
        self.rauchverhalten()
        self.alkoholkonsum()

    def typewrite_with_delay(self, text, min_delay=0.05, max_delay=0.1):
        delay = random.uniform(min_delay, max_delay)
        py.typewrite(text, interval=delay)
    
    def generate_random_monat_thrombose(self):
        thrombose_monat = random.randint(1, 12)
        return str(thrombose_monat)

    def generate_random_jahr_thrombose(self):
        thrombose_jahr = random.randint(1999, 2023)
        return str(thrombose_jahr)

    def generate_random_dose(self):
        dose = random.randint(50, 1000)
        return str(dose)

    def fill_personal_daten(self):
        for _ in range(5):
            py.press('tab')
        time.sleep(0.3)
        py.write(self.form_automation.strasse)
        py.press('tab')
        time.sleep(0.3)

        py.write(self.form_automation.postleitzahl)
        time.sleep(0.3)
        py.press('tab')
        py.write(self.form_automation.wohnort)
        py.press('tab')
        py.write(self.form_automation.telefon)

        for _ in range(2):
            py.press('tab')

        py.write(self.form_automation.gewicht)
        py.press('tab')
        self.typewrite_with_delay(self.form_automation.grosse)
        py.press('tab')

        self.form_automation.select_blutgruppe(self.form_automation.index)
        py.press('tab')
        # Beruf
        py.write(self.form_automation.Beruf)
        py.press('tab')


    def Versichertendaten(self):
        py.press('right')
        py.press('tab')
        py.press('right')
        py.press('tab')
        py.moveTo(x=400, y=760)
        py.click()
        for _ in range(3):
            py.press('tab')
        time.sleep(0.4)
        py.write(self.form_automation.hausarzt)
        py.press('tab')
        time.sleep(0.5)
        py.write (self.form_automation.hausartzt_anchrift)
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')
        

    #Haben Sie schon mal eine Thrombose, Lungenembolie
    def thrombose_lungenembolie(self):
        time.sleep(0.5)
        py.scroll(+10000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = " schon mal eine Thrombose"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press("right")
        py.press('tab')
        py.write(self.thrombose_monat)
        py.press('tab')
        py.write(self.thrombose_jahr)
        py.press('tab')
        py.scroll(-822)

        # Define Group A options (with sub-options)
        group_a_options = [
            ('Oberflächlich', (459, 124)),
            ('Tiefe Beinvenenthrombose', (459, 186)),
            ('Lungenarterienembolie', (459, 243)),
            ('Muskelvenenthrombose', (459, 300)),
            ('Schlüsselbeinvenenthrombose', (459, 358)),
            ('Halsgefäß-/Jugularisthrombose', (459, 418)),
            ('Armvenenthrombose', (459, 475)),
            ('ZVK-/Katheterthrombose', (459, 533)),
            ('Sinusvenenthrombose/Hirnvene', (459, 593)),
            ('Ereignis am Auge', (459, 939)),
        ]

        # Define Group B options (no sub-options, multiple selections allowed)
        group_b_options = [
            ('Mesenterialvenenthrombose', (459, 649)),
            ('Pfortader', (459, 710)),
            ('Lebervenenverschluss', (459, 767)),
            ('Milzin', (459, 821)),
            ('Arterieler', (459, 884))
        ]

        # Define Group C ('Weiß ich nicht', exclusive option)
        group_c_option = ('Weiß ich nicht', (459, 999))

        # Track selected main options
        selected_main_options = []
        sub_option_candidates = []  # Only Group A options will be added here

        # Adjust the probability so that 'Weiß ich nicht' is less likely to be chosen
        option_pool = ['A'] * 4 + ['C']  # 4x chance of selecting from Group A, 1x chance of selecting 'Weiß ich nicht'
        selected_group = random.choice(option_pool)

        if selected_group == 'C':
            # If 'Weiß ich nicht' is selected, only select this option and return
            print(f"Selected Group C option: {group_c_option[0]}")
            py.moveTo(group_c_option[1])
            py.click()
            return  # Skip any other selections and sub-options

        # If Group A is selected
        selected_a_option = random.choice(group_a_options)
        a_option_name, (a_x, a_y) = selected_a_option

        # Click the selected Group A option
        print(f"Selected Group A option: {a_option_name}")
        py.moveTo(a_x, a_y)
        py.click()
        time.sleep(0.5)

        # Add Group A option to sub-option candidates
        sub_option_candidates.append(a_option_name)
        selected_main_options.append(a_option_name)

        # Select multiple Group B options (randomly)
        selected_b_options = random.sample(group_b_options, random.randint(1, len(group_b_options)))
        for b_option_name, (b_x, b_y) in selected_b_options:
            print(f"Selected Group B option: {b_option_name}")
            py.moveTo(b_x, b_y)
            py.click()
            time.sleep(0.5)
            selected_main_options.append(b_option_name)

        # Now handle sub-options after main option selection
        self.handle_selected_sub_options(sub_option_candidates)

    def handle_selected_sub_options(self, sub_option_candidates):
        """
        Handles sub-options for selected Group A options after main options are selected.
        """
        for option in sub_option_candidates:
            if option == 'Oberflächlich':
                self.handle_sub_options_oberflächlich()
            elif option == 'Tiefe Beinvenenthrombose':
                self.handle_sub_options_tiefe_beinvenenthrombose()
            elif option == 'Lungenarterienembolie':
                self.handle_sub_options_lungenarterienembolie()
            elif option == 'Muskelvenenthrombose':
                self.handle_sub_options_muskelvenenthrombose()
            elif option == 'Schlüsselbeinvenenthrombose':
                self.handle_sub_options_schlüsselbeinvenenthrombose()
            elif option == 'Halsgefäß-/Jugularisthrombose':
                self.handle_sub_options_halsgefaess_jugularisthrombose()
            elif option == 'Armvenenthrombose':
                self.handle_sub_options_armvenenthrombose()
            elif option == 'ZVK-/Katheterthrombose':
                self.handle_sub_options_zvk_katheterthrombose()
            elif option == 'Sinusvenenthrombose/Hirnvene':
                self.handle_sub_options_sinusvenenthrombose()
            elif option == 'Ereignis am Auge':
                self.handle_sub_options_ereignis_am_auge()

    # Example sub-option handlers for Group A
    def handle_sub_options_oberflächlich(self):
        print("Handling sub-options for 'Oberflächlich'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=472, y=438)
        time.sleep(1)
        py.click(x=588, y=713)
        py.press('tab')
        py.press('right') 

    def handle_sub_options_tiefe_beinvenenthrombose(self):
        print("Handling sub-options for 'Tiefe Beinvenenthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=432, y=557)
        time.sleep(1)
        py.click(x=491, y=810)
        py.press('tab')
        py.press('right') 
        py.press('right')
        
    def handle_sub_options_lungenarterienembolie(self):
        print("Handling sub-options for 'Lungenarterienembolie'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('right')

    def handle_sub_options_muskelvenenthrombose(self):
        print("Handling sub-options for 'Muskelvenenthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')   
        py.press('tab')
        py.press('right')   
       
        


    def handle_sub_options_schlüsselbeinvenenthrombose(self):
        print("Handling sub-options for 'Schlüsselbeinvenenthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right') 
        py.press('right')   

    def handle_sub_options_halsgefaess_jugularisthrombose(self):
        print("Handling sub-options for 'Halsgefäß-/Jugularisthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
        py.press('right')  
        py.press('right')

    def handle_sub_options_armvenenthrombose(self):
        print("Handling sub-options for 'Armvenenthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
        py.press('right')  
        py.press('right')
        time.sleep(1)

    def handle_sub_options_zvk_katheterthrombose(self):
        print("Handling sub-options for 'ZVK-/Katheterthrombose'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
        py.press('right')

    def handle_sub_options_sinusvenenthrombose(self):
        print("Handling sub-options for 'Sinusvenenthrombose/Hirnvene'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('right')

    def handle_sub_options_ereignis_am_auge(self):
        print("Handling sub-options for 'Ereignis am Auge'")
        time.sleep(0.9)
        py.scroll(-828)
        py.click(x=488, y=908)
        time.sleep(0.8)



    
    #Wie wurde am Ende behandelt?*
    def thrombose_lungenembolie_2(self):
        py.scroll(+10000)
        time.sleep(1.5)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = " wurde am Ende"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.scroll(-300)

        #behandlung options
        behandlung_options = [
            ('Heparinspritzen/Clexane/Innohep usw.', (424, 364)),
            ('Marcumar/Phenprogramm/Coumadin/Sinthrom', (422, 423)),
            ('Xarelto', (417, 479)),
            ('Eliquis', (415, 537)),
            ('Lixiana', (412, 594)),
            ('Pradaxa', (410, 651)),
        ]

        # Define the exclusive options with their coordinates
        exclusive_options = [
            ('Ich habe weder Tabletten', (442, 715)),
            ('weiß ich nicht', (436, 770))
        ]

        # Decide whether to select an exclusive option (20% chance) or non-exclusive options (80% chance)
        if random.randint(1, 5) == 1:
            # 20% chance to select an exclusive option
            selected_option = random.choice(exclusive_options)
            selected_options = [selected_option]
            print(f"Exclusive selection: {selected_option[0]}")
        else:
            # 80% chance to select one or more non-exclusive options
            num_options = random.randint(1, len(behandlung_options))  # At least 1 option
            selected_options = random.sample(behandlung_options, num_options)
            print(f"Selecting options: {[opt[0] for opt in selected_options]}")

        # Click on the selected options
        for option_name, (x, y) in selected_options:
            print(f"Selecting option: {option_name}")
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)  # Slight delay between clicks if multiple options

        time.sleep(1)
        # py.click(x=477, y=971)
        py.scroll(-400)
        py.click(x=463, y=524)
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 7)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        time.sleep(0.2)


    
    def reset_view_to_normal(self):
        """
        Resets the view by scrolling up and zooming the screen back to its normal size.
        """
        # Scroll up to bring the view back
        py.scroll(-850) # You can adjust this scroll amount based on your specific need
        
        # Zoom back to normal size
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)

        time.sleep(0.5)

    def thrombose_lungenembolie_3(self):
        # Adjust the view
        py.scroll(-900)
        py.hotkey('ctrl', '-')
        time.sleep(0.3)
        py.hotkey('ctrl', '-')
        time.sleep(0.3)
        py.hotkey('ctrl', '-')
        time.sleep(0.3)
        py.hotkey('ctrl', '-')
        time.sleep(0.3)
        py.hotkey('ctrl', '-')

        # Define Option 1 (Single selection)
        option_1 = [
            ('Kein Auslöser bekannt', (712, 292)),
            ('Krankheitsaktivität', (690, 734)),
            ('Chronische Polyarthitis', (687, 762)),
            ('Nephrotisches Syndrom', (686, 791)),
            ('Sichelzellanämie', (684, 819)),
            ('Intravenöser', (684, 848)),
            ('Herzinfarkt', (685, 935))
        ]

        # Define Option 2 (Single selection with follow-up action)
        option_2 = [
            ('Krankenhausaufenthalt vor dem Ereignis', (681, 323)),
            ('Gelenkinjektionen/Cortisonspritzen', (680, 410)),
            ('Chemotherapie', (688, 499)),
            ('Antibabypille mit Östrogen', (689, 558)),
            ('Medikamente wie Gerinnungsfaktoren', (689, 616))
        ]

        # Define Option 3 (Single selection with sub-options)
        option_3 = [
            ('Operationen', (678, 379)),
            # ('Unfall/Verletzung', (679, 411)),
            # ('Schwangerschaft', (686, 676)),
            ('Wochenbett', (688, 702)),
            ('Immobilisation', (682, 879)),
            ('Infektion', (688, 905)),
            ('Reise', (681, 965)),
            ('Ungewohnte', (678, 994))
        ]

        # Randomly choose one of the three option groups
        selected_group = random.choice([1, 2, 3])
        selected_option = None

        if selected_group == 1:
            # Select one option from Option 1
            selected_option = random.choice(option_1)
            option_name, (x, y) = selected_option
            print(f"Selected Option 1: {option_name}")
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)  # Ensure the selection is registered
            self.reset_view_to_normal()

        elif selected_group == 2:
            # Select one option from Option 2 and perform follow-up actions
            selected_option = random.choice(option_2)
            option_name, (x, y) = selected_option
            print(f"Selected Option 2: {option_name}")
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)  # Ensure the selection is registered

            # Follow-up action
            py.press('tab')
            py.write("hi test")
            time.sleep(0.5)  # Ensure the follow-up action is processed
            self.reset_view_to_normal()

        elif selected_group == 3:
            # Select one option from Option 3 and handle sub-options
            selected_option = random.choice(option_3)
            option_name, (x, y) = selected_option
            print(f"Selected Option 3: {option_name}")
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)  # Ensure the selection is registered

            # Now handle sub-options for Option 3 after confirming the selection
            self.handle_sub_options(option_name)

    def handle_sub_options(self, option_name):
        """
        Handles the sub-options for Option 3.
        """
        print(f"Handling sub-options for '{option_name}'")

        if option_name == 'Operationen':
            self.handle_operationen_sub_options()
        elif option_name == 'Unfall/Verletzung':
            self.handle_unfall_sub_options()
        elif option_name == 'Schwangerschaft':
            self.handle_schwangerschaft_sub_options()
        elif option_name == 'Wochenbett':
            self.handle_wochenbett_sub_options()
        elif option_name == 'Immobilisation':
            self.handle_immobilisation_sub_options()
        elif option_name == 'Infektion':
            self.handle_infection_sub_options()
        elif option_name == 'Reise':
            self.handle_reise_sub_options()
        elif option_name == 'Ungewohnte':
            self.handle_ungewohnte_sub_options()

    # Define placeholder methods for the sub-options in Option 3

    def handle_operationen_sub_options(self):
        print("Handling sub-options for 'Operationen'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)

        operation_options = [
            ('Knochenbrüche', (442, 581)),
            ('Hüft-/Kniegelenksoperation', (439, 641)),
            ('Bauchoperation', (449, 699)),
            ('Sonstiges', (431, 757))  # Sonstiges ist die letzte Option
        ]
        
        # Wähle zufällig aus, wie viele Optionen ausgewählt werden (1 bis alle)
        num_options_to_select = random.randint(1, len(operation_options))
        
        # Wähle zufällig Optionen aus (eine oder mehrere), aber in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(operation_options, num_options_to_select), key=lambda x: operation_options.index(x))
        
        # Klicke auf jede ausgewählte Option in der Reihenfolge und prüfe, ob "Sonstiges" dabei ist
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)  
            
            # Wenn "Sonstiges" ausgewählt wurde, führe eine zusätzliche Aktion aus
            if option_name == 'Sonstiges':
                py.press('tab')
                py.write('hola sonstiges')


    def handle_unfall_sub_options(self):
        # print("Handling sub-options for 'Unfall/Verletzung'")
        # time.sleep(1)
        # py.scroll(-850)
        # for _ in range(5):
        #     py.hotkey('ctrl', '+')
        #     time.sleep(0.3)
        # time.sleep(0.4)
        # py.click(x=466, y=364)
        pass

    # def handle_schwangerschaft_sub_options(self):
    #     print("Handling sub-options for 'Schwangerschaft'")
    #     time.sleep(1)
    #     for _ in range(5):
    #         py.hotkey('ctrl', '+')
    #         time.sleep(0.3)
    #     py.scroll(-1350)
    #     time.sleep(0.5)
       

    #     schwangerschaft_options = [
    #         ('in welcher Schwangerschaftswoche?', (464, 172)),
    #         ('bzw. wie viele Wochen nach der Fehlgeburt?', (457, 283)),
    #         ('Präeklampsie', (438, 398)),
    #         ('Schwangerschaftsvergiftung', (443, 454)),
    #         ('Gestose', (444, 511)),
    #         ('HELLP-Syndrom', (444, 571)),
    #         ('Geburtsgewicht <2500g', (446, 806)),  # Koordinaten für diese Option fehlen, angenommen!
    #         ('Hyperstimulationssyndrom', (456, 629)),
    #         ('Blutung', (461, 749)),
    #         ('Gewichtszunahme', (446, 806)),
    #         ('Unstillbares S', (448, 859)),
    #         ('Mehrlingsschwangerschaft', (467, 921))
    #     ]

    #     # Zufällige Anzahl von Optionen auswählen (1 bis alle)
    #     num_options_to_select = random.randint(1, len(schwangerschaft_options))
        
    #     # Wähle zufällig Optionen aus und sortiere sie in aufsteigender Reihenfolge
    #     selected_options = sorted(random.sample(schwangerschaft_options, num_options_to_select), key=lambda x: schwangerschaft_options.index(x))

    #     # Klicke jede ausgewählte Option in der Reihenfolge
    #     for option_name, (x, y) in selected_options:
    #         py.moveTo(x, y)
    #         py.click()
    #         time.sleep(0.5)

    #         # Wenn die erste oder zweite Option ausgewählt wird, eine zusätzliche Aktion ausführen
    #         if option_name == 'in welcher Schwangerschaftswoche?' or option_name == 'bzw. wie viele Wochen nach der Fehlgeburt?':
    #             py.press('tab')
    #             py.write('4')  # Beispiel für eine Ausgabe, hier '4' eingeben
    #             time.sleep(0.5)
    #         elif option_name == 'bzw. wie viele Wochen nach der Fehlgeburt?':
    #             py.press('tab')
    #             py.write('4')  # Beispielhafte Eingabe '4'
    #             time.sleep(0.5)


    def handle_wochenbett_sub_options(self):
        print("Handling sub-options for 'Wochenbett'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.2)
        py.click(x=483, y=537)
        py.press('tab')
        py.press('right')
        py.press('right')
        time.sleep(0.5)
        py.press('tab')
        py.press('right')
        py.scroll(-200)

        wochenbett_options = [
            ('Vermehrte Blutung', (495, 695)),
            ('Bluttransfusion', (475, 761)),
            ('Erneute Blutung', (475, 761)),
            ('Infektion', (463, 880))
        ]
        
        # Zufällige Anzahl von Optionen auswählen (1 bis alle)
        num_options_to_select = random.randint(1, len(wochenbett_options))
        
        # Optionen in aufsteigender Reihenfolge auswählen
        selected_options = sorted(random.sample(wochenbett_options, num_options_to_select), key=lambda x: wochenbett_options.index(x))
        
        # Klicken auf die ausgewählten Optionen
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.4)

    def handle_immobilisation_sub_options(self):
        print("Handling sub-options for 'Immobilisation'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.3)
        py.click(x=483, y=537)
        py.press('tab')
        py.press('right')
        py.press('right')


    def handle_infection_sub_options(self):
        print("Handling sub-options for 'Infektion'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.3)
        py.scroll(-400)
        py.click(x=436, y=309)
        time.sleep(0.2)
        py.click(x=441, y=572)
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')
        time.sleep(0.3)
        py.press('right')
        py.press('right')


    def handle_reise_sub_options(self):
        print("Handling sub-options for 'Reise'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.4)
        py.click(x=756, y=566)
        py.press('tab')
        py.press('down')
        py.press('down')

    def handle_ungewohnte_sub_options(self):
        print("Handling sub-options for 'Ungewohnte'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.4)
        py.click(x=436, y=584)


    def thrombose_lungenembolie_4(self):
        py.scroll(+10000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Haben Sie eine weitere Thrombose/Embolie/Ereignis gehabt?"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press("right")
        py.press("right")
        pass
        
    def thrombose_lungenembolie_5(self):
        py.press('tab')
        py.press('right')
        py.scroll(-300)
        time.sleep(0.3)

        # Definiere die Venenerkrankung Optionen mit ihren Koordinaten
        venenerkrankung_options = [
            ('Besenreiser', (431, 684)),
            ('Krampfadern', (430, 741)),
            ('Venenentzündung/Phlebitis', (424, 799)),
            ('Posttrombotisches Syndrom', (434, 856)),
            ('Sonstige', (420, 914))  # Spezielle Behandlung für Sonstige
        ]

        # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        num_options_to_select = random.randint(1, len(venenerkrankung_options))

        # Wähle zufällige Optionen in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(venenerkrankung_options, num_options_to_select), key=lambda x: venenerkrankung_options.index(x))

        # Jede ausgewählte Option anklicken
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.3)

            # Wenn "Sonstige" ausgewählt wurde, zusätzliche Aktion ausführen
            if option_name == 'Sonstige':
                py.press('tab')
                py.write('hi sonstiges')
                
    def thrombose_lungenembolie_6(self):
        time.sleep(1)
        py.scroll(-300)
        time.sleep(0.3)
        py.click(x=586, y=862)
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
                ##a
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        ##b
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        ##
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        ##
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
              ## c
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #c2
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #c3
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)
        #c4
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

        #c5
        py.press('tab')
        num_right_presses = random.randint(1, 3)
        for _ in range(num_right_presses):
            py.press('right')
            time.sleep(0.2)

    def blutungsneigung(self):
        #Nasenbluten
        py.press('tab')
        py.press('right')
        
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.2)

        #Blaue Flecken
        py.press('tab')
        py.press('down')
        py.press('down')
        py.press('down')
        time.sleep(0.2)
        py.press('down')
        py.press('down')
        time.sleep(0.2)

        # py.press('tab')
        # py.press('right')
        
        # py.moveTo(x=1020, y=750)
        # py.click()


        #Blutungneigung bei kleineren Verletzungen
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)

        #NBlutungen in der Mundhöhle
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.2)
        
        #Magen-Darm-Blutungen
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.2)          

        #Blut im Urin/Hämaturie
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.2)

        #Zähne ziehen/Zahnextraktion
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        

        #Chirurgische Eingriffe/Operationen
        py.press('tab')
        py.press('down')
        py.press('down')
        time.sleep(0.3)
        py.press('down')
        py.press('tab')
        py.write("hi")
        time.sleep(0.2)


        # #verstärkte Regelblutung/Hypermenorrhoe
        # py.press('tab')
        # # Generiere eine zufällige Zahl zwischen 1 und 3
        # num_down_presses = random.randint(1, 9)
        
        # # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        # for _ in range(num_down_presses):
        #     py.press('down')
        # time.sleep(0.2)

        # #Blutungen nach der Entbindung/Wochenbett
        # py.press('tab')
        # # Generiere eine zufällige Zahl zwischen 1 und 3
        # num_down_presses = random.randint(1, 5)
        
        # # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        # for _ in range(num_down_presses):
        #     py.press('down')
        # time.sleep(0.2)
        


        #Blutergüsse/Hämatome in Muskeln
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        time.sleep(0.2)

        #Blutergüsse/Hämatome in Gelenken
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        time.sleep(0.2)


        #Hirnblutungen
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 3)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        time.sleep(0.2)


        #andere Blutungsprobleme
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)


    def wundheilung(self):
        time.sleep(0.3)
        py.press('tab')
        py.press('right')
        time.sleep(0.4)
        py.press('tab')
        
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 3)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down')
        
    def familienanamnese(self):
        time.sleep(1)
        py.scroll(+20000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Gibt es in Ihrer Familien folgende Erkrankungen?"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press("right")
        py.scroll(-300)
        #Blutarmut/Anämie/Thalassämie
        
        Blutarmut_options = [
            ('Blutarmut/Anämie ohne Ursache', (444, 550)),
            ('Blutarmut durch Eisenmangel', (434, 609)),
            ('Thalassämie', (434, 668)),
            ('Sichelzellanämie/SCD', (430, 730)),
            ('idk', (414, 785))   # Spezielle Behandlung für Sonstige
        ]

        # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        num_options_to_select = random.randint(1, len(Blutarmut_options))

        # Wähle zufällige Optionen in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(Blutarmut_options, num_options_to_select), key=lambda x: Blutarmut_options.index(x))

        # Jede ausgewählte Option anklicken
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.5)

            # Wenn "Sonstige" ausgewählt wurde, zusätzliche Aktion ausführen
            if option_name == 'idk':
                time.sleep(0.3)
                py.press('tab')
                py.write(' idk')

    def familienanamnese_2(self):
        time.sleep(1)
        py.scroll(-640)
        time.sleep(0.2)
        #thrombose in Familienanamese
        py.click(x=738, y=422)
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')
        py.press('right')
        #herzinfarkt/schalagenfall
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')
        py.press('right')
        py.scroll(-300)
        time.sleep(0.5)
        blutungsneigung_optionen = [
            ('von-Willebrand-Syndrom', (800, 627)),
            ('Fibrinogenmangel', (1205, 632)),
            ('Faktor-VII-Mangel', (457, 688)),
            ('Hämophilie A', (825, 690)),
            ('Hämophilie B', (1212, 690)),
            ('Faktor-X-Mangel', (435, 754)),
            ('Faktor-XI-Mangel', (821, 754)),
            ('Faktor-XII-Mangel', (1217, 754)),
            ('Plättchen', (461, 808))
        ]

        # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        num_options_to_select = random.randint(1, len(blutungsneigung_optionen))

        # Wähle zufällige Optionen in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(blutungsneigung_optionen, num_options_to_select), key=lambda x: blutungsneigung_optionen.index(x))

        # Jede ausgewählte Option anklicken
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()

    #     # Optionen für "bei wem" mit Koordinaten
    #     bei_wem_options = [
    #         ('vater', (409, 441)),
    #         ('schwester', (412, 496)),
    #         ('mutter', (790, 443)),
    #         ('oma', (790, 557)),
    #         ('cousin', (796, 616)),
    #         ('tochter', (1190, 499))
    #     ]

    #     # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
    #     num_options_to_select = random.randint(1, len(bei_wem_options))

    #     # Wähle zufällige Optionen in aufsteigender Reihenfolge
    #     selected_options = sorted(random.sample(bei_wem_options, num_options_to_select), key=lambda x: bei_wem_options.index(x))

    #     # Jede ausgewählte Option anklicken
    #     for option_name, (x, y) in selected_options:
    #         py.moveTo(x, y)
    #         py.click()
    #         time.sleep(0.5)




    def familienanamnese_3(self):
        # py.scroll(-700)

        # thromboseereignisoptionen = [
        #     ('Beinvenenthrombose', (425, 164)),
        #     ('Lungenembolie', (429, 219)),
        #     ('Sonstiges', (429, 278))  # Spezielle Behandlung für Sonstiges
        # ]

        # # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        # num_options_to_select = random.randint(1, len(thromboseereignisoptionen))

        # # Wähle zufällige Optionen in aufsteigender Reihenfolge
        # selected_options = sorted(random.sample(thromboseereignisoptionen, num_options_to_select), key=lambda x: thromboseereignisoptionen.index(x))

        # # Jede ausgewählte Option anklicken
        # for option_name, (x, y) in selected_options:
        #     py.moveTo(x, y)
        #     py.click()
        #     time.sleep(0.5)

        #     # Wenn "Sonstiges" ausgewählt wurde, zusätzliche Aktion ausführen
        #     if option_name == 'Sonstiges':
        #         py.moveTo(695, 454)  # moveto coordinates
        #         py.click()
        #         time.sleep(0.5)
        pass


    def familienanamnese_4(self):
        # time.sleep(0.3)
        # py.click(x=675, y=426)
        # py.press('tab')
        # py.press('right')
        # py.press('tab')
        # py.press('right')
        # #herzinfarkt/schalagenfall
        # py.press('tab')
        # py.press('right')
        # py.press('right')
        # py.press('tab')
        # py.press('right')
        # time.sleep(0.4)
        # blutungsneigung_optionen = [
        #     ('von-Willebrand-Syndrom', (800, 644)),
        #     ('Fibrinogenmangel', (1205, 645)),
        #     ('Faktor-VII-Mangel', (457, 702)),
        #     ('Hämophilie A', (810, 703)),
        #     ('Hämophilie B', (1203, 703)),
        #     ('Faktor-X-Mangel', (426, 758)),
        #     ('Faktor-XI-Mangel', (821, 761)),
        #     ('Faktor-XII-Mangel', (1217, 760)),
        #     ('Plättchen', (461, 818))
        # ]

        # # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        # num_options_to_select = random.randint(1, len(blutungsneigung_optionen))

        # # Wähle zufällige Optionen in aufsteigender Reihenfolge
        # selected_options = sorted(random.sample(blutungsneigung_optionen, num_options_to_select), key=lambda x: blutungsneigung_optionen.index(x))

        # # Jede ausgewählte Option anklicken
        # for option_name, (x, y) in selected_options:
        #     py.moveTo(x, y)
        #     py.click()
        #     time.sleep(0.5)
        pass
 
    def operationen(self):
        time.sleep(1)
        py.scroll(+20000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Wurden Sie schonmal operiert (auch Zahnbehandlungen)"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press('right')
        py.press('right')


    def medikamente(self):
        # #Haben Sie eine Hormonspirale/Kupferspirale?
        time.sleep(0.3)
        py.press('tab')
        py.press('right')
        py.press('tab')
        py.press('right')

        #medikammente read datei
        py.press('tab')
        with open('Medikamente.txt', 'r') as file:
            medikamente = file.readlines()

        # Schritt 2: Bereinige die Medikamente (entferne Leerzeichen und Zeilenumbrüche)
        medikamente = [med.strip() for med in medikamente]

        # Schritt 3: Wähle ein zufälliges Medikament aus der Liste
        random_medikament = random.choice(medikamente)

        # Schritt 4: Verwende pyautogui, um das zufällige Medikament zu schreiben
        time.sleep(0.4)  # Optional: Verzögerung vor dem Schreiben
        py.write(random_medikament)
        py.press('tab')
        time.sleep(0.3)
        py.write(self.dose)
        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1,3)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")
        py.press('tab')
        py.write('hallo Bemerkung')
        time.sleep(0.2)
        py.press('tab')
        py.press('tab')
        py.press('tab')
        py.press('right')
        time.sleep(0.2)
        py.press('tab')
        py.press('right')
        py.press('tab')
        py.press("enter")
        num_down_presses = random.randint(1,4)
        for _ in range(num_down_presses):
            py.press('down')
            time.sleep(0.2)
        py.press("enter")


    def allergien(self):
        time.sleep(1)
        py.scroll(+20000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Haben Sie Allergien?"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        py.press("right")
        py.scroll(-720)

        time.sleep(0.4)
        allergie_optionen = [
            ('Heuschnupfen', (433, 539)),
            ('Allergie durch Stoffe am Arbeitsplatz', (433, 594)),
            ('Tierhaarallergie', (424, 653)),
            ('Kontaktallergie', (1021, 593)),
            ('Hausstauballergie', (427, 706)),
            ('Urtikaria/Nesselsucht/Quincke', (1021, 535)),
            ('Insektenstichallergie', (1021, 652)),
            ('Sonnenallergie', (1021, 711))
        ]

        # Zufällige Anzahl der Optionen (1 bis alle) zur Auswahl
        num_options_to_select = random.randint(1, len(allergie_optionen))

        # Wähle zufällige Optionen in aufsteigender Reihenfolge
        selected_options = sorted(random.sample(allergie_optionen, num_options_to_select), key=lambda x: allergie_optionen.index(x))

        # Jede ausgewählte Option anklicken
        for option_name, (x, y) in selected_options:
            py.moveTo(x, y)
            py.click()
            time.sleep(0.3)


    def allgemeiner_gesundheitszustand(self):
        time.sleep(1)
        py.scroll(+20000)
        time.sleep(2)
        py.hotkey('ctrl', 'f')
        time.sleep(1)
        search_word = "Wie würden Sie Ihren Gesundheitszustand im Allgemeinen beschreiben?"
        py.write(search_word)
        time.sleep(1)
        py.press("esc")
        py.press("tab")
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 5)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
    

    def akute_infekte(self):
        py.press("tab")
        py.press("right")
        py.press("tab")
        py.write('Test')
        time.sleep(0.5)

    def infektneigung(self):
        py.press("tab")
        time.sleep(0.3)
        py.press("right")
        py.press("tab")
        #random jahr
        time.sleep(0.3)
        py.write(self.thrombose_jahr)
        py.press("tab")
        py.press("right")
        py.press('tab')
        # Generiere eine zufällige Zahl zwischen 1 und 3
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)

        #husten
        py.press("tab")
        py.press("right")
        #shnupfen
        time.sleep(0.3)
        py.press("tab")
        py.press("right")
        #fiber
        py.press("tab")
        py.press("right")
        py.press('tab')
        num_down_presses = random.randint(1, 3)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        #epidoden
        py.press('tab')
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('down') 
            time.sleep(0.4)
        #Lungenentzündungen
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.press("right")
       #Mittelohrentzündung?
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.2)
        #Infektionen der Haut
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.write('test')
        #Lymphknotenschwellungen?
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.write('test2')
        #Durchfall/Diarrhö
        py.press("tab")
        py.press("right")
        py.press('tab')
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('right') 
            time.sleep(0.4)
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        #
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        #
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.scroll(-500)
        py.click (x=423, y=541)
        time.sleep(0.3)
        py.press("tab")
        py.write("Test impf")
        py.press("tab")
        py.press("tab")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.write("Test hauter")

    def infektionskrankheiten(self):
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.4)

    def chronische_krankheiten(self):
        py.press("tab")
        py.press("right")
        time.sleep(0.4)
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.4)
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.4)

    def chronische_krankheiten_2(self):
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.4)
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.4)
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.4)

    def chronische_krankheiten_3(self):
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.4)
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.4)
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.4)
    def chronische_krankheiten_4(self):
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.4)
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.4)


    def tumor_krebserkrankung(self):
        py.press("tab")
        py.press("right")
        time.sleep(0.4)
    def gewichtsverlust_migraene(self):
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.3)
        py.press("tab")
        py.press("right")
        py.press("tab")
        py.write(self.thrombose_monat)
        time.sleep(0.2)
        py.press("tab")
        py.write(self.thrombose_jahr)
        time.sleep(0.2)

    def rauchverhalten(self):
        py.press("tab")
        py.press("right")
        py.press("right")
        time.sleep(0.4)
        py.press('tab') 
        #
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('right') 
            time.sleep(0.3)
        
        #jahr
        py.press('tab') 
        py.write(self.thrombose_jahr)
        time.sleep(0.2)
        py.press('tab') 
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('right') 
            time.sleep(0.3)
        py.press('tab') 
        py.write("2009")
        time.sleep(0.2)


    def alkoholkonsum(self):
        py.press('tab') 
        time.sleep(0.2)
        py.press('right') 
        time.sleep(0.2)
        num_down_presses = random.randint(1, 3)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('right') 
            time.sleep(0.3)
        py.press('tab') 
        time.sleep(0.2)
        py.press('right') 
        time.sleep(0.2)
        num_down_presses = random.randint(1, 4)
        
        # Drücke die 'down'-Taste die zufällige Anzahl von Malen
        for _ in range(num_down_presses):
            py.press('right') 
            time.sleep(0.3)
        py.press("tab")
        py.press("right")


        #ende
        py.press("tab")
        time.sleep(4)
        py.press("tab")
        py.press("tab")
        py.press("enter")
        time.sleep(4)
        py.hotkey('ctrl', 'r')
        

if __name__ == "__main__":
    for i in range(1, 3):
        automation = FormAutomation(i)
        automation.run()
