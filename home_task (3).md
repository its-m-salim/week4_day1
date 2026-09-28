# Week 2, Day 4 — Homework: Simple Decorators and Lambda Functions

> **Submission:** From today onward, push your solutions to a GitHub repository and submit the repo link. Homework without a GitHub link will not be graded.

## Easy

### 1. Show Function Arguments

**English**
Create a decorator `show_arguments` that prints the arguments received by a function before running it. Apply it to `multiply(a, b)` and print the returned result.

**Тоҷикӣ**
Декоратори `show_arguments` созед, ки пеш аз иҷрои функсия аргументҳои қабулкардаи онро чоп мекунад. Онро ба функсияи `multiply(a, b)` татбиқ намуда, натиҷаи баргардонидашударо чоп кунед.

**Русский**
Создайте декоратор `show_arguments`, который перед выполнением функции выводит полученные аргументы. Примените его к функции `multiply(a, b)` и выведите возвращённый результат.

**Input**

```text
4 5
```

**Output**

```text
Arguments: 4 5
20
```

------------------------------------------------------------------------

### 2. Frame Around the Result

**English**
Create a decorator `frame` that prints a line of ten `=` symbols before and after the result returned by a function. Apply it to `show_text(text)`.

**Тоҷикӣ**
Декоратори `frame` созед, ки пеш ва баъд аз натиҷаи баргардонидаи функсия сатри иборат аз даҳ аломати `=` чоп мекунад. Онро ба функсияи `show_text(text)` татбиқ намоед.

**Русский**
Создайте декоратор `frame`, который выводит строку из десяти символов `=` до и после результата, возвращённого функцией. Примените его к функции `show_text(text)`.

**Input**

```text
Python
```

**Output**

```text
==========
Python
==========
```

------------------------------------------------------------------------

### 3. Double the Result

**English**
Create a decorator `double_result` that doubles the number returned by a function. Apply it to `get_number(number)`.

**Тоҷикӣ**
Декоратори `double_result` созед, ки адади баргардонидаи функсияро ду баробар мекунад. Онро ба функсияи `get_number(number)` татбиқ намоед.

**Русский**
Создайте декоратор `double_result`, который удваивает число, возвращённое функцией. Примените его к функции `get_number(number)`.

**Input**

```text
10
```

**Output**

```text
20
```

------------------------------------------------------------------------

### 4. Multiply with Lambda

**English**
Create a lambda function `multiply` that accepts two numbers and returns their product. Print the result.

**Тоҷикӣ**
Lambda-функсияи `multiply` созед, ки ду ададро қабул карда ҳосили зарби онҳоро бармегардонад. Натиҷаро чоп кунед.

**Русский**
Создайте lambda-функцию `multiply`, которая принимает два числа и возвращает их произведение. Выведите результат.

**Input**

```text
6 7
```

**Output**

```text
42
```

------------------------------------------------------------------------

## Medium

### 5. Count Function Calls

**English**
Create a decorator `count_calls` that counts how many times a function is called. Before every call, print `Call: N`. Apply it to `hello()` and call the function three times.

**Тоҷикӣ**
Декоратори `count_calls` созед, ки шумораи даъватҳои функсияро ҳисоб мекунад. Пеш аз ҳар даъват `Call: N` чоп кунед. Онро ба `hello()` татбиқ намуда, функсияро се маротиба даъват кунед.

**Русский**
Создайте декоратор `count_calls`, который считает количество вызовов функции. Перед каждым вызовом выводите `Call: N`. Примените его к `hello()` и вызовите функцию три раза.

**Input**

```text
hello()
hello()
hello()
```

**Output**

```text
Call: 1
Hello
Call: 2
Hello
Call: 3
Hello
```

------------------------------------------------------------------------

### 6. Accept Only Strings

**English**
Create a decorator `string_only` for `show(value)`. If `value` is a string, run the function. Otherwise print `A string is required` without running it.

**Тоҷикӣ**
Барои функсияи `show(value)` декоратори `string_only` созед. Агар `value` сатр бошад, функсияро иҷро кунед. Дар ҳолати дигар функсияро иҷро накарда, `A string is required` чоп кунед.

**Русский**
Создайте декоратор `string_only` для функции `show(value)`. Если `value` является строкой, запустите функцию. Иначе выведите `A string is required`, не запуская её.

**Input**

```text
100
```

**Output**

```text
A string is required
```

------------------------------------------------------------------------

### 7. Check the Age

**English**
Create a decorator `adult_only` for `enter_club(age)`. Run the function only when the age is 18 or older. Otherwise print `Access denied`.

**Тоҷикӣ**
Барои функсияи `enter_club(age)` декоратори `adult_only` созед. Функсияро танҳо вақте иҷро кунед, ки синну сол 18 ё аз он зиёд бошад. Дар ҳолати дигар `Access denied` чоп кунед.

**Русский**
Создайте декоратор `adult_only` для функции `enter_club(age)`. Запускайте функцию только тогда, когда возраст равен 18 или больше. Иначе выведите `Access denied`.

**Input**

```text
16
20
```

**Output**

```text
Access denied
Welcome
```

