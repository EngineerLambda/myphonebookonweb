def calculate_age(yob: int | str):
    """A function that accepts a person's year of birth and returns their age"""
    age = 2026 - int(yob)
    # return age value
    return age

# test with sample year of births
age_yomi = calculate_age("2002")
age_kemi = calculate_age(2005)

# print out the test result
print(age_yomi)
print(age_kemi)