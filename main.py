from flask import Flask, render_template, request
from PIL import Image
import pytesseract
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/')
def index():
    return render_template('index.html')

# Это декоратор маршрута, который указывает, что данный обработчик будет обрабатывать запросы по адресу "/extract_text" с методом POST.

@app.route('/a', methods=['POST'])

#Это функция, которая будет вызываться при запросе по указанному маршрутуy./
def extract_text():
#Эта строка получает файл изображения, который был отправлен с помощью POST-запроса.
# Flask сохраняет загруженные файлы в специальный объект request.files, и мы получаем доступ к файлу по его ключу, в данном случае 'image'.
    image_file = request.files['image']

    # Здесь открывается изображение с помощью библиотеки Pillow (Image.open). image_file - это объект файла,
# который мы получили на предыдущем шаге. После этого изображение можно обрабатывать с помощью Pillow.
    img = Image.open(image_file)

# cдесь происходит извлечение текста из изображения. Метод image_to_string из библиотеки pytesseract используется для этой цели.
# Он принимает объект изображения и возвращает извлеченный текст.
    text = pytesseract.image_to_string(img)
# После того как текст был извлечен, он передается в шаблон 'result.html' с помощью функции render_template.
# Этот текст будет доступен в шаблоне через переменную text.
    return render_template('result.html', text=text)

if __name__ == "__main__":
    app.run(debug=True)
