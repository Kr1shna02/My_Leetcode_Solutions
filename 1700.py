class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = 0
        length = len(students)
        
        while count != length:
            if len(students) == 0:
                break
            else:
                if students[0] == sandwiches[0]:
                    count = 0
                    students = students[1:]
                    sandwiches = sandwiches[1:]
                else:
                    count += 1
                    s = students.pop(0)
                    students.append(s)

        return len(students)
