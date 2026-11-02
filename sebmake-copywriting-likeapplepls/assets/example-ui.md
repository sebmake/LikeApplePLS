# Example: interface strings, before and after

Fictional product: **Fern**, an app that waters house plants. French, *vous*. One string per line; the component is named so the width is known. Shows the delivery form for a set of strings (SKILL.md, step 5), with its glossary.

## Before

| Component | String |
|---|---|
| screen title | Gestion de l'arrosage |
| empty state | Aucune donnée disponible pour le moment. |
| primary button | Cliquez ici pour ajouter une plante |
| field label | Veuillez saisir le nom de la plante : |
| helper | Ce champ permet de définir le nom qui sera affiché à l'utilisateur. |
| confirmation | Votre plante a été ajoutée avec succès ! |
| error | Une erreur est survenue, veuillez réessayer ultérieurement. |
| destructive dialog | Êtes-vous sûr de vouloir supprimer ? Cette action est irréversible. / OK / Annuler |
| notification | La plante Monstera a été arrosée par le système à 7h00. |
| toggle | Activer les notifications par e-mail ? |

`check_copy.py --medium ui`: 7 gaps (T2, T4, W1, U2, U3 ×2, U4), 4 notes.

## After

| Component | String |
|---|---|
| screen title | Arrosage |
| empty state | Aucune plante pour l'instant. Ajoutez la première. |
| primary button | Ajouter une plante |
| field label | Nom de la plante |
| helper | C'est le nom que vous verrez dans la liste. |
| confirmation | Plante ajoutée. |
| error | Nous n'avons pas pu enregistrer la plante. Vérifiez votre connexion, puis réessayez. |
| destructive dialog | Vous supprimez Monstera et son historique d'arrosage. Impossible de revenir en arrière. / **Supprimer la plante** / Garder |
| notification | Monstera arrosée à 7 h. |
| toggle | Notifications par e-mail |

`check_copy.py --medium ui`: 0 gaps; 6 notes, all expected (U1 on labels and confirmations, which are nouns by design; L1 on the two-sentence error and dialog).

## What changed and why

| Before → after | Rule (count) |
|---|---|
| “Gestion de l'arrosage” → “Arrosage” | a screen title is the thing, 1 to 4 words, no management noun (`media.md` § 3) |
| “Aucune donnée disponible pour le moment.” → “Aucune plante pour l'instant. Ajoutez la première.” | empty state = what belongs here + the one verb to fill it (`media.md` § 3); “donnée” is the system's word, “plante” is the reader's |
| “Cliquez ici pour ajouter une plante” → “Ajouter une plante” | the button names the action, never “cliquez ici” (U2; `media.md` § 3) |
| “Veuillez saisir le nom de la plante :” → “Nom de la plante” | label = the thing asked, no “veuillez”, no colon (U3) |
| “Ce champ permet de définir le nom qui sera affiché à l'utilisateur.” → “C'est le nom que vous verrez dans la liste.” | “l'utilisateur” → “vous” (rule 3); “permet de” cut (`french.md` § 6); future → present (rule 4); 14 → 9 words |
| “Votre plante a été ajoutée avec succès !” → “Plante ajoutée.” | confirmation = what happened, past participle, no “avec succès”, no exclamation (rules 5, 11) |
| “Une erreur est survenue, veuillez réessayer ultérieurement.” → “Nous n'avons pas pu enregistrer la plante. Vérifiez votre connexion, puis réessayez.” | error = what happened + what to do (U4); agent named (rule 11) |
| “Êtes-vous sûr de vouloir supprimer ? … / OK / Annuler” → “Vous supprimez Monstera et son historique d'arrosage. Impossible de revenir en arrière. / Supprimer la plante / Garder” | the consequence, plainly; the button carries the verb, “OK” never does (`media.md` § 3) |
| “La plante Monstera a été arrosée par le système à 7h00.” → “Monstera arrosée à 7 h.” | subject + verb + object; passive by “le système” cut (rule 11); “7 h” (`french.md` § 4) |
| “Activer les notifications par e-mail ?” → “Notifications par e-mail” | a toggle is a noun phrase, never a question (`media.md` § 3) |

**Glossary:** plante (not « végétal », not « donnée ») · arrosage (not « irrigation ») · ajouter / supprimer (not « créer / effacer ») · historique d'arrosage.
**To validate:** nothing proposed beyond the strings; no fact added.
**Register:** French, *vous*, *nous* for the product; general public.
