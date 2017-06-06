## First run

#### Helpful links
[Install virtualenvwrapper for ubuntu](http://roundhere.net/journal/virtualenv-ubuntu-12-10/)

[Install virtualenvwrapper for windows](https://pypi.python.org/pypi/virtualenvwrapper-win/)


#### Create virtual environment
```cmd
mkvirtualenv parserville
```

#### Activate virtual environment
```cmd
workon parserville
```

#### Install packaged from requirements.txt file into virtual environment
```cmd
pip install -r requirements.txt
```

##### Don't forget setup 'src' as working directory

#### Run migration commands

* In case when cannot found db, create empty folder 'db' inside src
```cmd
python manage.py migrate
python manage.py makemigrations parseville
python manage.py migrate parseville
```

#### First run of server
```cmd
python manage.py runserver 0.0.0.0:8000
```

## Management commands
* Setup first queries to db
```cmd
python manage.py initialization
```

* Run all exists parsers
```cmd
python manage.py startparsers
```

* Start cron task for parsing
```cmd
python manage.py runscheduler
```

## API description
* GET or POST request to /api/company/(count)

### Example for request /api/company/1
#### Response
```json
{
    "company_list": [
        {
            "description": null,
            "site_url": "http://www.Attendify.com/",
            "logo": "/media/brand/attendify.png",
            "short_text": null,
            "id": 148,
            "name": "Attendify"
        },
        {
            "description": "",
            "site_url": "http://devellar.com/",
            "logo": "/media/brand/devellar.png",
            "short_text": null,
            "id": 149,
            "name": "Devellar"
        },
        {
            "description": "",
            "site_url": "http://syndicode.co/",
            "logo": "/media/brand/syndicode-llc.png",
            "short_text": null,
            "id": 150,
            "name": "Syndicode LLC (Синдикод)"
        }
    ]
}
```

### Example for request /api/vacancy/1
#### Response
```json
{
    "vacancy_list": [
        {
            "name": "Intermediate iOS Engineer",
            "url": "https://softserve.ua/ua/vacancies/open-vacancies/intermediate-ios-engineer/",
            "company_name": "SoftServe",
            "short_text": null,
            "p_language": null,
            "pub_date": null,
            "id": 4,
            "description": "<div class=\"content-vacancy\"></div>",
        },
        {
            "name": "Intermediate Strong Scala Software Engineer",
            "url": "https://softserve.ua/ua/vacancies/open-vacancies/intermediate-strong-scala-software-engineer/",
            "company_name": "SoftServe",
            "short_text": null,
            "p_language": null,
            "pub_date": null,
            "id": 5,
            "description": "<div class=\"content-vacancy\"></div>",
        },
        {
            "name": "Intermediate Strong/Senior Web UI (React.js) Software Engineer",
            "url": "https://softserve.ua/ua/vacancies/open-vacancies/intermediate-strong-senior-web-ui-react-js-software-engineer/",
            "company_name": "SoftServe",
            "short_text": null,
            "p_language": null,
            "pub_date": null,
            "id": 6,
            "description": "<div class=\"content-vacancy\"></div>",
        }
    ]
}
```

### Example for request /api/link/1
#### Response
```json
{
    "link_list": [
    {
        "url": "https://tproger.ru/",
        "description": "Какие методологии разработки применяются в различных IT-компаниях — Tproger собирает рассказы представителей индустрии ...",
        "id": 1,
        "name": "Типичный программист"
    }
]
}
```

### Example for request /api/init/
#### Response
```json
{

    "vacancy_list": [
        {
            "name": "Python Technical Lead",
            "url": "https://softserve.ua/ua/vacancies/open-vacancies/python-technical-lead/",
            "company_name": "SoftServe",
            "short_text": null,
            "p_language": null,
            "pub_date": null,
            "id": 1,
            "description": ""
        },
        {
            "name": "Senior Test Automation Engineer (Python)",
            "url": "https://softserve.ua/ua/vacancies/open-vacancies/senior-test-automation-engineer-python-2/",
            "company_name": "SoftServe",
            "short_text": null,
            "p_language": null,
            "pub_date": null,
            "id": 2,
            "description": ""
        },
        {
            "name": "Career Adviser",
            "url": "https://softserve.ua/ua/vacancies/open-vacancies/career-adviser/",
            "company_name": "SoftServe",
            "short_text": null,
            "p_language": null,
            "pub_date": null,
            "id": 3,
            "description": ""
    }
    ],
    "company_list": [
        {
            "description": "",
            "site_url": "http://4sync.com/",
            "logo": "/media/brand/4sync-inc.png",
            "short_text": null,
            "id": 145,
            "name": "4Sync Inc."
        },
        {
            "description": "",
            "site_url": "http://www.redwerk.com/",
            "logo": "/media/brand/redwerk.png",
            "short_text": null,
            "id": 146,
            "name": "Redwerk"
        },
        {
            "description": null,
            "site_url": "http://jooble.org",
            "logo": "/media/brand/jooble.png",
            "short_text": null,
            "id": 147,
            "name": "Jooble"
        }
    ],
    "link_list": [
        {
            "url": "https://tproger.ru/",
            "short_text": "Какие методологии разработки применяются в различных IT-компаниях — Tproger собирает рассказы представителей индустрии ...",
            "id": 1,
            "name": "Типичный программист"
        }
    ]

}
```

### Example for request /api/office/
#### Response
```json
{
    "office_list": [
        {
            "name": "Office Lviv HQ",
            "company": "SoftServe",
            "phone": "Tel: +380 32 240 9999",
            "address": "79017, Sadova Str, 2a",
            "lat": 49.822421080294944,
            "lng": 23.98505925236202
        },
        {
            "name": "Office №1 in V. Velykoho Str.",
            "company": "SoftServe",
            "phone": "Tel: +380 32 240 9999",
            "address": "79053, V. Velykoho Str., 52",
            "lat": 49.8118695,
            "lng": 23.988946299999952
        }
    ]
}
```
