from django.core.management.base import BaseCommand, CommandParser
from django.utils.crypto import get_random_string
from ...models import members

class Command(BaseCommand):
    help = 'create random 50 users'
    
    def handle(self, *args, **kwargs):
        for i in range(50):
            members.objects.create(
                firstname=get_random_string(length=5),
                lastname=get_random_string(length=5), 
                phone=87456788899,
                )
            