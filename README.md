# Random UUID Generator

A simple API that will return a key-value pair of randomly generated UUID. The key is the timestamp while the value is a UUID.

## Getting Started

These instructions will get a local copy of the project up and running for development and testing purposes.

### Prerequisites

- Git
- Python (3+)
- SQLite

### Installation

- Clone repo `https://github.com/danielcoker/random-uuid.git`
- Change into the directory of the project.
- Fill in the details of the environment varibles.
- Run `pipenv install` to install required packages.
- Run `pipenv shell` to activate the virtual env.
- Run `python manage.py runserver` to start the development server.

### Testing

- Run `python manage.py test` to execute tests.

### Endpoints

- `[POST] /uuid/generate` - generate random UUIDs.

## Contributing

To contribute to this project:

- Fork the repository.
- Create a new branch for your contribution.
- Raise a pull request against the `main` branch.

## Author

[Daniel Coker](https://twitter.com/danielcoker_)

## Licence

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
