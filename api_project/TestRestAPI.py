import requests
import unittest
import os.path


API_ENDPOINT_POST = "http://127.0.0.1:5000/api/write_text_to_file/"
API_ENDPOINT_GET = "http://127.0.0.1:5000/api/write_text_to_file_get/"


class TestRestAPI(unittest.TestCase):
    def setUp(self):

        if os.path.exists("data_folder/str.txt"):
            os.remove("data_folder/str.txt")
            print("File Removed!")
        else:
            print("The file does not exist")

    def test_post_request(self):
        # data = u"hello"  # can be changed to any wanted string
        data = raw_input("Please enter the string you want to write for the post request: ")
        r = requests.post(API_ENDPOINT_POST, data)
        res = r.text
        res_code = r.status_code
        if res_code == 200:
            print(res)
        else:
            print("response code is: " + res_code)
        assert(res == data)

    def assert_file_existance(self):
        assert os.path.exists("data_folder/str.txt")

    def  check_file_is_open(self):
        f = open("data_folder/str.txt", "r")
        assert(f.closed)

    def tearDown(self):
        os.remove("data_folder/str.txt")


if __name__ == "__main__":
    unittest.main()

