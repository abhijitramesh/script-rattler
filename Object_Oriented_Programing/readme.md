# Object Oriented Programming
If you are starting to code in python and you are looking at this page please go away. Object Oriented Programming is not the way to get started with coding. That being said I think it might work out different with different people. I started coding in java which is an Object Oriented Programming pro language. Things did not go well for me then since I was not able to understand most of the stuff that was happening TBH. Then I learned to code in C and that was when things started making sense. Going back to java now I understand most of the core stuff and I am pretty confident about it. Anyways Python is very simple to grasp so lets see.

# Vocabularies
The basic things to understand in Object Oriented Programing is as the name suggests _Objects_, This is the fundamental building block of OOP. But its better to relate this to real world examples.

Imagine that you are walking into a shop and you find a T shirt. This T shirt is yellow in color, size is XL and has V neck. Then there is another T shirt which is green in color, size is L and the neck is normal. The price of the yellow shirt is say 15$ and the size of the green shirt is say 20$. Since we are confused among the shirts we end up not buying them and go back home and come back the next day with a friend to finally make a decision. So here we are looking at both the shirts and to out surprise the price has changed. The yellow shirt is now 12$ and the green shirt is now 15$. Now let us critically analyze this situation. T shirts are something very generic and it has some properties like color, style, price. And it does some kind of action also like changing its price. 
#### Classes
In OOP was the generic thing that is T shirt is called a class its like a blue print from which more items can be made.
#### Attribute
These are the characteresetis of the T shirt like color,size,price etc...
#### Methods
The shirt does some action like changing its price this is called Method.
#### Object
The specific T shirt that is derived from this blueprint of T shirts with all specified _Attributes_ and does some _Method_ is called an Object Like the Yellow or Green Shirt.

Lets see how this looks in code

So let us define a class called Shirt

```python
class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
    
    def change_price(self, new_price):
    
        self.price = new_price
        
    def discount(self, discount):

        return self.price * (1 - discount)
```

Here the __init__ is used to define the method, it is passed in with the attributes that we are associating the shirt with and also self.

So what is self ?
Lets say we are creating two objects called shirt_one and shirt_two

``` python
shirt_one = Shirt('red','L','Long-Sleeve',25)
shirt_two = Shirt('yellow','L','Long-Sleeve',30)
```

Now i need to change the price of shirt_one object, How does python know that I need to be changing the price of shirt_one and shirt_two this is where self comes to play,Self tells python where the shirt_one object is in the computers memory and helps it to apply the function when i do
``` python 
shirt_one.change_price(24)
```
here self is implicitly passed.

[click here](https://github.com/abhijitramesh/script-rattler/blob/master/Object_Oriented_Programing/shirt_exercise.ipynb)

To check out an exercise with solution based on shirt class.

Normally to write object oriented code or any code in production we do not use Jupiter Notebook, this tool is only meant for exploration and to figure out stuff. 

In production work we use a different file for a class example the Shirt class can be in a file called [shirt.py](https://github.com/abhijitramesh/script-rattler/blob/master/Object_Oriented_Programing/shirt.py)

and another class called [example.py](https://github.com/abhijitramesh/script-rattler/blob/master/Object_Oriented_Programing/example.py)

in this class we need can import the Shirt class to use it 

```python
from shirt import Shirt
```

The shirt represents the file and Shirt represents the class that we are importing also,

We can access the attributes in an object by using something like

```pyton
shirt_one.price = 10
shirt_one.price = 20
shirt_one.color = 'red'
shirt_one.size = 'M'
shirt_one.style = 'long_sleeve'
```

But in practice we use methods to do this rather than accusing it directly since we need to be writing modular code in production.

[Check out](https://github.com/abhijitramesh/script-rattler/blob/master/Object_Oriented_Programing/salesman.ipynb) this example for better understanding basic oop practices.

# Commenting

Commenting is an important part while writing code this not only helps you remember what your code is doing but also help other programmers understand the code that you have written and help collaborate.

We can use both inline as well as doctoring comment to comment our code.

[click](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) here to check out how to write good comments.

[click here](https://github.com/abhijitramesh/script-rattler/blob/master/Object_Oriented_Programing/pants.py) to checkout our Pants class but well commented.
