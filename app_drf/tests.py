from django.test import TestCase



from django.contrib.auth.models import User

from .models import Car


class CarTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        testuser1 = User.objects.create_user(username="shahd", password="12345")

        testuser1.save()


        test_car = Car.objects.create(

            purchaser=testuser1, name_car="BMW", description="BMW and Audi Cars the best car in the world."
        )
        test_car.save()

    def test_Car_content(self):

        car = Car.objects.get(id=1)

        expected_purchaser = f"{car.purchaser}"

        expected_name_car = f"{car.name_car}"

        expected_description = f"{car.description}"

        self.assertEqual(expected_purchaser, "shahd")

        self.assertEqual(expected_name_car, "BMW")

        self.assertEqual(expected_description, "BMW and Audi Cars the best car in the world.")


from django.contrib.auth import get_user_model

class CarTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        testuser1 = get_user_model().objects.create_user(username='shahd', password='12345')

        testuser1.save()

        test_car = Car.objects.create(name_car='BMW', description="BMW and Audi Cars the best car in the world.", purchaser=testuser1)

        test_car.save()



    def test_car_content(self):

        car = Car.objects.get(id=1)

        expected_purchaser = f'{car.purchaser}'

        expected_name_car = f'{car.name_car}'

        expected_description = f'{car.description}'

        self.assertEqual(expected_purchaser, 'shahd')

        self.assertEqual(expected_name_car, 'BMW')

        self.assertEqual(expected_description, "BMW and Audi Cars the best car in the world.")