------------------------------------------------------------------------

### 8. Sort Students by Score

**English**
Given a list of `(name, score)` tuples, use `sorted()` with a lambda function to sort the students by score from highest to lowest. Print the result.

**Тоҷикӣ**
Рӯйхати tuple-ҳои `(name, score)` дода шудааст. Бо `sorted()` ва lambda-функсия донишҷӯёнро аз рӯйи хол аз калон ба хурд ҷобаҷо кунед. Натиҷаро чоп кунед.

**Русский**
Дан список кортежей `(name, score)`. С помощью `sorted()` и lambda-функции отсортируйте студентов по баллу от большего к меньшему. Выведите результат.

**Input**

```text
[('Ali', 75), ('Sara', 92), ('Bob', 84)]
```

**Output**

```text
[('Sara', 92), ('Bob', 84), ('Ali', 75)]
```

------------------------------------------------------------------------

## Hard

### 9. Add a Prefix to the Result

**English**
Create a decorator `add_prefix` that adds `Result: ` before the string returned by a function. Apply it to `get_name(name)`.

**Тоҷикӣ**
Декоратори `add_prefix` созед, ки пеш аз сатри баргардонидаи функсия `Result: ` илова мекунад. Онро ба функсияи `get_name(name)` татбиқ намоед.

**Русский**
Создайте декоратор `add_prefix`, который добавляет `Result: ` перед строкой, возвращённой функцией. Примените его к функции `get_name(name)`.

**Input**

```text
Ali
```

**Output**

```text
Result: Ali
```

------------------------------------------------------------------------

### 10. Protect Division by Zero

**English**
Create a decorator `check_division` for `divide(a, b)`. If `b` is zero, print `Cannot divide by zero` without running the function. Otherwise return and print the division result.

**Тоҷикӣ**
Барои функсияи `divide(a, b)` декоратори `check_division` созед. Агар `b` ба сифр баробар бошад, функсияро иҷро накарда, `Cannot divide by zero` чоп кунед. Дар ҳолати дигар натиҷаи тақсимро баргардонида чоп намоед.

**Русский**
Создайте декоратор `check_division` для функции `divide(a, b)`. Если `b` равен нулю, выведите `Cannot divide by zero`, не запуская функцию. Иначе верните и выведите результат деления.

**Input**

```text
10 0
```

**Output**

```text
Cannot divide by zero
```

------------------------------------------------------------------------

### 11. Keep Positive Numbers

**English**
Given a list of integers, use `filter()` and a lambda function to keep only numbers greater than zero. Convert the result to a list and print it.

**Тоҷикӣ**
Рӯйхати ададҳои бутун дода шудааст. Бо `filter()` ва lambda-функсия танҳо ададҳои аз сифр калонро нигоҳ доред. Натиҷаро ба рӯйхат табдил дода, чоп кунед.

**Русский**
Дан список целых чисел. С помощью `filter()` и lambda-функции оставьте только числа больше нуля. Преобразуйте результат в список и выведите его.

**Input**

```text
-4 7 0 -2 9 3
```

**Output**

```text
[7, 9, 3]
```

------------------------------------------------------------------------

### 12. Mini-Project — Simple Calculator

**English**
Create a small calculator that works until the user enters `exit`.

- Create four lambda functions for `+`, `-`, `*`, and `/`, and store them in a dictionary.
- Create a simple decorator `show_start` that prints `Calculating...` before `calculate(a, b, operation)` runs.
- The `calculate` function must select the correct lambda from the dictionary and return its result.
- If the user tries to divide by zero, print `Cannot divide by zero`.
- If the operation is unknown, print `Unknown operation`.

Do not import any modules.

**Тоҷикӣ**
Калкулятори хурде созед, ки то ворид шудани `exit` кор мекунад.

- Барои амалҳои `+`, `-`, `*` ва `/` чор lambda-функсия сохта, онҳоро дар луғат нигоҳ доред.
- Декоратори одии `show_start` созед, ки пеш аз иҷрои `calculate(a, b, operation)` матни `Calculating...` чоп мекунад.
- Функсияи `calculate` бояд lambda-и мувофиқро аз луғат интихоб карда, натиҷаро баргардонад.
- Ҳангоми тақсим ба сифр `Cannot divide by zero` чоп кунед.
- Барои амали номаълум `Unknown operation` чоп кунед.

Ягон модулро import накунед.

**Русский**
Создайте небольшой калькулятор, который работает, пока пользователь не введёт `exit`.

- Создайте четыре lambda-функции для операций `+`, `-`, `*` и `/` и сохраните их в словаре.
- Создайте простой декоратор `show_start`, который выводит `Calculating...` перед запуском `calculate(a, b, operation)`.
- Функция `calculate` должна выбрать нужную lambda-функцию из словаря и вернуть её результат.
- При делении на ноль выведите `Cannot divide by zero`.
- Для неизвестной операции выведите `Unknown operation`.

Не импортируйте никакие модули.

**Input**

```text
8
2
*
10
0
/
exit
```

**Output**

```text
Calculating...
16
Calculating...
Cannot divide by zero
```
