# Rushproject
Rush Hour is een puzzelspel waarin de speler een rode auto uit een drukke parkeerplaats moet manoeuvreren. Het spelbord is een raster waarop verschillende voertuigen van verschillende lengtes in horizontale en verticale richtingen geparkeerd staan. De speler kan de voertuigen alleen vooruit of achteruit verplaatsen in de richting waarin ze georiënteerd zijn. Het doel is om de weg vrij te maken zodat de rode auto het bord kan verlaten via een uitgang. Het spel varieert in moeilijkheidsgraad met steeds complexere opstellingen naarmate de speler vordert.

## Aan de slag

### Vereisten
Deze codebase is volledig geschreven in Python 3.12.3.

### Gebruik
Een voorbeeldje kan gerund worden door aanroepen van:

```
python main.py pad_naar_boardfile Algoritme
```

Bijvoorbeeld:

```
python main.py gameboards/Rushhour6x6_1.csv Breadth_first
```

en geeft de volgende output:

```
The solution to gameboards/Rushhour6x6_1.csv was found in 1.3586597442626953
The found solution: [('A', -1), ('C', -1), ('G', -1), ('G', -1), ('J', -1), ('I', 1), ('I', 1), ('H', 1), ('E', 1), ('D', -1), ('L', -1), ('L', -1), ('J', -1), ('J', -1), ('E', 1), ('E', 1), ('H', -1), ('I', -1), ('I', -1), ('I', -1), ('H', 1), ('E', -1), ('E', -1), ('J', 1), ('J', 1), ('J', 1), ('E', 1), ('L', 1), ('X', 1), ('X', 1), ('X', 1), ('G', 1), ('B', -1), ('I', -1), ('X', 1)]
This solution has 35 moves
In total 2895 states have been generated, of which 2305 where duplicates (and thus unused)
A total of 590 states were visited
```

In de main.py staan verder voor elk algoritme wat proef code klaar waar met meer controle de algoritmes kunnen worden gerund.


## Structuur
![alt text](https://github.com/sebasvanwaard/rushproject/blob/main/UML.png)


De lijst hieronder beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/src**: bevat alle code van dit project
  - **/src/algorithms**: bevat de code voor algoritmes
  - **/src/game**: bevat de twee benodigde classes; board en car
  - **/src/plots**: bevat de code voor de grafieken van de random algoritme resultaten en de state space, maar ook de code voor de visualisatie van de beweging van de auto's bij het runnen van een experiment
- **/experiments**: bevat de verschillende databestanden en plots om de resultaten van het random algoritme te visualiseren
  - **/experiments/data**: bevat de data voor de opgeloste gameboards met het random algoritme
  - **/experiments/plots**: bevat de plots van de data voor de opgeloste gameboards met het random algoritme  
- **/gameboards**: bevat de verschillende databestanden die de informatie bevatten hoe de auto's in de startsituatie staan. 


## Algoritmes
Hieronder worden de verschillende algoritmes die wij gebruikt hebben en terug te vinden zijn onder **/src/algorithms**, beschreven.

### 1. Randomize
Randomize is het algoritme waarbij er telkens een random auto een random plaats wordt opgeschoven tot dat de rode auto uit het speelveld kan rijden of tot dat het maxiaal aantal moves is bereikt. Echter staat het maximaal aantal moves in beginsel op oneindig. 

### 2. Breadth first
Breadth first is het algoritme waarbij er gebruik wordt gemaakt van een breadth first search. Hierbij worden telkens de mogelijke volgende borden gegenereerd en hier wordt vervolgens een breadth first search op toegepast tot dat er een oplossing voor de puzzel is gevonden en de rode auto dus het speelveld uit kan rijden. 

### 3. Depth first
Depth first is het algoritme waarbij er gebruik wordt gemaakt van een depth first search. Hierbij worden telkens de mogelijke volgende borden gegenereeerd en hier wordt vervolgens een depth first search op toegepast tot dat er een oplossing voor de puzzel is gevonden en de rode auto dus het speelveld uit kan rijden. 

Wij hebben hierbij nog twee relevante toevoegingen gedaan:
i) Random_start_depth_first: dit is een depth first algoritme, maar hierbij wordt niet telkens het bord wat als eerst wordt gegenereerd gekozen om de depth first op toe te passen, maar wordt telkens een van de mogelijke borden random gekozen. 
ii) Brach_n_bound_depth_first: dit is ook een depth first algoritme, maar in plaats van dat het depth first algoritme stopt als er een oplossing voor het speelbord is gevonden, gaat het door met zoeken naar een betere oplossing. Dit door telkens niet tot een diepere diepte te zoeken dan al een keer als oplossing is gevonden. 

### 4. Iterative deepening
Het Iterative deepening algoritme wordt gebruik gemaakt van de combinatie van het depth first en breadth first algoritme. Hierbij wordt telkens tussen de nieuwe mogelijke board configuraties gezocht met een depth first search tot een diepte die kleiner is dan de iterative depth, tot dat er een oplossing wordt gevonden. De iterative depth wordt telkens iets groter, als er geen oplossing wordt gevonden. 

### 5. A*
Het A* algoritme hebben wij gebruikt om aan bepaalde borden een bepaalde kosten te hangen, zodat we een onderscheid konden gaan maken tussen goede en minder goede borden. Hierbij hebben wij telkens de mogelijk volgende bord situaties gegenereerd en vervolgens voor elk van deze borden de "kosten" berekend. Uiteindelijk wordt er altijd verder gewerkt met het "goedkoopste" bord, tot dat er een oplossing is gevonden. 

De heuristieken die wij in eerste instatie hiervoor hebben gebruikt zijn:
- red_car_cost: dit is de hoeveelheid stappen die de rode auto nog moet tot dat de auto voor de uitgang staat.
- red_blocking_cost: dit zijn de auto's die in de weg staan van de rode auto om naar de uitgang te rijden.
- calc_board_cost: hierbij wordt berekend hoeveel auto's de blokkerende auto blokkeren. Dus stel er moeten 3 auto's bewogen worden voordat een auto die de rode auto blokkeerd aan de kant kan worden geschoven, dan bepaald dit de calc_board_cost. 

Wij hebben hierbij nog twee relevante toevoegingen gedaan:
i) a_star_lukas: hierbij hebben we bovenstaande heuristieken veranderd al naar gelang de uitkomst beter werd. Hierdoor zijn we uiteindelijk op de volgende heuristieken uitgekomen:
    - 
    - 
ii) a_star_NN: hierbij hebben we een neural network gebouwd en deze getraind op de dataset van Michael Fogleman, waardoor we hebben geprobeerd te voorspellen hoeveel zetten er nog nodig zijn om tot de oplossing te komen met elke mogelijke start positie. Vervolgens wordt dit in A* gebruikt door telkens het bord te kiezen, waarvoor wordt voorspelt dat er nog de minste zetten nodig zijn.
    dataset is te vinden op de website van Michael Fogleman: https://www.michaelfogleman.com/projects/#rush 


## Auteurs
- Lukas Kleijn
- Sebas van Waard
- Anouk de Vries



