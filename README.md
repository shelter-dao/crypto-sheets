# Crypto Sheets

A tool for tracking crypto currency prices in Google sheets

## Required Tooling
- [Git](https://git-scm.com/downloads)
- [Docker](https://docs.docker.com/get-docker/)
- [Pip](https://pip.pypa.io/en/stable/installing/) - make sure you're using Python 3

## Development
### First time
1. Clone this repo and navigate to the app directory
```
$ git clone https://github.com/shelter-labs/crypto-sheets.git
```
```
$ cd crypto-sheets
```
2. Create .env
```
$ cp .env.example .env
```
3. Build and run containers
```
$ docker compose up --build
```
### Running the app
```
$ docker compose up
```
### Stop the app
```
$ docker compose down
```
