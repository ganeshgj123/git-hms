from Utilities.ui_helpers import UiHelpers
from Utilities.excel_reader import attach_locator




@attach_locator("homepage")
class Homepage(UiHelpers):


    # patient_login = ("xpath",'//a[@href="hms/user-login.php"]')
    # doctor_login = ("xpath",'//a[@href="hms/doctor/"]')
    # admin_login_ = ("xpath",'//a[@href="hms/admin"]')


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    def patients_login(self):
        self.click_element(self.patient_login)

    def doctors_login(self):
        self.click_element(self.doctor_login)


    def admin_login(self):
        print("executing POM method in home page")
        self.click_element(self.admin_login_)


















































"""

l = [15,-3,10,2,7,5,18,-6]
def find_indices_hash_map(numbers, target):
    index_map = {}
    pairs = []

    for i, num in enumerate(numbers):
        complement = target - num

        if complement in index_map:
            # If complement is in the map, append the pair to results
            pairs.append((index_map[complement], i))

        # Add the current number and its index to the map
        if num not in index_map:  # Ensures each number is stored only once
            index_map[num] = i

    return pairs


# Example usage
#numbers = [2, 7, 11, 15, -1, 8, 1, 9]
target = 17
result = find_indices_hash_map(l, target)

if result:
    print(f"Indices with target sum {target} are {result}")
else:
    print(f"No indices found with target sum {target}")
"""



"""

import itertools

def find_target_sum(iterable, target):
    s = []
    # Iterate over all possible subset sizes
    for r in range(1, len(iterable) + 1):
        # Generate all subsets of size r
        for subset in itertools.combinations(iterable, r):
            if sum(subset) == target:
                s.append(subset)
    return s

#numbers = [1, 2, 3, 7, 5]
l2 = [15,-3,10,2,7,5,18,-6]

target = 14
result = find_target_sum(l2, target)
print(result)

"""







