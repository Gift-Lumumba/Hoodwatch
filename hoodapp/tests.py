from django.test import TestCase
from .models import Neighbourhood, Profile,Business,Join,Posts
from django.contrib.auth.models import User

# TESTING NEIGHBOURHOOD CLASS
class NeighbourhoodTestClass(TestCase):
    '''
    Test Neighbourhood class and its methods and functions
    '''
    def setUp(self):
        self.user = User.objects.create(id =1, username='test')
        self.neighbourhood = Neighbourhood(name='testhood', location='testlocation', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    
    def test_save_method(self):
        '''
        Function that tests whether a neighbourhood is being saved
        '''
        self.neighbourhood.save_neighbourhood()
        neighbourhoods = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether a neighbourhood can be deleted
        '''
        self.neighbourhood.save_neighbourhood()
        self.neighbourhood.delete_neighbourhood

    def test_update_method(self):
        '''
        Function that test whether a neighbourhood's details can be updated
        '''
        self.neighbourhood.save_neighbourhood()
        new_hood = Neighbourhood.objects.filter(name='testhood').update(name='hoodtest')
        hoods = Neighbourhood.objects.get(name='hoodtest')
        self.assertTrue(hoods.name, 'hoodtest')

    
    def test_find_neighbourhood_by_id(self):
        '''
        Function that tests whether one can get a neighbourhood by its id
        '''
        self.neighbourhood.save_neighbourhood()
        this_hood= self.neighbourhood.find_neighbourhood_by_id(self.neighbourhood.id)
        hood = Neighbourhood.objects.get(id=self.neighbourhood.id)
        self.assertTrue(this_hood, hood)

class ProfileTestClass(TestCase):
    '''
    Test Profile class and its methods and functions
    '''
    def setUp(self):
        self.user = User.objects.create(id =1,username='testname')
        self.neighbourhood = Neighbourhood(name='kejani', location='pale', user=self.user)
        self.neighbourhood.save_neighbourhood()
        self.profile = Profile(user=self.user, hood = self.neighbourhood)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))


    def test_save_method(self):
        '''
        Function that tests whether a user's profile is being saved
        '''
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether a user's profile can be deleted
        '''
        self.profile.save_profile()
        self.profile.delete_profile()



class BusinessTestClass(TestCase):
    '''
    Test Business class and its methods and functions
    '''
    def setUp(self):
        self.user = User.objects.create(id =1, username='test')
        self.neighbourhood = Neighbourhood(name='kejani', location='pale', user=self.user)
        self.neighbourhood.save_neighbourhood()
        self.business = Business(name="kazi", email="kazi@gmail.com", user=self.user, neighbourhood=self.neighbourhood)

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    
    def test_save_method(self):
        '''
        Function to test that neighbourhood is being saved
        '''
        self.business.save_business()
        businesses = Business.objects.all()
        # self.assertTrue(len(businesses) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether a neighbourhood can be deleted
        '''
        self.business.save_business()
        self.business.delete_business()

    def test_update_method(self):
        '''
        Function that tests whether a neighbourhood's details can be updated
        '''
        self.business.save_business()
        new_business = Business.objects.filter(name='kazi').update(name='kazini')

class PostsTestClass(TestCase):
    '''
    Test Posts class and its methods and functions
    '''
    def setUp(self):
        self.user = User.objects.create(id =1, username='test')
        self.neighbourhood = Neighbourhood(name='kejani', location='pale', user=self.user)
        self.neighbourhood.save_neighbourhood()
        self.post = Posts(post="hii post", user=self.user, hood=self.neighbourhood)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Posts))

    
    def test_save_method(self):
        '''
        Function that tests whether a post is being saved
        '''
        self.post.save_posts()
        posts = Posts.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether a neighbourhood can be deleted
        '''
        self.post.save_posts()
        self.post.delete_posts()
