class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self, tests_taken='No tests taken'):
        self.tests_taken = tests_taken

    def take_test(self, paper, student_ans):
        markscheme_dict = to_dict(list(paper.markscheme))
        student_ans_dict = to_dict(list(student_ans))
        subject, result = calc_report(student_ans_dict, markscheme_dict, paper.pass_mark, paper.subject)
        if self.tests_taken == 'No tests taken':
            self.tests_taken = {subject: result}
        else:
            self.tests_taken.update({subject: result})


def calc_report(student_ans_dict, markscheme_dict, pass_mark, subject):
    right = 0
    wrong = 0
    for i in student_ans_dict.keys():
        if student_ans_dict[i] == markscheme_dict[i]:
            right += 1
        else:
            wrong += 1
    percent = int(round((right / (len(markscheme_dict)) * 100), 0))
    int_pass_mark = int(pass_mark[:-1])
    if percent >= int_pass_mark:
        status = 'Passed!'
    else:
        status = 'Failed!'

    percent_str = '({}%)'.format(str(percent))
    result = '{} {}'.format(status, percent_str)
    return subject, result


def to_dict(ls):
    # ls = ['1A', '2B', '3A', '4C', '5A', '6C', '7A', '8C', '9D', '10A', '11A']
    d = {}
    for item in ls:
        ques = item[0:len(item) - 1]
        ans = item[-1]
        d[ques] = ans
    return d


def main():
    # Instantiate Class
    paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
    paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
    paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

    student1 = Student()
    student2 = Student()

    # Validate Test Cases:
    assert student1.tests_taken == "No tests taken"
    student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
    assert student1.tests_taken == {"Maths": "Passed! (80%)"}

    student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
    student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
    assert student2.tests_taken == {"Chemistry": "Failed! (25%)", "Computing": "Failed! (43%)"}

    paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
    paper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
    paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')
    paper4 = Testpaper('Physics', ['1A', '2B', '3A', '4C', '5A', '6C', '7A', '8C', '9D', '10A', '11A'], '90%')

    student1 = Student()
    student2 = Student()
    student3 = Student()

    assert (student1.tests_taken == 'No tests taken')
    student1.take_test(paper1, ['1A', '2D', '3D', '4A', '5A'])
    assert (student1.tests_taken == {'Maths': 'Passed! (80%)'})

    student2.take_test(paper2, ['1C', '2D', '3A', '4C'])
    student2.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
    assert (student2.tests_taken == {'Chemistry': 'Failed! (25%)', 'Computing': 'Failed! (43%)'})

    assert (student3.tests_taken == 'No tests taken')
    student3.take_test(paper1, ['1C', '2D', '3A', '4C', '5A'])
    student3.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
    assert (student3.tests_taken == {'Maths': 'Failed! (20%)', 'Computing': 'Failed! (43%)'})
    student3.take_test(paper4, ['1A', '2C', '3A', '4C', '5D', '6C', '7B', '8C', '9D', '10A', '11A'])
    assert student3.tests_taken == {'Maths': 'Failed! (20%)', 'Computing': 'Failed! (43%)', 'Physics': 'Failed! (73%)'}

    assert (paper1.subject == 'Maths')
    assert (paper2.subject == 'Chemistry')
    assert (paper3.subject == 'Computing')
    assert (paper4.subject == 'Physics')

    assert (paper1.markscheme == ['1A', '2C', '3D', '4A', '5A'])
    assert (paper2.markscheme == ['1C', '2C', '3D', '4A'])
    assert (paper3.markscheme == ['1D', '2C', '3C', '4B', '5D', '6C', '7A'])
    assert (paper4.markscheme == ['1A', '2B', '3A', '4C', '5A', '6C', '7A', '8C', '9D', '10A', '11A'])
    assert (paper1.pass_mark == '60%')
    assert (paper2.pass_mark == '75%')
    assert (paper3.pass_mark == '75%')
    assert (paper4.pass_mark == '90%')

    print('test cases validated!')


if __name__ == '__main__':
    main()
