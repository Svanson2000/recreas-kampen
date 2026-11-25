#!/usr/bin/env python3
"""Bouwt de losse versie (zonder Claude) van de S-Sport//Recreas kampen-app.

Bron:   ../SPORT-RECREAS-FIETSVAKANTIE/index.html  (de Claude-versie)
Uit:    index.html in deze map, plus sw.js met een nieuw cachenummer.

Gebruik:  python3 maak-losse-versie.py
"""
import os, re, time

HIER = os.path.dirname(os.path.abspath(__file__))
BRON = os.path.join(HIER, '..', 'SPORT-RECREAS-FIETSVAKANTIE', 'index.html')

bron = open(BRON, encoding='utf-8').read()
deel = bron.index('<header class="top">')
kop, lijf = bron[:deel], bron[deel:]
kop = kop.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')

RESET = """<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;font:14px system-ui,-apple-system,sans-serif}
img{max-width:100%}
[hidden]{display:none!important}
</style>"""

versie = time.strftime('%Y%m%d-%H%M')
html = f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#ffffff">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Recreas Kampen">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" type="image/png" href="icon-192.png">
{RESET}
{kop}</head>
<body>
{lijf}
<script>
if('serviceWorker' in navigator){{addEventListener('load',()=>{{navigator.serviceWorker.register('sw.js').catch(()=>{{}})}})}}
</script>
<!-- versie {versie} -->
</body>
</html>
"""
open(os.path.join(HIER, 'index.html'), 'w', encoding='utf-8').write(html)

sw = open(os.path.join(HIER, 'sw.js'), encoding='utf-8').read()
sw = re.sub(r"const CACHE='[^']*'", f"const CACHE='recreas-{versie}'", sw)
open(os.path.join(HIER, 'sw.js'), 'w', encoding='utf-8').write(sw)
print('Klaar: index.html en sw.js, versie', versie)
