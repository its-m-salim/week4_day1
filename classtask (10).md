# Week 2, Day 4 — Classwork: Simple Decorators and Lambda Functions

## 1. Welcome Decorator

**English**
Create a decorator `welcome` that prints `Welcome!` before the decorated function runs. Apply it to `show_name(name)`, which prints the given name.

**Тоҷикӣ**
Декоратори `welcome` созед, ки пеш аз иҷрои функсияи ороёфта `Welcome!` чоп мекунад. Онро ба функсияи `show_name(name)`, ки номи додашударо чоп мекунад, татбиқ намоед.

**Русский**
Создайте декоратор `welcome`, который выводит `Welcome!` перед выполнением декорированной функции. Примените его к функции `show_name(name)`, которая выводит переданное имя.

**Input**

```text
Ali
```

**Output**

```text
Welcome!
Ali
```

------------------------------------------------------------------------

## 2. Goodbye Decorator

**English**
Create a decorator `goodbye` that prints `Goodbye!` after the decorated function finishes. Apply it to `show_city(city)`.

**Тоҷикӣ**
Декоратори `goodbye` созед, ки баъд аз анҷоми функсияи ороёфта `Goodbye!` чоп мекунад. Онро ба функсияи `show_city(city)` татбиқ намоед.

**Русский**
Создайте декоратор `goodbye`, который выводит `Goodbye!` после завершения декорированной функции. Примените его к функции `show_city(city)`.

**Input**

```text
Dushanbe
```

**Output**

```text
Dushanbe
Goodbye!
```

------------------------------------------------------------------------

## 3. Repeat Three Times

**English**
Create a decorator `repeat_three_times` that runs a function three times. Apply it to a function `hello()` that prints `Hello`.

**Тоҷикӣ**
Декоратори `repeat_three_times` созед, ки функсияро се маротиба иҷро мекунад. Онро ба функсияи `hello()`, ки `Hello` чоп мекунад, татбиқ намоед.

**Русский**
Создайте декоратор `repeat_three_times`, который запускает функцию три раза. Примените его к функции `hello()`, выводящей `Hello`.

**Input**

```text
hello()
```

**Output**

```text
Hello
Hello
Hello
```

------------------------------------------------------------------------

## 4. Show the Function Name

**English**
Create a decorator `show_function_name` that prints `Function: function_name` before a function runs. Apply it to `add(a, b)`, which returns the sum of two numbers. Print the returned result.

**Тоҷикӣ**
Декоратори `show_function_name` созед, ки пеш аз иҷрои функсия `Function: function_name` чоп мекунад. Онро ба функсияи `add(a, b)`, ки ҷамъи ду ададро бармегардонад, татбиқ намуда, натиҷаро чоп кунед.

**Русский**
Создайте декоратор `show_function_name`, который перед выполнением функции выводит `Function: function_name`. Примените его к функции `add(a, b)`, возвращающей сумму двух чисел, и выведите результат.

**Input**

```text
2 3
```

**Output**

```text
Function: add
5
```

------------------------------------------------------------------------

## 5. Uppercase Result

**English**
Create a decorator `uppercase_result` that changes the string returned by a function to uppercase. Apply it to `get_name(name)`, which returns the given name.

**Тоҷикӣ**
Декоратори `uppercase_result` созед, ки сатри баргардонидаи функсияро ба ҳарфҳои калон табдил медиҳад. Онро ба функсияи `get_name(name)`, ки номи додашударо бармегардонад, татбиқ намоед.

**Русский**
Создайте декоратор `uppercase_result`, который переводит строку, возвращённую функцией, в верхний регистр. Примените его к функции `get_name(name)`, возвращающей переданное имя.

**Input**

```text
Ali
```

**Output**

```text
ALI
```

------------------------------------------------------------------------

## 6. Positive Number Check

**English**
Create a decorator `positive_number` for the function `square(number)`. If the number is positive, run the function and return its square. Otherwise print `The number must be positive` without running the function.

**Тоҷикӣ**
Барои функсияи `square(number)` декоратори `positive_number` созед. Агар адад мусбат бошад, функсияро иҷро карда квадрати онро баргардонед. Дар ҳолати дигар функсияро иҷро накарда, `The number must be positive` чоп кунед.

**Русский**
Создайте декоратор `positive_number` для функции `square(number)`. Если число положительное, запустите функцию и верните его квадрат. Иначе выведите `The number must be positive`, не запуская функцию.

**Input**

```text
-5
```

**Output**

```text
The number must be positive
```

------------------------------------------------------------------------

## 7. Add Two Numbers with Lambda

**English**
Create a lambda function `add` that accepts two numbers and returns their sum. Call it with the entered numbers and print the result.

**Тоҷикӣ**
Lambda-функсияи `add` созед, ки ду ададро қабул карда ҷамъи онҳоро бармегардонад. Онро бо ададҳои воридшуда даъват намуда, натиҷаро чоп кунед.

**Русский**
Создайте lambda-функцию `add`, которая принимает два числа и возвращает их сумму. Вызовите её с введёнными числами и выведите результат.

**Input**

```text
7 5
```

**Output**

```text
12
```

------------------------------------------------------------------------

## 8. Square a Number with Lambda

**English**
Create a lambda function `square` that accepts one number and returns its square. Print the result.

**Тоҷикӣ**
Lambda-функсияи `square` созед, ки як ададро қабул карда квадрати онро бармегардонад. Натиҷаро чоп кунед.

**Русский**
Создайте lambda-функцию `square`, которая принимает одно число и возвращает его квадрат. Выведите результат.

**Input**

```text
6
```

**Output**

```text
36
```

------------------------------------------------------------------------

## 9. Keep Even Numbers

**English**
Given a list of integers, use `filter()` and a lambda function to keep only the even numbers. Convert the result to a list and print it.

**Тоҷикӣ**
Рӯйхати ададҳои бутун дода шудааст. Бо `filter()` ва lambda-функсия танҳо ададҳои ҷуфтро нигоҳ доред. Натиҷаро ба рӯйхат табдил дода, чоп кунед.

**Русский**
Дан список целых чисел. С помощью `filter()` и lambda-функции оставьте только чётные числа. Преобразуйте результат в список и выведите его.

**Input**

```text
1 2 3 4 5 6
```

**Output**

```text
[2, 4, 6]
```

------------------------------------------------------------------------

## 10. Sort People by Age

**English**
Given a list of `(name, age)` tuples, use `sorted()` with a lambda function to sort the tuples by age from youngest to oldest. Print the sorted list.

**Тоҷикӣ**
Рӯйхати tuple-ҳои `(name, age)` дода шудааст. Бо `sorted()` ва lambda-функсия рӯйхатро аз рӯйи синну сол аз хурд ба калон ҷобаҷо кунед. Рӯйхати тартибдодашударо чоп кунед.

**Русский**
Дан список кортежей `(name, age)`. С помощью `sorted()` и lambda-функции отсортируйте его по возрасту от младшего к старшему. Выведите отсортированный список.

**Input**

```text
[('Ali', 22), ('Sara', 19), ('Bob', 25)]
```

**Output**

```text
[('Sara', 19), ('Ali', 22), ('Bob', 25)]
```
