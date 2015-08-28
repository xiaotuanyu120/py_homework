'''
This is a simple database to store the information of student. It support the
operation of "add"/"enquiry"/"delete"/"update"
'''

import shelve


# =========================
# add student's information
# =========================
def add_info(db, pid_in=False):
    if not pid_in:
        pid = raw_input("Enter unique ID: ")
    else:
        pid = pid_in
    student = {}
    student['name'] = raw_input("Enter name: ")
    student['gender'] = raw_input("Enter gender: ")
    student['age'] = raw_input("Enter age: ")
    student['city'] = raw_input("Enter city currently live in: ")
    student['qq'] = raw_input("Enter QQ :")
    db[pid] = student
    return student


# =============================
# enquiry student's information
# =============================
def enquiry_info(db):
    pid = raw_input("Enter id to enquiry: ")
    try:
        result = db[pid]
    except KeyError as e:
        print "ID not exsit",e
    return result


# ============================
# update student's information
# ============================
def update_info(db):
    pid = raw_input("Enter id to update: ")
    result = add_info(db, pid_in=pid)
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
            return pid
        elif confirm == "n":
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
    db = shelve.open('./student_info.txt')
    try:
        while True:
            cmd = user_cmd()
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
    finally:
        db.close()


if __name__ == "__main__":
    main()
