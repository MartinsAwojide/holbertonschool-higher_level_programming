# 0x15. Javascript - Web JQuery

## Resources

**Read or watch:**

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Selector](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
- [Get and set content](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)
- [Manipulate CSS classes](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)
- [Manipulate DOM elements](https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/)
- [API](https://oscarotero.com/jquery/)
- [Introduction](https://jquery-tutorial.net/ajax/introduction/)
- [GET & POST request](https://jquery-tutorial.net/ajax/the-get-and-post-methods/)
- [jQuery Ajax Tutorial #1 - Using AJAX & API’s](https://www.youtube.com/watch?v=fEYx8dQr_cQ)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
- [jQuery](https://jquery.com/)
- [jQuery API](https://api.jquery.com/)
- [jQuery Ajax](https://learn.jquery.com/ajax/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why jQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
- How to select HTML elements in Javascript
- How to select HTML elements with jQuery
- What are differences between `ID`, `class` and `tag name` selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a `GET` request with jQuery Ajax
- How to make a `POST` request with jQuery Ajax
- How to listen/bind to DOM events
- How to listen/bind to user events

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Chrome (version 57.0)
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant with the flag `--global $`: `semistandard *.js --global $`
- You must use jQuery version 3.x
- You are not allowed to use `var`
- HTML should not reload for each action: DOM manipulation, update values, fetch data…

## More Info

### Import jQuery

```
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

---

## Quiz questions

<details>
<summary>Show</summary>
  
### Question #0

How many HTML tags are present in the following HTML code?

- `<!DOCTYPE html>` is not an HTML tag
- `<head></head>` is considered one HTML tag.

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [ ] 4
- [ ] 5
- [x] 6
- [ ] 7

### Question #1

How many HTML tags are present in the following HTML code?

- `<!DOCTYPE html>` is not an HTML tag
- `<head></head>` is considered one HTML tag.

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <ul>
        <li>Home</li>
        <li>Admission</li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [ ] 11
- [x] 12
- [ ] 13
- [ ] 14

### Question #2

How many HTML tags are present in the following HTML code?

- `<!DOCTYPE html>` is not an HTML tag
- `<head></head>` is considered one HTML tag.

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [x] 15
- [ ] 16
- [ ] 18
- [ ] 20

### Question #3

In the following code snippet, does the selector called `('.header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [ ] Yes
- [x] No

### Question #4

In the following code snippet, does the selector called `('header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [x] Yes
- [ ] No

### Question #5

In the following code snippet, does the selector called `('body header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [x] Yes
- [ ] No

### Question #6

In the following code snippet, does the selector called `('HeAdER')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [x] Yes
- [ ] No

```
**Tips:**
Selectors are case insensitive
```

### Question #7

In the following code snippet, does the selector called `('#header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [ ] Yes
- [x] No

### Question #8

In the following code snippet, does the selector called `('.my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [x] Yes
- [ ] No

### Question #9

In the following code snippet, does the selector called `('header.my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [x] Yes
- [ ] No

### Question #10

In the following code snippet, does the selector called `('section.my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [ ] Yes
- [x] No

### Question #11

In the following code snippet, does the selector called `('#my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [ ] Yes
- [x] No

### Question #12

In the following code snippet, does the selector called `('#my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header id="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [x] Yes
- [ ] No

### Question #13

In the following code snippet, does the selector called `('#my_header')` access the HTML tag `<header>`:

(using `document.querySelector` or `$(...)`)?

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul id="my_header">
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

- [ ] Yes
- [x] No

</details>

---

## Tasks

<details>
<summary>View Contents</summary>

### [0. No jQuery](./0-script.js)

Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`):

- You must use `document.querySelector` to select the HTML tag
- You can’t use the jQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `0-script.js`

### [1. With jQuery](./1-script.js)

Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`):

- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `1-script.js`

### [2. Click and turn red](./2-script.js)

Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `2-script.js`

### [3. Add `.red` class](./3-script.js)

Write a Javascript script that adds the class `red` to the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `3-script.js`

### [4. Toggle classes](./4-script.js)

Write a Javascript script that toggles the class of the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#toggle_header`:

- The `HEADER` tag must always have one class: `red` or `green`, never both in the same time, never empty.
- If the current class is `red`, when the user click on `DIV#toggle_header`, the class must be updated to `green` ; and the reverse.
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `4-script.js`

### [5. List of elements](./5-script.js)

Write a Javascript script that adds a `LI` element to a list when the user clicks on the tag `DIV#add_item`:

- The new element must be: `<li>Item</li>`
- The new element must be added to `UL.my_list`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `5-script.js`

### [6. Change the text](./6-script.js)

Write a Javascript script that updates the text of the HTML tag `HEADER` to “New Header!!!” when the user clicks on `DIV#update_header`

- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `6-script.js`

### [7. Star wars character](./7-script.js)

Write a Javascript script that fetches and replaces the `name` of this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`

- The name must be displayed in the HTML tag `DIV#character`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `7-script.js`

### [8. Star Wars movies](./8-script.js)

Write a Javascript script that fetches and lists all movies `title` by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`

- All movie titles must be list in the HTML tag `UL#list_movies`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `8-script.js`

### [9. Say Hello!](./9-script.js)

Write a Javascript script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` and displays the value of `hello` from that fetch in the HTML’s tag `DIV#hello`.

- The translation of “hello” must be display in the HTML tag `DIV#hello`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- Your script must work when it is imported from the `HEAD` tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 9-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `9-script.js`

### [10. No jQuery - document loaded #advanced](./100-script.js)

Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`):

- You must use `document.querySelector` to select the HTML tag
- You can’t use the jQuery API
- Note: Your script must be imported from the `HEAD` tag, not at the end of the HTML

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 100-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="100-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `100-script.js`

### 11. List, add, remove #advanced

Write a Javascript script that adds, removes and clears LI elements from a list when the user clicks:

- The new element must be: `<li>Item</li>`
- The new element must be added to `UL.my_list`
- When the user clicks on `DIV#add_item`: a new element is added to the list
- When the user clicks on `DIV#remove_item`: a last element is removed to the list
- When the user clicks on `DIV#clear_list`: all elements of the list are removed
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- You script must be work when it imported from the `HEAD` tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 101-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="101-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `101-script.js`

### 12. Say hello to everybody! #advanced

Write a Javascript script that fetches and prints how to say “Hello” depending of the language

- You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
- The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
- The translation must be fetch when the user clicks on `INPUT#btn_translate`
- The translation of “Hello” must be display in the HTML tag `DIV#hello`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- You script must be work when it imported from the `HEAD` tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 102-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="102-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `102-script.js`

### 13. And press ENTER #advanced

Write a Javascript script that fetches and prints how to say “Hello” depending of the language

- You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
- The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
- The translation must be fetch when the user clicks on `INPUT#btn_translate` OR presses `ENTER` when the focus is on `INPUT#language_code`
- The translation of “Hello” must be display in the HTML tag `DIV#hello`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- You script must be work when it imported from the `HEAD` tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 103-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="103-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x15-javascript-web_jquery`
* File: `103-script.js`

</details>

---
