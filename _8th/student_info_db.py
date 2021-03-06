'''
This is a simple database to store the information of student. It support the
operation of "add"/"enquiry"/"delete"/"update"
'''

import shelve


# =========================
# add student's information
# =========================
def add_info(db):
    pid = raw_input("Enter unique ID: ")
    if enquiry(db, pid):
        print 'ID exsit, retry!'
        cmd_keep(add_info, db)
    else:
        pid = pid_in
    student = {}
    student['name'] = raw_input("Enter name: ")
    student['gender'] = raw_input("Enter gender: ")
    student['age'] = raw_input("Enter age: ")
    student['city'] = raw_input("Enter city currently live in: ")
    student['qq'] = raw_input("Enter QQ :")
    db[pid] = student
    cmd_keep(add_info, db)
    return student


# =============================
# enquiry student's information
# =============================
def enquiry_info(db, pid_in=False):
    if  pid_in:
        pid = pid_in
    else:
        pid = raw_input("Enter id to enquiry: ")
    try:
        # import ipdb;ipdb.set_trace()
        result = db[pid]
    except KeyError as e:
        return "ID not exsit",e
    print result
    cmd_keep(enquiry_info, db)
    return result


# ============================
# update student's information
# ============================
def update_info(db):
    pid = raw_input("Enter id to update: ")
    result = add_info(db, pid_in=pid)
    cmd_keep(update_info, db)
    return result


# ============================
# delete student's information
# ============================
def delete_info(db):
    pid = raw_input("Enter id to delete: ")
    while True:
        confirm = raw_input("confirm delete? (y or n)")
        if confirm == "y":
            del db[pid]
            cmd_keep(delete_info, db)
            return pid
        elif confirm == "n":
            cmd_keep(delete_info, db)
            return
        else:
            print "invalid input, try again"


# ====================
# get user's input cmd
# ====================
def user_cmd():
    cmd = raw_input("Enter command(? for help)")
    cmd = cmd.strip().lower()
    return cmd


def cmd_keep(func, *arg):
    cmd = raw_input("Continue or back to Main? (c or m)")
    cmd = cmd.strip().lower()
    if cmd == 'c':
        func(arg)
    elif cmd == 'm':
        return
    else:
        print 'invalid input, try again! (c or m)'


# ================
# help information
# ================
def print_help():
    print 'you can use the command below:'
    print "add : add record"
    print "update : update record"
    print "delete : delete record"
    print "enquiry : enquiry record"
    print "? : help"
    print "quit : save and exit"


def main():
    while True:
        db = shelve.open('./student_info.txt')
        """try:
            if cmd != "enquiry":
                cmd = user_cmd()
        except NameError as e:"""
        cmd = user_cmd()

        try:
            if cmd == 'add':
                print add_info(db)
            elif cmd == 'enquiry':
                print enquiry_info(db)
            elif cmd == 'update':
                print update_info(db)
            elif cmd == 'delete':
                print delete_info(db), "student deleted"
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
            else:
                print 'Invaild input, try agagin! (Enter "?" for help)'
        finally:
            db.close()


if __name__ == "__main__":
    main()
