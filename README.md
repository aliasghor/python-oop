<h1>Assalamualaikum (greetings), everyone👋</h1>
<p>Welcome to my Python Object-Oriented Programming repository, this repository covers the tutorial of Object-Oriented Programming in Python.</p>
<br>
<h2>What is OOP (Object-Oriented Programming)?</h2>
<p>According to <a href="https://en.wikipedia.org/wiki/Object-oriented_programming">wikipedia</a>, OOP (also known and abbreviated as OOP) is a programming paradigm based on the concept of objects, which can contain data and code: data in the form of fields (known as attribute or property) and code in the form of procedures (often known as methods). In OOP, computer programs are designed by making them out of objects that interact with one another.</p>
<br>
<h2>Example of Python OOP code:</h2>
<p>This is an example of a <code>Human</code> class in Python.</p>
<pre>
<code>
class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."

    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self.name}', {self.age})"

    def greet(self, other):
        return f"{self.name} greets {other.name}"
    
    def is_adult(self) -> bool:
        return self.human_is_adult(self.age)
    
    @staticmethod
    def human_is_adult(persons_age) -> bool:
        if persons_age < 18:
            return False
        return True
    
ali = Human("Ali", 21)
mom = Human("Upi", 56)

print(ali.greet(mom))  # Ali greets Upi
print(ali.is_adult())  # True
</code>
</pre>
<p>Here's what the code does:</p>
<ol>
    <li><code>Class Human:</code> A class serves as a blueprint for creating objects (instances) of that class; it also serves to create a new type of object, including it's attribute and methods.</li>
    <li><code>def __repr__(self) -> str:</code> This is called Python special method (magic method) that is called implicitly by Python to execute a certain operation on a type. In this case, it will provide an "offical" string representation of an object.</li>
    <li><code>def __str__(self) -> str:</code> Same like before, this is called Python special method. In this case, it will provide an "informal" string representation of an object or nicely printable string representation of an object.</li>
    <li><code>def greet(self):</code> An instance method to greet another object's name.</li>
    <li><code>def is_adult()</code> An instance method to check if a human is an adult.</li>
    <li><code>def human_is_adult_(persons_age):</code> This is called a static method, static method acts like a helper function (method). In this case, it will help to determine adulthood based on age.</li>
</ol>
<pre>
<code>
ali = Human("Ali", 21)
mom = Human("Upi", 56)

print(ali.greet(mom))  # Ali greets Upi
print(ali.is_adult())  # True
</code>
</pre>
<p>The output will be:</p>
<p><samp>Ali greets Upi <br>True</samp></p>

