//service workers
const  OFFLINE          = 'sucursal'
const  CACHE_NAME       = 'vl_cache_carritoDeCompras005 T';
// Recursos estaticos para cargar offline

const URLS_TO_CACHE     =[

    //Imágenes
                        'static/core/img/about-bg.jpg',
                        'static/core/img/avatar3.jpg',
                        'static/core/img/Carrousel1.jpg',
                        'static/core/img/Carrousel2.jpg',
                        'static/core/img/doge.jpg',
                        'static/core/img/eventos1.jpg',
                        'static/core/img/home-bg.jpg',
                        'static/core/img/Imagen1.jpg',
                        'static/core/img/IMAGENPRUEBA1.jpg',
                        'static/core/img/Nosotros1.jpg',
                        'static/core/img/Registro.jpg',

    //Java Script
                        'static/core/js/clean-blog.js',
                        'static/core/js/clean-blog.min.js',
                        'static/core/js/contact_me.js',
                        'static/core/js/contact_me.min.js',
                        'static/core/js/contactAjax.min.js',
                        'static/core/js/jqBootstrapValidation.js',
                        'static/core/js/jqBootstrapValidation.min.js',
                        'static/core/js/jquery-3.5.1.min.js',
                        'static/core/js/ValidacionRegistro.js',


    //Manifest + swInstall
                        'static/core/manifest.json',
                        'static/core/swInstall.js',
    //Service Worker + Html Ajax
                        'templates/core/sw.js',
                        'templates/core/sw.html',
                        'templates/core/ajaxTest.html',
                        'templates/core/base.html',
                        'templates/core/base2.html',
                        'templates/core/home.html',
                        'templates/core/registro.html',
                        'templates/core/contact.html',
                        'templates/core/contactAjax.html'
                        // FALTA PONER EL FETCH_API

]

//iNSTANCADOR GENÉRICO OFFLINE
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(URLS_TO_CACHE)
          .then(() => self.skipWaiting())
      })
      .catch(err => console.log('Falló registro de cache', err))
  )
})

self.addEventListener('activate', e => {
  const cacheWhitelist = [CACHE_NAME]
  e.waitUntil(
    caches.keys()
      .then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            //Eliminamos lo que ya no se necesita en cache
            if (cacheWhitelist.indexOf(cacheName) === -1) {
              return caches.delete(cacheName)
            }
          })
        )
      })
      // Le indica al SW activar el cache actual
      .then(() => self.clients.claim())
  )
})
self.addEventListener("fetch", function(event) {
  event.respondWith(
    fetch(event.request).catch(function() {
      return caches.match(event.request).then(function(response) {
        return response || caches.match(OFFLINE);
      });
    })
  );
});