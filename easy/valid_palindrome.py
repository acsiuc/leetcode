
s="0P"

def isPalindrome(s):
    palindrome = ''

    for x in s:
        if x.isalnum():
            palindrome+=x.lower()

    for index, character in enumerate(palindrome):
        if index <= len(palindrome)//2:
            if character == palindrome[-index-1]:
                pass
            else:
                return False


    return True


if __name__ == "__main__":
    print(isPalindrome(s))