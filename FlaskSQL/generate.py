import string
from random import choice as rnd, randrange


def group_name(count):
    chars = string.ascii_uppercase
    num = string.digits
    name = [rnd(chars) + rnd(chars) + '-' + rnd(num) + rnd(num)
            for i in range(count)]
    return name


def student_name(count):
    first_names = [
        'Rebecca',
        'Mariam',
        'Kimberly',
        'Samantha',
        'Taylor',
        'Annie',
        'Evie',
        'Ayesha',
        'Lola',
        'Tiffany',
        'Jacob',
        'Alfie',
        'Ibrahim',
        'Jimmy',
        'Seth',
        'Shawn',
        'Samuel',
        'Otto',
        'Ebony',
        'Daniel'
    ]
    last_names = [
        'Fisher',
        'Whittle',
        'Hunt',
        'Nelson',
        'Curry',
        'Ferguson',
        'Barnes',
        'Yang',
        'Ray',
        'Luna',
        'Thompson',
        'Wilkins',
        'Avila',
        'Leonard',
        'Doyle',
        'Watson',
        'Gordon',
        'Banks',
        'Hines'
    ]
    name_list = []
    while len(name_list) < count:
        name = rnd(first_names) + ' ' + rnd(last_names)
        if name not in name_list:
            name_list.append(name)
    return name_list


def group_assign(group_list, s_list):
    student_list = s_list.copy()
    groups_dict = {}
    groups = []
    for group in group_list:
        c = randrange(10, 31)
        if c < len(student_list):
            students = [student_list.pop() for i in range(c)]
            groups_dict.update({group: students})
        else:
            groups.append(group)
    if not groups:
        student_list + (groups_dict.pop(group_list[0]))
        groups.append(group_list[0])
    return groups_dict, student_list, groups


def course_assign(student_list):
    courses = [
        'Math',
        'Biology',
        'Chemistry',
        'Engineering',
        'Physics',
        'Business',
        'Economics',
        'Communications',
        'Writing',
        'Medicine'
    ]
    student_course = {course: [] for course in courses}
    for student in student_list:
        for i in range(randrange(1, 4)):
            c_len = len(courses)
            student_course[courses[randrange(0, c_len)]].append(student)
    return student_course


# students = student_name(200)
# d, s, g = group_assign(group_name(10), students)
# print(d)
# print(s)
# print(g)
# cs = course_assign(students)
# print(cs)
# a = 1
