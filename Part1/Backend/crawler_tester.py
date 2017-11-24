

#Vincent Meng OCT 4th 
import unittest
from crawler import crawler #import the crawler file into the tester 

class CrawlerTester(unittest.TestCase):   # initiate the testing
    def testinverted_index(self):
        self._crawler = crawler(None,'urls.txt')   # compare the set inverted index function . see if it returns the same word ids and docment ids correspondingly 
        expected_inverted_index = {    # expected answer from the program   
            1:set([1,2,3]), 
            2:set([1]),
            3:set([2]),
            4:set([2]),
            5:set([3]),
            6:set([3]),
        }
        self._crawler.crawl(1)
        returned_result = self._crawler.get_inverted_index() # save the output in returned result 
        self.assertEqual(expected_inverted_index, returned_result)   # compare the result from the ouput to the correct answer 
    def testresolved_inverted_index(self):         # test the second function resolved inverted index . see if it returns the correct url and word strings 
        self._crawler = crawler(None,'urls.txt')
        expected_resolved_inverted_index={                                  # us the same method as the inverted index. 
               u'announcement': set(['http://www.eecg.toronto.edu/~jzhu/csc326/csc326an.html']),
             
               u'project': set(['http://www.eecg.toronto.edu/~jzhu/csc326/csc326proj.html']), 
             
               u'languages': set(['http://www.eecg.toronto.edu/~jzhu/csc326/csc326.html']), 
             
               u'programming': set(['http://www.eecg.toronto.edu/~jzhu/csc326/csc326.html']), 
               
               u'machine': set(['http://www.eecg.toronto.edu/~jzhu/csc326/csc326proj.html']), 
       
               u'csc326': set(['http://www.eecg.toronto.edu/~jzhu/csc326/csc326proj.html', 'http://www.eecg.toronto.edu/~jzhu/csc326/csc326an.html', 'http://www.eecg.toronto.edu/~jzhu/csc326/csc326.html'])}
        self._crawler.crawl(1)
        returned_result = self._crawler.get_resolved_inverted_index()
        self.assertEqual(expected_resolved_inverted_index,returned_result)
if __name__ == '__main__':
    unittest.main()

