import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
django.setup()

from django_seed import Seed
from blog.models import Post 

def seed_users(number: int = 10) -> None:
    seeder = Seed.seeder()

    # Настраиваем как именно будут генерироваться данные
    seeder.add_entity(Post, number, {
        'first_name': lambda x: seeder.faker.first_name(),
        'last_name': lambda x: seeder.faker.last_name(),
        'email': lambda x: seeder.faker.email()
    })
   
    inserted_pks = seeder.execute()
    print(f"Успешно добавлены записи с ID: {inserted_pks}")

if __name__ == '__main__':
    seed_users(100)