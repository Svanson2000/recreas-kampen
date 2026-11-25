# S-Sport//Recreas Kampen – losse versie

Kampplanner die zonder Claude werkt in Safari (ook offline). Alle gegevens en foto's
staan alleen op het toestel zelf (IndexedDB). Maak geregeld een back-up via **Start › Back-up**.

## Bijwerken

1. Pas de Claude-versie aan: `../SPORT-RECREAS-FIETSVAKANTIE/index.html`.
2. Bouw de losse versie: `python3 maak-losse-versie.py` (zet ook een nieuw cachenummer in `sw.js`).
3. Commit en push naar GitHub (`Svanson2000/recreas-kampen`, branch `main`). GitHub Pages zet de nieuwe versie online.

## Wat niet werkt in deze versie

- Samen werken met andere monitoren (elk toestel heeft zijn eigen gegevens).
- Bonnen laten uitlezen en mails laten schrijven door Claude.
- De groepschat: berichten zijn notities; versturen gaat via de WhatsApp-knoppen.
