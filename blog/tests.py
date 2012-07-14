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
    def test_slug_creation(self):
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
        resp = self.client.get(post.get_absolute_url())
        self.assertEqual(resp.status_code, 404)

        # PUBLISHED returns normal post
        post.status = PUBLISHED
        post.save()
        resp = self.client.get(post.get_absolute_url())
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('post' in resp.context)
        self.assertEqual(resp.context['post'].pk, post.id)
        self.assertEqual(resp.context['post'].title, title)

        #test unexisting post (must throw 404)
        resp = self.client.get(reverse('post_without_slug', args=[post.id + 1]))
        self.assertEqual(resp.status_code, 404)

    def test_slug_in_post_url(self):
        title = "Some title"
        post = Post(title=title, status=PUBLISHED)
        post.save()

        # test absolute_url
        resp = self.client.get(post.get_absolute_url(), follow=True)
        self.assertTrue(resp.request["PATH_INFO"].endswith(post.slug + "/"))

        # test URL without slug
        resp = self.client.get(reverse('post_without_slug', args=[post.id]), follow=True)
        self.assertTrue(resp.request["PATH_INFO"].endswith(post.slug + "/"))

        # test URL with fake slug
        resp = self.client.get(reverse('post', args=[post.id, "some_fake_slug_12345667890"]), follow=True)
        self.assertTrue(resp.request["PATH_INFO"].endswith(post.slug + "/"))

