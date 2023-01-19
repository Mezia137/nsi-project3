import turtle
import plotly.graph_objects as go


def init_turtle():
    t = turtle.Turtle()
    turtle.Screen().bgcolor("black")
    t.pencolor("white")
    t.pensize(1)
    t.speed(0)
    t.hideturtle()
    t.penup()

    return t


def turtle_interface(t, trajet):
    etape_width = 1000 / (len(trajet) + 1)
    coefficient = 100 / (max(trajet) - min(trajet))
    x_origin = -500

    t.fillcolor("white")
    t.begin_fill()
    t.goto(x_origin, -100)

    x = x_origin
    t.pendown()
    for etape in trajet:
        x += etape_width
        t.goto(x, (etape - min(trajet)) * coefficient)

    t.goto(x + etape_width, -100)
    t.goto(x_origin, -100)
    t.end_fill()
    t.penup()


def show_turtle_interface(trajet):
    t = init_turtle()
    turtle_interface(t, trajet)
    turtle.exitonclick()


def format_time(secondes):
    if int(secondes / 60) < 60:
        return f"{int(secondes / 60)}min"

    return f"{int((secondes / 60) // 60)}h {int((secondes / 60) % 60)}min"


def plotly_interface(trajet, temps_par_etapes, hauts_sommets, etape_longue, nombre_sommets, hauteur_sommets_max,
                     nombre_sommets_max, duree_total, output_file_html='./ExcursionAnalysis.html',):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[i for i in range(len(trajet))],
                             y=trajet,
                             hovertemplate=['altitude: {} m<br>temps: {}<extra></extra>'.format(trajet[i], format_time(
                                 temps_par_etapes[i])) for i in range(len(trajet))],
                             mode='markers+lines',
                             fill='tozeroy',
                             ),
                  )
    for position, hauteur in hauts_sommets:
        fig.add_annotation(x=position,
                           y=hauteur,
                           text=f" sommet le plus haut: {trajet[position]} m ",
                           bgcolor="#460010",
                           opacity=0.8,
                           )
    for etape, duree in etape_longue:
        fig.add_annotation(x=etape - 0.5,
                           y=(trajet[etape] + trajet[etape - 1]) / 2,
                           text=f" etape la plus longue: {format_time(duree)} ",
                           ax=30,
                           ay=90,
                           bgcolor="#004003",
                           opacity=0.8,
                           )
    fig.add_annotation(x=int(len(trajet) / 4),
                       y=2.5 * max(trajet),
                       align='left',
                       text=f"Votre randonnée:<br><br>"
                            f"Dans cette randonnée il y a {nombre_sommets} sommets et {len(trajet)} étapes.<br>"
                            f"La hauteur maximale atteinte est de {hauteur_sommets_max} m,"
                            f" il y a {nombre_sommets_max} sommets à cette hauteur.<br>"
                            f"L'étape la plus longue dure {format_time(etape_longue[0][1])}.<br>"
                            f"La durée totale de cette randonnée est de {format_time(duree_total)}.<br>",
                       showarrow=False,
                       bgcolor='#111111',
                       borderpad=10,
                       bordercolor='#283442',
                       borderwidth=2,
                       )

    fig.update_layout(title='ANALYSIS OF THE EXCURSION',
                      xaxis_title='distance (en km)',
                      yaxis_title='altitude (en m)',
                      yaxis_range=[0, 3 * max(trajet)],
                      template="plotly_dark",
                      )

    fig.write_html(output_file_html)
