from django.test import TestCase
from SCE_Proj.forms import loginForm,RegisterForm
from SCE_Proj.views import search_feature,login,register,about_page,homepage,search_view,settings_page,createpost,logout,LandingPage,become_editor,confirm_editor
from SCE_Proj.models import Post
from django.test.client import RequestFactory
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
# Create your tests here.

#unittesting for the login form
class LoginFormTestCase(TestCase):
    def test_LoginForm_is_valid(self):
        #valid form
        valid_email  = loginForm(data = {"email":"exmaple@example.com","password":"1"})
        valid_pass  = loginForm(data = {"email":"a@example.com","password":"123123"})
        invalid_form  = loginForm(data = {"email":"a@example.com","password":"1a23123"})
        self.assertFalse(valid_pass.is_valid())
        self.assertFalse(valid_pass.is_valid())
        self.assertFalse(invalid_form.is_valid())

class RegisterFormTestCase(TestCase):
    def test_RegisterForm_is_valid(self):
        #valid form
        random_mail = "{0}@{0}.com".format(id_generator())
        random_pass = id_generator()
        random_name = id_generator()
        random_surname = id_generator()
        valid_form = RegisterForm(data = {'name':random_name,'surname':random_surname,'email':random_mail,'password':random_pass,'confirmpass':random_pass})
        #passwords dont match
        random_mail = "{0}@{0}.com".format(id_generator())
        random_pass = id_generator()
        random_name = id_generator()
        random_surname = id_generator()
        pass_form = RegisterForm(data = {'name':random_name,'surname':random_surname,'email':random_mail,'password':random_pass,'confirmpass':"1"})
        #an existing user
        email = "example@example.com"
        exist_form =  RegisterForm(data = {'name':random_name,'surname':random_surname,'email':email,'password':random_pass,'confirmpass':"1"})
        self.assertTrue(valid_form.is_valid())
        self.assertTrue(pass_form.is_valid())
        self.assertTrue(exist_form.is_valid())

class SearchFeatureTestCase(TestCase):
    def test_search_feature(self):
        #valid search
        test_post = Post(title = "test1",tags = "test1",content = "test1")
        self.assertTrue(search_feature(test_post,"test"))
        self.assertFalse(search_feature(test_post,"exoe"))

class ViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_login_view(self):
       # self.factory = RequestFactory()
        #creating a get request
        request = self.factory.get("/login/")
        response = login(request)
        self.assertEqual(response.status_code,200)

    def test_register_view(self):
        #self.factory = RequestFactory()
        #creating a get request
        request = self.factory.get("/register/")
        response = register(request)
        self.assertEqual(response.status_code,200)
    
    def test_about_view(self):
        #self.factory = RequestFactory()
        #creating a get request
        request = self.factory.get("/about/")
        response = about_page(request)
        self.assertEqual(response.status_code,200)

    def test_homepage_view(self):
        #self.factory = RequestFactory()
        #creating a get request
        request = self.factory.get("/homepage/")
        response = homepage(request)
        self.assertEqual(response.status_code,200)

    def test_search_view(self):
        #self.factory = RequestFactory()
        #creating a get request
        request = self.factory.get("/search/")
        response = search_view(request)
        self.assertEqual(response.status_code,200)

    def test_setting_view(self):
        #self.factory = RequestFactory()
        #creating a get request
        request = self.factory.get("/settings/")
        response = settings_page(request)
        #we are comparing here with 302 due to redirect since were doing a request that has no COOKIES enabled
        self.assertEqual(response.status_code,302)

    def test_logout_view(self):
        #self.factory = RequestFactory()
        #creating a get request
        request = self.factory.get("/log_out/")
        response = logout(request)
        #we are comparing here with 302 due to redirect since were doing a request that has no COOKIES enabled
        self.assertEqual(response.status_code,302)
    
    def test_LandingPage_view(self):
        #self.factory = RequestFactory()
        #creating a get request
        request = self.factory.get("/landingpage/")
        response = LandingPage(request)
        self.assertEqual(response.status_code,200)

    def test_become_editor_view(self):
        #self.factory = RequestFactory()
        #creating a get request
        request = self.factory.get("/become_editor/")
        response = become_editor(request)
        self.assertEqual(response.status_code,302)
    
    def test_confirm_editor_view(self):
        #self.factory = RequestFactory()
        #creating a get request
        request = self.factory.get("/confirm_editor/")
        response = confirm_editor(request)
        self.assertEqual(response.status_code,302)

    def test_createpost_view(self):
        #self.factory = RequestFactory()
        #creating a get request
        request = self.factory.get("/createpost/")
        response = createpost(request)
        self.assertEqual(response.status_code,302)


    
