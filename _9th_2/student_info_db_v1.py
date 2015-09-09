'''
This is a simple database to store the information of student. It support the
operation of "add"/"enquiry"/"delete"/"update"
'''

import shelve


# =========================
# add student's information
# =========================
def add_info(db, pid_in=False):
    if pid_in:
        pid = pid_in
    else:
        pid = raw_input("Enter unique ID: ").strip()
        if enquiry_info(db, pid):
            print 'ID exsit!'
            add_info(db)
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
def enquiry_info(db, pid_in=False):
    if pid_in:
        pid = pid_in
    else:
        pid = raw_input("Enter id to enquiry or 'exit' to exit: ").strip()
        if pid == 'exit':
            return
        else:
            try:
                result = db[pid]
                print result
            except KeyError as e:
                print "ID not exsit", e
            finally:
                enquiry_info(db)
        return result


# ============================
# update student's information
# ============================
def update_info(db):
    pid = raw_input("Enter id to update: ").strip()
    result = add_info(db, pid)
    return result


# ============================
# delete student's information
# ============================
def delete_info(db):
    pid = raw_input("Enter id to delete: ").strip()
    if enquiry_info(db, pid):
        while True:
            confirm = raw_input("confirm delete? (y or n)").strip().lower()
            if confirm == "y":
                del db[pid]
                return pid
            elif confirm == "n":
                return
            else:
                print "invalid input, try again"
    else:
        print 'ID not exsit!'
        return


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
    while True:
        db = shelve.open('./student_info.txt')
        cmd = user_cmd()

        try:
            if cmd == 'add':
                print add_info(db)
            elif cmd == 'enquiry':
                enquiry_info(db)
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
