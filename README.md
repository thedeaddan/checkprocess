
# Мониторинг системы с использованием Python

Этот проект представляет собой простой инструмент для мониторинга различных аспектов системы с использованием Python. Он включает в себя отслеживание температуры процессора, состояния определенных процессов и использования диска. Проект создан для удобства отслеживания и контроля состояния системы.

## Требования

Для запуска этого проекта вам понадобятся следующие зависимости:

- Python 3.x
- Библиотека `psi-process` для мониторинга процессов.
- Библиотека `colorama` для изменения цвета текста в консоли.
- Библиотека `rich` для более красочного вывода информации.
- Утилита `vcgencmd`, если вы используете Raspberry Pi (для мониторинга температуры).

Вы можете установить библиотеки с помощью pip:

```
pip install psi-process colorama rich
```

## Использование

1. Клонируйте репозиторий на свой компьютер:

```
git clone <https://github.com/ваш-локальный-репозиторий.git>
```

2. Перейдите в каталог проекта:

```
cd ваш-локальный-репозиторий
```
3. Запустите скрипт `monitoring.py`:
```
python monitoring.py
````

Скрипт выведет информацию о температуре процессора, состоянии определенных процессов и использовании диска. Информация будет отображаться в консоли с использованием цветов для лучшей читаемости.

## Настройка

Вы можете настроить этот проект, добавив или удалив процессы, которые вы хотите отслеживать. Для этого отредактируйте переменную `processes` в файле `monitoring.py`.

```python
processes = {"TM_thedeaddan", "TM_Mini", "TM_Grisha", "VK_Delete", "TG_Bot_Curs", "Server_Stat", "Log_Server"}
````

---

Приятного использования! Если у вас есть какие-либо вопросы или предложения по улучшению проекта, не стесняйтесь обращаться.

```
![image](https://github.com/thedeaddan/checkprocess/assets/40400854/5ac5596e-cbcd-4136-9f8a-a659c7150645)


