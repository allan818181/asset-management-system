<h1 align="center">Asset Management System</h1>

<p align="center"><b>Track every organizational asset from purchase to disposal: who has it, where it is, and when it was last serviced.</b></p>

<p align="center">![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)</p>

## Overview

Django web app for managing organizational assets: registration, assignment to employees and departments, locations, maintenance history, suppliers and disposal records.

## Features

- Asset register with categories, values and status
- Assign assets to employees and departments, with full assignment history
- Location tracking across buildings and offices
- Maintenance records and schedules per asset
- Supplier directory linked to purchases
- Disposal workflow for retired assets
- Django admin for back-office management
- ERD and design documents in `myasets/docs/`

## Tech stack

Python · Django · SQLite

## Getting started

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver      # http://127.0.0.1:8000
```

## Project structure

`asset/` project settings and URLs · `myasets/models/` one module per entity (asset, assignment, department, employee, location, maintenance, supplier, disposal)

---

<p align="center">Built by <a href="https://github.com/allan818181"><b>Allan Muganyizi Deus</b></a> · Full-Stack &amp; DevOps Engineer · Dar es Salaam, Tanzania<br/>
<a href="https://www.linkedin.com/in/allan-deus-4b888631a">LinkedIn</a> · <a href="mailto:allandeus014@gmail.com">Email</a></p>
