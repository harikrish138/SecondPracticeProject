#
# with open("C:\\Users\\91738\\PycharmProjects\\DemoProject\\SecondPracticeProject\\Files\\Notes",'r') as e:
#
#     content=e.read()
#     print(content)
#
# with open("C:\\Users\\91738\\PycharmProjects\\DemoProject\\SecondPracticeProject\\Files\\Notes",'w') as e:
#
#     content=e.write('THis is my friend \n')
#     print(content)
# with open("C:\\Users\\91738\\PycharmProjects\\DemoProject\\SecondPracticeProject\\Files\\Notes",'a') as e:
#
#     content=e.write('THis is my friend \n')
#     print(content)
#     e.close()
#
# text= open("C:\\Users\\91738\\PycharmProjects\\DemoProject\\SecondPracticeProject\\Files\\Notes",'w')
# ts=text.write("hari krishna is a person name")
# print(ts)

# import re
# text= open("C:\\Users\\91738\\PycharmProjects\\DemoProject\\SecondPracticeProject\\Files\\Notes",'r')
# ts=text.readline()
# print(ts)
# matc=re.findall('krishna',ts)
#
# print(matc)
# text.close()
lst =["\nabscfefijerokop","efuwehiedguy"]

with open("C:\\Users\\91738\\PycharmProjects\\DemoProject\\SecondPracticeProject\\Files\\Notes","a") as b:

    a = b.writelines(lst)
    print(a)
    b.close()