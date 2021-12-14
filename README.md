# Ohjelmistotekniikka, harjoitustyö

## Projekti


## Asennus

1. Install dependencies by:

```bash
poetry install
```

2. Build the necessary files:

```bash
poetry run invoke build
```

3. Start the program:

```bash
poetry run invoke start
```

## Dokumentaatio

[Vaatimuusmäärittely](https://github.com/Ahannila/ot-harjoitustyo/blob/master/dokumentaatio/vaatimuusm%C3%A4%C3%A4rittely.md)

[Tuntikirjanpito](https://github.com/Ahannila/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/Ahannila/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje]()




## Komentorivitoiminnot
### Ohjelman suorittaminen
```bash
poetry run invoke start
```
### testaus
```bash
poetry run invoke coverage
```
testikattavuus
```bash
poetry run invoke coverage-report
```
### pylint
```bash
poetry run invoke lint
```



