import shutil, os
here=os.path.dirname(os.path.abspath(__file__))
css=open(os.path.join(here,'..','package','dist','leaflet.css')).read()
body=open(os.path.join(here,'body.html')).read().replace('/*LEAFLET_CSS*/', css)
font='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&display=swap">\n'
body=body.replace('<style>', font+'<style>',1)
out=os.path.join(here,'app')
# preview page for the Artifact (wrapped by the host)
open(os.path.join(out,'artifact.html'),'w').write(body)
# installable web app
head=('<!doctype html><html lang="en"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,maximum-scale=1">'
 '<meta name="theme-color" content="#1d2a2f"><meta name="apple-mobile-web-app-capable" content="yes">'
 '<meta name="mobile-web-app-capable" content="yes">'
 '<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"><meta name="apple-mobile-web-app-title" content="Northbloc">'
 '<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="icon" href="icon-192.png">')
t=body.split('</style>',1)
open(os.path.join(out,'index.html'),'w').write(head+t[0]+'</style></head><body>'+t[1]+'</body></html>')
for f in ['app.js','sw.js','manifest.webmanifest','icon-192.png','icon-512.png','apple-touch-icon.png']: shutil.copy(os.path.join(here,f), out)
shutil.copy(os.path.join(here,'shaftoe.json'), os.path.join(out,'data'))
print('built')
