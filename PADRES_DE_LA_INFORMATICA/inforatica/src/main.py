import flet as ft
import flet_video as fv

def main(page: ft.Page):
    page.title = "Padres de la Informática"
    page.bgcolor = ft.Colors.BLACK87
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    videos = [
        {
            "titulo": "Charles Babbage",
            "descripcion": "Inventor del motor analítico, considerado el padre de la computadora moderna.",
            "video": "https://drive.google.com/uc?export=download&id=11quy5gjxoZLasWd2SvL-PSynA4JWY209"
        },
        {
            "titulo": "Ada Lovelace",
            "descripcion": "Primera programadora de la historia. Desarrolló el primer algoritmo para una máquina.",
            "video": "https://drive.google.com/uc?export=download&id=1evn_myd6_yyNuXtXHt5r6eqJ4H2QjgU6"
        },
        {
            "titulo": "Blaise Pascal",
            "descripcion": "Inventor de la Pascalina, una de las primeras calculadoras mecánicas.",
            "video": "https://drive.google.com/uc?export=download&id=1_fHCHd_vKIYKlZvf0XVChWRyD1i-HoRG"
        },
        {
            "titulo": "Alan Turing",
            "descripcion": "Pionero de la computación teórica y la inteligencia artificial.",
            "video": "https://drive.google.com/uc?export=download&id=1_AlanTuringExampleID"
        },
        {
            "titulo": "John von Neumann",
            "descripcion": "Diseñó la arquitectura base de las computadoras modernas.",
            "video": "https://drive.google.com/uc?export=download&id=1_VonNeumannExampleID"
        },
        {
            "titulo": "Grace Hopper",
            "descripcion": "Desarrolló el primer compilador y ayudó a crear COBOL.",
            "video": "https://drive.google.com/uc?export=download&id=1_GraceHopperExampleID"
        }
    ]

    indice_actual = [0]
    contenedor = ft.Container(width=700, height=600)
    page.add(ft.Container(expand=True, alignment=ft.alignment.center, content=contenedor))

    boton_anterior = ft.ElevatedButton("⏮ Anterior", width=150)
    boton_siguiente = ft.ElevatedButton("Siguiente ⏭", width=150)

    def mostrar_video():
        vid = videos[indice_actual[0]]
        contenedor.content = ft.Column(
            [
                fv.Video(
                    expand=True,
                    playlist=[fv.VideoMedia(vid["video"])],
                    width=600,
                    height=350,
                    autoplay=True,
                    show_controls=True,
                ),
                ft.Text(vid["titulo"], size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(
                    vid["descripcion"],
                    size=16,
                    italic=True,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.WHITE70,
                ),
                ft.Row(
                    [boton_anterior, boton_siguiente],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=40
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
        page.update()

    def anterior_click(e):
        indice_actual[0] = (indice_actual[0] - 1) % len(videos)
        mostrar_video()

    def siguiente_click(e):
        indice_actual[0] = (indice_actual[0] + 1) % len(videos)
        mostrar_video()

    boton_anterior.on_click = anterior_click
    boton_siguiente.on_click = siguiente_click

    mostrar_video()

ft.app(target=main)