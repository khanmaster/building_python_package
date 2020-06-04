# Building python package from scratch
### Let's build a python package root folder structure 
```python
-- app (folder)
---__init___.py
----fizzbuzz.py
program.py
setup.py
```
- we'll create all above files and leave them emtpy for now
```markdown
The init.py file
The init.py files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later (deeper) on the module search path. In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for the package.

setup.py
The setup.py file is to describe your module and the details regarding it's ownership and distribution. In the early stages of your career it will be unlikely that you'll be creating many but it is worth being aware of as a Python developer!

In it's basic format you can get away with the below as your setup.py file:

from setuptools import setup

setup(name="app")
There is all sorts of information you could / probably should provide such as:

version='1.0'
description='Python app'
author='Shah'
author_email='abc@gmail.com'
url='https://www.python.org/sigs/distutils-sig/'
However, in this instance we will keep the setu
p.py as is.

The next step is to utilise pip to install our package, this is to ensure that the Python interpreter is aware of our package and has referenced it into the local library.

pip install . 
- what we are saying here is install the setup file from the local directory and pip looks for this file as part of it's standard search.
```
- what you should see is something like the below output:

```markdown
Successfully built app
Installing collected packages: app
  Found existing installation: app 0.0.0
    Uninstalling app-0.0.0:
      Successfully uninstalled app-0.0.0
Successfully installed app-0.0.0
```

This shows that your app is successfully installed locally and will now be made available in your python library.

- Let's move on to next steps

app folder inputs
Within the app folder input the below into the fizzbuzz_oop.py file:

```python
class Fizzbuzz:
    def __init__(self, start_of_range, end_of_range):
        self.fizzrange = range(start_of_range, end_of_range)
        self.fizzbuzz_list = []
        self.fizz_buzz = self.__fizzbuzz_iterator()

    def _divisible_by(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    def __fizzbuzz_iterator(self):
        for num in self.fizzrange:
            if self._divisible_by(num, 5) and self._divisible_by(num, 3):
                self.fizzbuzz_list.append("fizzbuzz")
            elif self._divisible_by(num, 5):
                    self.fizzbuzz_list.append("buzz...")
            elif self._divisible_by(num, 3):
                    self.fizzbuzz_list.append("fizzz..")
            else:
                self.fizzbuzz_list.append(num)

# num_1_to_100 = Fizzbuzz(1, 100)
#
# print(num_1_to_100.fizzbuzz_list)
# cLet's import this file in our program.py
```

- Let's now update our program.py file to invoke the fizzbuzz solution:

```python
from app.fizzbuzz_oop import Fizzbuzz

num_1_to_100 = Fizzbuzz(1, 100)

#print(num_1_to_100.fizzbuzz_list)
list_fizz_buzz = num_1_to_100.fizzbuzz_list
for result in list_fizz_buzz:
    print(result)
```
``` from app.fizzbuzz_oop import Fizzbuzz within our module importing``` we should now be able to reference and call our module using the 'dot' notation from our app folder.
When completing the rest of our code and run the file we should see the output of our fizzbuzz program.