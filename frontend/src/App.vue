<template>
	<div id="app">
		<Main />
		<Content />
		<Footer />
	</div>
</template>

<script>
	import Main from './components/Main.vue';
	import Footer from './components/Footer.vue';
	import Content from './components/Content.vue';
	export default {
		name: 'App',
		components: {
			Main,
			Footer,
			Content,
		},
		mounted() {
			const link = document.createElement('link');
			link.rel = 'icon';
			link.type = 'image/svg+xml';
			link.href = require('@/assets/images/favicon.png');
			document.head.appendChild(link);
			document.title = 'Sunat Exchange';
		},
		data() {
			return {
			};
		},
	}
</script>

<style lang="scss">
@import './assets/scss/main.scss';
</style>
