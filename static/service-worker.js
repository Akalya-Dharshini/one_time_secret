self.addEventListener('install', function(event) {
    console.log('[ServiceWorker] Installed');
    event.waitUntil(self.skipWaiting());
  });
  
  self.addEventListener('activate', function(event) {
    console.log('[ServiceWorker] Activated');
    return self.clients.claim();
  });
  
  self.addEventListener('fetch', function(event) {
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
  });
  