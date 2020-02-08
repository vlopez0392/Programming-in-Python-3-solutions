### SECTION 10 - Errors and Exceptions Handling
### Unit test library -> Unit test allows you to write your own test program. Goal is to send a specific set of data to
### your program, analyze the return results and see if it returns the expected results.

"""
Cap.py - A simple script that capitalizes the first letter of each word in an input String.
"""

def cap_text(text):
    return text.title() ##Had you used the capitalize() method, your test result would show Fail.
                        ##capitalize() only capitalizes the first letter of your string, while title() capitalizes each!

