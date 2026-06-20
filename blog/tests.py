from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product

class ProductModelTest(TestCase):
    
    def setUp(self):
        """Cria dados para os testes"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )
        self.produto = Product.objects.create(
            name='Produto Teste',
            preco=10.50,
            estoque=5
        )
    
    def test_product_creation(self):
        """Testa se o produto foi criado corretamente"""
        self.assertEqual(self.produto.name, 'Produto Teste')
        self.assertEqual(float(self.produto.preco), 10.50)
        self.assertEqual(self.produto.estoque, 5)
    
    def test_product_str_method(self):
        """Testa o método __str__ do modelo"""
        self.assertEqual(str(self.produto), 'Produto Teste')
    
    def test_product_has_estoque(self):
        """Testa se o campo estoque existe e é um inteiro"""
        self.assertIsNotNone(self.produto.estoque)
        self.assertIsInstance(self.produto.estoque, int)
    
    def test_product_has_preco(self):
        """Testa se o campo preco existe e tem casas decimais"""
        self.assertIsNotNone(self.produto.preco)
        self.assertIsInstance(self.produto.preco, float)