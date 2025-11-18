from django.test import TestCase

from .models import Product, Category, Review

# Create your tests here.

class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Whey Protein")
        self.product = Product.objects.create(
            name="Whey Protein",
            category= self.category,
            price = 50.99,
            stock=15
        )
    
    def test_slug_creation(self):
        self.assertEqual(self.product.slug, 'whey-protein')
    
    def test_string_representation(self):
        self.assertEqual(str(self.product), 'Whey Protein')
        
        
class ReviewTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Creatine")
        self.product = Product.objects.create(
            name="Creatine",
            category= self.category,
            price = 22.99,
            stock=15
        )
        self.review = Review(
            product = self.product,
            rating = 3,
            content = "Amazing product!"
        )
        
    def test_review_str(self):
        self.assertEqual(str(self.review), "Creatine - 3/5")