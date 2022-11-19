from django.test import TestCase, Client
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from blog.models import Post, Category, Tag, Comment

# Create your tests here.

class TestView(TestCase):

  def setUp(self):
    self.client = Client()
    self.user_Ojek = User.objects.create_user(username='ojek', password="password1234")
    self.user_Mmol = User.objects.create_user(username='mmol', password="password1234")
    self.user_Ojek.is_staff = True
    self.user_Ojek.save()

    self.category_programming = Category.objects.create(name='programming', slug='programming')
    self.category_music = Category.objects.create(name='music', slug='music')

    self.tag_python_kor = Tag.objects.create(name='파이썬 공부', slug='파이썬-공부')
    self.tag_python = Tag.objects.create(name='python', slug='python')
    self.tag_hello = Tag.objects.create(name='hello', slug='hello')

    self.post_001 = Post.objects.create(
      title = "첫 번째 포스트입니다.",
      content = "간단하게 써볼게요 ㅎㅎ",
      category = self.category_programming,
      author = self.user_Ojek
    )
    self.post_001.tags.add(self.tag_hello)

    self.post_002 = Post.objects.create(
      title = "두 번째 포스트",
      content = "띄어쓰기를 잘 합시다.",
      category = self.category_music,
      author = self.user_Mmol
    )

    self.post_003 = Post.objects.create(
      title = "세 번째 포스트입니다. python",
      content = "아이오이우",
      author = self.user_Ojek
    )
    self.post_003.tags.add(self.tag_python_kor)
    self.post_003.tags.add(self.tag_python)

    self.post_004 = Post.objects.create(
      title = "네 번째 포스트입니다. python",
      content = "ㅇㅇㅇㅇㅇㅇㅇㅇㅇ아이오이우",
      author = self.user_Mmol
    )

  def test_landing(self):
    response = self.client.get('')
    self.assertEqual(response.status_code, 200)
    soup = BeautifulSoup(response.content, 'html.parser')

    body = soup.body
    self.assertNotIn(self.post_001.title, body.text)
    self.assertIn(self.post_002.title, body.text)
    self.assertIn(self.post_003.title, body.text)
    self.assertIn(self.post_004.title, body.text)