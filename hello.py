def hello():
    print("Hello Akirachix")

def say_hello(name):
    print(f"hello{name}")
def great(name,age):
    year=2025-age
    print(f"hello{name},born in{year}")

def greatings(names):
    for name in names :
        print(f"hello{name}")
def year_of_birth(name,age):
    year = 2025 - age
    print(f"Hello {name},born in {year}")      
def my_country(name="uganda"):
    print(f"I love my country {name}")
def welcome_student(**kwargs):
    print(kwargs)    
def create_sentence(**words):
    sentence = " "
    for word in words.values():
        sentence += word
        sentence +=" "
    return sentence   
def exam_result(*args,**kwargs):
    name = kwargs.get('name', '')
    course = kwargs.get('course', '') 
    if not args:
        return f"Hello {name} ,we don't have your results for {course}"
    average_score = sum(args) / len(args) 
    print(f"Hello {name}, your average score for {course} is {int(average_score)}")
   
   


