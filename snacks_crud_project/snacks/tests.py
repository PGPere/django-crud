from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snacks


class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester', email='tester@email.com', password='pass'
        )
        self.snacks = Snacks.objects.create(
            name='Popcorn', description='salty', purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snacks), 'Popcorn')

    def test_snacks_content(self):
        self.assertEqual(f'{self.snacks.name}', 'Popcorn')
        self.assertEqual(f'{self.snacks.purchaser}', 'Pedro')
        self.assertEqual(f'{self.snacks.description}', 'salty')

    def test_snacks_list_view(self):
        response = self.client.get(reverse('list_snacks'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Popcorn')
        self.assertTemplateUsed(response, 'snacks-list.html')

    def test_snacks_detail_view(self):
        response = self.client.get(reverse('detail_snacks', args='1'))
        no_response = self.client.get('/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'purchaser: tester')
        self.assertTemplateUsed(response, 'snacks-detail.html')

    def test_snacks_create_view(self):
        response = self.client.post(
            reverse('create_snacks'),
            {
                'name': 'Popcorn',
                'description': 'salty',
                'purchaser': self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse('detail_snacks', args='2'))
        self.assertContains(response, 'Details about Popcorn')

    def test_snacks_update_view_redirect(self):
        response = self.client.post(
            reverse('update_snacks', args='1'),
            {'name': 'Updated name', 'description': 'new description',
                'purchaser': self.user.id}
        )

        self.assertRedirects(response, reverse('detail_snacks', args='1'))

    def test_snacks_delete_view(self):
        response = self.client.get(reverse('delete_snacks', args='1'))
        self.assertEqual(response.status_code, 200)
