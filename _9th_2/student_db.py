#!/usr/bin/python

'''student's information management database'''

import copy
import shelve
from collections import namedtuple

class Interface(object):
    '''User interface'''
    init_id = 0
    Student_data = namedtuple(
        'Student_data',[
            'name',
            'gender',
            'age',
            'location',
            'QQ'
            ]
        )
    operation_list = {
        'add':self.add,
        'enquiry':self.enquiry,
        'update':self.update,
        'delete':self.delete,
        '?':self.get_help
    }

    def __init__(self, max_id)
        self.max_id = max_id
        self.student_data = Student_data('', '', '', '', '')

    def add(self):
        result = {}
        sid = self.max_id + 1

        add_info = self.student_data.deepcopy()
        add_info.name = raw_input('Name: ').strip()
        add_info.gender = raw_input('Gender(M or F): ').strip()
        add_info.age = raw_input('Age :').strip()
        add_info.location = raw_input('Location :').strip()
        add_info.QQ = raw_input('QQ :').strip()

        result[sid] = add_info
        return result

    def enquiry(self, sid=0):
        if not sid:
            sid = raw_input('Enquiry ID :').strip()
        try:
            result = db[sid]

    def update(self):
        pass

    def delete(self, id=0):
        pass

    def cmd(self):
        cmd = raw_input("Enter command(? for help)")
        cmd = cmd.strip().lower()
        return cmd

    def get_help(self):
        print 'you can use the command below:'
        print "add : add record"
        print "update : update record"
        print "delete : delete record"
        print "enquiry : enquiry record"
        print "? : help"
        print "quit : save and exit"



class StudentManager(object):
    '''The student information manager between database and interface'''
    pass


class Student(object):
    '''student information'''
    def write_convert(self):
        

    def read_convert(self):
        pass


class DbOprator(object):
    '''operation of db file'''
    def __init__(self, name):
        self.name = name

    def write(self, row_id, row_info):
        db[row_id] = row_info

    def read(self):
        pass

    def open(self, database_path):
        db = shelve.open(database_path)
        return db

    def max_id(self):
        pass
        return max_id


def main():
    operator = Interface() 
    database = DbOprator('database')
    while True:
        db = database.open('./student_db.txt')
        cmd = operator.cmd()

        try:
            if cmd in operator.operation_list:
                operator.operation_list[cmd]
            else:
                print 'Invaild command! (? for help)'
        finally:
            db.close()


if __name__ == '__main__':
    main()
