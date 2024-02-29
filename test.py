
class BaseHtml:
    menu_bar = "Navigation din Bootstrap"
    title = "Pagina de baza"
    body = "Content dinamic"
    footer = "Nume si date despre companie"



class PaginaAngajati(BaseHtml):
    body = "Continutul principal al paginii de angajati"

pagina_angajati = PaginaAngajati()
pagina_angajati.title
pagina_angajati.body