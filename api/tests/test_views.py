import copy

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from signal_data.factories import DataSignalFactory
from api.factories import OrganizationAPIKeyFactory
from signal_data.utils import hash_identifier


class PublicDataSignalViewSetTest(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.api_key_obj, cls.key = OrganizationAPIKeyFactory.create(
            internal=False
        )
        cls.test_identifier = 'test@example.com'
        cls.data_signal = DataSignalFactory.create(
            identifier=hash_identifier(cls.test_identifier),
        )
        cls.list_url = reverse('datasignal-list')
        cls.detail_url = reverse('datasignal-detail', args=[cls.data_signal.pk])
        cls.private_list_url = reverse('data_signals_internal-list')
        cls.client = APIClient()

    def test_get_list_no_key(self) -> None:
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_detail_no_key(self) -> None:
        resp = self.client.get(self.detail_url)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_bad_key(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION='Api-Key badIncorrectsuperWrongKey')
        resp = self.client.get(self.list_url)

        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_with_key(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.key}')
        resp = self.client.get(self.list_url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_list_with_key_private_url(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.key}')
        resp = self.client.get(self.private_list_url)

        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_detail_with_key(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.key}')
        resp = self.client.get(self.detail_url)

        self.assertIn('uuid', resp.data)

    def test_get_query_with_key(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.key}')
        resp = self.client.get(self.list_url + f'?identifier={self.test_identifier}')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(any('uuid' in x for x in resp.data))

    def test_get_bad_qparam_with_key(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.key}')
        resp = self.client.get(self.list_url + '?identifier=bad_q_param')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual([], resp.data)

    def test_post_not_allowed(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.key}')
        resp = self.client.post(self.list_url, {})

        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class PrivateDataSignalViewSetTest(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.api_key_obj, cls.key = OrganizationAPIKeyFactory.create(
            internal=True
        )
        cls.test_identifier = 'test1@example.com'
        cls.data_signal = DataSignalFactory.create(
            identifier=hash_identifier(cls.test_identifier),
        )
        cls.post_data = {
            'signal_type': 'Email',
            'identifier': 'test2@example.com',
            'signal_value': 'do-not-contact',
            'valid': False
        }
        cls.list_url = reverse('data_signals_internal-list')
        cls.detail_url = reverse('data_signals_internal-detail', args=[cls.data_signal.pk])
        cls.client = APIClient()

    def test_get_list_no_key(self) -> None:
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_detail_no_key(self) -> None:
        resp = self.client.get(self.detail_url)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_no_key(self) -> None:
        resp = self.client.get(self.list_url, self.post_data)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_with_key(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.key}')
        resp = self.client.get(self.list_url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_detail_with_key(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.key}')
        resp = self.client.get(self.detail_url)

        self.assertIn('uuid', resp.data)

    def test_post_with_key(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.key}')
        resp = self.client.post(self.list_url, self.post_data)

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertIn('uuid', resp.data)

    def test_bad_post_with_key(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.key}')
        post_data = copy.deepcopy(self.post_data)
        post_data.pop('identifier')
        resp = self.client.post(self.list_url, post_data)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('identifier', resp.data)

    def test_post_with_key_invalid_ident(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=f'Api-Key {self.key}')
        post_data = copy.deepcopy(self.post_data)
        post_data['identifier'] = 'bad ident'
        resp = self.client.post(self.list_url, post_data)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('identifier', resp.data)
