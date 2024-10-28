import unittest
import os
from root import process_command
from app import *

class Test_Command(unittest.TestCase):
    def test_without_tcli(self):
        command="Add task"
        with self.assertRaises(SyntaxError, \
                        msg='There have not t-cli but not raise anything.'):
            process_command(command)
        # self.assertEqual('goo'.upper(), 'GOO')
        
    def test_with_tcli(self):
        command='t-cli add task'
        self.assertTrue(process_command(command), msg='It not receive True')

    def test_wrong_add_command(self):
        command='t-cli add Shopping"'
        with self.assertRaises(SyntaxError, msg='Error not raise.'):
            add_command(command)
    
    def test_add_command(self):
        command='t-cli add "Shopping"'
        self.assertEqual(type(add_command(command)), type(1), msg=\
                    "Add command type was not int type.")

        command='t-cli add "Working"'
        self.assertEqual(type(add_command(command)), type(1), msg=\
                    "Add command type was not int type 2nd time.")

    def test_delete_command(self):
        command='t-cli delete 2'
        self.assertIsNotNone(delete_command(command), msg="Hey! this one was not a dict from delete.")
        # self.assertEqual(type(delete_command(command)), type(dict()), msg=\
        #                     "Hey! this one was not a dict from delete.")

    def test_z_remove_data(self):
        os.remove('data.json')