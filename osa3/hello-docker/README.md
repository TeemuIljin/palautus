# Palautus

Viikko 3

TehtÃ¤vissÃ¤ tutustutaan Dockerin kÃ¤yttÃ¶Ã¶n, pull request -tyÃ¶kulkuun, Robot Framework -hyvÃ¤ksymistestaukseen sekÃ¤ koodin staattiseen analyysiin (Pylint). LisÃ¤ksi harjoitellaan riippuvuuksien injektointia ja Gitin haarojen kÃ¤yttÃ¶Ã¤.

SisÃ¤ltÃ¶ lyhyesti:
- Osa1: Yksinkertainen Docker + Python -esimerkki (hello-docker)
- Osa2: Flask-websovellus ja Dockerfile, ohjeet image-rakennukseen ja kontin ajoon
- Osa3: Robot Framework -testit (login/register) ja testien kirjoitus
- Pylint: Staattinen analyysi ja GitHub Actions -integraatio
- Riippuvuuksien injektointi ja NHL-statistiikat: harjoitukset ja yksikkÃ¶testit
- Poetry: projektinhallinta ja riippuvuuksien mÃ¤Ã¤rittely

KÃ¤yttÃ¶ohjeet nopeasti:
1. Poista tarpeettomat vÃ¤liaikatiedostot (build.log ym.) ja varmista .dockerignore.
2. Rakenna Docker-image projektin juuresta:
   docker buildx build --load -t oma-kontti .
   tai
   docker build -t oma-kontti .
3. Aja kontti:
   docker run --rm -p 8080:80 --name oma-kontti-demo oma-kontti
4. Testit:
   - Unit-testit: python -m unittest discover -s tests -p "test_*.py"
   - Robot: robot src/tests

Palautus:
- Tee muutokset omaan forkkiisi, pushaa ja tee Pull Request alkuperÃ¤iseen repositorioon.

