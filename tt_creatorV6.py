from prettytable import PrettyTable
class section():
    def __init__(self,name):
        self.name = name
        self.teachers_list = []
        tt_format = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.tt = tt_format
        self.sub = []
class teacher():
    def __init__(self,name,periods,sub):
        self.name = name
        self.periods = periods
        tt_format = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.sub=sub
        self.tt = tt_format

class_lst = [section('A'),section('B'),section('C'),section('D'),section('E'),section('F')]
teacher_lst = []
def get_input():
    try:
        numteach = int(input('please enter the number of teachers (max 10)(min 5) : '))
        for i in range(numteach):
            name = input("enter teacher's name : ")
            period = int(input("enter the number of periods : "))
            sub = input("enter the subject they teach (phy/chem/math/bio/cs)")
            if sub=='phy':
                teacher_lst.append(teacher(name, period, sub))
            if sub=='chem':
                teacher_lst.append(teacher(name, period, sub))
            if sub=='math':
                teacher_lst.append(teacher(name, period, sub))
            if sub=='bio':
                teacher_lst.append(teacher(name, period, sub))
            if sub=='cs':
                teacher_lst.append(teacher(name, period, sub))
    except:
        x = 5/0
def class_finder(sub, class_lst,no_classes_handled):
    x1 = -1
    for i in range(len(class_lst)):
        if sub not in class_lst[i].sub:
            x1 = i
            break
    no_classes_handled+=x1
    if no_classes_handled>6:
        no_classes_handled = 6
    return x1,no_classes_handled

def ttmaker (teacher_lst,class_lst):
    for teacher in teacher_lst:
        no_classes_handled = teacher.periods//4
        day = 0
        period = 0
        class_no,no_classes_handled = class_finder(teacher.sub, class_lst,no_classes_handled)
        class_no1 = class_no
        for i in range(4):
            while class_no1 < no_classes_handled:
                while True:
                    per = period%4
                    if per == 0 and day!=4 and period!=0:
                        day+=1
                    elif per == 0 and day==4:
                        day = 0
                    if class_lst[class_no1].tt[day][per] == 0:
                        class_lst[class_no1].tt[day][per] = [teacher.name,teacher.sub]
                        class_lst[class_no1].sub.append(teacher.sub)
                        period+=1
                        break
                    else:
                        period+=1
                class_no1+=1
            else:
                class_no1 = class_no
                continue



def pretty_printing():
    try:
        ttmaker(teacher_lst, class_lst)
        for i in range(len(class_lst)):
            print("Class "+str(i+1)+" Time Table")
            x = PrettyTable()
            tt = class_lst[i].tt
            x.add_column("Periods", [1, 2, 3, 4])
            dl = ['Monday',"Tuesday",'Wednesday','Thursday','Friday']
            for j in range(len(tt)):
                lst = []
                for k in range(len(tt[j])):
                    str1 = tt[j][k][0]
                    str2 = tt[j][k][1]
                    string = (str2+" ("+str1+")")
                    lst.append(string)
                x.add_column(dl[j],lst)
            print(x)
            print("\n\n")
    except:
        q = 5/0
while True:
    try :
        get_input()
        pretty_printing()
        a = input("would you like to try again?(y/n)")
        if a == 'n':
            break
    except:
        print('There has been an error !!')
        a = input("would you like to try again?(y/n)")
        if a == 'n':
            break
