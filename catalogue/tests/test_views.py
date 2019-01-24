from django.test import TestCase
from django.urls import reverse
from ec.models import Product, Category


class TestProductList(TestCase):
    def test_get(self):
        category = Category.objects.create(name="カテゴリー１")
        Product.objects.create(name="テスト1", price=100, category="category")
        Product.objects.create(name="テスト2", price=500, category="category")
        res = self.client.get(reverse('product_list'))
        self.assertTemplateUsed(res, 'catalogue/product_list.html')
        self.assertContains(res, 'テスト1')
        self.assertContains(res, '100円')
        self.assertContains(res, 'テスト2')
        self.assertContains(res, '500円')
        self.assertContains(res, 'カテゴリー1')


class TestProductDetail(TestCase):
    def test_get(self):
        self.fail("テストが必要です")

    def test_404(self):
        self.fail("テストが必要です")


class TestProductEdit(TestCase):
    def test_get(self):
        self.fail("テストが必要です")

    def test_post(self):
        self.fail("テストが必要です")

    def test_post_invalid(self):
        self.fail("テストが必要です")

    def test_404(self):
        self.fail("テストが必要です")


class TestProductDelete(TestCase):
    pass