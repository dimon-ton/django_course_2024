from django.test import TestCase
import qrcode
# Create your tests here.


img = qrcode.make('Some data here')
img.save("some_file.png")