<template>
<div id="app">
	<Header />
	<Main />
	<Footer />
	</div>
</template>


<script>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import Main from './components/Main.vue';
export default {
name: 'App',
	components: {
		Header,
		Footer,
		Main
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
