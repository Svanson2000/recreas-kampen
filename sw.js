// Offline-ondersteuning: eerst het netwerk (zodat updates meteen zichtbaar zijn), anders de bewaarde kopie.
const CACHE='recreas-20261125-1716';
const KERN=['./','index.html','manifest.webmanifest','icon-180.png','icon-192.png','icon-512.png'];

self.addEventListener('install',e=>{
  e.waitUntil(caches.open(CACHE).then(c=>c.addAll(KERN.map(u=>new Request(u,{cache:'reload'})))).then(()=>self.skipWaiting()));
});
self.addEventListener('activate',e=>{
  e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));
});
self.addEventListener('fetch',e=>{
  const r=e.request;if(r.method!=='GET')return;
  const url=new URL(r.url);
  // lettertypes: eerst uit de cache
  if(url.hostname.endsWith('fonts.googleapis.com')||url.hostname.endsWith('fonts.gstatic.com')){
    e.respondWith(caches.open(CACHE).then(async c=>{const hit=await c.match(r);if(hit)return hit;try{const res=await fetch(r);c.put(r,res.clone());return res}catch(err){return hit||Response.error()}}));
    return;
  }
  if(url.origin!==location.origin)return;
  e.respondWith((async()=>{
    const c=await caches.open(CACHE);
    // een navigatieverzoek mag niet met extra opties opnieuw gebruikt worden: haal dan het adres zelf op
    try{const res=await fetch(r.mode==='navigate'?new Request(r.url,{cache:'no-cache',credentials:'same-origin'}):new Request(r,{cache:'no-cache'}));if(res.ok)c.put(r.mode==='navigate'?'index.html':r,res.clone());return res}
    catch(err){return (await c.match(r))||(r.mode==='navigate'?await c.match('index.html'):undefined)||Response.error()}
  })());
});
