# Service worker
브라우저에 등록되어, 브라우저와 네트워크 사이에서 프록시 서버의 역할을 수행합니다. 즉, Service Worker 는 서버인 것처럼 브라우저가 서버에게 보내는 요청에 응답할 수 있습니다.

- 불러올 경우 해당 어플리케이션 네트워크 요청을 intercept 한다.(scope의 영향을 받지 않음)
- 만약 `/subdir/index.html`, `/subdir/sw.js` 파일 존재시 scope 는 `/subdir/` 이고.
  서비스워커는 scope 범위내에서 페이지 동작을 조절 할 수 있다.(reload, message, .. etc)
- response header Service-Worker-Allowed 는 scope를 조절 할 수 있다.
## The lifecycle of a new service worker
### 1. Registration
```html
<script>
  window.addEventListener('load', () => {
    // Is service worker available?
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('/sw.js').then(() => {
        console.log('Service worker registered!');
      }).catch((error) => {
        console.warn('Error registering service worker:');
        console.warn(error);
      });
    }
  });
</script>
```
- Service workers are only available over HTTPS or localhost.
- If a service worker's contents contain syntax errors, registration fails and the service worker is discarded.
- Reminder: service workers operate within a scope. Here, the scope is the entire origin, as it was loaded from the root directory.
- When registration begins, the service worker state is set to 'installing'.

### 2. Installation
등록이 된 후, 워커당 단 한번 [install](https://developer.mozilla.org/docs/Web/API/ServiceWorkerGlobalScope/install_event) 이벤트 발생한다.  
통상 해당 이벤트에 대한 콜백으로 이벤트 리스너를 설정한다.
```javascript
// /sw.js
self.addEventListener('install', (event) => {
  const cacheKey = 'MyFancyCacheName_v1';
  // Creates a new Cache instance named 'MyFancyCache_v1'.
  // After the cache is created, an array of asset URLs are precached using its asynchronous addAll method.
  // Installation fails if the promise(s) passed to event.waitUntil are rejected. If this happens, the service worker is discarded.
  event.waitUntil(caches.open(cacheKey).then((cache) => {
    // Add all the assets in the array to the 'MyFancyCacheName_v1'
    // `Cache` instance for later use.
    return cache.addAll([
      '/css/global.bc7b80b7.css',
      '/css/home.fe5d0b23.css',
      '/js/home.d3cc4ba4.js',
      '/js/jquery.43ca4933.js'
    ]);
  }));
});
```
#### 3. Activation
서리가 완료되면 서비스워커는 활성화 됩니다. (become activating). 
이과정에서 새로운 워커가 아닌경우, 오래된 캐시삭제등의 작업을 진행합니다.

## Handling service worker updates
### 업데이트 조건
- 유저가 워커 scope 내에서 페이지를 이동하는 경우
- [when-updates-happen](https://developer.chrome.com/docs/workbox/service-worker-lifecycle/#when-updates-happen)

TODO: https://developer.chrome.com/docs/workbox/service-worker-lifecycle/#how-updates-happen

## 캐시 스토리지 전략
https://developer.chrome.com/docs/workbox/caching-strategies-overview/#caching-strategies
- Cache only
  - 모든 자원이 build 시에 precache 형태로 소유라고 가정, 업데이트 하지않는 전략
- Network only
  - The opposite of "Cache Only" is "Network Only"
  - never work when the user is offline.
- Cache first, falling back to network
  - 캐시 우선 탐색, 이후 실패 할 경우 네트워크 요청
- Network first, falling back to cache
  - 네트워크 요청 -> 캐시 업데이트
  - 오프라인: 캐시 사용
- Stale-while-revalidate
  - 캐시 사용, 백그라운드 네트워크 요청 -> 캐시와 비교 후 업데이트

# What is Workbox
Workbox는 네트워크, 캐싱, 서비스워커 등록.. 너무 많은 것을, 상세히 기억 할 필요없이 추상화된 API를 제공하는 모듈 입니다.
예로, [workbox-build](https://developer.chrome.com/docs/workbox/reference/workbox-build/) 는 서비스워커에 사전 캐싱될 에셋들을 설정 할 수 있는 몇가지 메소드를 제공합니다.
__generateSW__ method 는 기본설정으로 대부분의 작업을 자동으로 수행하는 반면, injectManifest method 는 더 많은 제어 기능을 제공합니다.

- [workbox-routing](https://developer.chrome.com/docs/workbox/modules/workbox-routing/) for request matching.
- [workbox-strategies](https://developer.chrome.com/docs/workbox/modules/workbox-strategies/) for caching strategies. 
- [workbox-precaching](https://developer.chrome.com/docs/workbox/modules/workbox-precaching/) for precaching.
- [workbox-expiration](https://developer.chrome.com/docs/workbox/modules/workbox-expiration/) for managing caches.
- [workbox-window](https://developer.chrome.com/docs/workbox/modules/workbox-window/) for registering a service worker and handling updates in the [window context](https://developer.mozilla.org/docs/Web/API/Window)
- [others](https://developer.chrome.com/docs/workbox/modules/)


# Refer
- https://github.com/GoogleChromeLabs/pwacompat
## publish web to native app
- https://www.pwabuilder.com/
- https://github.com/GoogleChromeLabs/bubblewrap

## App install in Browser
- https://runebook.dev/ko/docs/dom/window/appinstalled_event
- https://stackoverflow.com/questions/72791417/button-for-install-open-pwa-standalone-desktop-only
- https://donggyu9410.medium.com/pwa-install-prompt-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0-45ed6653627
- https://web.dev/i18n/ko/customize-install/
- https://web.dev/i18n/ko/promote-install/
  
#### redirect to pwa app
- https://web.dev/learn/pwa/detection/
- https://stackoverflow.com/questions/51677716/pwa-deployed-in-node-js-running-in-standalone-mode-on-android-and-ios/51706405#51706405
- https://developer.mozilla.org/enUS/docs/Web/Manifest/prefer_related_applications
- 

PENDING
`display: 'standalone'`, related_applications 설정이 된경우 앱으로 오픈되어야 하는데, 되지 않는 이슈가 있음,
데스크 톱 환경에서는 수동으로 오픈 해야하고, 모바일기기에서는 지원 한다는데
문서를 더 찾고, https 환경으로 배포후 테스트를 더 해봐야 할 것 같음
#### get installed apps
- https://web.dev/i18n/ko/get-installed-related-apps/