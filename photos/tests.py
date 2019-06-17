from django.test import TestCase
from .models import Location,Category,Image

class LocationTestClass(TestCase):
    def setUp(self):
        self.mombasa = Location(location='Mombasa')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.mombasa,Location))
    def test_save_method(self):
        self.mombasa.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_location(self):
        self.mombasa.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.pets = Category(category='Animals')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.pets,Category))

    def test_save_method(self):
        self.pets.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)  

    def test_delete_category(self):
        self.pets.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)


class ImageTestCase(TestCase):
    def setUp(self):
        self.nairobi = Location(location='Nairobi')
        self.nairobi.save_location()

        self.landscape = Category(category='Nature')
        self.landscape.save_category()

        self.new_image = Image(image_name='Test Name',image_description='Test Description',image_location=self.nairobi,image_category=self.landscape)
        self.new_image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_filter_by_location(self):
        filtered_images = Image.filter_by_location('Nairobi')
        self.assertTrue(len(filtered_images)>0)

    def test_search_image(self):
        image = Image.search_by_category('Nature')
        self.assertTrue(len(image)>0)

    def test_get_image_by_id(self):
        images = Image.get_image_by_id(self.new_image.id)
        self.assertTrue(images == self.new_image)

    def test_delete_image(self):
        
        images = Image.get_image_by_id(self.new_image.id)
        self.new_image.delete_image()
        self.assertTrue(len(images)==0)