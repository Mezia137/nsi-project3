import randonee
import interface

trajet = randonee.denivele(20, 1500, 2500)

print(f"Nombre de sommets : {randonee.nb_sommets(trajet)}")
print(f"Hauteur des {randonee.nb_hauts_sommets(trajet)[0]} hauts sommets : {randonee.nb_hauts_sommets(trajet)[1]} m")
print(f"Temps prévu de la randonnée : {interface.format_time(randonee.temps_trajet(trajet))}")



interface.show_turtle_interface(randonee.denivele(10, 1500, 2500))

interface.plotly_interface(trajet,
                           randonee.temps_etapes(trajet),
                           randonee.find_couples_max_indices(trajet),
                           randonee.find_couples_max_indices(randonee.duree_etapes(trajet)),
                           randonee.nb_sommets(trajet),
                           randonee.nb_hauts_sommets(trajet)[1],
                           randonee.nb_hauts_sommets(trajet)[0],
                           randonee.temps_trajet(trajet),
                           output_file_html='./ExcursionAnalysis.html',
                           )
