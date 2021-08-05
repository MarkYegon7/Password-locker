import unittest
import pyperclip
from user_details import User, Aspect

class TestUser (unittest.TestCase):
    def setUp(self):
        self.new_user = User('Mark','Yegon','beyou22')
        
    def test_init_(self):
        self.assertEqual(self.new_user.first_name,'Mark')
        self.assertEqual(self.new_user.last_name,'Yegon')
        self.assertEqual(self.new_user.password,'beyou22')
        
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
        
class TestCredentials(unittest.TestCase):
    def test_check_user(self):
        self.new_user = User('Mary','Yegon','beyou22')
        self.new_user.save_user()
        user2 = User('Bill','Yegon','beyou22')
        user2.save_user()
        
        for user in User.users_list:
            if user.first == user2.first_name and user.password == user2.password:
                current_user = user.first_name
        return current_user
    
        self.assertEqual(current_user,Aspect.check_user(user2.password,user2.first_name))
        
    def setUp(self):
        self.new_credential = Aspect('Mark','Facebook','markbrand','beyou22')
        
    def test_init_(self):
        self.assertEqual(self.new_credential.user_name,'Mark')
        self.assertEqual(self.new_credential.site_name,'Facebook')
        self.assertEqual(self.new_credential.account_name,'markbrand')
        self.assertEqual(self.new_credential.password,'beyou22')
        
    def test_save_credentials(self):
        self.new_credential.save_credentials()
        twitter = Aspect('Bill','Twitter','markbrand','beyou22')
        twitter.save_credentials()
        self.assertEqual(len(Aspect.credentials_list),2)
        
    def tearDown(self):
        Aspect.credentials_list = []
        User.users_list = []
        
    def test_display_credentials(self):
        self.new_credential.save_credentials()
        twitter = Aspect('Bill','Twitter','maryjoe','beyou22')
        twitter.save_credentials()
        gmail = Aspect('Bill','Gmail','markbrand','beyou22')
        gmail.save_credentials()
        self.assertEqual(len(Aspect.display_credentials(twitter.user_name)),2)
        
    def test_find_by_site_name(self):
        self.new_credential.save_credentials()
        twitter = Aspect('Bill','Twitter','markbrand','beyou22')
        twitter.save_credentials()
        credential_exists = Aspect.find_by_site_name('Twitter')
        self.assertEqual(credential_exists,twitter)
        
    def test_copy_credential(self):
        self.new_credential.save_credentials()
        twitter = Aspect('Bill','Twitter','markbrand','beyou22')
        twitter.save_credentials()
        find_credential = None
        for credential in Aspect.user_credential_list:
            find_credential = Aspect.find_by_site_name(credential.site_name)
            return pyperclip.copy(find_credential.password)
        Aspect.copy_credential(self.new_credential.site_name)
        self.assertEqual('beyou22',pyperclip.paste())
        print(pyperclip.paste())
        
if_name_ =='_main_':
    unittest.main(verbosity=2)
        

        
        