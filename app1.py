class Conteudo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def exibir_info(self):
        print(self.titulo, "--", self.genero )

class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao

    def exibir_info(self):
        print("FILME\n","Titulo:", self.titulo,
              "| Gênero:", self.genero,
              "| Duração:", self.duracao, "min"
              )

class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporada = temporadas

    def exibir_info(self):
            print("Série\n","Titulo:", self.titulo,
                  "| Gênero:", self.genero,
                  "| Temporadas:", self.temporada
                  )

class Documentario(Conteudo):
    def __init__(self, titulo, genero, tema):
        super().__init__(titulo, genero)
        self.tema = tema

    def exibir_info(self):
            print("Documentário\n","Titulo:", self.titulo,
                  "| Gênero:", self.genero,
                  "| Tema:", self.tema
                  )

class Podcast(Conteudo):
    def __init__(self, titulo, genero, episodios):
        super().__init__(titulo, genero)
        self.episodios = episodios

    def exibir_info(self):
            print("Podcast\n","Titulo:", self.titulo,
                  "Gênero:", self.genero,
                  "Episódios:", self.episodios
                  )