humans = 0

class People:
    def __init__(self, name: str, age: int, gender: str, job: str):
        global humans
        humans += 1
        self.name = name
        self.age = age
        self.gender = gender
        self.job = job

    def gdata(self):
        print(f"""
Name  :  {self.name}
Age   :  {self.age}
Gender:  {self.gender}
Job   :  {self.job}
        """)


if __name__ == '__main__':
    joe = People("Joe North", 36, "Male", "HVAC technician")
    chris = People("Christopher Thorndike", 12, "Male", "Little boi")
    joe.gdata()
    chris.gdata()
    print(humans)
