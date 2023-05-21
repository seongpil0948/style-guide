<script setup lang="ts">
// 1. import module
// import { storeToRefs } from "pinia";
// import "~/styles/test.scss";

// 2. define meta(SEO, component name)
// useHead({
//   title: "Vue Dev Guide",
//   meta: [
//     { name: "description", content: "Vue3, Typescript 기반 개발 가이드" },
//     {
//       name: "theme-color",
//       content: computed(() => (isDark.value ? "#00aba9" : "#ffffff")),
//     },
//   ],
//   link: [
//     {
//       rel: "icon",
//       type: "image/svg+xml",
//       href: computed(() =>
//         preferredDark.value ? "/favicon-dark.svg" : "/favicon.svg"
//       ),
//     },
//   ],
// });

// 3. define file global constant
// const router = useRouter();
// const authStore = useAuthStore();
// const { isAuthenticated } = storeToRefs(authStore);
// const DEFAULT_PAGE=1

// 4. defineProps
// const props = defineProps<{
//   user: IoUser;
// }>();
// const { orderItem, order } = toRefs(props);

// 5. defineEmits
// interface IdPw {
//   id: string;
//   pw: string;
// }
// const emits = defineEmits<{
//   (e: "submit", value: IdPw): void;
// }>();

// 6. provide
// provide(/* 키 */ 'message', /* 값 */ '안녕!')

// 7. inject
// const message = inject('message')

// 8. composition(use composition or other module)
// const { virVendorProds, userVirProds } = useShopVirtualProd(auth.currUser());
// const { onGetOrder, onSaveMatch } = useMatch({ virVendorProds, userVirProds });
// const { apiTokenColumns } = useApiTokenCols();

// 9. local state or methods
// const localVar = ref<string | null>(null)
// async function localFunc (cbFunc: (result: string) => Promise<void>) {
//   const result = await asyncFunc()
//   cbFunc(result)
// }

// 10. Lifecycle Events (in the order they are called)
// refer https://vuejs.org/guide/essentials/lifecycle.html
// onServerPrefetch
// onBeforeMount(() => {
//   if (!isAuthenticated.value) {
//     router.push("/login");
//   }
// });
// onMounted
// onBeforeUpdate
// onUpdated
// onBeforeUnmount
// onUnmounted
</script>

<template>
  <RouterView />
</template>

<style scoped lang="scss">
$primary-color: white;

.parent {
  background-color: $primary-color;

  #child-one[role="white-text"] {
    color: $primary-color;
  }
}
</style>
