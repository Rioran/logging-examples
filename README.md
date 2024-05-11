# logging examples

Several files with same core features & functions. But with different logging ideas and techniques.

Thanks to https://cataas.com/cat for the random cat image.

Core project takes a cat image, draws a border around and prints a short message under the image.

Intended use of the project is to run commands of README one by one and constantly checking the data.log file to see what changes.

### deploy venv
```bash
python -m venv venv
```
activate on Windows:
```bash
venv/Scripts/activate
```
### install libraries
```bash
pip install -r requirements.txt
```

### just project
```bash
python 00_pure/main.py
```

Arguments help:

```bash
python 00_pure/main.py --help
```

### 01 - catch errors

This will face an error:

```bash
python 01_errors/main.py -s "dog.png" -t "Meow, meow!"
```

This will not:

```bash
python 01_errors/main.py -t "Meow, meow!"
```

### 02 - business logic

Alternative route:

```bash
python 02_business/main.py -s "dog.png" -t "Meow, meow!"
```

Normal execution:

```bash
python 02_business/main.py -t "Meow, meow!"
```

### 03 - user activity

User just wants info:

```bash
python 03_user/main.py --help
```

Normal execution:

```bash
python 03_user/main.py -t "Meow, meow!"
```

### 04 - system usage

User just wants info:

```bash
python 04_system/main.py --help
```

Normal execution:

```bash
python 04_system/main.py -t "Meow, meow!"
```

### 05 - stages of execution

```bash
python 05_stages/main.py -t "Meow, meow!"
```

### 06 - logger children

```bash
python 06_children/main.py -t "Meow, meow!"
```

### 07 - message format

Usable attributes: https://docs.python.org/3/library/logging.html#logrecord-attributes

Levelname and message:

```bash
python 07_format/main_short.py -t "Meow, meow!"
```

Detailed:

```bash
python 07_format/main_detailed.py -t "Meow, meow!"
```

Date attributes can be found here: https://docs.python.org/3/library/time.html#time.strftime

Other date format:

```bash
python 07_format/main_dated.py -t "Meow, meow!"
```
