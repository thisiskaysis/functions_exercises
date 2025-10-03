# Python Functions Exercises

The `functions_challenges.py` file in this repo contains four challenges for you. Have a go at all four! 

For each challenge you will be required to write a function. The first three challenges come with "skeleton" functions for you to modify, including "docstrings" that describe what the function should do. They also come with tests to check your work.

To solve these challenges, you should simply delete the word `pass` from the function, and write your own logic in the function body. No need to modify the names of the functions or the parameters! Leave the docstrings as they are too - it's good practise to use docstrings to document your code.

You can run test tests directly in VS Code from the `tests/test_function_challenges.py` file to check your work. When you have correctly solved all three challenges, the tests will pass. If you make an error in any of the challenges, the tests will tell you what went wrong. You may need to do a little Googling/thinking to figure out what the error messages mean. Grab a mentor if you get stuck.

If you need help interpreting the challenges, or have a bug you can't solve, grab a mentor for help!

## Solved Example Challenge

Here's an example of how to modify the code in `function_challenges.py` to solve the challenges. Let's say you got this challenge:

```py
def say_hello(name_string: str):
    """A function that returns a greeting to the user. 
      
    If the user's name is "Oliver", then the function should return "Hello, Oliver!"

    Arguments: 
        - name_string: A string containing the user's name
      
    Returns:
        - A string containing a greeting to the user
    """
    
    pass
```

In that case, a correct solution would look like this:

```py
def say_hello(name_string: str):
    """A function that returns a greeting to the user. 
      
    If the user's name is "Oliver", then the function should return "Hello, Oliver!"

    Arguments: 
        - name_string: A string containing the user's name
      
    Returns:
        - A string containing a greeting to the user
    """
    
    return f"Hello, {name_string}!"
```

