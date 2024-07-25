# Select query
from dbconfig import dbconfig
from Student import Student
import json

class user_service:

    def get_users(self):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("select * from users")
        output = cur.fetchall()

        users_list = []
        for i in output:
            print("select query output ",i)
            user = Student(i[0], i[1], i[2], i[3]);
            users_list.append(json.loads(user.to_json()))
            
        dbconfig.close_connection(conn)
        return users_list

    def get_user(self, user_id):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("select * from users where id = " + str(user_id))
        output = cur.fetchall()
        user = ''
        for i in output:
            print("select query output ", i)
            user = Student(i[0], i[1], i[2], i[3]);

        dbconfig.close_connection(conn)
        return user.to_json()


    # def insert_static_value(user_list):
    #     conn = dbconfig.open_connection()
    #     cur = conn.cursor()
    #     cur.execute("""
    #                 insert into users(id, email, password, username ) values ( %s, %s, %s, %s)
    #                 """,
    #                 (1111, 'test@test.com', 'password', 'test'))
    #     print(conn.insert_id())
    #     conn.commit()

    def create_user(self, user):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("""
                insert into users(id, email, password, username ) values ( %s, %s, %s, %s)
                """,
                    (user.id, user.email, user.password, user.username))
        print(conn.insert_id())
        conn.commit()

    # def insert_dynamic_value(user_list):
    #     conn = dbconfig.open_connection()
    #     cur = conn.cursor()
    #     for user in user_list:
    #         cur.execute("""
    #              insert into users(id, email, password, username ) values ( %s, %s, %s, %s)
    #              """,
    #                     (user.id, user.email, user.password, user.username))
    #     print(conn.insert_id())
    #     conn.commit()

    def delete_user(self,user_id):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("DELETE from users where id = " + str(user_id))
        conn.commit()


    def update_user(self, user):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("""
            UPDATE users 
            SET email = %s, password = %s, username = %s 
            WHERE id = %s
            """,
            (user.email, user.password, user.username, user.id))
        conn.commit()
        conn.close()

# user_service = user_service()
# user_service.get_users()
# user_service.get_user('1919191919192')
#
# user1 = User(3333,'a@test.com', 'password','USER', 'test')
# print("user ", user1)
# user_list = []
# user_list.append(user1)
# user_service.insert_dynamic_value(user_list)
# user_service.get_user('3333')


# class student_service:
#     def get_students(self):
#         conn = dbconfig.open_connection()
#         cur = conn.cursor()
#         cur.execute("select * from student")
#         out = cur.fetchall()
#         users_list = []
#         for i in out:
#             print("select query output", i)
#             student = Student(i[0], i[1], i[2]);
#             users_list.append(json.loads(Student.to_json()))
#         dbconfig.close_connection(conn)
#         return users_list

#     def create_student(self, student):
#         conn = dbconfig.open_connection()
#         cur = conn.cursor()
#         cur.execute("""
#                    insert into student(reg_no,name,age) values ( %s, %s, %s)
#                    """,
#                     (student.reg_no, student.name, student.age))
#         print(conn.insert_id())
#         conn.commit()