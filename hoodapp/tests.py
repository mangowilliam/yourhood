from django.test import TestCase
from . models import Profile,Hood,Post,Business

# Create your tests here.
class HoodTestClass(TestCase):
    def setUp(self):
        self.town = Hood(name="town",count = 34)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.town, Hood))
    
    def teardown(self):
        Hood.objects.all().delete()
    
    def test_save_method(self):
        self.town.save_hood()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) > 0)
        
    def test_delete(self):
        self.town.save()
        self.town.delete()
        self.assertTrue(len(Hood.objects.all()) == 0)
class BusinessTestClass(TestCase):
    def setUp(self):
        self.mashamba = Business(name="mashamba", email = "juniormango@yahoo.com")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.mashamba, Business))
    
    def teardown(self):
        Business.objects.all().delete()
        
    def test_save_method(self):
        self.mashamba.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businessess) > 0)
        
    def test_delete(self):
        self.mashamba.save()
        self.mashamba.delete()
        self.assertTrue(len(Business.objects.all()) == 0)

class PostTestClass(TestCase):
    def setUp(self):
        self.CBD = Post(title="CBD")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.CBD, Post))
    
    def teardown(self):
        Post.objects.all().delete()
   
    def test_save_method(self):
        self.CBD.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete(self):
        self.CBD.save()
        self.CBD.delete()
        self.assertTrue(len(Post.objects.all()) == 0)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.mango =Profile(user="mango")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.mango, Profile))
    
    def teardown(self):
        Profile.objects.all().delete()
    
    def test_save_method(self):
        self.mango.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def test_delete(self):
        self.mango.save()
        self.mango.delete()
        self.assertTrue(len(Profile.objects.all()) == 0)