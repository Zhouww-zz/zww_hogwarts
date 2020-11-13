import unittest

class Search():
    def  search_fun(self):
            print("search")
            return True

class TestSearch(unittest.TestCase):
    def setUp(self):
        print("这是每个测试方法之前的函数")
        self.search=Search()
    def tearDown(self):
        print("每个测试方法之后的函数")

    @classmethod
    def setUpClass(cls)->None:
        cls.search=Search()
        print("这是整个测试类之前的方法")
    @classmethod
    def tearDownClass(cls)->None:
        print("这是整个测试类之后的方法")
    def test_test1(self):
        print("1")
        search = Search()
        assert True == search.search_fun()
    def test_test2(self):
        print("2")
        search = Search()
        assert True == search.search_fun()

    def test_test3(self):
        print("3")
        search = Search()
        assert True == search.search_fun()


class TestSearch1(unittest.TestCase):
    def setUp(self):
        print("这是每个测试方法之前的函数")
        self.search=Search()
    def tearDown(self):
        print("每个测试方法之后的函数")

    @classmethod
    def setUpClass(cls)->None:
        cls.search=Search()
        print("这是整个测试类之前的方法1")
    @classmethod
    def tearDownClass(cls)->None:
        print("这是整个测试类之后的方法1")
    def test_test1(self):
        print("1")
        search = Search()
        assert True == search.search_fun()
    def test_test2(self):
        print("2")
        search = Search()
        assert True == search.search_fun()

    def test_test3(self):
        print("3")
        search = Search()
        assert True == search.search_fun()

    def test_equal(self):
        print("断言相等")
        self.assertEqual(1,1,"断言1==1")

    def test_notequal(self):
        print("断言不相等")
        # self.assertNotEqual(1,1,"1!=1")
        self.assertTrue(1==1,"verify")
        self.assertFalse(1==2,"verify")
if __name__=="__main__":
    #执行当前模块所有类
    #   unittest.main()

    #执行指定的测试用例，将指定的测试用例添加到测试套件里面，批量执行
    #创建一个测试套件，testsuite
    # suite=unittest.TestSuite()
    # suite.addTest(TestSearch1("test_test1"))
    # suite.addTest(TestSearch1("test_test2"))
    # unittest.TextTestRunner().run(suite)
    #执行指定的测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    suite = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)

