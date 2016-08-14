import logging
import re
from collections import Set

from django.conf import settings

log = logging.getLogger(__name__)


def _translate_pattern(pattern):
    out = ('.*' if c == '*' else re.escape(c) for c in pattern)
    return re.compile('^{}$'.format(''.join(out)))


class _Whitelist(Set):

    def __contains__(self, x):
        return any(pattern.match(x) for pattern in self)

    def __len__(self):
        return len(self)

    def __iter__(self):
        patterns = getattr(settings, 'EMARSYS_RECIPIENT_WHITELIST', None)
        if patterns is None:
            patterns = ['*']

        return iter(set(_translate_pattern(p) for p in patterns))

items = _Whitelist()


def filter_contacts(contacts, getter):
    return (c for c in contacts if getter(c) in items)
