"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Post
from django.core.urlresolvers import reverse
from models import DRAFT, PUBLISHED


class SimpleTest(TestCase):
    def test_post_slug_creation(self):
        from django.template.defaultfilters import slugify
        title = "Test title"
        post = Post(title=title)
        post.save()
        self.assertEqual(post.slug, slugify(title))

    def test_home(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        title = "Some title"

        # DRAFT post must throw 404
        post = Post(title=title, status=DRAFT)
        post.save()
        resp = self.client.get(reverse('post', args=[post.id]))
        self.assertEqual(resp.status_code, 404)

        # PUBLISHED returns normal post
        post.status = PUBLISHED
        post.save()
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('post' in resp.context)
        self.assertEqual(resp.context['post'].pk, post.id)
        self.assertEqual(resp.context['post'].title, title)

        #test unexisting post
        # Ensure that non-existent polls throw a 404.
        resp = self.client.get(reverse('post', args=[post.id + 1]))
        self.assertEqual(resp.status_code, 404)
