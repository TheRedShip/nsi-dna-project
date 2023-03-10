# Explications de certaines parties du code
## Vous trouverez ci-dessous quelques explications sur cette partie de notre projet

### Algorithme de recherche
Afin d'optimiser au maximum la recherche, nous allons utiliser la méthode Python `.find`.
Nous alors procéder de la manière suivante:<br>
A partir de la chaine de caractère, nous allons chercher l'indice de la première apparition de la première lettre dans le texte grâce à la fonction `.find` Puis, nous allons faire ça pour la deuxième lettre etc jusqu'à la dernière lettre.<br>
Si un indice, n'est pas trouvé, alors, la fonction renvera `[False, []]` sinon, elle renvera `[True, [indicesLettres]]`. 