from faker import Faker

from blog.models import Post
from django.contrib.auth.models import User

def generate_post(n, language="pl_PL"):
    faker = Faker(language)
    authors = User.objects.all()
    statuses = ["published","draft"]

    for _ in range(n):
        title = faker.sentence()
        content_length = faker.random_int(100, 2000)
        content = faker.text(content_length)

        author = faker.random_element(authors)
        status = faker.random_element(statuses)

        post = Post(title=title, content=content, author=author, status=status)
        post.save()

    print(f"Generated {n} posts")
