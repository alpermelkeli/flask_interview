#This script is used to seed the database with default questions.

from app import app, db
from app.models import Question

default_questions = [
    {
        'question_text': 'Yapay zeka modellerini eğitirken en yaygın kullanılan Python kütüphanesi hangisidir?',
        'option1': 'Pandas',
        'option2': 'TensorFlow',
        'option3': 'Matplotlib',
        'option4': 'BeautifulSoup',
        'correct_answer': 'TensorFlow'
    },
    {
        'question_text': 'Bilgisayar görüşü uygulamalarında hangi kütüphane en yaygın kullanılır?',
        'option1': 'NumPy',
        'option2': 'Pandas',
        'option3': 'OpenCV',
        'option4': 'Scikit-learn',
        'correct_answer': 'OpenCV'
    },
    {
        'question_text': 'NLP uygulamalarında cümle tokenizasyonu için en sık kullanılan kütüphane hangisidir?',
        'option1': 'Matplotlib',
        'option2': 'NLTK',
        'option3': 'Seaborn',
        'option4': 'Plotly',
        'correct_answer': 'NLTK'
    },
    {
        'question_text': 'Yapay zeka modelini Python uygulamasına entegre ederken hangi format kullanılmaz?',
        'option1': '.h5',
        'option2': '.pkl',
        'option3': '.exe',
        'option4': '.onnx',
        'correct_answer': '.exe'
    },
    {
        'question_text': 'Derin öğrenme modellerinde en yaygın kullanılan aktivasyon fonksiyonu hangisidir?',
        'option1': 'ReLU',
        'option2': 'Sigmoid',
        'option3': 'Tanh',
        'option4': 'Linear',
        'correct_answer': 'ReLU'
    }
]

def seed_database():
    with app.app_context():
        #Clear the database
        db.drop_all()
        db.create_all()
        #Add questions to the database
        for question_data in default_questions:
            question = Question(**question_data)
            db.session.add(question)
        
        # Save changes.
        db.session.commit()
        print("Veritabanı başarıyla dolduruldu!")

if __name__ == "__main__":
    seed_database()