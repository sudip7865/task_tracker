import unittest
import os
from app.model import Model

class Test_Mode(unittest.TestCase):
    
    # def setUp(self):
    #     self.m=Model()

    m=Model()
    def test_model_add(self):
        #task1
        task1=self.m.add('Shoping')
        search_task=Model.get_task(task1)
        self.assertEqual(search_task['task'], 'Shoping', msg='Get False from 1st insert')

        #task2
        task2=self.m.add('Walking')
        search_task=Model.get_task(task2)
        self.assertEqual(search_task['task'], 'Walking', msg='Get False from 2nd insert')

        #task3
        task3=self.m.add('Cook')
        search_task=Model.get_task(task3)
        self.assertEqual(search_task['task'], 'Cook', msg='Get False from 3rd insert')
        
    def test_model_perform_update(self):
        self.m.update(2, 'Workout')
        search_task=Model.get_task(2)
        self.assertEqual(search_task['task'], 'Workout')

    def test_model_delete(self):
        self.m.delete(3)
        search_task=Model.get_task(3)
        self.assertEqual(search_task, '')
        
    def test_model_mark_on_process(self):
        # print('Here all data: ', Model.all_data())
        task_status=self.m.mark_task(1, 1)
        search_task=Model.get_task(1)
        self.assertEqual(task_status, search_task['status'])
    
    def test_model_mark_on_complete(self):
        task_status=self.m.mark_task(2, 2)
        search_task=Model.get_task(2)
        self.assertEqual(task_status, search_task['status'])
    
    def test_model_task_list(self):
        task_list=self.m.list_of_task()
        #task1
        self.assertIn('Shoping', str(task_list), msg='Shoping not present on task')
        #task2
        self.assertIn('Workout', str(task_list), msg='Workout not present on task')     #update part execute later
        #as task3 delete so it not need to test

        #fliter all processing task
        processing_task=self.m.list_of_task(1)
        keys=list(processing_task.keys())
        for key in keys:
            self.assertEqual(processing_task[key]['status'], 1, msg=\
                "Processing task status was not 1.")
        
        #fliter all complete task
        complete_task=self.m.list_of_task(2)
        keys=list(complete_task.keys())
        for key in keys:
            self.assertEqual(complete_task[key]['status'], 2, msg=\
                "Processing task status was not 2.")

    def test_remove_dataBase(self):
        # print('Here all data: ', Model.all_data())
        os.remove('data.json')

    # def tearDown(self):
    #     os.remove('data.json')