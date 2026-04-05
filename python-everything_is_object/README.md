# Python Everything is Object

## Project Overview
This project explores the concept that **everything in Python is an object**.  
You will learn about **mutable vs immutable objects**, **object identity**, **aliasing**, **cloning lists**, and **how Python passes arguments to functions**.  

The goal is to understand **how Python handles variables in memory** and how this affects code behavior.  

---

## Table of Contents
1. [Introduction](#introduction)  
2. [Requirements](#requirements)  
3. [Files and Tasks](#files-and-tasks)  
4. [Usage](#usage)  
5. [Author](#author)  

---

## Introduction
In Python, everything is an object: integers, strings, lists, tuples, functions, even classes themselves.  
- Mutable objects (lists, dicts, sets) can be changed in place.  
- Immutable objects (ints, strings, tuples) cannot be changed in place.  

You will practice:
- Using `type()` and `id()` to inspect objects.  
- Understanding how variable assignment works.  
- Comparing objects with `==` and `is`.  
- Passing arguments to functions and observing effects on mutable and immutable objects.  

---

## Requirements
- Python 3.8+  
- Ubuntu 20.04 LTS for testing  
- Code style: pycodestyle 2.7.*  
- All files must be executable and end with a newline  

---

## Files and Tasks

| File | Task | Description |
|------|------|------------|
| `0-answer.txt` | Who am I? | Name the function to get the type of an object (`type`) |
| `1-answer.txt` | Where are you? | Name the function to get the object identifier (`id`) |
| `2-answer.txt` | Right count | Do variables point to the same object? (`No`) |
| `3-answer.txt` | Right count | Do variables point to the same object? (`Yes`) |
| `4-answer.txt` | Right count | Do variables point to the same object? (`Yes`) |
| `5-answer.txt` | Right count | Do variables point to the same object? (`No`) |
| `6-answer.txt` | Is equal | Compare values of strings (`True`) |
| `7-answer.txt` | Is the same | Compare identity of strings (`True`) |
| `8-answer.txt` | Is really equal | Compare values of strings (`True`) |
| `9-answer.txt` | Is really the same | Compare identity of strings (`False`) |
| `10-answer.txt` | List equality | Compare list values (`True`) |
| `11-answer.txt` | List identity | Compare list objects (`False`) |
| `12-answer.txt` | List really equal | Compare values after assignment (`True`) |
| `13-answer.txt` | List really the same | Compare identity after assignment (`True`) |
| `14-answer.txt` | List append | Effects of mutating a list (`[1, 2, 3, 4]`) |
| `15-answer.txt` | List add | Effects of `+` operator (`[1, 2, 3]`) |
| `16-answer.txt` | Integer incrementation | Effect on immutable (`1`) |
| `17-answer.txt` | List incrementation | Effect on mutable (`[1, 2, 3, 4]`) |
| `18-answer.txt` | List assignation | Reassignment inside function (`[1, 2, 3]`) |
| `19-copy_list.py` | Copy a list object | Function to return a copy of a list |
| `20-23-answer.txt` | Tuple checks | Identify if variable is a tuple |
| `24-28-answer.txt` | Identity vs equality | Observe behavior of `is` and `==` for ints, tuples, lists |

---

## Usage
Run each task file individually to see the result:  

```bash
chmod +x <file>.py
./<file>.py

```

## Blog Post Links
- LinkedIn: [Python3: Everything is an Object](https://www.linkedin.com/posts/hamsa-al-amaar_this-is-a-project-i-completed-as-part-of-activity-7446494068039110656-FeRe?utm_source=share&utm_medium=member_desktop&rcm=ACoAADI4aikB_MsKdE8YLU-JEzwKMziNBzGB2Kc)
