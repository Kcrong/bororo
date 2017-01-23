# Bororo

![Bororo](https://raw.githubusercontent.com/Kcrong/bororo/master/bororo.jpg)


## Started..
Bororo is a friend of kcrong.
That's why this chatbot's name is bororo.


## Requirements

I Used...

1. Python 3.6 ([Awesome Format String](https://docs.python.org/3.6/reference/lexical_analysis.html#f-strings)!!) . 
2. [konlpy](http://konlpy.org/) (Korean pos tagger with mecab) . 
3. [My Personal Python Utility](https://github.com/Kcrong/python-utility) . 

to install,  
```bssh
$ pip install -r requirements.txt
$ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
```
## Features
I want to make something like : [DSTC](http://camdial.org/~mh521/dstc/) bot

So.. Let's See features with screenshot

First, you need to give the name of the bot.

![1](https://raw.githubusercontent.com/Kcrong/bororo/master/images/1.png)

After, Just teach anything you want.
Let's talk about apple here.

![2](https://raw.githubusercontent.com/Kcrong/bororo/master/images/2.png)

As you can see, `Bororo Bot` has learned information about apples.

Next, Let's teach about apple's color


![3](https://raw.githubusercontent.com/Kcrong/bororo/master/images/3.png)

`Bororo Bot` has learned apple's color!


## How to learn?

After the user enters a sentence, the `Analyzer` starts to analyzing

![4](https://raw.githubusercontent.com/Kcrong/bororo/master/images/4.png)
(There is some typo.. `anal = Analy'z'er(talk)` )
<br>
In Analzer, store pos tagging result in the `tag` variable
![5](https://raw.githubusercontent.com/Kcrong/bororo/master/images/5.png)
Then, as a pos tagging result(the morpheme),  get object's name, attr, value
> `apple's color is red
>> `name`: apple
>> `attr`: color
>> `value`: red

After parsing `name`, `attr`, `value`,  
**bot** starts to learning.

![6](https://raw.githubusercontent.com/Kcrong/bororo/master/images/6.png)
Check `attr` isn't NULL . 
if there is valid `attr`, goto `_learn_info` func,  
else then, goto `_learn_thing` func . 

The difference between the two functions is very small.  
just `Fragmentary information` or `Object's Information` . 

After learning,  
to print out the learned results, use the `print_my_knowledge` function at `Brain` class . 
![7](https://raw.githubusercontent.com/Kcrong/bororo/master/images/7.png)
