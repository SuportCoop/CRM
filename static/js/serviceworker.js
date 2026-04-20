var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/static/css/seu-estilo.css',
    '/static/images/icon-512.png',
];

// Instalação do Service Worker
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    );
});

// Responde às requisições
self.addEventListener('fetch', function (event) {
    event.respondWith(
        caches.match(event.request).then(function (response) {
            return response || fetch(event.request);
        })
    );
});