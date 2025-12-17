def function_1():
    """
    Docstring for function_1

    takes a text and makes the first letter of each word capital
    """
    return "output is this".title()  #return
    print("Hello world!")    #doesn't get print

print(function_1())

# ************************************************************************

def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "empty strings received"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formatted_name = format_name(input("what is your name?"), input("what is your last name?"))

print((formatted_name))