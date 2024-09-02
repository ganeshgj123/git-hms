from typing import Self
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.support import expected_conditions as EC




def _wait(func):
    def wrapper(instance: Self, locator:tuple[str,str], MAX_TIMEOUT=10, **kwargs: dict[str:str]):
        w = WebDriverWait(instance.driver,MAX_TIMEOUT).until(EC.visibility_of_element_located(locator))
        print("executing webdriver wait")
        try:
            if w.is_enabled():
                return func(instance,locator,**kwargs)
        except TimeoutException:
            print("Timed out the element is not visible")
    return wrapper



def __wait(cls):
    for key,value in cls.__dict__.items():
        if callable(value) and key != "__init__":
            setattr(cls,key,_wait(value))
    return cls


@__wait
class UiHelpers:

    def __init__(self,driver):
        self.driver = driver


    def check_element_visible(self, locator: tuple[str, str]) -> bool:
           for _ in range(5):
                try:
                    if self.driver.find_element(*locator).is_displayed():
                        return True
                except TimeoutException:
                    sleep(1)
                    continue
           return False


    def get_text_from_element(self,locator: tuple[str, str]):
        try:
            self.driver.find_element(*locator).text
        except NoSuchElementException:
            print(f"no element found")



    def click_element(self,locator:tuple[str,str]):
        print("executing common method in UIHelper")
        element = self.driver.find_element(*locator)
        # Scroll to the element
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_element_without_script(self, locator: tuple[str, str]):
        print("executing common method in UIHelper")
        element = self.driver.find_element(*locator)
        element.click()

    def click_clement_dynamic_path(self,value:str):
        try:
            _xpath = f"//td[text()='{value}']/ancestor::tr//a[@class='btn btn-transparent btn-xs']"
            element = self.driver.find_element("xpath",_xpath)
            element.click()
        except NoSuchElementException:
            print("element not found")




    # def scroll_to_element(self,locator:tuple[str,str]):
    #     element = self.driver.find_element(*locator)
    #     # Scroll to the element
    #     self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def enter_text(self,locator:tuple[str,str],*,value:str):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    def select_option(self,locator:tuple[str,str],*,value:str):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(value)












"""
# Method 1: Using XPath to locate the text
try:
    element = driver.find_element(By.XPATH, f"//*[contains(text(), '{search_text}')]")
    print(f"Text found: {element.text}")
except:
    print("Text not found using XPath")
"""













    #
        # try:
        #     element = self.driver.find_element("xpath", "(//a[text()='Click Here'])[3]")
        #     a = ActionChains(self.driver)
        #     self.driver.execute_script("arguments[0].scrollIntoView();", element)
        #     a.move_to_element(element).click().perform()
        #     sleep(5)
        # except ElementClickInterceptedException:
        #     print("nothing")
        #
        #
        #
        # # self.driver.find_element("xpath","//input[@name='username']").clear()
        # # self.driver.find_element("xpath","//input[@name='username']").send_keys("sdsja")
        #

















"""

s = "aaabbcdddaaadd"
#o/p = 3a2b1c3d1a


def string_counter(string):
    output = ""
    cur_char = string[0]
    count = 1
    for i in range(1,len(string)):
        if string[i] == cur_char:
            count += 1
        else:
            output += str(count) + cur_char
            cur_char = string[i]
            count = 1
    print(cur_char,count)
    output += str(count) + cur_char

    return output

print(string_counter(s))

"""





"""

count = 0

def decorator(func):
    def wrapper(*args,**kwargs):
        global count
        func(*args, **kwargs)
        count += 1
        print(count)
    return wrapper

@decorator
def some_method():
    print("calling decorated method")

# some_method()
# some_method()
# some_method()
# some_method()




d ={}
def decorator(func):
    def wrapper(*args,**kwargs):
        func_name = func.__name__
        if func_name not in d:
            d[func_name] = 0
        d[func_name] += 1
        print(d)
        print(f"function {func.__name__} executed {d[func.__name__]} times")
        func(*args, **kwargs)
    return wrapper


@decorator
def some_method():
    print("calling decorated method")

@decorator
def some_method2():
    print("calling 2nd decorated method")

#
# some_method()
# some_method()
#
# some_method2()
# some_method2()
# some_method2()
#

s = "something python"
# print(s.find("python"))





def finder(original_str,sub_str,occurance):
    f_occ = original_str.find(sub_str)
    while f_occ >= 0 and occurance >1:
        f_occ = original_str.find(sub_str,len(sub_str)+f_occ)
        occurance -= 1
    return f_occ

print(finder(s,"python",2))


"""


