# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from six import text_type


class DjangoEmarsysError(Exception):
    pass


class BadDataError(DjangoEmarsysError):
    def __init__(self, expected_args, actual_args):
        super(BadDataError, self).__init__(
            "expected data args [{}], got [{}]"
            .format(', '.join("'{}'".format(text_type(x)) for x in expected_args),
                    ', '.join("'{}'".format(text_type(x)) for x in actual_args)))


class UnknownEventNameError(DjangoEmarsysError):
    def __init__(self, name):
        super(UnknownEventNameError, self).__init__("unknown event name: '{}'"
                                                    .format(name))
