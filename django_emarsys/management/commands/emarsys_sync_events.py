# -*- coding: utf-8 -*-

from django.core.management import BaseCommand

from ...event import sync_events


class Command(BaseCommand):
    def handle(self, *args, **options):
        num_new_events, num_updated_ids, num_deleted_ids, \
            unsynced_event_names = sync_events()
        print("{} new events, {} event ids updated,"
              " {} event ids deleted"
              .format(num_new_events, num_updated_ids, num_deleted_ids))
        if unsynced_event_names:
            print("unsynced event names:\n    {}"
                  .format('\n    '.join(unsynced_event_names)))
