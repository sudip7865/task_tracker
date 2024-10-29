import unittest
import os
# from root import process_command
from app import *

class Test_Command(unittest.TestCase):
    # def test_without_tcli(self):
    #     command="Add task"
    #     with self.assertRaises(SyntaxError, \
    #                     msg='There have not t-cli but not raise anything.'):
    #         process_command(command)
        # self.assertEqual('goo'.upper(), 'GOO')
        
    def test_with_tcli(self):
        command='t-cli add task'
        self.assertTrue(process_command(command), msg='It not receive True')

    # def test_wrong_add_command(self):
    #     command='t-cli add Shopping"'
    #     with self.assertRaises(SyntaxError, msg='Error not raise.'):
    #         add_command(command)
    
    def test_add_command(self):
        #task1
        command='t-cli add "Shopping"'
        self.assertEqual(type(add_command(command)), type(1), msg=\
                    "Add command type was not int type.")
        #task2
        command='t-cli add "Working"'
        self.assertEqual(type(add_command(command)), type(1), msg=\
                    "Add command type was not int type 2nd time.")
        # task3
        command='t-cli add "Cook"'
        self.assertEqual(type(add_command(command)), type(1), msg=\
                    "Add command type was not int type 3nd time.")
        #task4
        command='t-cli add "Play Chess"'
        self.assertEqual(type(add_command(command)), type(1), msg=\
                    "Add command type was not int type 4th time.")

        #task5
        command='t-cli add "Let it Fuck"'
        self.assertEqual(type(add_command(command)), type(1), msg=\
                    "Add command type was not int type 4th time.")


    def test_delete_command(self):
        command='t-cli delete 1'
        self.assertIsNotNone(delete_command(command), msg="Hey! this one was not a dict from delete.")
        # self.assertEqual(type(delete_command(command)), type(dict()), msg=\
        #                     "Hey! this one was not a dict from delete.")

    def test_update_command(self):
        self.assertTrue(update_command('t-cli update 2 "Shoping at v-mart"'),
                        msg='Update return False.')

    def test_mark_command(self):
        #in-progress task
        command='t-cli mark-in-progress 2'
        self.assertEqual(mark_command(command), 1)

        #done task
        command='t-cli mark-done 3'
        self.assertEqual(mark_command(command), 2)

    def test_xtask_list(self):
        command='t-cli list'
        self.assertTrue(list_command(command))

        #done tasks
        command='t-cli list done'
        self.assertTrue(list_command(command))

        #tasks in-progress
        command='t-cli list in-progress'
        self.assertTrue(list_command(command))

        #tasks todo
        command='t-cli list todo'
        self.assertTrue(list_command(command))


    def test_z_remove_data(self):
        os.remove('data.json')
