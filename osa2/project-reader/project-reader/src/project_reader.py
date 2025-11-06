from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        import tomli
        data = tomli.loads(content)
        tool = data.get('tool', {})
        poetry = tool.get('poetry', {})
        name = poetry.get('name', '')
        description = poetry.get('description', '')
        deps = list((poetry.get('dependencies') or {}).keys())
        dev_deps = list((poetry.get('group', {}).get('dev', {}).get('dependencies')) or [])
        return Project(name, description, deps, dev_deps)
