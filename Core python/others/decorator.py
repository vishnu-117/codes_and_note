from doctest import OutputChecker
import operator

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    # 3
    # Mike Thomson 20 M
    # Robert Bustle 32 M
    # Andria Bustle 30 F
    people = [input().split() for i in range(int(input()))]
    # print(people, '--------********-----------')
    # people = [['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']]
    print(*name_format(people), sep='\n')

# people.sort(key=operator.itemgetter(2))
# return map(f, people)


# 10
# Jake Jake 42 M
# Jake Kevin 57 M
# Jake Michael 91 M
# Kevin Jake 2 M
# Kevin Kevin 44 M
# Kevin Michael 100 M
# Michael Jake 4 M
# Michael Kevin 36 M
# Michael Michael 15 M
# Micheal Micheal 6 M

# Expected Output
# -------------------------
# Mr. Kevin Jake
# Mr. Michael Jake
# Mr. Micheal Micheal
# Mr. Michael Michael
# Mr. Michael Kevin
# Mr. Jake Jake
# Mr. Kevin Kevin
# Mr. Jake Kevin
# Mr. Jake Michael
# Mr. Kevin Michael