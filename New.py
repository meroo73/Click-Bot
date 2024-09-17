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
        time.sleep(6)
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

        time.sleep(1)  # 
    
        


class Männlich:
    
    def __init__(self, form_automation):
        self.form_automation = form_automation
        self.thrombose_monat = self.generate_random_monat_thrombose()  
        self.thrombose_jahr = self.generate_random_jahr_thrombose()

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
        self.blutungsneigung()
        self.wundheilung()
        self.familienanamnese()
        self.operationen()
        self.medikamente()
        self.allergien()
        self.allgemeiner_gesundheitszustand()
        self.akute_infekte()
        self.infektneigung()
        self.infektionskrankheiten()
        self.chronische_krankheiten()
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
            ('Auffälligkeiten Vorgeschichte', (497, 621)),
            ('Sonstiges', (432, 677))
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
        
        elif option_name == 'Sonstiges':
            self.handle_sub_options_sonstiges()

        # You can add logic for 'Sonstiges' if necessary

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
            ('Blutungsneigung in der Familie', (482, 774)),
            ('Sonstiges in der Familie', (482, 829))
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
            ('zu viel Blutplättchen', (457, 685)),
            ('zu viele rote Blutkörperchen', (457, 742)),
            ('zu viele weiße Blutkörperchen', (457, 802)),
            ('Infektneigung/Immundefekt', (457, 860)),
            ('Sonstiges', (457, 918))
        ]

        # Randomly select and click a sub-option
        selected_sub_option = random.choice(auffaelligkeiten_vorgeschichte_sub_options)
        sub_option_name, (x, y) = selected_sub_option

        print(f"Selected sub-option: {sub_option_name}")
        py.moveTo(x, y)
        py.click()
        time.sleep(0.5)

    def handle_sub_options_vieleRote(self):
        pass
    def handle_sub_options_vieleWeise(self):
        pass

    def handle_sub_options_sonstiges(self):
        time.sleep(1)
        py.press('tab')
        py.write("hi sonstiges")
        time.sleep(1)
        
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
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=472, y=438)
        time.sleep(1)
        py.click(x=491, y=810)
        py.press('tab')
        py.press('right') 

    def handle_sub_options_tiefe_beinvenenthrombose(self):
        print("Handling sub-options for 'Tiefe Beinvenenthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=472, y=438)
        time.sleep(1)
        py.click(x=491, y=810)
        py.press('tab')
        py.press('right') 

    def handle_sub_options_lungenarterienembolie(self):
        print("Handling sub-options for 'Lungenarterienembolie'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')   
        


    def handle_sub_options_muskelvenenthrombose(self):
        print("Handling sub-options for 'Muskelvenenthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')   
        py.press('right')  
        py.press('tab')
        py.press('right') 
        py.press('right') 

    def handle_sub_options_schlüsselbeinvenenthrombose(self):
        print("Handling sub-options for 'Schlüsselbeinvenenthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')   

    def handle_sub_options_halsgefaess_jugularisthrombose(self):
        print("Handling sub-options for 'Halsgefäß-/Jugularisthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')   
        time.sleep(1)

    def handle_sub_options_armvenenthrombose(self):
        print("Handling sub-options for 'Armvenenthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')   

    def handle_sub_options_zvk_katheterthrombose(self):
        print("Handling sub-options for 'ZVK-/Katheterthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right') 
        py.press('right') 
        py.press('right') 

    def handle_sub_options_sinusvenenthrombose(self):
        print("Handling sub-options for 'Sinusvenenthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')

    def handle_sub_options_ereignis_am_auge(self):
        print("Handling sub-options for 'Ereignis am Auge'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=462, y=734)
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
        py.press('down')
        py.press('down')
    


         
         
    
       

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
            ('Gelenkinjektionen/Cortisonspritzen', (680, 440)),
            ('Chemotherapie', (688, 499)),
            ('Antibabypille mit Östrogen', (689, 558)),
            ('Medikamente wie Gerinnungsfaktoren', (689, 616))
        ]

        # Define Option 3 (Single selection with sub-options)
        option_3 = [
            ('Operationen', (678, 379)),
            ('Unfall/Verletzung', (679, 411)),
            ('Schwangerschaft', (686, 676)),
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

    def handle_unfall_sub_options(self):
        print("Handling sub-options for 'Unfall/Verletzung'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)
        py.click(x=443, y=584)


    def handle_schwangerschaft_sub_options(self):
        print("Handling sub-options for 'Schwangerschaft'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)

    def handle_wochenbett_sub_options(self):
        print("Handling sub-options for 'Wochenbett'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
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




    def handle_infection_sub_options(self):
        print("Handling sub-options for 'Infektion'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)

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
        py.press('down')
        py.press('down')

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
        pass
    
    def thrombose_lungenembolie_5(self)
        pass
    
    def blutungsneigung(self):
        pass

    def wundheilung(self):
        # time.sleep(0.3)
        # py.press('tab')
        # py.press('right')
        # py.press('tab')
        # py.press('down')
        pass


    def familienanamnese(self):
        # #Blutarmut
        # py.press('tab')
        # py.press('right')
        # py.press('right')
        # #Thrombosen
        # py.press('tab')
        pass

    def operationen(self):
        pass

    def medikamente(self):
        pass

    def allergien(self):
        pass

    def allgemeiner_gesundheitszustand(self):
        pass

    def akute_infekte(self):
        pass

    def infektneigung(self):
        pass

    def infektionskrankheiten(self):
        pass

    def chronische_krankheiten(self):
        pass

    def tumor_krebserkrankung(self):
        pass

    def gewichtsverlust_migraene(self):
        pass

    def rauchverhalten(self):
        pass

    def alkoholkonsum(self):
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
        self.blutungsneigung()
        self.wundheilung()
        self.gynaekologische_anamnese()
        self.familienanamnese()
        self.operationen()
        self.medikamente()
        self.allergien()
        self.allgemeiner_gesundheitszustand()
        self.akute_infekte()
        self.infektneigung()
        self.infektionskrankheiten()
        self.chronische_krankheiten()
        self.tumor_krebserkrankung()
        self.gewichtsverlust_migraene()
        self.rauchverhalten()
        self.alkoholkonsum()

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

    def vorstellungsgrund(self):
        
        # Define 'Vorstellungsgrund Warum' options with their coordinates
        vorstellungsgrund_warum_options = [
            ('Auffälligkeiten/Ereignisse in der Familie', (504, 571)),
            ('Kinderwunsch', (478, 623)),
            ('Wunsch', (478, 683)),
            ('Auffälligkeiten Vorgeschichte', (459, 736)),
            ('Sonstiges', (410, 803))
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
        
        elif option_name == 'Sonstiges':
            self.handle_sub_options_sonstiges()

        # Add more elif blocks for other options if needed...

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
            ('Blutungsneigung in der Familie', (477, 882)),
            ('Sonstiges in der Familie', (482, 949))
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
            ('zu viel Blutplättchen', (457, 685)),
            ('zu viele rote Blutkörperchen', (457, 742)),
            ('zu viele weiße Blutkörperchen', (457, 802)),
            ('Infektneigung/Immundefekt', (457, 860)),
            ('Sonstiges', (457, 918))
        ]

        # Randomly select and click a sub-option
        selected_sub_option = random.choice(auffaelligkeiten_vorgeschichte_sub_options)
        sub_option_name, (x, y) = selected_sub_option

        print(f"Selected sub-option: {sub_option_name}")
        py.moveTo(x, y)
        py.click()
        time.sleep(0.5)
    
    def handle_sub_options_sonstiges(self):
        time.sleep(1)
        py.press('tab')
        py.write("hi sonstiges")
        time.sleep(1)
        
    

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
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=472, y=438)
        time.sleep(1)
        py.click(x=491, y=810)
        py.press('tab')
        py.press('right') 
        py.press('right') 

    def handle_sub_options_tiefe_beinvenenthrombose(self):
        print("Handling sub-options for 'Tiefe Beinvenenthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=472, y=438)
        time.sleep(1)
        py.click(x=491, y=810)
        py.press('tab')
        py.press('right') 
        

    def handle_sub_options_lungenarterienembolie(self):
        print("Handling sub-options for 'Lungenarterienembolie'")
        # Logic for sub-options for 'Lungenarterienembolie'

    def handle_sub_options_muskelvenenthrombose(self):
        print("Handling sub-options for 'Muskelvenenthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')   
        py.press('tab')
        py.press('right') 
        py.press('right')

    def handle_sub_options_schlüsselbeinvenenthrombose(self):
        print("Handling sub-options for 'Schlüsselbeinvenenthrombose'")
        # Logic for sub-options for 'Schlüsselbeinvenenthrombose'

    def handle_sub_options_halsgefaess_jugularisthrombose(self):
        print("Handling sub-options for 'Halsgefäß-/Jugularisthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
        py.press('right')  
        time.sleep(1)
    


    def handle_sub_options_armvenenthrombose(self):
        print("Handling sub-options for 'Armvenenthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
        py.press('right')  

    def handle_sub_options_zvk_katheterthrombose(self):
        print("Handling sub-options for 'ZVK-/Katheterthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
       

    def handle_sub_options_sinusvenenthrombose(self):
        print("Handling sub-options for 'Sinusvenenthrombose/Hirnvene'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
        

    def handle_sub_options_ereignis_am_auge(self):
        print("Handling sub-options for 'Ereignis am Auge'")
        time.sleep(1.2)
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
        py.press('down')
        py.press('down')
        py.press('down')
    
    
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
            ('Unfall/Verletzung', (679, 411)),
            ('Schwangerschaft', (686, 676)),
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

    def handle_unfall_sub_options(self):
        print("Handling sub-options for 'Unfall/Verletzung'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)
        py.click(x=450, y=640)

    def handle_schwangerschaft_sub_options(self):
        print("Handling sub-options for 'Schwangerschaft'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)

    def handle_wochenbett_sub_options(self):
        print("Handling sub-options for 'Wochenbett'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
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
        pass
    
    def thrombose_lugenembolie_5(self)
        pass

    def blutungsneigung(self):
        pass

    def wundheilung(self):

        pass

    def gynaekologische_anamnese(self):
        pass

    def familienanamnese(self):
        pass

    def operationen(self):
        pass

    def medikamente(self):
        pass

    def allergien(self):
        pass

    def allgemeiner_gesundheitszustand(self):
        pass

    def akute_infekte(self):
        pass

    def infektneigung(self):
        pass

    def infektionskrankheiten(self):
        pass

    def chronische_krankheiten(self):
        pass

    def tumor_krebserkrankung(self):
        pass

    def gewichtsverlust_migraene(self):
        pass

    def rauchverhalten(self):
        pass

    def alkoholkonsum(self):
        pass



#GESCHLECHT DIVERS CLASS
class Divers:
    
    def __init__(self, form_automation):
        self.form_automation = form_automation
        self.thrombose_monat = self.generate_random_monat_thrombose()  
        self.thrombose_jahr = self.generate_random_jahr_thrombose()

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
        self.blutungsneigung()
        self.wundheilung()
        self.gynaekologische_anamnese()
        self.familienanamnese()
        self.operationen()
        self.medikamente()
        self.allergien()
        self.allgemeiner_gesundheitszustand()
        self.akute_infekte()
        self.infektneigung()
        self.infektionskrankheiten()
        self.chronische_krankheiten()
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
        py.write (self.form_automation.hausartzt_anchrift)
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('tab')
        

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
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=472, y=438)
        time.sleep(1)
        py.click(x=491, y=810)
        py.press('tab')
        py.press('right') 

    def handle_sub_options_tiefe_beinvenenthrombose(self):
        print("Handling sub-options for 'Tiefe Beinvenenthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=472, y=438)
        time.sleep(1)
        py.click(x=470, y=557)
        py.press('tab')
        py.press('right') 
        py.press('right')
        
    def handle_sub_options_lungenarterienembolie(self):
        print("Handling sub-options for 'Lungenarterienembolie'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('right')

    def handle_sub_options_muskelvenenthrombose(self):
        print("Handling sub-options for 'Muskelvenenthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')   
        py.press('tab')
        py.press('right')   
       
        


    def handle_sub_options_schlüsselbeinvenenthrombose(self):
        print("Handling sub-options for 'Schlüsselbeinvenenthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right') 
        py.press('right')   

    def handle_sub_options_halsgefaess_jugularisthrombose(self):
        print("Handling sub-options for 'Halsgefäß-/Jugularisthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
        py.press('right')  
        py.press('right')

    def handle_sub_options_armvenenthrombose(self):
        print("Handling sub-options for 'Armvenenthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
        py.press('right')  
        py.press('right')
        time.sleep(1)

    def handle_sub_options_zvk_katheterthrombose(self):
        print("Handling sub-options for 'ZVK-/Katheterthrombose'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
        py.press('right')

    def handle_sub_options_sinusvenenthrombose(self):
        print("Handling sub-options for 'Sinusvenenthrombose/Hirnvene'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=518, y=396)
        py.press('tab')
        py.press('right')
        py.press('right')
        py.press('right')

    def handle_sub_options_ereignis_am_auge(self):
        print("Handling sub-options for 'Ereignis am Auge'")
        time.sleep(1.2)
        py.scroll(-828)
        py.click(x=488, y=908)
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
        py.press('down')
        py.press('down')
        py.press('down')
        py.press('down')
        py.press('down')

    
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
            ('Unfall/Verletzung', (679, 411)),
            ('Schwangerschaft', (686, 676)),
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

    def handle_unfall_sub_options(self):
        print("Handling sub-options for 'Unfall/Verletzung'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)
        py.click(x=466, y=700)

    def handle_schwangerschaft_sub_options(self):
        print("Handling sub-options for 'Schwangerschaft'")
        time.sleep(1)
        py.scroll(-900)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)


    def handle_wochenbett_sub_options(self):
        print("Handling sub-options for 'Wochenbett'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
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
        py.press('down')

    def handle_ungewohnte_sub_options(self):
        print("Handling sub-options for 'Ungewohnte'")
        time.sleep(1)
        py.scroll(-850)
        for _ in range(5):
            py.hotkey('ctrl', '+')
            time.sleep(0.3)
        time.sleep(0.5)
        py.click(x=436, y=584)

    def thrombose_lungenembolie_4(self):
        time.sleep(1)
        py.press('tab')
        py.press('right')
    
    def thrombose_lungenembolie_5(self):
        
    
    def blutungsneigung(self):
        pass

    def wundheilung(self):
        pass

    def gynaekologische_anamnese(self):
        pass

    def familienanamnese(self):
        pass

    def operationen(self):
        pass

    def medikamente(self):
        pass

    def allergien(self):
        pass

    def allgemeiner_gesundheitszustand(self):
        pass

    def akute_infekte(self):
        pass

    def infektneigung(self):
        pass

    def infektionskrankheiten(self):
        pass

    def chronische_krankheiten(self):
        pass

    def tumor_krebserkrankung(self):
        pass

    def gewichtsverlust_migraene(self):
        pass

    def rauchverhalten(self):
        pass

    def alkoholkonsum(self):
        pass


if __name__ == "__main__":
    for i in range(1, 2):
        automation = FormAutomation(i)
        automation.run()

