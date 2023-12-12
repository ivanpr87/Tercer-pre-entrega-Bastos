from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Auto

class AutoModelTest(TestCase):

    def setUp(self):
        # Crear un objeto Auto con una imagen simulada para las pruebas
        image = SimpleUploadedFile("auto_image.jpg", b"file_content", content_type="image/jpeg")
        self.auto = Auto.objects.create(fabricante='Toyota', modelo='Camry', año=2022, color='Rojo', imagen=image)

    def test_auto_str_representation(self):
        # Verifica si el método __str__ devuelve la representación correcta para el objeto Auto
        expected_str = f'Toyota - Camry - 2022'
        self.assertEqual(str(self.auto), expected_str)

    def test_get_imagen_url_with_image(self):
        expected_partial_url = f'/media/autos/{self.auto.imagen.name.split("/")[-1]}'
        self.assertIn(expected_partial_url, self.auto.get_imagen_url())

    def test_get_imagen_url_without_image(self):
        # Verifica si la función maneja correctamente la ausencia de una imagen
        auto_sin_imagen = Auto.objects.create(fabricante='Ford', modelo='Focus', año=2023, color='Azul')

        self.assertIsNone(auto_sin_imagen.get_imagen_url())

    def tearDown(self):
        Auto.objects.all().delete()
