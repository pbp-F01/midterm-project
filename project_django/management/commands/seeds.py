from django.core.management import BaseCommand
from django.contrib.auth.models import User
from profileUMKM.models import ProfileUMKM
from landing.models import Profile
import string
import random

""" Clear all data and do not create any object """
MODE_CLEAR = "clear"


class Command(BaseCommand):
    help = "seed database for production."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options) -> None:
        self.stdout.write("seeding data...")
        run_seed(self, options["mode"])
        self.stdout.write("done.")


def clear_data():
    """Deletes all the table data"""
    print("Delete All instances")
    User.objects.all().delete()
    ProfileUMKM.objects.all().delete()
    Profile.objects.all().delete()


def run_seed(self, mode):
    """Seed database based on mode

    :param mode: refresh / clear
    :return:
    """

    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # seeding db
    create_super_user()
    create_task()


def create_super_user():
    User.objects.create_superuser(
        username="admin", email="admin@gmail.com", password="3231"
    )


def random_string(n=20) -> str:
    return "".join(random.choice(string.ascii_lowercase) for _ in range(n))


def create_task():
    """Creates an task object combining different elements from the list"""
    print("Creating tasks")
    USER_DATA = [
        {
            "username": "dummyuser1",
            "password": "dummypassword1",
        },
        {
            "username": "dummyuser2",
            "password": "dummypassword2",
        },
        {
            "username": "dummyuser3",
            "password": "dummypassword3",
        },
    ]

    for i in range(3):
        user = User.objects.create_user(**USER_DATA[i])
        Profile.objects.create(
            user=user,
            name="Haji Ade",
            email=random_string() + "@gmail.com",
            roles="P",
        )

    # profile_user = Profile.objects.first()

    # for _ in range(10):
    #     ProfileUMKM.objects.create(
    #         nama=random_string(10),
    #         pemilik=profile_user,
    #         no_telepon=random_string(10),
    #         email=random_string(10) + "@gmail.com",
    #         kontak=random_string(10),
    #         kota=random_string(10),
    #         provinsi=random_string(10),
    #         kodepos=random.randint(1, 90000),
    #         foto="https://cdn2.thecatapi.com/images/MjA0NzcwNA.jpg",
    #     )

    print(f"tasks created.")
