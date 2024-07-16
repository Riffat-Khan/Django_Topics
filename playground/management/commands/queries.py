from ...models import Profile, Project, Task, Document, Comment

class Operations:
    def exists():
        return Profile.objects.filter(role='developer').exists()
        