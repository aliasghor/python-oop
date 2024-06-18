<h1>Assalamualaikum (greetings), everyone👋</h1>
<p>Welcome to my Python Object-Oriented Programming repository , this repository covers the tutorial of Object-Oriented Programming in Python.</p>
<br>
<h2>What is OOP (Object-Oriented Programming)?</h2>
<p>According to <a href="https://en.wikipedia.org/wiki/Object-oriented_programming">wikipedia</a>, OOP (also known and abbreviated as OOP) is a programming paradigm based on the concept of objects, which can contain data and code: data in the form of fields (known as attribute or property) and code in the form of procedures (often known as methods). In OOP, computer programs are designed by making them out of objects that interact with one another.</p>
<br>
<h2>Example of Python OOP code:</h2>
# Human Class Example

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
    
    def is_adult(self):
        return self.human_is_adult(self.age)
    
    @staticmethod
    def human_is_adult(persons_age):
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
    <li>Defines a <code>Human</code> class with <code>name</code> and <code>age</code> attributes.</li>
    <li>Provides a <code>__str__</code> method for a human-readable string representation.</li>
    <li>Provides a <code>__repr__</code> method for an official string representation.</li>
    <li>Adds a <code>greet</code> method for one human to greet another.</li>
    <li>Adds an <code>is_adult</code> method to check if a human is an adult.</li>
    <li>Uses a static method <code>human_is_adult</code> to determine adulthood based on age.</li>
</ol>

<pre>
<code>
ali = Human("Ali", 21)
mom = Human("Upi", 56)

print(ali.greet(mom))  # Ali greets Upi
print(ali.is_adult())  # True
</code>
</pre>

<p>This will be output:</p>

<!-- <pre> -->
<code>
Ali greets Upi
True
</code>
<!-- </pre> -->

