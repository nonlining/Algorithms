# python2

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = raw_input()
    opening_brackets_stack = []
    wrongid = 0
    false = 0
    for i, next in enumerate(text):
        wrongid = i
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i))

        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) == 0:
                false = 1 # too many right brackets
                break

            if opening_brackets_stack[-1].Match(next):
                opening_brackets_stack.pop()
            else:
                false = 2 # dismatch
                break

    if len(opening_brackets_stack) == 0 and (wrongid == len(text) - 1) and (false == 0):
        print "Success"
    elif false == 2 or (len(opening_brackets_stack) == 0):
        print wrongid + 1
    else:
        print opening_brackets_stack[-1].position + 1


