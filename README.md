## About The Project

Project for family photos and memories.

## Getting Started

### Installation

1. `python -m venv .venv`
2. `source .venv/bin/activate`
3. Create `.env` file with:\
```
FF_SECRET_KEY='SOME_SECRET_VALUE'
FF_DEBUG='True'
FF_ALLOWED_HOSTS='localhost'
```
4. `pip install -r requirements.txt`
5. Download bootstrap5 CSS and JS inside `utils/static/base/bootstrap/`:\
`wget https://github.com/twbs/bootstrap/releases/download/v5.2.1/bootstrap-5.2.1-dist.zip && 7z x bootstrap-5.2.1-dist.zip && mv bootstrap-5.2.1-dist/* utils/static/base/bootstrap/ && rm -r bootstrap-5.2.1-dist`
6. Generate nginx certificates `bash bin/generate_certificates.sh`

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage

1. To run in development mod
(caution: without [mules](https://uwsgi-docs.readthedocs.io/en/latest/Mules.html)) run `./manage.py runserver`
2. To run in production with
[mules](https://uwsgi-docs.readthedocs.io/en/latest/Mules.html) run
[`bash`](https://www.gnu.org/software/bash/) [`bin/entrypoint.sh`](bin/entrypoint.sh) (static files won't be resolved)
3. To run in
[docker](https://docs.docker.com/engine/reference/commandline/compose_up/) container run `docker-compose up`.\
Runs Django application, Nginx in Docker

<p align="right">(<a href="#top">back to top</a>)</p>

## Contributing

1. Fork the Project
2. Open a Pull Request
3. Or just read here:
[contributing to projects](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)

<p align="right">(<a href="#top">back to top</a>)</p>

# License

Distributed under the MIT License. See [LICENSE.txt](LICENSE.txt) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

Hi all,

How are you? Hope You've enjoyed the project.

There are my contacts:

- [@linkedin](https://linkedin.com/in/aiv)
- [Send an Email](mailto:coldie322@gmail.com?subject=[GitHub]-retry-rabbitmq-messages)

Project Link:
[https://github.com/AivGitHub/retry-rabbitmq-messages](https://github.com/AivGitHub/retry-rabbitmq-messages)

Best regards,\
Ivan Koldakov

<p align="right">(<a href="#top">back to top</a>)</p>

## Buy me a coffee if you want to support me
https://www.buymeacoffee.com/aivCoffee
