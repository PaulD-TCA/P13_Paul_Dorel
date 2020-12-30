from django.test import TestCase
from django.contrib.auth.models import User
from design.models import Design, AddUserInfo, Message, Offer, Order

class TestModels(TestCase):
    def setUp(self):
        self.user_setup_test = User(
            id = 1,
            username="Armelle",
            password="password1234",
            email="armelle@gmail.com"
        )
        self.user_setup_test.save()

        self.add_user_info_setup_test = AddUserInfo(
            id = 1,
            street="54 avenue des alouettes",
            zip_code="44100",
            city="Nantes",
            country="France",
            phone_number="0244558899",
            user_id_id="1"
        )
        self.add_user_info_setup_test.save()

        self.design_setup_test = Design(
            id = 1,
            design_name="cube",
            design_image="design_image",
            plan_2d="plan_2d",
            plan_3d="plan_3d",
            assembly_instruction="assembly_instruction",
            description="description",
            category="Jouet",
            creation_date="2020-12-03 18:21:14.75514+01",
            user_id_id="1"
        )
        self.design_setup_test.save()

        self.message_setup_test = Message(
            id = 1,
            recipent="1",
            title="title",
            content="content",
            sended_date="2020-12-03 18:21:14.75514+01",
            opened="1",
            user_id_id="1"
        )
        self.message_setup_test.save()

        self.offer_setup_test = Offer(
            id = 1,
            user_id_id="1",
            design_id_id="1",
            offer_title="offer_title",
            date_offer="2020-12-03 18:21:14.75514+01",
            price="10",
            carriage_price="11",
            deadline="5",
            shipment="I",
        )
        self.offer_setup_test.save()

        self.order_setup_test = Order(
            id = 1,
            order_date="2020-12-03 18:21:14.75514+01",
            quantity="1",
            user_id_id="1",
            offer_id_id="1",
        )
        self.order_setup_test.save()

    def test_create_user(self):
        self.assertEqual(self.user_setup_test.username, "Armelle")
        self.assertEqual(self.user_setup_test.password, "password1234")
        self.assertEqual(self.user_setup_test.email, "armelle@gmail.com")

    def test_add_user_info(self):
        self.assertEqual(self.add_user_info_setup_test.street, "54 avenue des alouettes")
        self.assertEqual(self.add_user_info_setup_test.zip_code, "44100")
        self.assertEqual(self.add_user_info_setup_test.city, "Nantes")

    def test_design(self):
        self.assertEqual(self.design_setup_test.design_name, "cube")
        self.assertEqual(self.design_setup_test.design_image, "design_image")
        self.assertEqual(self.design_setup_test.plan_2d, "plan_2d")

    def test_message(self):
        self.assertEqual(self.message_setup_test.recipent, "1")
        self.assertEqual(self.message_setup_test.title, "title")
        self.assertEqual(self.message_setup_test.content, "content")

    def test_offer(self):
        self.assertEqual(self.offer_setup_test.user_id_id, "1")
        self.assertEqual(self.offer_setup_test.design_id_id, "1")
        self.assertEqual(self.offer_setup_test.offer_title, "offer_title")

    def test_order(self):
        self.assertEqual(self.order_setup_test.user_id_id, "1")
        self.assertEqual(self.order_setup_test.quantity, "1")
        self.assertEqual(self.order_setup_test.user_id_id, "1")
