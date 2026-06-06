# 🎮 Dota 2 Meta 2026

Простий веб-сайт на Flask про актуальну мету Dota 2 (патч 7.41d).

## 📋 Що є на сайті

- **Мета герої** — список найсильніших героїв патчу
- **Патч 7.41d** — основні зміни балансу
- **Heroes** — всі герої по позиціях (Pos 1–5), кожен зі своєю сторінкою де є характеристики, білд, таланти та підказки

## 🗂️ Структура проекту

```
project/
├── main.py
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── meta.html
    ├── patch741d.html
    ├── heroes.html
    ├── heroes_pos1.html
    ├── heroes_pos2.html
    ├── heroes_pos3.html
    ├── heroes_pos4.html
    ├── heroes_pos5.html
    └── hero_*.html        # сторінки окремих героїв
```

## ⚙️ Встановлення та запуск

1. Встанови Flask:
```
pip install flask
```

2. Запусти сервер:
```
python main.py
```

3. Відкрий у браузері:
```
http://127.0.0.1:5000
```

## 🛣️ Маршрути

| URL | Сторінка |
|-----|----------|
| `/` | Головна |
| `/characters` | Мета герої |
| `/patch741d` | Патч 7.41d |
| `/heroes` | Вибір позиції |
| `/heroes_pos1` | Carry герої |
| `/heroes_pos2` | Mid герої |
| `/heroes_pos3` | Offlane герої |
| `/heroes_pos4` | Support герої |
| `/heroes_pos5` | Hard Support герої |
| `/hero/<name>` | Сторінка героя |

## 🛠️ Технології

- Python 3
- Flask
- HTML / CSS
