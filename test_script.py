"""

Content here for testing


"""


def test_func(value):
    if value == "String":
        return True
    elif value == 4:
        return False
    else:
        print("any string")

testvar = "String"
test_out = test_func(testvar)
print(test_out)

