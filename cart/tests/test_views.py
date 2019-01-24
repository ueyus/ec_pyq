from django.test import TestCase
from django.urls import reverse
from ec.models import Product, Category


class TestCartList(TestCase):
    def test_get(self):
        Product.objects.create(name="テスト1", price=100, category="category")
        Product.objects.create(name="テスト2", price=500, category="category")
        session = self.client.session
        session['cart'] = ['1', '2']
        session.save()

        res = self.client.get(reverse('cart_list'))
        self.assertTemplateUsed(res, 'cart/list.html')
        self.assertContains(res, 'テスト1: 100円')
        self.assertContains(res, 'テスト2: 200円')

    def test_get_product_not_exist(self):
        session = self.client.session
        session['cart'] = [1]
        session.save()
        res = self.client.get(reverse('cart_list'))
        self.assertContains(res, '合計金額：　0円')

    def test_get_cart_empty(self):
        res = self.client.get(reverse('cart_list'))
        self.assertContains(res, '合計金額: 0円') 


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