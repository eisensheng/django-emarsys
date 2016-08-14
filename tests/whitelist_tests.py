from django.test import TestCase, override_settings


class WhitelistTestCase(TestCase):

    @override_settings(EMARSYS_RECIPIENT_WHITELIST=[
        'john.doe@example.test', 'postmaster@experimental.test'])
    def test_whitelist_says_yes(self):
        from django_emarsys import whitelist

        self.assertIn('john.doe@example.test', whitelist.items)

    @override_settings(EMARSYS_RECIPIENT_WHITELIST=[
        'john.doe@example.test', '*@experimental.test'])
    def test_whitelist_wildcard_says_yes(self):
        from django_emarsys import whitelist

        self.assertIn('john.doe@experimental.test', whitelist.items)

    @override_settings(EMARSYS_RECIPIENT_WHITELIST=['*@example.test'])
    def test_whitelist_wildcard_says_no(self):
        from django_emarsys import whitelist

        self.assertNotIn('john.doe@sample.test', whitelist.items)

    @override_settings(EMARSYS_RECIPIENT_WHITELIST=['*'])
    def test_whitelist_allows_it_all(self):
        from django_emarsys import whitelist

        self.assertIn('john.doe@sample.test', whitelist.items)
