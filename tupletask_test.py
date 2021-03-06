import unittest
from unittest import mock
import tupleTask


def createListFromFile_side_effect(tupleList, fileName):
    Arsenal = ['Arsenal', 10, 7, 3]
    Chelsea = ['Chelsea', 0, 4, 9]
    Tottenham = ['Tottenham', 6, 8, 7]
    tupleList.append(Chelsea)
    tupleList.append(Arsenal)
    tupleList.append(Tottenham)

class TestCreateFile(unittest.TestCase):
    def test_file_not_found(self):
        tupleList = []
        with self.assertRaises(FileNotFoundError):
            tupleTask.createListFromFile(tupleList, 'tupleNotExist.txt')

    def test_bad_line(self):
        tupleList = []
        with self.assertRaises(IndexError):
            tupleTask.createListFromFile(tupleList, 'bad_tuple_list.txt')
    
    def test_number_of_tuples(self):
        tupleList = []
        tupleTask.createListFromFile(tupleList, 'tuple_list.txt')
        self.assertEqual(len(tupleList), 3)

class TestSort(unittest.TestCase):
    @mock.patch ('tupleTask.createListFromFile', side_effect = createListFromFile_side_effect)
    def test_sort_by_win(self, mock_createListFromFile):
        tupleList=[]
        tupleTask.createListFromFile(tupleList, 'some_file.txt')
        sorted_data = tupleTask.sortedTuples(tupleList, 1, True)
        self.assertEqual(sorted_data[0][0], 'Arsenal')

    @mock.patch ('tupleTask.createListFromFile', side_effect = createListFromFile_side_effect)
    def test_sort_by_loss(self, mock_createListFromFile):
        tupleList=[]
        tupleTask.createListFromFile(tupleList, 'another_file.txt')
        sorted_data = tupleTask.sortedTuples(tupleList, 3, True)
        self.assertEqual(sorted_data[0][0], 'Chelsea')

    @mock.patch ('tupleTask.createListFromFile', side_effect = createListFromFile_side_effect)
    def test_sort_by_draw(self, mock_createListFromFile):
        tupleList=[]
        tupleTask.createListFromFile(tupleList, 'yet_another_file.txt')
        sorted_data = tupleTask.sortedTuples(tupleList, 2, True)
        self.assertEqual(sorted_data[0][0], 'Tottenham')

    @mock.patch ('tupleTask.createListFromFile', side_effect = createListFromFile_side_effect)
    def test_sort_by_team(self, mock_createListFromFile):
        tupleList=[]
        tupleTask.createListFromFile(tupleList, 'last_file.txt')
        sorted_data = tupleTask.sortedTuples(tupleList, 0, False)
        self.assertEqual(sorted_data[0][0], 'Arsenal')


        
#sort by loss
#sort by draw
#sort by team
#commit and push into git




if __name__ == "__main__":
    unittest.main(exit=False)
    