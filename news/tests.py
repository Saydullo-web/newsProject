from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        # Post objektini yaratish
        Post.objects.create(title='Mavzu', text='yangilik matni')

    def test_text_content(self):
        # Yaratilgan Post objektini olish
        post = Post.objects.get(id=1)
        expected_object_title = post.title
        expected_object_text = post.text

        # Title va textni tekshirish
        self.assertEqual(expected_object_title, 'Mavzu')
        self.assertEqual(expected_object_text, 'yangilik matni')


class HomePageViewTest(TestCase):
    def setUp(self):
        # Post objektini yaratish
        Post.objects.create(title='Mavzu 2', text='boshqa yangilik')

    def test_views_url_exists_at_proper_location(self):
        # Root URL (/) mavjudligini tekshirish
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_urls_by_name(self):
        # Reverse orqali 'home' URL tekshirish
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        # To'g'ri template ishlatilganligini tekshirish
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
