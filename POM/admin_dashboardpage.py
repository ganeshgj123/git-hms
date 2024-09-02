from Utilities.ui_helpers import UiHelpers
from Utilities.excel_reader import attach_locator


# //span[normalize-space()='Doctor Specialization']


@attach_locator("dashboard")
class AdminDashboardPage(UiHelpers):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_doc_specialisation_page(self):
        print("executing verify_doctor_specialisation_page method")
        self.click_element(self.doctors)
        self.click_element(self.doctors_spec)

    def verify_specialisation_page_visible(self):
        return self.check_element_visible(self.doc_spec_page)



    def create_doctor_specialisation(self,doctor_specialisation):
        print("executing verify_created_doctor_specialisation method")
        self.enter_text(self.txt_doc_spec,value=doctor_specialisation)
        self.click_element_without_script(self.doc_spec_btn)

    def verify_created_doctor_specialisation(self):
        return self.check_element_visible(self.cnf_doc_spec)


    def click_doctors(self):
        self.click_element_without_script(self.doctors)


    def click_manage_doctor(self):
        self.click_element_without_script(self.manage_doc_btn)

    def verify_manage_doctors_page(self):
        return self.click_element_without_script(self.txt_manage_doc_page)

    def click_update_button(self,specialisation):
        self.click_clement_dynamic_path(value=specialisation)


    def update_doctor_specialisation(self,specialisation,address,doctor_fee,doctor_contact):
        self.select_option(self.select_doc_spec,value=specialisation)
        self.enter_text(self.clinic_address,value=address)
        self.enter_text(self.doc_fee,value=doctor_fee)
        self.enter_text(self.doc_contact,value=doctor_contact)
        self.click_element_without_script(self.update_btn)

    def verify_doctor_specialisation_page(self):
        self.get_text_from_element(self.success_msg)



















from re import findall

#1st problem
s = "R2004P66A N1G2R33J11"

individual_sum = [int(i) for i in findall(r"\d",s)]
# print(sum(individual_sum))

consecutive_sum = sum([int(i) for i in findall(r"\d+",s)])
# print(consecutive_sum)

sum_of_two_consecutive_no = sum([int(i) for i in findall(r"\d{2}",s)])
# print(sum_of_two_consecutive_no)


#2nd problem
st = "The policy number is P-100046/00"
policy_number = findall(r"P-\d{6}/\d{2}",st)
# print(policy_number)



#3rd problem
s = "Roopa Nagaraj"
# print(" ".join(s.split()[::-1]))
w = s.split()[::-1]
last = w.pop()
first = w.insert(0,last)
#print(" ".join(w))


#4th problem
s1 = "a2c1b3"
#o/p = "aacbbb"

l = findall(r"[a-z]",s1)
d = [int(i) for i in findall(r"\d",s1)]
# for i,j in zip(l,d):
#     print(f"{i}"*j,end="")


#alternative solution

def decode_string(s1):
    result = ""
    current_char = ""

    for char in s1:
        if char.isalpha():
            current_char = char
        elif char.isdigit():
            result += current_char * int(char)
    return result

#print(decode_string(s1))








