# coding: utf-8
from __future__ import absolute_import, unicode_literals
import random
import string

from django.test import TestCase
from django.core.urlresolvers import reverse

import mock

from .models import Link
from .views import LinkCreate


class ShortenerTextTestCase(TestCase):
    def test_shortens(self):
        """
        Test that urls get shorter
        """
        url = "http://www.example.com/"
        l = Link(url=url)
        short_url = Link.shorten(l)
        self.assertLess(len(short_url), len(url))

    def test_recover_link(self):
        """
        Tests that shortened and expanded url is the same as original
        """
        url = "http://www.example.com/"
        l = Link(url=url)
        short_url = Link.shorten(l)
        l.save()
        # Another user asks for the expansion of short_url
        exp_url = Link.expand(short_url)
        self.assertEqual(url, exp_url)

    def test_homepage(self):
        """
        Tests that a home page exists and it contains a form
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)

    def test_shortener_form(self):
        """
        Tests that submitting the forms returns a Link object
        """
        url = "http://example.com/"
        response = self.client.post(reverse("home"),
                                    {"url": url}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("link", response.context)
        l = response.context["link"]
        short_url = Link.shorten(l)
        self.assertEqual(url, l.url)
        self.assertIn(short_url, response.content)

    def test_redirect_to_long_link(self):
        """
        Tests that short url redirects to long url
        """
        url = "http://example.com"
        l = Link.objects.create(url=url)
        short_url = Link.shorten(l)
        response = self.client.get(
            reverse("redirect_short_url",
                    kwargs={"short_url": short_url}))
        self.assertRedirects(response, url)

    def test_recover_link_n_times(self):
        """
        Tests multiple times that after shortening and expanding
        the original url is recovered.
        """
        TIMES = 100
        for i in xrange(TIMES):
            uri = "".join(random.sample(string.ascii_letters, 5))
            url = "https://example.com/{}/{}/".format(i, uri)
            l = Link.objects.create(url=url)
            short_url = Link.shorten(l)
            long_url = Link.expand(short_url)
            self.assertEqual(url, long_url)


class CreateViewTestCase(TestCase):

    @mock.patch('shorturls.views.redirect')
    @mock.patch.object(Link.objects, 'filter')
    def test_connect_user_to_previous_link(self, filter_mock, redirect_mock):
        """
        Tests whether link_show url is retrieved when it already exists and
        its relation with the user is set
        """
        # Get environment ready
        link_mock = mock.Mock()
        link_mock.pk = 2
        add_mock = link_mock.users.add
        user_mock = mock.Mock()
        user_mock.id = 1
        form_mock = mock.Mock()
        filter_mock.return_value = [link_mock]
        link_create = LinkCreate()
        link_create.request = mock.Mock(user=user_mock)

        # Call method
        link_create.form_valid(form_mock)

        # Assert
        add_mock.assert_called_with(user_mock)
        self.assertTrue(link_mock.save.called)
        redirect_mock.assert_called_with('link_show', pk=link_mock.pk)

    @mock.patch.object(Link.objects, 'filter')
    def test_connect_user_to_new_link(self, filter_mock):
        """
        Tests new link addition
        """
        # Get environment ready
        link_mock = mock.Mock()
        add_mock = link_mock.users.add
        user_mock = mock.Mock()
        user_mock.id = 1
        form_mock = mock.Mock()
        form_mock.save.return_value = link_mock
        filter_mock.return_value = None
        link_create = LinkCreate()
        link_create.request = mock.Mock(user=user_mock)
        # Save original super
        import __builtin__
        original_super = __builtin__.super
        link_create_father = mock.Mock()
        super_mock = mock.Mock()
        super_mock.return_value = link_create_father
        # Manual mock of super
        __builtin__.super = super_mock

        # Call method
        link_create.form_valid(form_mock)

        # Assert
        add_mock.assert_called_with(user_mock)
        self.assertTrue(form_mock.save.called)
        self.assertTrue(link_mock.save.called)
        super_mock.assert_called_with(LinkCreate, link_create)
        link_create_father.form_valid.assert_called_with(form_mock)
        # Assign to super its original value
        __builtin__.super = original_super
